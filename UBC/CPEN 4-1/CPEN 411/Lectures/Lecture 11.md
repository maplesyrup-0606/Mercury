#### Register Renaming by Hand
Hazard observation:
- WAW and WAR come from **name dependencies**.
- **No values are transferred** between the instructions.
- What if we had an infinite supply of names?

Original Code:
```
LD R1, 0(R2)
DADD R3, R1, E3
DADDUI R2, R2, #8
LD R1, 0(R2)
```

For each `Rd` give a fresh `Tn`,
```
LD T1, 0(R2) ; R2 -> T1
DADD T2, T1, R3 ; R3 -> T2
DADDUI T3, R2, #8 ; R2 -> T3
LD T4, 0(T3) ; R1 -> T4
```

We removed WAW, WAR but there is still a RAW hazard across 1→2 and 3→4

IBM 360 model 91 floating unit (mid 1960s):
- FU latencies: mul 6, div 10, add 2, load 8
- FP ISA is Rd ← Rd p Rs
- ISA has 4 FP registers

Can we change ISA? → We want binary compatibility.
Scoreboard? → Stalls for WAW and WAR hazards.

***Don’t track register names, track data dependencies directly.***

#### Tomasulo Algorithm Hardware
- **Reservation Stations (RSs)** in front of each FU.
	- Buffer instructions waiting for operands.
- Registers in instructions renamed to **tags (essentially temporary regs)**.
	- Destination register gets fresh tag - mapping to reg. alias table (RAT).
	- Source registers get corresponding tags from RAT.
	- Can have more physical registers than ISA registers.
	- Tracks data dependencies directly: no WAW or WAR hazards.
- Results broadcasted on **common data bus (CDB)**.
	- Each results carries tag of source RS.
	- all RSs and the RF listen to the CDB for tags they want values for tag of interest on CDB pick up associated value.


[Stages of algorithm]
- Issue (after decode)
	- If we have free RS (assuming structural hazard), **allocate RS entry**.
	- Lookup source operand registers in RF; get either **values** or **tag**.
	- **Rename destination register** to allocated **RS entry tag** (always). 
- Execute
	- Listen for unready operand **tags** on the CDB, snarf values.
	- Once all operands ready, commence execution.
- Write Result (before End)
	- Broadcast **<dst tag, result>** on the CDB.
	- Interested RSs and RF will see the tag and update value.
	- Mark reservation station available.

[Design Tradeoffs]
- Complexity.
- CDB limits performance.
- Only one FU can complete per cycle.
	- Multiple CDBs: more FU logic for parallel assoc. stores.
- Non-precise interrupts.

#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 12|Lecture 12]]

