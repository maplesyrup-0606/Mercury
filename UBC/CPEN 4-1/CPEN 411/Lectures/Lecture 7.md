### Block Offsets
![[Screenshot 2024-09-25 at 10.30.44 AM.png]]
Look up at the tag, if the tag matches and based on the offset within the data we fetch the right data.

## Problems with fully associative caches
![[Pasted image 20240925103433.png]]

#### How does computer architecture join here?
1. Caches exploit spacial / temporal locality
	1. Our programs are consisted of loops and etc.
2. If we have a cache, and an enormous memory → There exists a lot of conflict for each line.
		![[Pasted image 20240925103659.png]]
3. If we compare the hit rate (mainly versus Directly mapped and Fully associative)
		![[Pasted image 20240925103747.png]]
		DM is more efficient (+ simpler design) but the problem is that we have to much conflicts. → lower hit rate.
		On the other hand, a fully associative cache will have a higher hit rate. → The cost is way too high due to how complex it is to design.
		*The biggest bump comes from moving from a DM to a 2-way set associative cache.*



==People realized that we don’t need a FA, we might rather have a 4-way or a 8-way set associative cache.==

### Direct Mapped Cache
![[Screenshot 2024-09-25 at 10.47.37 AM.png]]
In this case, we have 4 byte blocks hence $\log_{2}{4} =2$ bits are used for block offset.
We have 1024 rows, so index is $\log_{2}{1024}= 10$ bits are used for the index bits.

## Problem: Conflicts!
![[Pasted image 20240925104925.png]]
It doesn’t matter how large the cache is, they just end up evicting each other out!

### Solution: Set-associative Cache
![[Screenshot 2024-09-25 at 10.52.03 AM.png]]
The idea is to **use cache index to select a set of blocks**,
- Say, 4 or 16 blocks.
- Each set is like a **small fully associative cache**.

When looking up on a cache:
1. Select a set.
2. Compare tage in parallel.
3. Retrieve the block with the matching tag.

Then if it hits we read the data, else don’t.

## What if the cache (or set) is full?
We need to choose some valid blocks to evict. But, **which block in a set should we evict?**
→ That’s why there exists cache replacement policies.

![[Screenshot 2024-09-25 at 10.56.41 AM.png]]
Though one is DM and the other is FA, we still have
$$\frac{64\text{MB}}{64\text{B}} = 2^{20} \text{ lines in the cache.}$$
**But**, in a *DA the number of sets are the number of lines in the cache*, and in a *FA the number of ways are the numbers of lines in the cache*.

When we have an index we look up a set,
- In a DM: We look up one line,![[Screenshot 2024-09-25 at 11.05.50 AM.png]]
- In a FA: We look up in each line,![[Screenshot 2024-09-25 at 11.06.10 AM.png]]

The **index** gives you the set number, not if the line is present or not. We verify via the tag to either know if the line exists or not. → And thus figure if it’s a hit or not.

==Anyways, we need to go through all of the bits, tag, index and etc. to figure out anything.==

##### Belay-optimal replacement
We evict a block that is going to be re-referenced **furthest in the future.**
→ It is *optimal*, we need to know the future to apply such a policy. 
→ Hardware does not know the future, **we need a prediction mechanism.**


### Reuse Distance
Consider accesses to blocks A, B, C, D, and E. And the following access pattern,
$$\text{A BB C B CC D BB E D BBB A}$$

- Between to accesses of A,
	- We have a total of 14 accesses.
	- And there are for unique blocks, $\text{B, C, D, E}$.

The reuse distance for A $= \# \text{ of unique blocks} = 4$.

![[Screenshot 2024-09-25 at 11.21.06 AM.png]]
- Typically, **recently used** data is accessed more frequently → ex. loops

==Workload characterization is key in computer architecture.== → We want to find out how workloads behave so that we don’t over optimize the system.


### Replacement Policy
An algorithm that is used to decide which block should be evicted.

Some ideas are,
- Random (works better than expected)
- LFU (least frequently used)
	- We keep track of # of accesses to each block.
- LRU (least recently used)
	- We keep track of time or order of accesses.

#### Random Replacement
Select victim uniformly at random. 
- pros: Don’t need to remember anything.
- But how well does it work?

	Consider the access pattern $\text{AAAABAAAACAAAAD...}$,
	- With a 32-entry FA cache & random RP
		- What is the miss rate if we always evict A?
		- What is the lowest possible hit rate of $(\text{AAAAx})^n$

#### LRU
Keep a timestamp per each cache block.
- Time stamps tend to be large → So it becomes expensive in terms of area and power.

Two-way set associative: one LRU bit.
- If last touched left-way, LRU bit → 0
- If last touched right-way, LRU bit → 1
- If bit is 0, replace right, else left.

ex.
![[Screenshot 2024-09-25 at 11.31.54 AM.png]]
If access pattern is AAAABC,
1. Access A first, set LRU to 0.
2. Again, reinforce to 0.
3. Same.
4. Same.
5. Access B, replace LRU to 1.
6. Access C, we look at LRU bit: [1] → Then A gets evicted.

**But,** if we have > 2 ways, we incorporate pseudo-LRU (pLRU)
- MRU bit per block, clear all when all set.
- Reference prediction value (RRPV) per block, set to max at insert or hit, decrement over time.


### The 3 Cs (3 types of misses)

**Cold start** misses
- first time a block is accessed.
- increasing size or associativity does not help.
- can increase block size, considering spacial locality.

