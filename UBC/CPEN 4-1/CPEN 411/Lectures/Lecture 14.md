If we say we have an accuracy of predicting the right branch at 90%, is this actually a really good branch predictor? If we have multiple branches, say 100 in a row, then the probability of predicting all correct becomes 0.9^100 = 0.0026561399% → Pretty hard to so..


#### Intro
- We know how to **speculate** on branch outcomes.
- How do we predict them?
- What results / information do we require?

#### Two problems of branch instructions
- Problem 1: **branch direction (taken / not-taken)**
	- Hardware to predict this: *branch predictor*
- Problem 2: If taken, what is the **target PC**?
	- Hardware to do this: *branch target buffer*

#### Branch Predictors
###### Intuition
- Observation: **Many branches are predictable**
- Insight: **History repeats itself**
	- If branch taken many times recently → we should probably take it again!
- Cunning Plan:
	- record *past behaviour of this branch*.
	- next time encountering the branch, *predict the same thing (if confident)*.

###### Example
```
loop: ...
      ...
      dsubi r1, r1, #1
      benz r1, loop ; say it was taken 9 times, not taken at the end (once)
```
Observations:
- The last outcome of this branch is good (but not a perfect) prediction.
- We know the specific PC the branch instruction is executed.
	- Relies only on the *branch instruction’s PC*.

==Let’s look up the PC, get the last outcome.==
==To know the PC, do we need to decode the instruction? → No, it is already known at fetch.==


#### 1-Bit Branch Predictor
![[Screenshot 2024-12-06 at 1.25.29 PM.png]]
We have a $2^n \times {1}\text{ bit}$ branch history table (BHT). If we look at the red entry, the output is 0 → This corresponds to the actual previous outcome.
- 1 → taken (T) last time.
- 0 → not taken (NT) last time.

How are the entries selected though?
![[Screenshot 2024-12-06 at 1.27.01 PM.png]]
Given a PC, we use a specific range of the PC. In the example above, we have $2^n$ rows so we would use a total of $n$ bits.
- Yes, this will have congestion in the case the range is too small.
	- We might hash these to normalize the congestion.

###### 1-Bit Branch Predictor Rules
- Step 1: **Prediction**
	- Use subset of *branch PC* to access prediction table.
	- If table entry is 1, *predict taken*; otherwise not-taken.
- Step 2: **Update**
	- Resolve branch in execute stage.
	- Update table entry for branch PC with *actual outcome*.
	- What if branch is resolved but still speculative?
		- This means what if the branch was resolved but cannot be committed? ![[Screenshot 2024-12-06 at 1.31.53 PM.png]]
		- Wait till it is committed!
	- May be many many cycles later!

###### Example 2
```
loop: ...
      ...
      dsubi r1, r1, #1
      benz r1, loop ; say it was taken 9 times, not taken at the end (once)
```
Assume this loop above is nested inside another loop.

We can analyze the outcome and predictions,
```
                   1234567890123456789012...
Actual outcome   : TTTTTTTTTNTTTTTTTTNTTT...
Predicted outcome: ?TTTTTTTTTNTTTTTTTTNTT...
```
We can see that at the end of the loop + the start of the next loop that we have incorrect predictions. → There are 2 mis-predictions each time a loop is encountered.

**Problem**: A brach that is **almost** always taken (not-taken) *will mis-predict twice* each time branch is not-taken (taken).

==We need to track more history..!!==

#### More Intuition
Observation: **one-bit history** is not enough.
- We only know something happened last time.
- We don’t know if it happens **usually**.
	- 2 mis-predictions for every “exception to the rule”.

Insight: can we keep *longer history*?
- If last $n$ branches taken → probably next one is also taken.
- If last not taken but previous $n-1$ taken → taken is **probably still a good guess**.

#### 2-Bit “Saturating Counter” Predictor
![[Screenshot 2024-12-06 at 1.42.27 PM.png]]
- 2-bit counter.
- +1 after taken branch.
- -1 after not-taken branch.
- prediction = *most significant bit*.
	- In the case above, if we divide by 2 → we would get the most significant bit.

![[Screenshot 2024-12-06 at 1.43.21 PM.png]]
What is the new size? → We have $2^n \times 2\text{ bit}$ tables, the size has increased by 2. That is quite a significant size increase just for one more bit.

- Row contents specify current state → ex) Row $00_{2}$ = 00, not-taken state.
- Prediction is based on *current state*.
- When actual outcome is known, *advance FSM*.
	- Each row’s FSM is trained independently.

If we try the original example with the new branch predictor,
```
loop: ...
      ...
      dsubi r1, r1, #1
      benz r1, loop ; say it was taken 9 times, not taken at the end (once)
```
```
                   1234567890123456789012...
Actual outcome   : TTTTTTTTTNTTTTTTTTNTTT...
Predicted outcome: ?TTTTTTTTTTTTTTTTTTTTT...
```
Now there is 1 mis-prediction each time a loop is encountered.

#### 3-Bit  “Saturating Counter” Predictor
![[Screenshot 2024-12-06 at 1.47.42 PM.png]]
We are just tracking more history with the cost of increase in size.

- How many row entries (rows) in a 12KB BHT that stores 3-bit saturating counters?
$$12\text{KB} / 3\text{bit}= 12 \times 2^{10} \times 8 \text{bits} / 3\text{bit}=32 \times 2^{10} = 32\text{KB rows}$$
#### FAQ
- Branch prediction **only makes predictions**.
	- Predictions **are not necessary for correct execution**.
	- Correct predictions improve performance.
	- Predictions **must be verified** by executing branch.
		- Can’t squash the branch instruction itself.
