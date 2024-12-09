Memory needs to be consistent among multiple cores (processes), we need all cores to be having fresh copies without any issues. Especially with caches (per core), it is more important to maintain consistency among these processes.

#### Problems with multiple copies
![[Screenshot 2024-12-06 at 3.07.33 PM.png]]
Look at the setup above, now let’s assume that P3 update the value of `u` to 7. It would write to its own cache.

What’s the problem? → P3 only wrote it to its own cache, other Processes have no idea if the value of `u` that they hold (if in cache) is a stale or not.

![[Screenshot 2024-12-06 at 3.08.53 PM.png]]
- We need to let others know about the new value of `u`.
- Value being written back to memory is **not well defined**:
	- Really depends on which cache evicts the block first so that the new value is written into memory.

#### Single Write, Multiple Readers
![[Screenshot 2024-12-06 at 3.10.16 PM.png]]
For a write, we have only one owner doing all the memory write etc. Once a read hits, we can have multiple owners so that this is a fresh value.

Problems? → During the store, we can have the ROB being filled. While non-independent instructions can be safely completed, if the ROB of other cores have the `load A` instruction → the cores have to be stalled. The `load` cannot even be executed since memory won’t be consistent.

==We want to split events based on space not time, we can lock certain regions in memory rather than locking the whole memory when a writing operation happens.==

#### Coherence Invariants
- Single Write Multiple Readers Invariant (SWMR)
	- If *multiple* copies of a cache block exist, all are **read-only**.
	- A **read-write** copy of a block must be the **only** copy.
		- If shared: read-only, if one has it all others are invalidated.
- Data Value Invariant
	- Value of a memory location $A$ at the start of an epoch $n$ equals the value of $A$ at the end of epoch $n-1$.
- *Must hold separately for every cache block (spatial)!*

On boundaries,
![[Screenshot 2024-12-06 at 3.17.49 PM.png]]
Basically if writing, we have to invalidate others. → We can only have one writeable copy at a time (among all cores).

If shared among different cores → make sure it is read-only.

#### MSI protocol
- **INVALID (I)**: the block may not be read or written.
- **SHARED (S)**: the block may be read but not written.
- **MODIFIED (M)**: the block may be read or written.
	- Only one holder exists.

*coherence protocol: mechanism for updating all coherence states to maintain coherence invariants.*

![[Screenshot 2024-12-06 at 3.21.34 PM.png]]
- CPI + cache units are connected via a single bus.
	- We can assume atomic and instant.
- A cache can be accessed by CPU or bus.
- Need a *cache controller* to update states.

#### Cache Controller

#####  Core Requests
1. Receive load / store from core.
2. Update state of block.
3. Issue coherence request.
4. Receive response.
5. Update state of block.
6. Reply to core.
![[Screenshot 2024-12-06 at 3.23.54 PM.png]]

##### Bus Requests
1. Receive coherence request.
2. Update state of block.
3. Issue coherence response.

#### Snooping Cache Coherence Protocol
- Observation: All cache-memory requests *cross the bus*.
- Idea: *Snoop* other caches’ bus requests, update our own coherence states.

![[Screenshot 2024-12-06 at 3.26.12 PM.png]]

#### Cache Block States
- Memory point of view (implicit):
	- **I**: No cache has a copy (all invalid)
	- **S**: Multiple caches have clean copies.
	- **M**: One cache has dirty copy.
- Cache point of view (explicit):
	- **I**: Block not cached (Have useless copy).
	- **S**: Block cached, read permissions only.
	- **M**: Block cached, read / write permissions (for that core only)


###### Read Hits
![[Screenshot 2024-12-06 at 3.40.43 PM.png]]
Let’s say that P2 reads a certain part of memory and it hits in its $.
- Read hit (block is in S or M): Have a valid copy → use it.
- No bus messages required (we know nobody has M copy whether its S or M).

###### Read Misses
![[Screenshot 2024-12-06 at 3.42.35 PM.png]]
Let’s say that Pn had a read miss and P1 had a M copy of the memory in its cache.
- Read miss (block is in I): Send a read request on the bus.
- If another cache has block in M state (P1 only has the fresh copy), it will downgrade to S and sends us the latest value.
- If no cache block is in M or S, memory up-to-date, will respond.

If P1 was in S, no downgrade is needed.

###### Write Hits
![[Screenshot 2024-12-06 at 3.46.52 PM.png]]
Let’s say now Pn has a write hit in its $.
- If block is in M: update cached data.
	- No bus messages, we know nobody else has a copy.
