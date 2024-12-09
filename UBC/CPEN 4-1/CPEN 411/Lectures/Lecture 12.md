Up till now, we have removed WAR and WAW hazards but not yet RAW hazards. So we will investigate Tomasulo’s Algorithm to see how we can remove RAW hazards.

#### Story so far
The out-of-order story so far
- Pipelining partially overlaps instruction processing.
	- RAW hazards are resolved by **stalling** and **forwarding**.
- Concurrent execution in FUs with different latencies.
	- **out-of-order completion** causes WAW hazards.
	- workaround: **scoreboard** tracks Rd, **stalls ID** until Rd is ready.
- Reading operands out-of-order
	- **WAR hazards**, need to stall in WB if Rd pending.

#### Hazard Observation
- WAW and WAR hazards come from **name dependencies**.
- No actual values are transferred between the instructions.
- Can we supply infinite names?

##### Renaming registers by hand
Let’s see the original code,
```
LD R1, 0(R2)
DADD R3, R1, R3
DADDUI R2, R2, #8
LD R1, 0(R2)
```

Let’s give each Rd a fresh Tn (Temporal name),
```
LD T1, 0(R2)
DADD T2, T1, R3 // Need to use T1 now
DADDUI T3, R2, #8 // Only Rd is renamed
LD T4, 0(T3) // Forward T3
```

If we look at what hazards we’ve removed, we have removed WAR and WAW hazards so far.
→ We still have RAW hazards.

==We wouldn’t set the destination registers as Arch. registers since we still want to ensure binary compatibility → AMD and Intel have to be able to run the same thing.==


*The key insight was to not track register names, but to track data dependencies directly.*

#### Tomasulo’s Algorithm

##### Hardware
We need some hardware to be implementing the algorithm.

- **Reservation stations (RS)**: In front of each functional unit.
	- Buffer instructions waiting for operands.
- Registers in instructions are **renamed to tags**.
	- Destinations registers get a fresh tag (ALWAYS) - mapping to RAT.
	- Source registers get corresponding tags from RAT.
- Results are broadcasted on **common data bus (CDB)**
	- Each result carries tag of source RS (where it was produced).
	- All RSs and the RF listen to the CDB for tags that they want values for and pick up if needed.
		- This is to reduce the time from the RF back to the RS, we’d rather have RSs pick up from the CDB to reduce time.


##### Algorithm
We have some stages for the algorithm itself.

- Decode
- Issue
	- If we have a free RS (no structural hazard) → It allocates to RS entry.
	- Lookup source operand registers in RF: get either **values** or **tags**.
		- We get one of them, NOT BOTH.
	- **Rename destination register** to allocated **RS entry tag**.

- Execute
	- Listen for unready operand tags on the CDB, snarf values.
	- Once all operands are ready → start execution.
- Write Result
	- Broadcast **<dst tag, result>** on the CDB.
		- Interested RSs and RF will see the tag and update the value.
	- Mark reservation station available.


##### Design Tradeoffs
- It is often complex to implement such a structure.
- The CDB actually limits performance.
	- Many associative comparisons happen at high speeds.
	- Each CDB goes to multiple FUs: High capacitance, high wiring density.
- Only one FU can complete per cycle **(because of the CDB)**.
	- Multiple CDBs: More FU logic for parallel associative stores.
- Non-precise with interrupts.


##### Example
- **Instructions**: are fetched and decoded from the instruction memory and are waiting to be issued → they can only be issued if there is somewhere to put them (no structural hazard).
- **Register File**: Holds values for registers that are ready (they do not wait for any functional unit).
	- **Register Status**: Tags are held for registers that are waiting for a result from a functional unit.
		- Value O → Tag X
		- Tag X → Tag O
- **Functional Units**: The following examples has 3 FUs.
	- Adder: pipelined, 2 cycle latency.
	- Divider: un-pipelined, 40 cycle latency.
	- Multiplier: un-pipelined, 10 cycle latency.
	- All these units can execute in parallel.
- **Reservation Stations**: The following example has independent RSs, we can also have a unified one but this would be per design.
- **Normal Bus**: They are used to retrieve tags of the next instructions operands, and send the instruction / operands to the appropriate reservations station (issuing).

![[Screenshot 2024-12-05 at 7.24.29 PM.png]]

Let’s get the first instruction, `add.d f8, f4,f4`.
All registers have values for this instruction, we can thus issue the instruction the add,
![[Screenshot 2024-12-05 at 7.26.20 PM.png]]
And starting cycle 2, we can start executing.

----
Now let’s get the next instruction. `mult.d f4, f6, f2`, similar to the instruction above, we have the destination register ready also the MU is empty → Let’s issue it.

