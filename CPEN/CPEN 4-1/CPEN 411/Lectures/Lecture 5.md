## DRAM cell
![[Screenshot 2024-09-18 at 11.24.53 AM.png]]

- 1T (transistor) + 1C (capacitor): cheap as chips.
- **read operation**:
	- pre-charge bitline to $\frac{1}{2}V_{\text{DD}}$.
		- Needed to make a reference voltage to determine cell value.
	- Capacity changes bit line $V$ by a little bit.
	- read **destructive**: writes value back to the cell after read.

#### Read Operation
![[Screenshot 2024-09-18 at 2.20.24 PM.png]]

All things, such as the **bit line, word line and the cell** have a capacitance $C$.
The **sense amplifier** detects the change in voltage and amplifies that outside in to the ADC.

*It is important to know that pre-charging the word line and bit line require a lot of energy since they are long.*

Let’s see the few steps of how reading happens.


![[Screenshot 2024-09-18 at 2.24.24 PM.png]]

##### Pre-charging
In this step, the bit line voltage is tuned to $\frac{1}{2}V_{\text{DD}}$.

##### Turn on the word line
Depending on if the cell was 1 or 2 the bit line as a change in voltage. Which is $V_{\text{DD}} \pm \Delta$. 
Which is further amplified by the sense amplifiers to make digital 1, 0.

##### Reinforce
When the bit line voltage gets discharged to 0 (a.k.a the cell has been removed).
Hence, a reinforcement step is required to recover the value read from the cell.


#### Spacial Locality
![[Screenshot 2024-09-18 at 2.28.43 PM.png]]

Let’s consider the figure, it takes 45ns to access the row and hence reading the whole row into the sense amplifiers. 
Then it takes an extra 2ns to extract / edit the values to the structure that holds the data for consecutive accesses (Assume the 45ns includes the first data access as well).

For this type of spacial locality, the following average time for accesses is established:
$$n = 1, \hspace{.1in}45\text{ns}$$
$$n = 2, \hspace{.1in} \frac{45+2}{2} = 27.5\text{ns}$$
$$n = 3, \hspace{.1in} \frac{45+2 + 2}{3} \approx 16\text{ns}$$

![[Screenshot 2024-09-18 at 2.33.51 PM.png]]
So we can see that the average latency reduces for more accesses.

***What if we made the word line smaller?*** → We would consume less energy for each row, however we wouldn’t be able to exploit spacial locality as much.


## DRAM Structure
- **Row buffer**
	- a few KB → so that we use spacial locality.
	- **open row policy**:
		- Keep the word line activated so that the sense amplifier holds data.
		- Repeat the precharge → Energy consumption would be high.
		- We hope for the same hit, or else we have latency in accessing a different word line.
	- **closed row policy**:
		- Instead of keeping the word line activated, we turn it off and precharge a different word line.
		- We assume that we have to access a different wordline.
		- Would be inefficient if we had subsequent address accesses.
	- Scheduling becomes important!

#### Next Lecture [[CPEN/CPEN 4-1/CPEN 411/Lectures/Lecture 6|Lecture 6]]
