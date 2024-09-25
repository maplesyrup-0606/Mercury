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