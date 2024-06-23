## Compound Interest Factors for Discrete Compounding

- Four discrete cash flow patterns are commonly used
	1. Single disbursement / receipt
	2. Set of equal disbursements / receipts over a sequence of periods (**annuity**).
	3. Set of disbursements / receipts that change by a 
		1. constant amount from one period to another (**arithmetic gradient**).
		2. constant proportion from one period to another (**geometric gradient**).

Some assumptions exist for discrete compounding
	1. Compounding periods are of equal length.
	2. Each disbursement / receipt occurs at the end of a period.
	3. Timing of annuities and gradient align exactly with full time period, and how time is broken up.

## Compound Interest Factors for Single

**Compound Amount Factor** : Gives the future amount, $F$, equivalent to a present amount $P$, interest rate is $i$ and the number of periods until $F$ is $N$.

$$ F = P(1+i)^N = P(F/P, i, N)$$

**Present Worth Factor**: Gives the present amount, $P$ , that is equivalent to the future amount, $F$, when the interest rate is $i$ and the number of periods is $N$.
$$ P = F/(1+i)^N = F(P/F, i, N)$$
### Ex) 
How much money will be in a bank account at the end of 15 years if \$100 is invested today, and the nominal interest rate is 4\%, compounded semiannually? 

$$i_e = (1+0.04/2)^2 - 1 = 0.0404$$
$$ F = P(1+i_e)^N = 100 \cdot 1.0404^{15} = 181.136$$
Or Alternatively, given that $i_s = 0.04/2 = 0.02$ semiannually and the number of periods being $N = 30$. 
$$ F = 100 ( 1+ 0.02)^{30} = 181.136 $$


## Compound Interest Factors for Annuities

**Annuity**: Series of *uniform* receipts / disbursements that begin at the end of period 1 and continue over $N$ periods.
	- For instance, Mortgage and lease payments 

**Sinking Fund Factor**: Gives the size, $A$, of a repeated receipt or disbursement that is equivalent to a future amount, $F$, if the interest rate is $i$ and the number of periods is $N$.

$$(A/F, i, N) = \frac{i}{(1+i)^N - 1}$$

**Uniform Series Compound Amount Factor**: Gives the future value, $F$, that is equivalent to a series of equal-sized receipts / disbursements, $A$, when the interest rate is $i$ and the number of periods is $N$.

$$(F/A, i, N) = \frac{(1+i)^N - 1}{i}$$

***Proof***
$$F = \sum_{k = 1}^{N} A_k,\hspace{0.2in} A_k = A(1+i)^k$$
$$F = \sum_{k=1}^{N}A(1+i)^k = A \cdot \frac{1+i-1}{(1+i)^N - 1} = A \cdot \frac{i}{(1+i)^N - 1}$$
$$\therefore (A/F,i,N) = \frac{i}{(1+i)^N - 1}$$
$$\therefore (F/A, i, N) = \frac{(1+i)^N - 1}{i}$$


**Capital Recovery Factor**: Gives the value,$A$, of the equal periodic payments or receipts that are equivalent to a present amount, $P$, when the interest rate is $i$ and the number of periods is $N$.

$$P = F(P/F,i,N) = A(F/A,i,N)(P/F,i,N)$$
$$A = P(A/F,i,N)(F/P,i,N) = P \cdot \frac{i}{(1+i)^N - 1} \cdot (1+i)^N$$
$$\therefore (A/P,i,N) = \frac{i(1+i)^N}{(1+i)^N-1}$$
**Series Present Worth Factor**: Gives the present amount,$P$, that is equivalent to an annuity with disbursements / receipts in the amount $A$, where the interest rate is $i$ and the number of periods is $N$.

$$(P/A,i,N) = \frac{(1+i)^N-1}{i(1+i)^N}$$

### Salvage Value
When there is a salvage value at the end of the life of an asset, it is represented as a one-time cash flow benefit (revenue) at the end of the asset’s life.

- Salvage value is a special kind of future revenue ($F$), so we can apply the $F$ equations when we have a salvage value.


