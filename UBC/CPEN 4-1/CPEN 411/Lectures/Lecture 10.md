### Data Dependency
If two instructions with a dependency execute in a different order, **the result may be different.**

```
dadd x2, x3, x4							dadd x2, x3, x4
dadd x5, x6, x7							dadd x5, x2, x7
```

The first set have independent instructions, thus re-ordering wouldn’t be a problem. On the other hand, The second set has dependent instructions, re-ordering would potentially cause hazards.

This is the property of a program, **not the hardware** (The program cannot change hardware).

### Hazard
A hazard occurs when execution (by an implementation can violate data dependencies).
![[Pasted image 20241019184418.png]]
And this is a property of the architecture.

### True data dependency
Consider the instructions,
```
I: DADD x1, x2, x3
J: DSUB x4, x1, x3
```
The instruction “J” has a **true data dependency** on instruction “I”. Since “I” writes to `x1` , then “J” reads from x1.

**It is a true dependency because a value was communicated.**
=> A true dependency leads to a “read-after-write (RAW)” hazard *if* the hardware can perform the read before the write.

*RAW hazards point from left to right.*

This is potentially impossible to solve, but there are some approaches to fixing this:
- Maybe re-order instructions to prevent stalling.
- Value prediction.

### Name dependency
Maybe two instructions use the same register or memory location, **but no data passes between them**.

**Dependency is on data location (name) not the value (contents at location).**

#### Anti-dependencies and WAR hazards
```
I: DSUB x4, x1, x3 <--- NOTE THAT I AND J CANNOT BE REORDERED
J: DADD x1, x2, x3
K: XOR  x6, x1, x7
```

This is called an “anti-dependency” - it results from reuse of the name “x1”. It should not stall, but from the machine view the pipeline would stall (WAR).

A WAR hazard points to the left.

We can add temporary registers to avoid such hazards.

#### Output dependencies and WAW hazards
```
I: DSUB x1, x4, x3 <--- NOTE THAT I AND J CANNOT BE REORDERED
J: DADD x1, x2, x3
K: XOR  x6, x1, x7
```

This is an output dependency which also results from the reuse of the name “x1”.
And such dependencies cause WAW (write after write) hazards.

WAW hazards point from left to left.

### Pipelined Function Units
![[Pasted image 20241019185806.png]]
Maybe we can take the approach of using different pipelining function units for different operations. But this comes with great responsibility.
- Longer RAW hazards.
- Structure hazards for MEM, WB.
	- Since multiple units are running in parallel we might have concurrent accesses to memory from the different instructions.

In the case of independent instructions, this is awesome. But if the instructions are not independent what should we do?

![[Pasted image 20241019190014.png]]
We still have to stall a long time. 
In the above, timing assumes we stall instructions at the latest pipeline stage possible before operand value is used (Rather than stalling at IF/ID).


##### Scoreboard: tracking register accesses
For each register, track “**will be written to by in-flight instruction**” info.
![[Pasted image 20241019190339.png]]
“Note that reading instructions will not set the bit.”
- If new instruction **reads or will write** a register with the bit set, the instruction will stall in decode state.
- **set bit** for destination register at end of **decode**, **clear bit** when instruction reaches **write-back**.

##### In-order scoreboard execution
**scoreboard**: a bit-array, 1-bit for each GPR (general purpose register)
- allows issue in-order: RF ← Fn(RS, RT)
	- If SB[RS] or SB[RT] is set → RAW, stall
	- if SB[RD] is set → WAW, stall
	- Else, dispatch to FU (Fn) and set SB[RD]
- allows complete out-of-oder
	- Update GPR[RD], clear SB[RD]

##### However..
Structural Hazards is not solved. (from scoreboards)
![[Pasted image 20241019191139.png]]

In theory, only LD uses MEM on cycle 10, but definitely MUL.D and ADD.D and LD all want to use WB on cycle 11 → which causes a structural hazard.

We can stall, but for how many cycles is the question.
→ The idea is to maintain a shift register to maintain a “schedule” for when WB is busy.
We need to know the Latency of the current operation for this.
If the bit $N$ is 1, then the WB stage will be busy $N+M$ cycles from now. (where $M$ is the minimum number of cycles between decode and write-back).

==This was possible for processors in the 80s,90s. Now we have caches, we can’t really estimate how long a memory stage would take anymore!==

