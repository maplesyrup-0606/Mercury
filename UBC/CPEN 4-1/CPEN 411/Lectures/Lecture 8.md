## Virtual Memory
![[Pasted image 20240929180745.png]]
It is basically lying that you have more memory than you actually have.

When running code, we do not specify:
- Which part of the memory the code is going to be in.
	- Don’t specify it’s address, we only know we have it.
	- We let the OS/HW manage access to allocated memory.

How do we know the address specified for a specific memory is contiguous, secured and access is seamless?


**Problem: OS wants to multitask (Time-multiplex)**
- But all programs assume address space starts at 0. (In fact, that’s a highly low chance of happening)
- There’s enough physical RAM to run one program, but not enough to fit them all at once.

**Solution: Separate the address space per program**
- Each program has a separate address space ID (`ASID`).
- Program executes using virtual addresses (`VA`).
- CPU + OS translates to physical addresses (`PA`).
	- {ASID 42, VA 0xdeadbeef} != {ASID 17, VA 0xdeadbeef}
	- They will map to different physical addresses.


### Multiple programs using memory
![[Pasted image 20240929182219.png]]
1. OS starts, reserves some memory.
2. Browser starts, wants memory.
3. Word starts, wants memory.
4. Open webpage: browser allocates more memory.
5. Open another word doc, word allocates more memory.
6. Open webpage, allocate more memory for browser (memory capacity exceeds).
7. User edits doc, wants more memory.

**Total is more than physical memory!**
- Also possible in memory with more than 1 user sharing memory.

### Fragmentation
Now from the previous example, say that the user exited word.

![[Pasted image 20240929182412.png]]
Now the memory is fragmented. But what if we wanted to play a game or run something?
We do not have enough RAM to run those applications! (assuming they require more than the screenshot above.)

- We want contiguous addresses.
- We can’t move the browsers (there are pointers pointing to the green memory).
	- High overhead exists of moving the browser memory.

**Having ASID was not enough! → We need a more fine grain approach (not course grain).**
**Only a fraction of the allocated memory is actually used.**

### Paged Virtual Memory
![[Pasted image 20240929183250.png]]

The program has virtual addresses starting from 0 to some address. We don’t use large size chunks and map them to a physical address.

*Instead, we use smaller chunks (pages) and several of them to map each chunk to physical addresses.*

Notice that, some pages are going to the disk (cold pages), the virtual address is not used as much and is placed on the disk. While other frequent ones get placed on the main memory space.

It is also possible to not have contiguous physical addresses. 

Also moving pages from/to the hard disk or pages expiring is possible → making other programs being able to use the free space.
- **Caveat**: We need a mechanism for address translation while maintaining user security.

**Program View (Virtual Space):**
- Nice contiguous address space.
- Can always allocate more.
	- Can allocate much more memory than physical address space.

**Main Memory View**:
- Fragmented, non-contiguous (holes).
- Out-of-order, some on the disk.

==Physical Page and Virtual Page are the same size.==
### Address Translation
![[Pasted image 20240929184148.png]]

We have a 32bit virtual address and a 30bit physical address. Both containing a 12bit page offset.

**Virtual Address**
Then we have 2^12 = 4KB pages and 2^20 = 1Million of them (Normally, the page offset is not translated. We only translate the leftover 20bits).

**Physical Address**
We have the same size pages but 2^(30-12) = 2^18 = 256K of them.

*Need to go from 1M → 256K, while ensuring page offset remains constant.*

### Page Table
A table that contains all of the translation information.
![[Pasted image 20240929184912.png]]
**Page Table Register:**
Tells where the page table is for that process.

**Page Table:**
Takes Virtual Page Number to index to one of the entries in the physical page number.
These locations would give an address in the physical memory space.

In the above example, for each process, the physical memory space was 1/4 th of the virtual memory space (1M vs. 256K). → *All the locations cannot be full in the page table.*

That’s why some page table entries tell that the page is on the disk (as shown in the screenshot).

**What’s the problem with this?**
- If we compute the size of the page table, we have 2^20 locations in the page table.
- Each location has a valid bit, 18 bits for the physical page number.
	- **For one process!**
$$\text{Total size } = 19 \times 2^{20} = 2.4\text{MB / process}$$

- Assume the virtual address was 2^32 Bytes, nowadays it is 2^64 Bytes.
$$\text{Total size}_{\text{new}} = 19 \times 2^{52} = 1\text{Billion Bytes / process.}  $$
**Impractical amount of memory overheads are required! And the storage isn’t even that large!**

#### Where do we put the page table?
- option 1: **on-chip** near the CPU (L1$).
	- pros: very fast access.
	- cons: many entries >> any reasonable L1$.
- option 2: **off-ship** in main memory.
	- pros: *might* actually fit.
	- cons:
		- access is very slow. (but must be done up to 2x per instr)
		- per-process tables still take up lots of memory.