**Capacity** misses
- Access wouldn’t be a miss if cache were infinite.
	- Try to fit in the workload is a modern approach (for instance, browsers).
	- Difference between fully associative (assumed) and infinite-size cache.

**Conflict** misses
- set size < # accesses that map to given set.
- access wouldn’t be a miss if cache were fully associative.

## Victim Caches
There were some problems of fully associative caches,
- Lots of associativity is good, but expensive.
- Some sets require more associativity.

![[Pasted image 20241014153312.png]]

The **idea** was to have a “small fully associative cache” the stores recently evicted lines.
- On evict, place it in victim $.
- On hit in victim $, bring it to normal $.
- Managed with LRU (for instance) just like a normal cache.
- Effectively extra associativity for some lines.
	- Can’t make it large, but placed near to L1 $.
	- Tries to improve reuse.


### Writes that hit in the Cache
Say for the instruction `sw R1, 0(R2)` which stores a word (hence a write).

#### Write-Through Cache
On hit, updates cache and memory at the same time. 

Pros:
- Simple to implement.
- Memory is always valid, no need to write extra to the memory.

Cons:
- Performance cost is high.

#### Write-Back Cache
Data in the cache is managed by a modified (dirty) bit. When this cache line is evicted the memory is updated.

Hence, the cache contains the latest data. Has best design performance.

#### Write-Evict Cache
The Cache always remains clean (no dirty lines exist). There is no modified bit. 
When a write operation occurs, it is written straight to memory, and if the data is present in the cache, it is evicted (invalidated).

### Writes that miss in the Cache

#### Write-Allocate
When writing to memory locations not in cache, we allocate a cache block for the location and write the data to the cache.

#### Write-No-Allocate
If a cache miss occurs, we directly write to the memory (No dirty line exists).

Only store in cache for reads since no memory updated is needed.

### Evictions in a Cache Hierarchy

#### Inclusive
![[Pasted image 20241014154630.png]]

If data is in L1 Cache, it also exists in LLC (or lower) cache. If invalidated in L1$ also evicted in LLC (or lower) $.

Capacity: $max(x,y)$ where $x,y$ denote the size of LLC / L1 $.

It is efficient since, if we know that the data does not exist in higher level cache, there is no need to go to lower level caches. Also, if data exists in Lower Level Cache, we can go to higher level cache and reduce latency since it would exist in higher level caches for sure. So other cores can get an advantage of going to upper level caches to save latency.

#### Exclusive
![[Pasted image 20241014154902.png]]

If data exists in L1$, does not exist in LLC (or lower level) $. When L1 cache evict happens, data is spilled to other level caches to ensure that data is still accessible.

Capacity: $x+y$ where $x,y$ is size of caches.

#### Non-Inclusive 
Somewhere in between the above, don’t know whether some data would be included in L1 or LLC or both at the same time. Evicting is independent. Capacity is also somewhere in between.


##### Two points about reads and writes
**Considering a load access to a cache: can this a memory write?**
→ Yes, if dirty / modified data is evicted, then we have to write that to memory to keep the memory valid.

**Considering a store access to cache, can this cause a memory read?**
→ Yes, if cache is write-allocate, we have to fetch and read from memory after evicting the memory that was inside the cache.

## Lockup-free Caches
The problem now is that there is only one outstanding cache miss → and this might take 100s of cycles.

The **idea** is MSHRs (miss status handling registers)
- Contain block address and offset.
- Dst tag (or reg) for a load, value for a store.
- CPU *continues executing*.
- Broadcast value of CDB after miss serviced.
- Can **merge multiple requests to same address** (must be careful in order).


##### Ex.
Consider a FA cache, eight 16 Byte blocks, empty $ MSHRs, all empty memory access are very long (100s of cycles).

The load sequence: 0, 8, 16, 4, 12, 20, 24, 32, 128, 96, 64

```
MSHR0 - 0 8 4 12 
MSHR1 - 16 20 24 
MSHR2 - 32
MSHR3 - 128
```

So 96 will be stall since there is no space for 96 to go into the MSHR.

### Pre-fetching

The access pattern might be predictable, e.g., `x[0],x[8],x[16],x[24] ..` .
→ For this example, with 8 Byte values and 64 Byte blocks: we will keep getting cold misses.

But since we know the pattern in advance, we can just **prefetch**!

Tradeoffs:
- Effective only if *accurate* and *timely*.
- If not, wastes valuable memory bandwidth.
- Real prefetchers turn off if ineffective.

#### Stream buffer
The idea is to “buffer sequential access stream”.
→ Maybe several buffers for multiple streams.

If we get a hit in the stream buffer, move to the $ (only the hit), prefetch next.

The problem is if the access is not in a stream if might not work (e.g. jump accesses).

#### Stride Prefetcher
The accesses as mentioned above, might not be adjacent. We can multiple access streams with different strides.

The **idea** is to track the previous address, stride and correctness. → If predictions are confirmed, keep prefetching.


![[Pasted image 20241014160936.png]]

##### Ex
Let’s consider the access sequence: 4, 8, 12, 16, 10, 20, 30, 40

```
prev | stride | state | prefetch
0      0		    init    -
4      4        trans   -
8      4        steady  12
12     4        steady  16
16     4        steady  20
10     4        init    -
20     10       steady  30
30     10       steady  40
40     10       steady  50
```

#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 8|Lecture 8]]

