We discussed at the end that we want in-order commitment despite out-of-order completion. Let’s see how!

#### Flush Pipelines?
Why would we flush pipelines?

- Mis-predicted branches![[Screenshot 2024-12-05 at 8.16.03 PM.png]]
	- In tomasulo, if we figured out that we mis-predicted a branch we would need to un-do everything. → ==This is impossible.==
- External interrupt
- Program fault
- Trap
- OS context switch
- Page fault

#### Exceptions
- Exceptions are events *detected in the micro architecture at execution time*.
- Require *transfer of control* to an OS interrupt service routine.
- May need to *resume to the original program* as if nothing happened.

==Regardless of the number of exceptions → computations shouldn’t change.==

##### Precise Exceptions
If architectural state is
- Updated by *all* instructions before a faulting instruction.
- And *not updated* after (and including) faulting instruction.

→ Then the pipeline supports **precise exceptions**.

![[Screenshot 2024-12-05 at 8.19.54 PM.png]]

##### Exceptions in an in-order pipeline
When an exception strikes:
1. Switch instruction fetch to point to the exception handler.
2. Convert instructions after and including “faulting instruction” to **nops**.
3. **Remember PC** of faulting instruction.
	1. Need to remember where to come back to after handling.


#### Speculative Execution
- We know how to predict branches as **not taken**.
- But most branches are **taken**.
	- If we look at loops, then we can see that they are taken.
- Often compiler (or hardware) can **predict** outcome.
- We would need a way to **cancel mis-predicted path** (something similar to precise exception).

If we can do such a thing, this capability is known as **speculative execution**.

For instance,
```
*Instructions*                      *Pipeline*

DIVD R3, R1, R2                     F:1, D:2, I:3, X:4, W:104
BEQZ R3, Label                      F:2, D:3, I:4, X:105, ("not taken")
^Assume predicted "taken"
...

Label: 
DMUL R4, R4, R2                     F:3, D:4, I:5, X:6, W:?
```
In this example, we can see that the branch prediction was incorrect. 

Our goal is to,
**Support execution of instructions fetched following a prediction *before* we know if the prediction is correct. We also want to execute and broadcast the result of DMUL *speculatively* long before branch resolved on cycle 105.**

- We want to write early enough and wait until the correct branch outcome is known.


The problem is that,
**Such instructions should not update the register file because the branch might’ve been predicted incorrectly.**

##### Completion and Commit
- insight: The problem is writing to RF on a wrong predict and not finishing the computation early.
- idea: compute & buffer the result but delay the RF write until prior instructions guaranteed to retire.

- Split write-back into **completion** and **commit**!!!
	- completion - buffer computed result.
	- commit - write result to RF.

#### Reorder Buffer (ROB)
- Stores instructions in **program order** (a FIFO).
- **Buffers** computed results before RF write.
- Commits in **program order**.

![[Screenshot 2024-12-05 at 8.33.42 PM.png]]

- It tracks the **execution status** for each instruction.
```
busy? | sent to FU? | finished? | PC | dst reg | speculative? | valid? | val
```
- issue stage allocates RS and ROB entry.
	- May or may not use ROB entry to hold computed value.
	- May or may not use ROB entry ID as renaming tag.


##### Tomasulo with re-order buffer
![[Screenshot 2024-12-05 at 8.36.06 PM.png]]
At cycle 3: the `DIVD` has been issued, allocates ROB and Reservation Station entries, updates RAT.

In the RS for DIVD, what does `1` represent? → ROB1.

---
At cycle 4: BEQZ is issued, allocates ROB and RS entries.
![[Screenshot 2024-12-05 at 8.39.05 PM.png]]

---
Cycle 5: DMUL issued, allocates ROB and RS entries.
![[Screenshot 2024-12-05 at 8.39.46 PM.png]]

---
Cycle 6: DADD issued, same as above.
![[Screenshot 2024-12-05 at 8.40.10 PM.png]]

---
Cycle 16: DMUL writes to CDB and ROB gets values, ***however RF is not updated.***
Cycle 17: DADD writes to CDB, ROB gets value, ***RF not updated.***
Cycle 104: DIVD writes to CDB, BEQZ and ROB gets value.
Cycle 105: Register R3, updated (from DIVD), **BEQZ resolved as “not taken” - flushes ROB and resets RAT**.

![[Screenshot 2024-12-05 at 8.43.22 PM.png]]

One question, Since the branch was mis-predicted should we flush the branch and execute it again too?
→ **No, already knows the outcome we do not need to.**

If the ROB had 100 entries → the maximum flush amount would be 99 instructions, since we do not need to flush the branch instruction.

##### Some Challenges
- Modern high-performance CPU: ~ 8-way issue.
	- max. how many deqs. from ROB per cycle?
	- max. how many enqs. to ROB per cycle?
	- max. how many new results in ROB per cycle?
- Problem: multi-ported SRAMs are expensive.
- Observation: Not all instructions produce a value.

But the main takeaway is “can we increase the ROB infinitely?”
→ Assume we have 1000 entries in the ROB, with 95% accuracy. We already burn a lot of power with this much entries. 

Also,
- Branches are frequent. → if we have the first branch mis-predicted, we have a whole tree of instructions from the decision tree that have to be flushed.
	- This costs too much once again.
- We can’t have ROB size as $\infty$.

==To increase ROB, we first need to have accuracy increased.==

#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 14|Lecture 14]]