- **Tradeoff** between table size and accuracy.
	- Good metric: **MPKI** (mis-predictions per kilo instrs.)
	- This is better than % since % gives no notion of # of instructions.

==It’s purely an optimization of performance, not correction of performance.==

#### Branch Target Buffer (BTB)
We need something that holds the PC to go to, since the branch prediction table only gives whether the branch should be taken or not.

![[Screenshot 2024-12-06 at 1.57.02 PM.png]]

#### Function calls…
Let’s consider the following code,
```C
for(;;){                                      print(...){
...                                              ...
                                                 return;
print(...); // first function call              
...                                           }
print(...); // second function call
...
print(...); // third function call
...
}
```
Would our BTB mentioned above work for the following case?
→ We have three `print` calls, each with different PCs originating from. Then, whenever we call it with a different PC originating from, the `print` function call would have the previous return address.
	→ ==Mis-predicted return address for every `print` return.==


We need a way to manage targets for function calls… since the return address depends on where the function was called from.

##### Return Address Stack
Special case for function call / return.
- Hardware can distinguish these from other jumps.
	- We can differ the process of getting the PC just for function calls.

![[Screenshot 2024-12-06 at 2.03.17 PM.png]]

#### Correlated Branch
Let’s have the following C code,
```c
if (d==0) // b1
	d = 1;

if (d==1) { // b2
 ...
}
```

Let’s see the assembly for the same code,
```
BNEZ R1, L1 ;branch b1 (d != 0)
DADDI R1, R0, #1 ; R1 = d + 1

L1:
DADDI R3, R1, #-1 ; R3 = d - 1
BNEZ R3, L2 ; branch b2 (d != 1)

...


L2:
```

The outcome of one branch can affect the outcome of another branch. → It becomes much harder to predict.

Consider the initial values for d = 0, 1, 2 (Assume predictor initialized to not-taken):

| init d. | d==0? | b1  | value of d before b2 | d==1? | b2  |
| ------- | ----- | --- | -------------------- | ----- | --- |
| 0       | yes   | N   | 1                    | yes   | N   |
| 1       | no    | T   | 1                    | yes   | N   |
| 2       | no    | T   | 2                    | no    | T   |
We can see that one branch affected how the second branch’s outcome.

###### cont’d
Let’s simulate the behaviour of a simple 1-bit predictor (all tables entries are initialized to “not taken”). Consider when d alternates from 2 to 0 : d = 2,0,2,0…


| d=? | b1 pred. | b1 act. | new b1 pred. | b2 pred. | b2 act. | new b2 pred. |
| --- | -------- | ------- | ------------ | -------- | ------- | ------------ |
| 2   | N        | T       | T            | N        | T       | T            |
| 0   | T        | N       | N            | T        | N       | N            |
| 2   | N        | T       | T            | N        | T       | T            |
| 0   | T        | N       | N            | T        | N       | N            |
***It is never predicting accurately!***
→ What if we use a 2-bits? Also, it really depends on the starting state as well.

If we take a look at the branches, ***If b1 is not taken → b2 is also not taken.*** There’s a correlation!

###### Why are branch outcomes correlated?
We know that if a branch is,
- taken: PC + X
- not taken: fall through, PC + 1

```c
x = 0;
if (cond1) { /* branch A */
	x = 3;
}

if (cond2) { /* branch B */
	y += 19;
}

if (x <= 0) { /* branch C */
	doSomething();
}
```
Say `cond1` was True, then branch C will never be taken. branch A is an affecter branch.

###### 1-Bit Branch Predictor + 1-Bit Correlation
![[Screenshot 2024-12-06 at 2.23.26 PM.png]]
- One table for each **context**: previous is T? previous is NT?
- use PC to index both tables, use context to choose among the tables.

This is different to a 2-bit saturating counter in how it takes into account of the actual code.

If previous is NT? → Index in first table; otherwise second table.

###### Example
Consider behaviour of a 1-bit predictor with one bit of correlation history.. if d alternates from 2 to 0: d=2, 0, 2, 0 …

```
BNEZ R1, L1 ;branch b1 (d != 0)
DADDI R1, R0, #1 ; R1 = d + 1

L1:
DADDI R3, R1, #-1 ; R3 = d - 1
BNEZ R3, L2 ; branch b2 (d != 1)

...


L2:
```

| d=? | b1 pred. | b1 act. | new b1 pred. | b2 pred. | b2 act. | new b2 pred. |
| --- | -------- | ------- | ------------ | -------- | ------- | ------------ |
| 2   | **N**/N  | T       | **T**/N      | N/**N**  | T       | N/**T**      |
| 0   | T/**N**  | N       | T/**N**      | **N**/T  | N       | **N**/T      |
| 2   | **T**/N  | T       | **T**/N      | N/**T**  | T       | N/**T**      |
| 0   | T/**N**  | N       | T/**N**      | **N**/T  | N       | **N**/T      |
We only have 2 miss-predictions now! (With the same setup)

#### Others
We can also have 2-bit predictors with 1-bit of correlation!
![[Screenshot 2024-12-06 at 2.42.06 PM.png]]
The size is indeed larger now. Also, depending on how much context we want the size changes larger. If we want to keep track of the previous $n$ branches, we want $2^n$ tables each with the same bits for the saturating count. 

==Design tradeoffs!!!!!==

#### Correlating against Multiple Branches
- Problem: relevant context **not immediate**.
	- e.g., a few branches up.
- Solution: *track $n$ last branches*.
	- We need a shift register to keep track of the history.
		- This is different to a 2-bit saturating counter.
		- This could be done by GBHR (Global Branch History Register).


#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 15|Lecture 15]]

