When considering load / store operations, what is the fundamental difference among the two?

Let’s consider the two instructions `str x1, 0(R2)` and `ld x1, x3, #8`. We have to wait for a load to happen in order to use the value, *but in the case of a store* we just have to send it out and dip. → Loads are on the critical, stores are (usually) not.

#### Load bypassing
```
sw r2, 0(r9)
lw r2, 0(r8)
addi r4, r2, #0xf00
```
Is this set of instructions hazard-less? → No, what if `r8,r9` have the same value? → In that case, we need to ensure that these store and loads are in-order so that the `add` gets the right `r2`.

- Loads are on the critical path, stores are (usually) not.
- Would like to use cache bandwidth for loads and send stores to the cache when free (~20% better performance in general).

#### Store Buffer
The idea is to “**delay stores** until bandwidth available.”
- Queue stores in a **store buffer**.
- Allows loads to **bypass**.
- If the store is still in ROB, **mark as non-committed**.
- If store retired from ROB, **mark as committed**.

![[Screenshot 2024-12-09 at 2.22.33 PM.png]]
What is the benefit of this buffer?
→ Either cache or LSQ has latest state, so when LSQ is full we start writing things to the cache.
→ If we have back-to-back stores, we just need to edit the buffer rather than waste the bandwidth.

If we look at the design of this, does this have the capacity to allow by-passed loads?
→ *No, we don’t have a mechanism for re-ordering loads and stores. We only have the capacity of O.O execution.* [Load by-passing ensures that the data is prepared in the right order, as shown in the first example.]

==No way to check for dependencies among instructions!==
![[Screenshot 2024-12-09 at 2.29.28 PM.png]]
If the committed store that was buffered has `D'` in `addr(A)` and a load instruction requests for data at `addr(A)` then if it is not written to the cache yet (due to the fact that the buffer is not full) the `load` would get the stale data.

#### Back to Load bypassing
```
sw r2, 0(r9)
lw r2, 0(r8)
addi r4, r2, #0xf00
```
If instructions 1 and 2 are dependent, we cannot do any load by passing (it cannot be moved above `sw`). 

==Loads can bypass stores **only if** their results do not depend on previous stores.==

But before deciding to execute a load, we must check for dependencies vs. **the whole store buffer**,
- *For un-committed stores*: These are check since the stores are speculative, we cannot know until a branch is resolved whether to commit it or not. In the case of a match, but false prediction, we just flush the load as well. 
- *For committed stores*: If a match exists, we fetch from the store directly without the need to wait for fetching from the memory.
- *No match*: We let the load proceed hence by-pass the registers.


#### Load bypassing so far
- Store executed in a store buffer.
- If load address matches in the store buffer, stall.
- Is stalling always necessary?
- What if store value is already available?

```
sw r4, 0(r9)
lw r2, 0(r8)
addi r4, r2, #0xf00
```
- on RAW dependency: if store *value is known*, there is no need to stall → just forward it.
- Value can be forwarded directly to waiting load (additional ~5% performance).

**It’s kind of different with bypassing,** 
- **If memory dependency → forward.**
- **if no memory dependency → bypass.**

#### Dependencies?? Resolved??
- Problem: must wait until **addresses resolved** to determine if there is a dependency.
	- ==It is possible that uncommitted stores don’t have addresses resolved.==
		- Maybe it is waiting for a `add` instruction to compute the addresses.
- Idea: **speculate** no dependency, **cancel** if wrong. (Guess!)
	- As stores, complete, cancel mix-executed code (roll-back).
- Better alternative: **memory dependency prediction**.
![[Screenshot 2024-12-09 at 3.27.36 PM.png]]
Basically, before the addresses are resolved we do two predictions,
1. An address won’t exist, and we bypass.
2. An address will exist, and we forward.

Based on these predictions, the load instruction would proceed with a bypass or a forward.
→ Once, the store resolves an address and checks the prediction unit. It can check if the load prediction unit has made the right prediction.

In case of a,
- Right prediction: Mark the stores as committed and proceed.
- Wrong prediction: Roll-back, we fucked up.

![[Screenshot 2024-12-09 at 3.57.43 PM.png]]

#### Next Lecture [[Lecture 17 & 18|Lecture 17 & 18]]
