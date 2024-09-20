## Ideal Main Memory
- Zero cost
- Zero latency
- Infinite bandwidth
- Infinite capacity
- Zero error rate
If we have a very small memory + optimized technology → We will have very low latency and high bandwidth.

On the other hand, if we have a very large memory + commodity → We will have high latency and low bandwidth. Yet, we have high capacity.

Ideally, we want the latency / bandwidth benefits along with the capacity benefits for ideal memory.

## Memory Addressing Patterns

|                    | random access                                    | associative lookup                               |
| ------------------ | ------------------------------------------------ | ------------------------------------------------ |
| **access pattern** | address → data                                   | key → has a match?                               |
| **example apps**   | register file, main memory, direct-mapped caches | associative caches / TLBs, load-store queue etc. |
| **technology**     | SRAM, DRAM, RF                                   | CAM                                              |

## RAM addressing
![[Screenshot 2024-09-15 at 3.08.33 PM.png]]
**Word line : refers to the row being selected.**
**Bit line : refers to the column(s) being selected.**


Each cell stores data.
1. `addr[n - 1 : k]` selects the row (activates the line of row cells).
2. `addr[k - 1 : 0]` selects the word (column | bunch of bit lines).
	-  In each column, we have a bunch of bit lines, unlike the row decoder. (The above example selects two bits of columns)
	- In bit addressable memory, we only read a bit from the column decoder. (But this is inefficient.)
	- In general, we group 64 bytes of data and filter out (by a different unit) the bytes that are actually needed.
		- We use something called spacial locality for instance of accessing arrays and etc.
3. column decoder selects a pair of cells in that row and reads data out.

- Ideally we want $n \approx m$, the number of bit lines and the size of the word line should be similar.
	- The length of the word / bit line determines capacitance and the worst case latency would be the end of each row and column.
		- Then we just replicate to form units of memory (4mb, 8gb etc.).

Example of spacial locality,
```
Array[0] <-- In int8
Array[1]
Array[2]

If we fetch 64B of data for 2ns.

[                                   ]
	^A[0] ^A[1]
	
So accessing A[1] is much faster since we fetched 64B of data in the first place.
```

### RAM read operation
![[Screenshot 2024-09-15 at 3.35.25 PM.png]]

- We select a row to read from.
- We pre-charge the the columns (a.k.a condition the bit lines to be ready).
	- Bit line conditioning is done while the rows are selected to parallelize it.
- Activated to select the bit line (column) we want to read and the data is sent to sense amplifiers.
	- Sense amplifiers convert voltages to a binary.

### RAM write operation
![[Screenshot 2024-09-15 at 3.41.30 PM.png]]

- Select a row of cells.
- Pre-charge the bit line.
- Drive the data to the cells (and overwrite the data inside the cells).

**What is the purpose of bit line conditioning? → Prepare the bit-line to have a reference voltage.**

**If we wanted to do a thing where we want to update 8 bytes of the 64 byte bit line what would we do ? → We would do a thing called a read modified write, we simply read the 64 bytes and update the 8 bytes and then re-write the updated 64 bytes back into memory.**

### How to store bits
![[Screenshot 2024-09-15 at 3.49.11 PM.png]]

In a DRAM, each of the cells would be a capacitor. Or for SRAM, we can have the following two structures to store data.

Since each cell is very expensive, we use back to back inverters (the third figure above).

The capacitor can keep data for some time (**passive**) without a power source (low power overhead). While as the CMOS transistors require a power source (**active**) (more power overhead).

CMOS transistors have feedback, so they are more robust and less error correction is needed. On the other hand, capacitors are more prone to errors since there is no feedback.

### SRAM Cell
![[Screenshot 2024-09-15 at 3.53.10 PM.png]]

- **reading** 
	- pre-charge both bit lines **high**.
	- cell will pull down one of the bit lines.
- **writing**
	- same pre-charging.
	- one bit line pulls cell down.

### DRAM Cell
![[Screenshot 2024-09-15 at 3.55.20 PM.png]]

- Cheap 1T + 1C structures.
- **read**
	- pre-charge bit line to 1/2 Vdd.
	- Capacity changes bit line V a little bit.
	- read **destructive**: write value back.
- requires refresh
	- capacitor loses charge over time.
	- need to **refresh** (read and write value back) ever so often.

#### Next Lecture [[CPEN/CPEN 4-1/CPEN 411/Lectures/Lecture 5|Lecture 5]]
