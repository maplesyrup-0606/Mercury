#### Real Number Representation
Let’s look at an instance of the floating point representation,
$$\text{fl}(x) = \pm d_{0}d_{1}\cdots d_{t-1} \times 10^e$$
$$= \pm \left(  \frac{d_{0}}{10^0} + \frac{d_{1}}{10} + \cdots + \frac{d_{t-2}}{10^{t-2}} + \frac{d_{t-1}}{10^{t-1}}  \right) \times 10^e$$

for $t=4,e=0$,
$$\frac{8}{3} \approx \left( \frac{2}{10^0} + \frac{6}{10} + \frac{6}{10^2} + \frac{7}{10^3} \right) \times 10^0 = 2.667 \times 10^0$$

==Note that we use the normalized floating point representation by letting $d_0 >0$.==

#### General Floating Point System
We define it by $(\beta, t, L, U)$, where:
- $\beta$ : base of the number system.
- $t$ : precision (number of digits).
- $L$ : lower bound on exponent $e$.
- $U$ : upper bound on exponent $e$.

For each $x \in \mathbb{R}$ corresponds a normalized floating point representation,
$$\text{fl}(x) = \pm \left( \frac{d_{0}}{\beta_{0}} + \frac{d_{1}}{\beta_{1}} + \cdots + \frac{d_{t-1}}{\beta_{t-1}} \right) \times \beta^e$$
where $0 \leq d_{i} \leq \beta - 1$, $d_{0}>0$  and $L \leq e\leq U$.


###### Binary floating point system
Standard floating point systems are typically binary: $\beta =2$. For these systems, we can gain a leading bit if we normalize, because we can only have $d_{0}=1$. So, the significand is in practice larger by one than the number of bits it occupies.

Modern binary floating point systems guarantee that the relative error in the presentation, 
$$ \frac{\lvert \text{fl} (x) - x \rvert }{\lvert x \rvert } $$
is bounded by 
$$ \eta = \frac{1}{2} \times 2^{-t} $$

e.g.
Suppose 
$$(\beta,t,L,U) = (10,4,-2,1)$$

The **largest number** is $9.999 \times 10^U = 9.999 \times 10^1$.
The **smallest positive number** is $1.000 \times 10^{L} = 1.000 \times 10^{-2}$.

[i-clicker]
![[Screenshot 2025-01-30 at 8.18.35 PM.png]]
Suppose we have the number in the form,
$$ \pm d_{0}.d_{1}d_{2}d_{3} \times \beta^e$$
For $d_{0}$, we have 9 possibilities. For $d_{1},d_{2}$ and $d_{3}$, 10 possibilities.
$\beta$ is fixed and we have $1 - (-2) + 1= 4$ possibilities for $t$.

Hence,
$$9 \times 10 \times 10 \times 10 \times 4 = 36,000$$

###### Error in floating point number representation
**Chopping**:
$$\text{fl}(x) = \pm d_{0}.d_{1}d_{2}d_{3} \dots d_{t-1} \times \beta^e$$
The absolute error is bounded by $\beta^{1-t} \cdot \beta^e$.

**Rounding**:
$$\text{fl}(x) = 
\begin{cases}
\pm d_{0}.d_{1}d_{2}d_{3}\dots d_{t-1} \times \beta^e \quad d_{t} < \frac{\beta}{2} \\
\pm (d_{0}.d_{1}d_{2}d_{3} \dots d_{t-1} + \beta^{1-t}) \times \beta^e, d_{t} > \frac{\beta}{2} \\
\end{cases}
$$

round to even in case of a tie.
Absolute error bounded by,
$$ \frac{1}{2} \times \beta^{1-t} \times \beta^e $$

Relative error bounded by **rounded unit**,
$$\eta= \frac{1}{2} \times \beta^{1-t}$$

###### Floating point arithmetic
Important to use **exact rounding**: if $\text{fl}(x)$ and $\text{fl}(y)$ are machine numbers, then
$$\text{fl}(\text{fl}(x) \pm \text{fl}(y)) = (\text{fl}(x) \pm \text{fl}(y))(1+\epsilon_{1})$$
$$\text{fl}(\text{fl}(x) \times \text{fl}(y)) = (\text{fl}(x) \times \text{fl}(y))(1+\epsilon_{2})$$
$$\text{fl}(\text{fl}(x) /\text{fl}(y)) = (\text{fl}(x) / \text{fl}(y))(1+\epsilon_{3})$$
where each $\lvert \epsilon_{i} \rvert \leq \eta$.

→ Thus, the **relative errors** remain small after each such operation. This is achieved using what is known as guard digits.

###### Roundoff errors
Roundoff errors are **inevitable**: triggered by representation of numbers on a floating point system or arithmetic operations; relative errors bounded by the machine rounding unit.

- In general, if $E_{n}$ is error after $n$ elementary operations, cannot avoid linear roundoff error accumulation$$E_{n} \simeq c_{0}nE_{0} $$
- Will not tolerate an **exponential** error growth such as $$E_{n} \simeq c_{1}^nE_{0} \text{ for some constant }c_{1} > 1$$
	- An unstable algorithm.

#### Next Lecture [[UBC/CPEN 4-2/CPSC 303/Lectures/Lecture 3|Lecture 3]]