#### Capital Recovery Formula
Capital asset has an initial cost $P$, and a salvage value, $S$, after $N$ periods.
An equivalent annual cost can be obtained using the capital recovery factor and the sinking fund factor:
$$A = P(A/P, i,N) - S(A/F, i,N)$$
The reason this works, is because salvage cost $S$ is a future asset. We can convert it to an annual cost which then can be subtracted from the original annuity $A$.

$$A = P(A/P, i,N) - S(A/F, i,N)$$
$$= P \cdot \frac{i(1+i)^N}{(1+i)^N-1} - S \cdot \frac{i}{(1+i)^N - 1}$$
$$= P \cdot \frac{i(1+i)^N}{(1+i)^N-1} - S \cdot (\frac{i(1+i)^N}{(1+i)^N-1} -i) $$
$$ = (P-S) \cdot \frac{i(1+i)^N}{(1+i)^N-1}  + Si$$
$$ = (P-S)(A/P,i,N) + Si$$
**$A$ in this case is often called the ***capital recovery cost*****.


## Conversion Factor for Arithmetic Gradient Series

**Arithmetic Gradient to Uniform Series Factor**: Give the value of an annuity, $A$, that is equivalent to an arithmetic gradient series where the constant increase in disbursements / receipts is $G$ per period, the interest rate is $i$ and the number of periods is $N$.

- Arithmetic gradient series is a series or receipts / disbursements that’s **starts at zero at the end of the first period** and then **increases by a constant amount** from period to period.
- Basically period $k$, the increase $G_k$ is 
	$$ G_k = G \cdot (k - 1)$$

$$(A/G,i,N) = \frac{1}{i} - \frac{N}{(1+i)^N - 1}$$
$$A_{\text{tot}} = A' + G(A/G, i, N)$$

**Geometric Gradient**: Gives the present worth, $P$, that is equivalent to a geometric gradient series where the base receipt / disbursement is $A$, and where the rate of growth is $g$, interest rate is $i$, and the number of periods is $N$.

Case (1) : $i = g$
$$P = A_1 \cdot [n (1+i)^{-1}]$$
Case (2) : $i \neq g$
$$P = A_1 \cdot [\frac{1 - (1+g)^n(1+i)^{-n}}{i -g}]$$
***Proof***
$$F = \sum_{k=1}^N A(1+i)^{N-k}(1+g)^{k-1} = A\cdot \frac{(1+i)^N}{1+g} \cdot \sum_{k=1}^N (\frac{1+g}{1+i})^k$$
$$ =  A\cdot \frac{(1+i)^N}{1+g} \cdot \frac{1+g}{1+i} \cdot \frac{ 1- (\frac{1+g}{1+i} )^N}{1- \frac{1+g}{1+i} } $$
$$= A \cdot (1+i)^N \cdot \frac{1 - (1+g)^N(1+i)^{-N}}{i - g}$$
$$\therefore P = F/(1+i)^N = A \cdot \frac{1 - (1+g)^N(1+i)^{-N}}{i-g}$$
## Capitalized Value: Present Worth Computations When $N \rightarrow \infty$ 
Used for long-lived projects: 
- When it is reasonable to model the cash flows as if they will continue indefinitely
Present worth of an infinitely long series: **capitalized value $P = A \div I$**

## Non-Standard Annuities and Gradients

If payment period ≠ compounding period, formulas given cannot be used directly.
- Treat each cash flow in the annuity or gradient individually.
- Convert the non-standard annuity or gradient to standard form by changing compound period.
- Convert the non-standard annuity form by finding an equivalent standard annuity for the compounding period.

## Bonds and Bond Pricing
A Bond is a way for firms or governments to borrow money from others.
When Bonds are purchased, the fixed items are:
* Face Value
	* Amount paid out when the bond matures.
* A nominal interest rate
	* Sometimes called “coupon rate”.
	* The amount of interest paid out to the bond holder per compounding period.
* The purchase price can vary depending on the current market interest rate as the present worth of a bond is determined from the fixed values above.

$$\text{Worth of Bond} = \text{Present worth of face value} + \text{Present worth of coupons}$$

==Include Examples==
## Opportunity Cost
Opportunity cost is the ***net benefit of your next best*** alternative.

## Next Lecture [[Lecture 4]]
## Assignment [[Assignment 2 Mercury Mcindoe 85594505]]

