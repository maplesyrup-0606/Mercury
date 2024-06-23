## Computing Cash Flows

We describe the benefits and costs as **receipts** and **disbursements** at different points in time.
* **receipts** - cash flowing *in*
* **disbursements** - cash flowing *out* 

## Introduction

Engineering decisions frequently involve ㄹtradeoffs among cost and benefits occurring at ***different times***.

## Time value of money 

When monetary consequences of a project we’re considering doing will occur over a period of time into the future, but **we can’t just simply** add up the various sums of money.

Why? It’s because money
1. Has a value over time.
2. Is a valuable asset that people are willing to pay to have available for use.
3. Can be rented in roughly the same way other things can.
	* The charge is called **interest** instead of rent.

### Present Value (PV)
Measures current worth of future benefits and costs
$$PV(\$_n) = \frac{(\$_n)}{(1+r)^n}$$ 
Example of present value)

| time period              | 0     | 1     | 2     | 3        | 4        |
| ------------------------ | ----- | ----- | ----- | -------- | -------- |
| interest earned (r = 10) |       | $ 10  | $ 11  | $ 12.1   | $ 13.31  |
| new account balance      | $ 100 | $ 110 | $ 121 | $ 133.10 | $ 146.41 |
Present value after 4 years,
$$\frac{(\$_n)}{(1+r)^n} = \frac{\$146.41}{(1+0.1)^4}= \$100$$
Which shows that $146.41 4 years later, is **equivalent to** $100 today.

### Time Value of Money Continued
- Our preference for having money now rather than money in the future differs from person to person.
	- The preference for having money now rather than later has ***nothing to do with inflation**.
	- The bank expresses the time value it puts on money by publishing the interest rate that it charges to borrow money.



## Interest and Interest Rates

### Interest

**Interest** is compensation for giving up the use of money.
- The different between the amount loaned and the amount repaid.

An amount of money today, $P$, can be related to a future amount, $F$, by the interest amount $I$, or interest rate $i$:
$$F = P + I = P + Pi = P(1 + i)$$
To wrap up the terms a bit, for example, you receive a loan of amount $P$ now, in exchange for paying a future amount $F$ at some future time, where $F = P(i + 1)$.
- $i$ → **interest rate**
- $P$ → **present worth** of $F$
- $F$ → **future worth** of $P$
- base period → **interest period**


### Interest Rates

The dimension of an **interest rate** is (dollars / dollars) / time.
	- i.e., if $1 is lent at a 9% interest rate, then $0.09/year would be paid in interest per time period

Period over which interest is calculated is the **interest period**.
	- Assume all actions happen when periods occur

The longer the interest period, the higher the interest rate must be to provide the same return.

==When you are given an interest rate without a specified period, assume it is annual (per year).==


| Interest Period | Interest is Calcualted                        |
| --------------- | --------------------------------------------- |
| Semiannualy     | Twice per year, every 6 months                |
| Quarterly       | Four times a year, or once every three months |
| Monthly         | 12 times per year                             |
| Weekly          | 52 timers per year                            |
| Daily           | 365 times per year                            |
| Continuous      | For infinitesimally small periods             |
## Compound and Simple Interest

### Compound Interest

If amount $P$ is lent for one period at interest rate, $i$ 
- Then amount repaid at the end of the period is $F = P(1+i)$.

If it’s more than one period, interest is compounded.
- At the end of each period, interest is added to principal that existed at the **beginning of that period**. → Therefore meaning it’s *compounded*.

If an amount $P$ is borrowed for $N$ periods at interest rate $i$, the amount that must be repaid at the end of $N$ periods is:
$$F=P(1+i)^N$$

This method of computing interest is called ***compounding***.
- Compounding assumes there are $N$ sequential one-period loans.
- At the end of each period, ==the amount borrowed plus interest added== in that period is borrowed for the next period.

**Compound interest (total interest)** on loan over $N$ periods is : 
$$ I_c = F - P = P(1+i)^N - P$$
The interest period used with the compound interest method is called the **compounding period**.

### Simple Interest

Interest without compounding (interest is not added to principal at the end of period) : 
$$I_s = P * i * N$$
Compound and simple interest amounts equal if $N = 1$.
$$ I_c = P(1+i) - P = i*P = P * i * 1 = I_s$$
As $N$ increases, difference between accumulated interest amounts for the two methods increases exponentially.

The conventional approach for computing interest is the **compound interest** method (Simple interest is rarely used today).


## Effective and Nominal Interest Rates

### Nominal Interest Rates 

Interest rates are stated for some period, usually a year.
Computation is based on shorted compounding sub-periods.

- The ***nominal interest rate*** is stated for the full-period.
- The ***effective interest rate*** that results from the compounding based on the sub-periods.
- An interest rate is **effective** when the compounding period and the interest period are the same.

Unless otherwise noted, rates are **nominal annual rates**.
- Calculated by multiplying the interest rate per compounding period by the number of compounding periods per year.

Suppose: $r$ is a nominal rate stated for a period (1 year) consisting of $m$ equal compounding periods (sub-periods).

The interest rate for each sub-period is calculated as: $$i_s = \frac{r}{m}$$
### Effective Interest Rates

An **effective interest rate** is the actual (but not usually stated) interest rate, found by:
- converting a given interest rate with an arbitrary compounding period (normally less than a year) to an equivalent interest rate with a one-year compounding period.