### Efficient Page Table Storage
Each process needs its own page table & page tables are sparse (few programs use the entire address space) 
=> There exists a substantial memory overhead to store all page tables.

The solution was to use **multi-level PTs**
- Top-level table in RAM.
- Next level is either in RAM or paged out to disk

```
[P1 Index | P1 Index | Page offset]
```

![[Pasted image 20241015192214.png]]

This way if the page is not used it is the second level PT is not allocated.
Hence, memory is not used for not allocated pages (or unused pages).
=> Effective size of Page Table is remained small.

However, there still exists a disadvantage. That is there exists a delay due to look up latency.

#### Translation-related Exceptions
**Page Fault**:
- Page is accessible, but it is sitting on the disk.
- *Not a program error*.
- Resume to instruction once the page is placed in the RAM (need to recover from disk).

**Segmentation Fault / General Protection Fault**:
- Page is not user-accessible (maybe not accessible for that specific user).
- Page is R/O but tried to write / exec.
- Program is terminated (unless caught).
- Meltdown avoided this by miss-peculating.


#### Translation Lookaside Buffer (TLB)
The TLB acts as a cache for the page table. It is a small structure, so can be FA.
![[Pasted image 20241015192544.png]]
If translation is valid / present → read out the physical address from the TLB. (One TLB for each core)

We have valid bits to represent if the translation is valid, and hence can be used. While there could also be permission bits (read-only, execute), sharing info and etc.

#### Instruction Cache access with Address Translation
Let’s say we wanted to run an instruction.

1. Look up the ITLB to see if a valid translation exists.
	1. If hit, proceed with that physical address.
	2. If miss, proceed with translation and get physical address.
2. Translate VA to PA (as mentioned above).
3. Access Instruction Cache.
	1. Check the Tag from physical address and compare with the tag from the cache.
		1. If hit, W.
		2. If miss, welp gonna take a while to get it.

![[Pasted image 20241015193251.png]]

What is the problem here? Let’s consider the situation where looking up the TLB takes 2 cycles and the looking up the cache takes 5 cycles. (assuming they’re both hits)

**Physically Addressed Cache**
![[Pasted image 20241015193405.png]]
If the TLB look up and Cache look up take 2 and 5 cycles each. 40\% of the time is being used in the TLB look up and delaying cache access. → The Ogs did not like this happening.


**Virtually Addressed Cache**:
![[Pasted image 20241015194032.png]]
Now the L1$ has no access latency, but most VA start at 0 so for certain addresses contention can happen. Also, during a context switch numerous cache-lines are flushed and brought back. There also exists more complex management since the nature of how VA is used (it is not unique).

**Overlap Cache access with VA translation**:
![[Pasted image 20241015194225.png]]
This is using the crucial fact that *not all portions of the virtual address is being translated*.
We know that only the first 20 bits (for example) are being translated while the other bits are used for page offset etc. 

For instance,
```
VA - [Translated Portion 20 bits | Not Translated Portion 12 bits]
												/        \
											Index bits	Cache line bits
```

We run both L1$ look up and TLB look up in parallel, assuming we get hits, during the TLB look up we can use the left over non-translated bits to index into the cache.

1. TLB look up & Cache Look up
	1. In Cache Look up,
		1. Cache Controller uses index bits to select sets in the $n$ ways.
		2. Byte Select bits are used to get the data at that certain Byte offset.
2. Once Cache Look up is done,
	1. Compare all the tags and fetch if it is a hit.
	2. This tag is obtained at translation (in parallel)

![[Pasted image 20241015195059.png]]

##### Virtually addressed, Physically tagged Cache
The problem is that some address bits can **change**, that is we may have a overlap in bits that use address translation and cache indexing.

Consider the following case,
```
[                       |  $idx (7 bits) | offset (6 bits)]
[    virtual page number (20 bits) | page offset (12bits) ]
```
In this case, if we have two programs with the same last 12 bits but different 13th bit, we are fine.

But if we also have the same 13th bit, we might end up in the same place for two different programs.


**Possible Solutions**:
- Bigger Page Size → In the above case, if we use 8KB pages we can solve the problem.
- OS guarantees `VA[13]==PA[13]` in this case. Having a unique bit per program.
- bite the bullet and deal with the **synonym problem**.

#### Synonym Problem
The synonym problem is when several VA’s map to the same PA.

Consider the example,
- 64KB DM $, 16B blocks.
	- 4 bits for block offset: `addr[3:0]`
	- 12 bits for cache index: `addr[15:4]`
- 4KB Pages.
	- 12 bits for page offset: `addr[11:0]`

Basically, the problem arises from the fact that the bits used from cache indexing overlap with the address translation. The same physical address can be mapped to different locations in the cache, hence leading to a coherence problem.
#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 9|Lecture 9]]


