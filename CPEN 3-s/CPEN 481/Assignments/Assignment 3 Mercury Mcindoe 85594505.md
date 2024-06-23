         
## Problem 1

Let’s first get the interest for the sub-period ($i_s$),
$$i_s = \frac{4\%}{12} = \frac{1}{300
}$$

Given the future, $F$, of \$1,000,000, we can the monthly saving $A$ as,

$$\$1000000 \cdot \frac{i_s}{(1+i_s)^{500} - 1} = \$778.846$$

Therefore, \$779/month.

## Problem 2

Let’s convert the initial cost of \$35000 and the salvage value of \$40000 to an annual cost-benefit,

$$-\$35000 \cdot \frac{0.08\cdot 1.08^8}{1.08^8-1} = -\$6090.5166  $$
$$\$40000 \cdot \frac{0.08}{1.08^8-1} = \$3760.59$$

Given the annual net saving of \$2,000, per year the equivalent annual(A) is

$$-\$6090.5166 + \$3760.59 + \$2000 = -\$329.926$$

So roughly -\$330 a year, this is not desirable.

## Problem 3

**(a)**
The nominal interest rate is 4.2\%, thus the sub-period interest becomes $i_s = 4.2\%/12$.
25 years becomes $N = 25 \cdot 12 = 300$ months.

$$ A=  \$445000 \cdot \frac{i_s(1 + i_s)^{300}}{(1+i_s)^{300} - 1} = \$2398.293/\text{month}$$

Thus, \$2398 /month.

**(b)**

$$\$445000 \cdot \frac{i_s(1 + i_s)^{n}}{(1+i_s)^{n} - 1} = \$3000 / \text{month}$$
$$ (1+i_s)^n = \frac{1200}{577} = (1.0035)^n $$
$$ n = \log_{1.0035}{\frac{1200}{577}} = 209.575781$$

Rounded up, it would take 210 months.

**(c)**

The monthly payment being 40\% more than (a) would be 

$$\$2398.293/\text{month} \cdot 1.4 = \$3357.6102/\text{month}$$

$$ \$445000 \cdot \frac{i_s(1 + i_s)^{n}}{(1+i_s)^{n} - 1} = \$3357.6102 / 
\text{month}$$
$$ (1+i_s)^n = (1.0035)^n = 1.865225$$
$$n = \log_{1.0035}{1.865225} = 178.421$$

Rounded up, it would take 179 months.

## Problem 4

Let’s first convert all the costs to present value with $i_s = \frac{0.12}{12} = 0.01$ and $N=240$.

The initial cost, -\$6,000,000.

Salvage value, 
$$(\$2.2M + \$4M \cdot 0.4) \cdot \frac{1}{(1+i_s)^{240}} = \$348862.1788$$
Annual operating and maintenance,
$$-\$640000 / 12 = -\$53333.333$$

Annual property taxes and insurance,

$$-\$6.2 \cdot 10^6 \cdot 0.04 /12 = -\$20666.66667$$


**(a)**

In order to have a 12\% internal rate of return, let’s say the monthly lease is $x$.
We need to satisfy,

$$-\$6.2\cdot10^6 + \$348862.1788 + (-\$53333.333 -\$20666.6667 +x)\cdot\frac{(1+i_s)^{240}- 1}{i_s(1+i_s)^{240}} = 0$$
$$ \$5851137.821 = (x-\$73999.99967)\cdot 90.81942$$
$$\therefore  x = \$138426$$

The $x$ we solved for indicates the total lease for 10,000 $\text{ft}^2$, thus the monthly lease per square foot is \$13.84.

**(b)**

We just need to divide $x$ from above by 9,500 $\text{ft}^2$, therefore \$14.57.

## Problem 5

$$7500 = 2000 \cdot \frac{(1 + i_s)^5 - 1}{i_s(1+i_s)^5}$$
Solving for $i_s$ we get $i_s = 10.4\%$

## Problem 6

If we use option (1), we pay \$40,000 immediately and we pay annually,

$$ A = \$60000 \cdot \frac{0.06(1.06)^4}{1.06^4 - 1} = \$17315.48954$$
If we use option (2), we pay immediately $\$100000 \cdot 0.95 = \$95000$.

| Year | Option 2 | Option 1 | Option 2 - Option 1 |
| ---- | -------- | -------- | ------------------- |
| 0    | -95000   | -40000   | -55000              |
| 1    |          | -17315   | 17315               |
| 2    |          | -17315   | 17315               |
| 3    |          | -17315   | 17315               |
| 4    |          | -17315   | 17315               |
The IRR becomes,

$$ -55000 + \frac{17315}{1 + i} +\frac{17315}{(1+i)^2} +\frac{17315}{(1+i)^3}+\frac{17315}{(1+i)^4} = 0  $$
Solving for $i$ we get, $i = 0.099044 = 9.9\%$ which is the effective annual interest rate.

## Problem 7

For X, using IRR analysis,

$$-2500 + 900 \cdot \frac{\frac{1}{1+i_x}\cdot (1-\frac{1}{1+i_x}^4)}{1-\frac{1}{1+i_x}} = 0$$
$$ i_x = 16.37\%$$

For Y, using IRR analysis,

$$-1500 + 600 \cdot \frac{\frac{1}{1+i_y}\cdot (1-\frac{1}{1+i_y}^4)}{1-\frac{1}{1+i_y}} = 0 $$
$$i_y = 24.54\%$$

Considering, that Y has a higher internal rate of return we should choose Y.

## Problem 8

Let’s use IRR analysis to compare the IRR for each project.

A,
$$-50000 + 12500\cdot\frac{(1+i_a)^5-1}{i_a(1+i_a)^5} + 5000\cdot\frac{1}{(1+i_a)^5} = 0$$
$$i_a = 10.36\%$$

B,
$$-50000 + 8300\cdot\frac{(1+i_b)^{10}-1}{i_b(1+i_b)^{10}} + 3000\cdot\frac{1}{(1+i_b)^{10}} = 0$$
$$i_b = 10.97\%$$

C,
$$-50000 + 10500\cdot\frac{(1+i_c)^{7}-1}{i_c(1+i_c)^{7}} + 3000\cdot\frac{1}{(1+i_c)^{7}} = 0$$
$$i_c=11.55\%$$

D,
$$-50000 + 9500\cdot\frac{(1+i_d)^{8}-1}{i_d(1+i_d)^{8}} + 6000\cdot\frac{1}{(1+i_d)^{8}} = 0$$$$i_d = 11.79\%$$
**(a)**

Given the capital budget of \$100,000, we can fund two projects, thus from the internal rate of return solved from above we should fund projects C and D.

**(b)**

The next best option would be funding B and D. Thus, the opportunity cost is the IRR forgone by not choosing B. 10.97\%