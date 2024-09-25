# Caches / Prefetching

## Available Technologies

**DRAM**
- Dense and cheap.
- But is slow.

**SRAM**
- ~5 x **more area per bit** → This is totally based on fabrication.
- **Fast**
	- Small (4KB) SRAM: 0.2ns Access.
	- Big (32MB) SRAM: 5ns Access.
		- Still fast comparing to DRAM.

***Fundamental Problem***:
- We can have either **big** or **fast** but ==**not both**==.

## Memory Hierarchy
![[Pasted image 20240923121029.png]]

## What should we keep in Cache?
```c
void saxpy(float a, float *X, float *Y, unsigned N) {
	for(int i = 0; i < N; i ++) {
		Y[i] = a*X[i] + Y[i];
	}
}
```

**Do we notice any locality?**:
- We read and write to `Y[i]` → ***Temporal Locality***
- We read `X[0]` then `X[1], X[2] ...` → ***Spatial Locality***

***Caches Explore Patterns..***

#### Temporal Locality
If the program accesses a single location, then accesses it soon there after.

Ex: `Y[i] = a*X[i] + Y[i]`
```c
1: L.S F1, 0(R1) // read X[i]
2: MUL.S F2, F1, F0 // a * X[i]
3: L.S F3, 0(R2) // read Y[i] <-- Temporal Locality
4: ADD.S F4, F2, F3 // a*X[i] + Y[i] <-- Spacial Locality 
5: S.S F4, 0(R2) // write Y[i] <-- Temporal Locality
```

#### Exploiting Temporal Locality
The Idea is to **keep a copy of the recently accessed data nearby**. (for instance, in a small fast memory).

![[Pasted image 20240923121905.png]]

#### Exploiting Spacial Locality
After accessing one location, **the program accesses nearby locations**.
The Idea is when **filling a cache entry, also transfer adjacent data.**
![[Pasted image 20240923124823.png]]
#### Managing Fast Storage

- Option 1 : **scratchpad**
	- Program copies most useful data.
	- Used in GPUs and other contexts.
- Option 2 : **cache**
	- *Managed automatically in hardware.*
	- Hardware keeps track of locality patterns.
	- Functionally transparent to programmers.
	- Used in most CPUs and GPUs.

**Why is the fact that it is managed by hardware so important?**
→ Cache can’t give priority as well as can’t ask for priority. It is hard to manage but all programmers do not need to care.


- GPU cache is used for special applications, we know entirely which application is being ran on it.
- Have a lot of control on how caches be influenced.


#### Fully Associative Cache
![[Pasted image 20240923122450.png]]
- Tags are full addresses.
- We track data through dirty bits and valid bits.

#### Set Associative Caches and Direct Mapped Caches
![[Pasted image 20240923125026.png]]
In reality, when accessing caches, we access via the cache controller.
When doing so, a set associative cache, divides the whole cache into $n$ ways and $m$ sets.
- Ways - The number of blocks as seen in the photo (used for parallel access).
- Sets - The number of cache lines within those “ways”.

**What is a fully associative cache?**
A fully associative cache are those with $n$ ways and 1 set. We need to access $n$ sets in parallel.

→ When using big memory, it is physically impossible to make an $n$ way cache.

**How about a direct mapped cache?**
It is completely the opposite, it has 1 way and $n$ sets.


#### Next Lecture [[Lecture 7]]
