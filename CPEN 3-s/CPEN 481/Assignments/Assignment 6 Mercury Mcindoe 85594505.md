
## Problem 1

**(a)**
$$\$10000000\cdot(\frac{6.4}{4})^{0.72} = \$14027051.3714$$
$$\approx \$14000000$$

**(b)**
$$\$10000000\cdot(\frac{6.4}{4})^{0.72}\cdot\frac{170}{105} = \$14027051.3714\cdot\frac{170}{105} =\$22710464.1251$$
$$\approx \$22700000$$

## Problem 2

Excel File Attached for q2.

## Problem 3

$$i'=\frac{1+i}{1+f} - 1$$Given that $i=0.15$ and $f=0.1$,
$$i' = \frac{1.15}{1.1} - 1 = 0.045=4.5\%$$

## Problem 4

Filterco:
$$-\$5000-\$5000\cdot(\frac{1.08}{1.05})^5 -\$1300\cdot\frac{1-1.04^{10}1.05^{-10}}{0.05-0.04} = -\$22619.88\approx-\$22620$$

Duro:
$$-\$15000-\$1000\cdot\frac{1-1.04^{10}1.05^{-10}}{0.05-0.04}+500\cdot\frac{1}{1.05^{10}}=-\$23818.88\approx-\$23819$$

Based on NPW analysis, Filterco unit should be purchased.

## Problem 5

**(a)**
$$a = \frac{94-87}{87} = 0.0805$$
$$5.90\% = \frac{b-94}{94}$$
$$b=0.059\cdot94+94=99.546$$
$$c=\frac{104-b}{b} = 0.0447431338$$
$$d=\frac{108-104}{104} = 0.0384615385$$
$$\frac{118-e}{e} =0.038$$
$$e=\frac{118}{1.038}=113.6801541426$$
$$\therefore a =8.05\%,b=100,c=4.47\%,d=3.85\%,e=114$$
**(b)**
The base year of the PSI is 2015. The reason is because the index at this year is 100.

**(c)**
2012~2017:
$$(\frac{108}{82})^{\frac{1}{5}}-1 = 0.056627673 \approx 5.7\%$$
2015~2019:
$$(\frac{118}{99.546})^{\frac{1}{4}} - 1=0.0422466355 - 1= 0.0434329535 \approx 4.3\%$$

## Problem 6

**(a)**
The interest rate of 7\% would be best for the discount rate, it is also the most common lowest value.

**(b)**
**Case 1: Rent duplex**
Let’s first determine the yearly costs for rent fees and utilities,
$$\text{rent}=\$460\cdot12=\$5520$$
$$\text{utilities} = \$100\cdot12=\$1200$$
$$NPW = \$5520\cdot\frac{1-(1.025)^{15}(1.07)^{-15}}{0.07-0.025}+\$1200\cdot\frac{1-(1.05)^{15}(1.07)^{-15}}{0.07-0.05} $$
$$=\$58275.265 + \$14790.045 = \$73065.31 \approx \$73065$$
is the amount it will cost the couple.

**Case 2: Buying the house**
The down payment + sales commission is
$$0.05\cdot\$94000\cdot2=\$9400$$
Leaving us $\$94000-\$4700=\$89300$ to borrow.

Given that we are borrowing for 25 years at a 7\% interest rate,
$$n=25,\hspace{0.4in} i = 7\%$$
$$A=\$89300\cdot(A/P,7\%,25)= \$7662.88/\text{year}$$

The utilities, home insurance and maintenance costs can be calculated as,
$$12\cdot\$300\cdot\frac{1-1.04^{15}\cdot1.07^{-15}}{0.07-0.04}=\$41670.62$$

Let’s now get the appreciation when selling the house, in 15 years the house price becomes,
$$\$94000\cdot(1.035)^{15}=\$157482.79$$

Then the present price is 
$$\$157482.79\cdot\frac{1}{1.07^{15}}=\$57079.01$$
However, we want to subtract the left over mortgage at this point,
$$\$57079.01-(\$89300 - \$7662.88\frac{1.07^{15}-1}{0.07\cdot1.07^{15}})=\$57079.01-\$19507.148= \$37571.86$$
Will be the eventual present value of the revenue from the selling the house.

The final costs of buying the house is therefore,
$$\$9400+\$41670.62+\$7662.88\cdot\frac{1.07^{15}-1}{0.07\cdot1.07^{15}}-\$37571.86$$
$$=\$83291.61 \approx \$83292$$

Renting the one-bedroom duplex would be a cheaper option.
**(c)**
The saving rate for additional cash flows is not provided.

## Problem 7

$$P(\text{roll }7)=\frac{6}{36}, P(\text{roll 8})=\frac{5}{36}$$
$$P(\text{Hard-way 8})=\frac{1}{36},P(\text{roll 8} \cup \text{Hard-way 8}^\complement)=\frac{4}{36}$$

Then the winning probability becomes,
$$P(\text{win})=\frac{\frac{1}{36}}{\frac{1}{36}+\frac{10}{36}}=\frac{1}{11}$$
Likewise the losing probability is,
$$P(\text{lose})=\frac{\frac{10}{36}}{\frac{1}{36}+\frac{10}{36}}=\frac{10}{11}$$

Thus,
$$\mathbb{E}[\text{return}]=\$9\cdot\frac{1}{11}-\$1\cdot\frac{10}{11}=-0.0909090909$$
The expected return is -9 cents.
