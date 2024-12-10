We’re going to talk about memory consistency now, how is it different with coherence?
Consistency defines the order in which memory operations appear across all processors.

#### Communication via shared memory
Let’s see when two processes are sharing some memory among them.
![[Screenshot 2024-12-09 at 6.49.27 PM.png]]
We need to make sure core 0 finished writing **before** core 1 starts reading.
→ What could happen if we don’t ensure this? The read would read stale values without the opportunity to see the updated value of the shared data structure.

###### Ordering accesses to shared memory
Consider the following,
```
thread A (C0)                          thread B

S1: store data = NEW
S2: store flag = SET   --------------  L1: load x1 <- flag
                                       B1: if x1 is not SET: goto L1
                                       L2: load x2 <- data
```
In this example, regardless of thread A, thread B would stall until the flag is updated (assuming initially data = 0 and flag != SET). And `data,flag` are shared memory.

What ordering is **required** for correctness?
- A. `S1` before `S2`
- B. `S2` before `L1`
- C. `L1` before `L2`
- both A and C
- all of A,B and C

In order for correctness, it is obvious that `S1` should come before `S2` and `L1` should come before `L2`.
But what about, `S2` and `L1`? → Is the program wrong if `S2` doesn’t come before `L1`?
Not necessarily, especially in this case, thread B would just loop until the appropriate `x1` is set. 

==Don’t need `S2` before `L1`!!!==

![[Screenshot 2024-12-09 at 6.57.23 PM.png]]

What is important here is the order in which order the threads, individually, advance the instructions. We cannot re-order → correctness can’t be assured.

- `flag` communicates that all data has been written.
- It is not cool to read data before write is finished.
- Not cool to write data after we claim we’re done.

With no other mechanisms, re-ordering might hurt correctness. But at the same time, restricting order ==limits performance==.

When are memory ordering restrictions needed?
- in multi-cores?
- in single-cores?
- both multi and single cores?


Ordering restriction is needed
- **within single core** because of multiple concurrent threads.
- **within multiple cores** obviously we have multiple threads/channels.


###### Memory access reordering
When can memory access reordering happen?
- programmer’s head
- compiler optimization
- inside CPU core
	- store buffer / LSQ, prefetching, speculation…
- interconnect (some cores might be near each other)
- in RAM

#### Memory consistency model
- Rules that specify what sequences of memory states may be observed by different threads / cores / RAM.
- Equivalently, the **allowed memory access orderings** as observed by different threads / cores / RAM.
- Equivalently, rules about which stores may be **sources** for a specific load.

##### “Ideal” consistency model
- Memory ordering as seen by everyone reflects physical order of events.
- **Physically impossible**.
	- What if events occur precisely concurrent.
	- Information transfer speed is limited by a finite amount.

#### Sequential Consistency (SC)
A multiprocessor system is **sequentially consistent** if:
- the result of **any execution** is the same as if the operations of all processors were executed in **some sequential order**.
- the operations of **each individual processor** appear in this sequence in the **order specified by its program**.

==Essentially, within each core, the order of the instructions execution has to be the same.==
![[Screenshot 2024-12-09 at 7.10.31 PM.png]]
And memory will be updated in many many permutations possible.
Is the the programmer’s responsibility to write a program that would produce the right result.

###### Checking if an execution is SC
![[Screenshot 2024-12-09 at 7.12.00 PM.png]]
- Draw lines for cores, memory.
- Plot memory ops in program order.
- Connect to memory line.
- If lines don’t cross then it is sequentially consistent.

Each left and right, should have no crossing. Each section should have its order ensured.

###### Example
```
				t0:mem[X]=mem[Y]=0

core A:                                 core B:

A1: store X <- 1                        B1: store Y <- 1
A2: load x1 <- Y                        B2: load x2 <- X
```
Assuming this is an SC system, what are the possible values of x1 and x2 after **both threads** have finished?

| x1  | x2  | SC Ordering  |
| --- | --- | ------------ |
| 1   | 1   | A1 B1 A2 B2  |
| 1   | 0   | B1 B2 A1 A2  |
| 0   | 1   | A1 A2 B1 B2  |
| 0   | 0   | Impossible ! |
Why is x1=0 and x2=0 not possible?
→ A possible ordering for this outcome is “A2 B2 A1 B1” or a similar permutation as long as “A2, B2” comes before “A1, B1”.

