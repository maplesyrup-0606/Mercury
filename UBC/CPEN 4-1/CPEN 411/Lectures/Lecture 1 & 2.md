## Iron Law
![[Pasted image 20240909125643.png]]
Each $i_j$ refers to each instruction, and $CPI \hspace{.1in} (\text{Cycles per Instruction})$ refers to the number of cycles by that certain instruction $i_j$.

The Iron Law measures Performance in terms of these metrics,
$$\frac{\text{CPU time}}{\text{Program}} = \frac{\text{Instructions}}{\text{Program}}\times \frac{\text{Clock Cycles}}{\text{Instructions}}\times \frac{\text{Seconds}}{\text{Clock Cycle}}$$
a.k.a
$$\text{Execution Time} = \frac{1}{\text{Performance}} = (\text{Instruction Count})\times (\text{CPI})\times (\text{cycle time})$$

- Instruction Count : **Algorithm**
- CPI : **Architecture / Design**
- Cycle Time : **Frequency**

So we eventually want a smarter architecture to reduce CPI (and have a high IPC).

Let’s try some examples,

#### EX1
Say we want to add a new instruction to the processor, and the measures are as the following:
- cycle_time (with) = 1.05 * cycle_time (w/o)
- IC (with) = 0.99 * IC (w/o)
- CPI (with) = 1.01 * CPI (w/o)
Should we implement it?

Let’s do the calculations,

Execution Time (with) = 1.05 x 0.99 x 1.01 x Execution Time (w/o) = 1.05 x Execution Time (w/o)
The speed up is 1 / 1.049895 = 0.95, so we do not want to implement it.



**However**,
![[Pasted image 20240909130640.png]]

We have to keep in mind that often when we try to reduce one factor in the processor performance equation, ***another factor increases***.

Optimizable features,

|            | Inst Count | CPI | Clock Rate |
| ---------- | ---------- | --- | ---------- |
| Program    | x          | x   |            |
| Compiler   | x          | x   |            |
| Inst set   | x          | x   | x          |
| micro arch |            | x   | x          |
| technology |            | x   | x          |

## Amdahl’s Law
Amdahl’s Law is a formula which gives the theoretical speedup in latency of a task at fixed workload.

![[Pasted image 20240909131306.png]]

$$\text{ExTime}_{\text{new}} = \text{ExTime}_{\text{old}} \times \left[(1-\text{Fraction}_{\text{Enhanced}}) + \frac{\text{Fraction}_{\text{Enhanced}}}{\text{Speedup}_{\text{Enhanced}}}\right] $$
$$\text{Speedup}_{\text{overall}} = \frac{\text{ExTime}_{\text{old}}}{\text{ExTime}_{\text{new}}} = \frac{1}{\left[(1-\text{Fraction}_{\text{Enhanced}}) + \frac{\text{Fraction}_{\text{Enhanced}}}{\text{Speedup}_{\text{Enhanced}}}\right]}$$
$$\text{Speedup}_{\text{maximum}} = \frac{1}{1-\text{Fraction}_{\text{enhanced}}}$$

But let’s try out some examples,

#### EX2
Floating Point (FP) Square Root (FPQSR)
- 20% of ExTime_old due to FPQSR
- 50% of ExTime_old due to **all** FP operations
- We have to alternatives
	1. Speedup FPQSR by a factor of 10
	2. Speedup all FP operations by a factor of 1.6

Which alternative is better?

$$1.\hspace{.2in}\frac{1}{1-0.2+\frac{0.2}{10}} = 1.22$$
$$2. \hspace{.2in} \frac{1}{1-0.5+\frac{0.5}{1.6}} = 1.23$$
## Power Consumption / Dissipation

### Power (1 / 2)
For CMOS chips, traditional dominant energy consumption has been in switching transistors, called ***dynamic power***.
$$\text{Power}_{\text{dynamic}} = \frac{1}{2} \times \text{Capacitive Load} \times \text{Voltage}^2 \times \text{Frequency Switched}$$
- For mobile devices, energy is a better metric,
$$\text{Energy}_{\text{dynamic}} = \text{Capacitive Load} \times \text{Voltage}^2$$
1. Capacitive load is a function of the number of transistors connected to output and technology, which determines the **capacitance of wires and transistors.**
2. Dropping voltage helps both power and energy.
3. For a fixed task, *slowing down the clock rate* (frequency switch) reduces power, but **not energy**. (However, slowing down the clock rate may allow voltage to decrease).
4. **Clock gating** is common, saves energy and dynamic power. 
	→ turning off clock for a certain peripheral.

### Power (2 / 2)
Even when a transistor is off there exists leakage in current flows, so **static power** is important.
$$\text{Power}_{\text{static}} = \text{Current}_{\text{Static}}\times\text{Voltage}$$
- Leakage current increases in processors with smaller transistor sizes.
- Increasing the number of transistors increases power even if they are turned off.
- Very low power systems even **gate voltage** to inactive modules.


#### Next Lecture [[UBC/CPEN 4-1/CPEN 411/Lectures/Lecture 3|Lecture 3]]