$$i_e = (1 + i_s)^m - 1$$
- $i_s$ : interest rate over a compounding sub-period.
- $i_e$ : effective interest rate over a longer period.
- $m$ : number of sub-periods in the longer period.

Example)
Nominal 24% interest rate, compounded daily.
Assuming 365 days per year, we can calculate the interest rate per year:
$$\frac{r}{m} = \frac{0.24}{365} = 0.0006575$$ 
then
$$i_e = (1+i_s)^m - 1 = (1+0.0006575)^365 - 1= 0.271$$

The **effective interest rate** is 27.1%.

### Continuous Compounding

Suppose that the nominal interest rate is 12% and interest is compounded **semi-annually**.
We compute the effective interest rate as follows (where $r = 0.12$  , $m = 2$):
$$i_s = \frac{r}{m} = \frac{0.12}{2} = 0.06$$
$$i_e = (1+i_s)^m - 1 = (1+ 0.06)^2 - 1 = 0.1236 \space (12.36\%)$$

What if interest were compounded monthly?
$$i_e = (1 + i_s)^m = (1+ 0.01)^12 - 1 = 0.1268 \space (12.68\%)$$

Daily would increase and more for smaller intervals (**continuous compounding**).

Compounding can be done yearly, quarterly, monthly, or daily and is normally referred to as ***discrete compounding***.

For infinitesimally small sub-intervals, we say that interest is ***compounded continuously***.

The effective interest rate under continuous compounding is:
$$i_e = e^r -1$$

## Cash Flow Diagrams

**Cash flow diagram** is a graphical summary of the timing and magnitude of a set of cash flows.

![[Pasted image 20240515195138.png]]

- As illustrated in a cash flow diagram, the end of one period is exactly the same point in time as the beginning of the next period.
- Now is time 0, which is the end of period -1 and, also the beginning of period 1.
- The end of period 1 is the same as the beginning of period 2, and so on.
- $N$ years from now is the end of period $N$ and the beginning of period $N + 1$.

![[cashflow_img.canvas|Untitled]]
- Each arrow represents a cash flow, labelled with the amount of the receipt or disbursement.
- When two or more cash flows occur in the same time period, the amounts may be shown individually or in summary form.

### Assumptions in Solving Economic Analysis Problems

**Each-of-Year Convention**
All cash flow amounts are calculated as amounts at the end of each period:
- Now = end of period $N$ (beginning of $N+1$).
- Future amounts happen at the end of the period specified.

**No Sunk Costs**
- Only the current situation and the potential future is considered.
	- Once money is spent, it shouldn’t influence the current decision.

### Equivalence 

Engineering Economics utilizes “time value of money” to compare certain values at different points in time.
Equivalence is a condition that exists when:
- The value of a cost at one time is equivalent to the value of the related benefit at a different time.

#### Mathematical Equivalence

1. A consequence of the mathematical relationship between time and money.
2. Decision-makes change exchange $P$ dollars now for $F$ dollars $N$ periods from now using rate $i$ and the mathematical relationship: $F = P(1+i)^N$.

#### Decisional Equivalence

1. Happens when a decision maker judges available choices to be equally good.
2. Two cash flows, $P_t$ at time $t$ and $F_{t1N}$ at time $t+N$, are equivalent if the individual is **indifferent** between the two.
3. Implied interest rate relating to $P_t$ and $F_{1tN}$ can be calculated from the decision that cash flows are equivalent.
4. In ***mathematical equivalence***, the interest rate determines whether the cash flows are equivalent.

#### Market Equivalence 

1. Arises due to the availability of a market to exchange one cash flow for another a zero cost.


We assume:
1. Market equivalence holds.
2. Decisional equivalence can be expressed in monetary terms.

If these two assumptions hold (are reasonably valid), then mathematical equivalence can be used as accurate model of costs/benefits relationships.


### Computing $ Flows - extra notes

- Not every benefit or cost will involve a real change to the physical system you’re making choices about.
	- ex) tax consequences of depreciation
- Not every benefit or cost will involve cash flow.
	- ex) avoided environmental damages, depreciation of assets


## Computing Electricity Rates

![[Screenshot 2024-05-15 at 8.19.55 PM.png]]

Total usage: 72,600 kWh this month.

Usage cost = 0.0816 x 14,800 + 0.0393 x (72,600 - 14,800) = $3,479.22.

Demand: 900 kW peak demand this month.

Demand charge  = $0 x 35 + $4.18 x (115 - 35) + $8.02 x (900 - 115) = $6,630.10.

Total monthly bill = $3,479.22 + $6,630.10 = $10,109.32.

==But why consider demand charge? It’s because though we might have used 900 kW once this month, the supplier still needed to buy the capital that has to be ready to produce 900 kW.==

## Blended rate

- Can be calculated over any time of period of interest.
- Consequent cost per kWh is a "blended" rate that accounts for all variable costs.
- Note that fixed administrative costs are not included (though they might be significant).
	- Because they won’t change if a project increases energy use or (peak) demand.

$$\text{blended rate} = [\frac{\text{total usage cost} + \text{demand charge cost}}{\text{usage amount (kWh)}}]$$
## Average Cost vs Marginal Cost

Average cost = Total cost / # of units sold or purchased.
Marginal cost = Extra cost of one additional unit.


## Next Lecture [[Lecture 3]]
## Assignment [[Assignment 1 Mercury Mcindoe 85594505]]