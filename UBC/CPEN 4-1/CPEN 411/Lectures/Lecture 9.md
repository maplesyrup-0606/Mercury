## Pipelining
We know the main stages of the pipeline we’ve been learning.
- Fetch - take VA to get PA and hence get binary stream of the instruction.
- Decode - figure out what the instruction is from the binary stream.
- Execute - execute the instruction.
- Memory Access - load or store from/to memory.
- Write back - write back to register file.

![[Pasted image 20241019171307.png]]
Note that not all instructions need to go through all stages. e.g. a `mv` instruction would not need to access the memory but still goes through it.

In theory, CPI is 1. We have 1 instruction entering and leaving the pipeline every cycle.

==Also, the fetch and memory access stages are not that simple, they involve caches. In most cases, these stages would require 1 cycle, however, if a cache miss occurs it might take for ever.==

- Essentially, fetch one instruction every cycle.
- Commit one instruction every cycle.
- Enable multiple instructions to move through the processor.
- Ensure that there are no incorrect executions.

Eventually, we require pipeline registers in between to allow tracking of intermediate values.

![[Pasted image 20241019172348.png]]

###### What would we like in pipelining?
- **Uniform Subcomputations**
	- Goal: Each stage has the same delay.
	- Achieved by balancing pipeline stages.
- **Identical Computations**
	- Goal: Each computation uses the same number of stages.
- **Independent Computations**
	- Goal: Start new computation each cycle.

*However, programs often have dependencies => we no longer have uniform / identical / independent stages!*

![[Pasted image 20241019172631.png]]
Let’s look at the instruction memory and the data memory. If it is not a cache hit for either the instruction cache or the data cache, we don’t know how many cycles it would take.

In the case the stages do not run in 1 cycle, the pipeline then has to stall…

##### Intro to Hazards
Let’s look at the set of instructions,
```
LD R1, 1000
MOV R2, R3
ADD R4, R5, R6
MOV R2, R1
SD R2, 2000
```

Let’s look at the stage when the 1st instruction actually loads 1000 into the register and when the 4th instructions needs to fetch the data of R1 from the register file.

Maybe let’s show the stages,
![[Pasted image 20241019173632.png]]
By the time we decoded and fetched the data from the register file (4th instruction) and move to the execution stage, we don’t have updated value!
So we would need to stall the `MOV` instruction to remove that problem from dependency.

### Hazards
![[Pasted image 20241019174912.png]]
Consider the sequence of this (hopefully) independent instructions.
After cycle 5 → You process complete and commit one instruction per clock cycle.
If it runs a large number of instructions the IPC is almost 1.
**But dependencies can lower the IPC.**

###### Potential hazards from pipelining
![[Pasted image 20241019175316.png]]
- Here R1 is the destination of the ADD instruction.
- R1 is also the source of SUB, AND, OR, and XOR instructions.
- How do instructions after ADD get the correct value for R1?

R1 becomes the source for the succeeding instructions, and hence causes a dependency problem. **Even if in our eyes the dependency doesn’t seem like a problem, we should note that we have to look into the machine’s view. The machine only looks at a certain window.**

For the OR, XOR instruction, by proper forwarding we can solve these hazards and move on. But for the SUB and AND instruction, we are forced to stall the pipeline. ← We can’t go back in time..

#### Pipeline Hazards
##### Structural Hazards
- Caused by resource conflicts.
	- Two or more instructions want to use the same hardware at the same time.
- Two ways to resolve structural hazards:
	- Stall
		- Wait until earlier instruction is finished using the resource.
	- Replicate Hardware
		- Often we can eliminate need for stalling by replicating hardware or building hardware capable of servicing multiple instructions at the same time.

*The things is that infinite replication is not possible, eventually we will end up stalling.*

##### Data Hazards
A data hazard is when a successive stage of the pipeline requires a resource, however the previous stage has not prepared it yet.
###### Forwarding
Forwarding is the process of literally forwarding the data to stages that need it directly. And this can be done in one cycle.

![[Pasted image 20241019180858.png]]

###### Unavoidable Stalls
As mentioned, in the case of the “go back in time” situations, we are forced to stall.

##### Control Hazards
Control hazards are due to branches.
- A branch may or may not change the program counter.
- Therefore, which instruction should follow a branch depends upon the result of **executing** the branch instruction.
- The result of a branch is typically known by the end of EX (or even ID).

Consider the following example,
```
BNEZ R1, Label <-- Branch instruction
ADD R1, R2, R3 <-- Branch successor for "not taken" branch
LD R1, 0(R2)
...

Label: SUB R1, R2, R3 <-- Branch successor for "taken" branch
```

###### Option 1: Stall
![[Pasted image 20241019182956.png]]
Since we know that the next instruction will depend on the end of the execution stage. We stall the succeeding instruction until X. After X, we fetch the next instruction.

###### Option 2: Predict “Not Taken”
Branches tend to “weakly biased” meaning they are taken and not-taken roughly the same number of times.
=> This means that about half the time, if we had just guessed that the branch was not taken, we would have been right.

*If we’re wrong, we still need a way to fix our mistake.*

![[Pasted image 20241019183306.png]]
In the case of a correct prediction, nothing really has to been done. Though we would only know the result at the end of the execution stage of the branch instruction, since it is a correct prediction we can just proceed with the pipeline.

![[Pasted image 20241019183522.png]]
In the case of a wrong prediction, we realize that we have been fetching the wrong instructions. So we flush the left over instruction stages by just forcing no-ops. At the same cycle, start fetching the correct instruction.

#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 10|Lecture 10]]