- If block is in S: update cached data + invalid others.
	- Need to use bus to invalidate others.

###### Write Misses
![[Screenshot 2024-12-06 at 3.49.15 PM.png]]
Now Pn tried to write, but found that the block was invalidated → hence a miss.
- Write miss (block in I): send **write** request on bus.
- If another cache has block in M state, it will invalidate block and send us the latest value.
- If no cache has block in M,S → memory is up-to-date, will respond.

- Write miss (block in S): send **invalidate** request on bus.
- If another cache has block, it must be in S state; will **invalidate** block (since we already have the latest value).
==It’s a write miss since the cache block is not in a valid state to write in.==

###### Example
![[Screenshot 2024-12-06 at 4.01.14 PM.png]]
And consider the operation `P1: read 100`

Let’s first see where the tag `100` exists. 
```
P1: B0 [I, 00 | 00]
P2: None
P3: B0 [I, 00 | 00]
P4: B0 [1, 00 | 00]
Memory: [00 | 07]
```

P1 is currently in invalid state, it’s a read miss! → Also, other cores are also invalid. We only have the choice to find it in memory..

Therefore, the following operation(s) are:
```
P1: B0 [S, 00 | 07]
```


**Wait wait wait..** Why do we update to S state? shouldn’t it be updated to M state?
→ If we look at the operation, we are ***reading*** not **writing**. Hence, we update to S not M.

![[Screenshot 2024-12-06 at 4.09.54 PM.png]]
Now, let’s consider the operation: `P4: read 118`

Let’s then look at the cache blocks,
```
P1: B3 [M , 80 | 40]
P2: B3 [I , 80 | 00]
P3: B3 [M , 00 | 28] // tag is 138
Memory: [80 | 00]
```

We can see that `P1` has it in M state, it has the most recent value!
We need to get the value from `P1` M to S.

Thus, the following operations are
```
P1: B3 [S, 80 | 40]
P4: B3 [S, 80 | 40]
Memory: [80 | 40] tag 118
```

If we see what’s interesting, not only do we downgrade `P1` to S state. But we also have to update memory!

Now, another one
![[Screenshot 2024-12-06 at 4.14.36 PM.png]]
operation: `P1: read 138`, there’s no 138 in `P1` though?

```
P3: B3 [M, 00 | 28]
Memory: [00 | 00] tag.138
```

Similarly we have to downgrade `P3` to S state and update the memory with the appropriate value. 

But… wasn’t `P1` filled with a different block in `B3`? Yes, so we have to evict it. If we look closer at `B3` the value is in M state, so when evicting the memory also has to be updated.

```
P1: B3 [S, 00 | 28]
P3: B3 [S, 00 | 28]
Memory: tag.118 [00 | 40] // evict comes first!
Memory: tag.138 [00 | 28]
```

#### Limits of bus-based interconnects

- High core count → bus is too slow.
	- Takes longer for end-to-end communication.
- Multi-cycle interconnect.
- Neither instant nor atomic !!!!
	- Have to find something else.

##### Directory-based cache coherence
- Idea: send all messages via a directory.
	- Directory knows all shares and state for a block.
	- Usually attached to memory.
- Directory entry for each block:
	- Presence bit-vector (sharer set)
	- dirty bit (indicates M state)
	- other reps possible.
	- tracked *explicitly*.

###### Directory Protocol
- locations
	- **local** node: originating cache.
	- **home** node: directory location (where data lives).
	- **remote** node: cache with copy (the one needed to be invalidated)

So to summarize it, **we have a home node for each place in the memory.** So if we want to access some address X → we have to contact a specific home node.

The remote node is where the valid data exists as seen from the home node. 

The local node is the one that wants something.

You can be a Local and a home node, but you wouldn’t be a remote node and a home node.


*life of an example request*:
- local → home (get S)
- home → remote (invalidate if in M)
- remote → home (invalidate acknowledge)
- home → local (grant S)

#### Coherence Misses
- We talked about a few cache misses:
	- Cold - block never seen before.
	- Capacity - cache too small.
	- Conflict - not enough associativity.

- Fourth C in multiprocessors / multicores:
	- Coherence miss - not enough coherence permissions.

###### Types of misses
- True sharing: real communication between cores
	- C0 reads cache block to access word 3.
	- C1 writes word 3, invalidates C0’s copy of block.
- False sharing: same block, different word.
	- C0 reads cache block to access word 3.
	- C1 writes word 5, invalidates whole cache block (C0’s copy of the block).


#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 16|Lecture 16]]
