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
- Also possible in memory with more than 1 user sharing memory.\

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

Also moving pages from / to the hard disk or pages expiring is possible → making other programs being able to use the free space.
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

#### Next Lecture [[Lecture 9]]