Also, The previous add instruction can start executing.

![[Screenshot 2024-12-05 at 7.27.33 PM.png]]

----
`add.d f6, f2, f2` 
We also have a the destination free, thus we can go on and issue it. In this cycle (cycle 3), we can start executing the previous instruction, and the first instruction will be in the last step of the pipeline.

![[Screenshot 2024-12-05 at 7.33.40 PM.png]]

---
`div.d f2, f4, f2`
We finally, have a register with only a tag! `f4`!!! We can go on create the tag for `f2` and fetch the `M1` tag for `f4`. 

Also, in this cycle the first add instruction has finished, therefore we can return the new value which is 6 and remove the tag for `f6`.

The multiplying instruction is still on the way…

![[Screenshot 2024-12-05 at 7.36.05 PM.png]]

---
`add.d f8, f6, f8`
We have to create a new tag for `f8`, but we can see from the reg file that `f6` is still in-flight. Also, since the previous add instruction has been removed from the RS, we can fill the RS with the adding tag `A1` with `f8`. Also, we take the tag `A2` for `f6`.

The second add instruction is in the last cycle of the pipeline.

![[Screenshot 2024-12-05 at 7.37.53 PM.png]]

---
`add.d f6, f2, f8`
All of them only have tags!  Also, in this cycle the previous add instruction has been finished executing. At the same time, the result from the add instruction from cycle 5 can be forwarded to the pipeline and register file.

BUT, we have to wait a cycle for the instruction to be issued since the RS is filled. The CDB broadcasting and issuing cannot happen simultaneously.

![[Screenshot 2024-12-05 at 7.41.54 PM.png]]

---
From the previous step, we couldn’t issue the instruction since the RS was full. Now that it is empty, we can take the tag `A2` again for `f6` and fetch the other tags. 

The previous step’s add instruction is now also forwarded to the pipeline.

`dst tag: A2, tag1: D1, tag2: A1`

![[Screenshot 2024-12-05 at 7.45.32 PM.png]]

---
`mult.d f2, f8, f4`
All of them are tags, and the RS for multiplying is empty. Let’s put it in the entry, 
`dst tag: M2, tag1: f8, tag2: M1`

![[Screenshot 2024-12-05 at 7.50.22 PM.png]]

==Wait!==, what about the divider result? Previously, `f2` was named to `M2`, and the RF is no longer waiting for `D1` → what will happen?

RS `A2` is still snooping for`D1`, so it will snarf from CDB when the value is ready. Any following instructions that read `f2` will want the `mult.d` result not `div.d`.

***It’s ok! :)***

---
No instruction.

The 4 + 6 add instruction is now done, it will broadcast `A2`, but since no other RS is waiting for it, we write to the RF and call it.

![[Screenshot 2024-12-05 at 7.54.10 PM.png]]

---
No instruction.

Nothing interesting happens.
![[Screenshot 2024-12-05 at 7.54.38 PM.png]]

---
Cycle: 13
Finally the `mult.d` instruction that came first is done! It will broadcast `M1` with the value! We can see that the stalling `div.d` instruction can finally proceed!!! (Also, the value is written to the RF as well)

![[Screenshot 2024-12-05 at 7.55.44 PM.png]]

---
Cycle: 14 

Nothing interesting happens.
![[Screenshot 2024-12-05 at 7.56.37 PM.png]]

---
Cycle: 24
By this cycle, the second `mult.d` instruction has ended. We broadcast `M2` with the values. But nothing interesting can happen since we only need to write to the RF.

![[Screenshot 2024-12-05 at 7.57.32 PM.png]]

---
Cycle: 54
Now the `mult.d` instruction with `dst tag: D1` is done!!! We can broadcast to the adding unit, but not the RF since we don’t have a tag associated with it.

![[Screenshot 2024-12-05 at 8.00.14 PM.png]]

---
Now we just need the add to end and write to the `A2` tag. Everything is done.

##### Summary
- We’ve seen out-of-order techniques:
	- two scoreboards, register renaming.
- Scoreboards have WAW and WAR hazards.
	- Resolved by stalling.
- Tomasulo algorithm **tracks dependencies directly**.
	- Renaming eliminates WAW/WAR.
	- Also allows more physical registers than ISA regs.


#### But..
What are the problems of Tomasulo? We fixed structural hazards.. isn’t this enough?
Let’s look closely at the step that we update the register file. Would the program order be conserved? No, it wouldn’t

We’ve ensured out-of-order completion, but ***we don’t want out-of-order commitment!***

#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 13|Lecture 13]]