But this considers re-ordering, in a SC system, we cannot have instructions happening in a non-sequential order!

##### Same code, with store buffer / LSQ
Now we allow re-ordering, so load store by-passing is possible.
```
				t0:mem[X]=mem[Y]=0

core A:                                 core B:

A2: load x1 <- Y                        B1: store Y <- 1
A1: store X <- 1                        B2: load x2 <- X
```
Does core A have a memory dependency between A1 and A2? → No, these instructions are not dependent within core A.
=> We can **bypass**! (memory dependencies are checked within one core!!)

Now the outcome of “A2 B1 B2 A1” will be x1=0 and x2=0!

###### Implications for reordering load/stores
A **sequentially consistent** system must maintain:
- **load < load** ordering.
- **load < store** ordering.
- **store < store** ordering.
- **store < load** ordering.
for accesses to **all addresses** within each core.

#### Back to the main story…
![[Screenshot 2024-12-09 at 7.27.03 PM.png]]
What are the true logical constraints of this situation?
- **green** write accesses can be out-of-order if all finish before the **blue** read starts.
- **blue** read accesses can be out-of-order if none start before the **green** writes finish.

Essentially, if the read-write dependencies are not a problem → We can freely re-order anything within those boundaries.

Idea: Allow arbitrary reordering, **except for synchronization ops**.

#### Weak Ordering (WO)
![[Screenshot 2024-12-09 at 7.45.41 PM.png]]
- Before synchronization operations: finish all prior load/store ← can be re-ordered.
- Before any load/store: finish all prior synchronization operations.
- **Synchronization operations are sequentially consistent.**

As long as the synchronization operations are in the order we want, we can re-order what ever comes before or later.

##### Hardware Support: Memory Fences
```
thread A                                      thread B
S1: store data = NEW                          L1: load x1 <- flag
-------------------------------fence----------------------------------------
S2: store flag = SET                          B1: if x1 is not SET: goto L1
                                              L2: load x2 <- data
```
- Special **memory fence (memory barrier)** instructions.
- Fences ordered like synchronization operations.
	- $\text{prior mem ops} <_{\text{depend}} \text{ fence } <_{\text{depend}} \text{ subsequent mem ops}$


##### Illustrating weak ordering and fences
![[Screenshot 2024-12-09 at 7.52.47 PM.png]]
- Draw memory operations, allow reordering.
- Draw fences.
- Make sure **nothing crosses fences**.
- Make sure **fences are sequentially consistent**.
==All processes are synchronized at the fences.==

###### Are full fences too strong?
Yes, we are forcefully stopping all processes to stop at some memory fence. This will make it less performant since every object will just stop and not do anything till all fences reach the memory fence.

Idea: separate **stores-go-before** and **loads-go-after** synchronization operations.

#### Release Consistency (RC)
![[Screenshot 2024-12-09 at 7.55.55 PM.png]]
- Before **release store**: finish all prior load / store.
- Before any load / store: finish all prior **acquire** loads.
- Allows optimizations like store buffer / LSQ (re-ordering is possible).

##### Illustration
![[Screenshot 2024-12-09 at 7.57.55 PM.png]]
- Draw memory operations, allow reordering.
- Draw Fences.
- Make sure **no load / store leak past release**.
- Make sure **no load / store leak before acquire**.

How is this different from weak consistency?
→ For weak consistency, we have a memory fence that blocks all operations from crossing the fence line. But in release consistency, these operations can cross the somewhat fence like thing as long as they don’t cross the next release / acquire.

The,
- **reordered loads and stores**: all finish before release.
	- We can do this freely since all groups of instructions will see a next release.
	- As long as they are independent load / store instructions, we can have instructions after the release be re-ordered before the release anywhere.
- For acquire, it’s the opposite.

==This can happen between two processes, not all.==

#### Store Atomicity
SC requires that all processor cores observe **the same memory operation order**.

Store Atomicity,
- if one processor observed our write.
- then everyone else observed it too.
- Relaxing this can break *causality*.


```
P1                P2                             P3
----------------------------------------------------------------------------
A = 1; ---------> while (A == 0);
                  B = 1; ----------------------> while (B == 0);
                                                 print A;
```
- lack of store atomicity can break causality.
- P3 may see the new B but not see the new A even though P2 saw A before changing B.
- implies special global-scope fence operation.
