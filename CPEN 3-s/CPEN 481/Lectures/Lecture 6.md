## Minimal Acceptable Rate of Return (MARR)

**MARR is a benchmark**: an estimation of how much you think you could earn through other investments.
- The purpose of rate of return analysis is to allow us to decide between different possible projects.
- Once we have calculated the rate of return, we need some form of benchmark against which we can compare this number.
- The average rate at which we have to recompense our creditors and investors sets a lower bound on the rate of return at which a proposed project becomes attractive.
- The ==highest of these lower bounds is the Minimum Acceptable Rate of Return (MARR)==

1. Projects that earn at least the MARR are **attractive**.
2. Projects that earn less than the MARR are **not desirable**.
	- Investing money in these projects denies the opportunity to use the money more profitably elsewhere.
3. MARR can be viewed as the rate of return required to get investors to invest in a business.
	- Known as the **company’s cost of capital**.
4. MARR should be high enough to satisfy.
	- expectations of financial institutions lending the money at a given interest rate.
	- Shareholders risking their capital for investing in a project.

### Choosing a MARR

- A lower boundary for MARR must be the cost of the money borrowed to invest in a project.
- MARR should not be less than the rate of return on the best opportunity forgone.
- An MARR must also reflect stockholder expectations of dividends and profits.

### Adjusting MARR to Account for Risk and Uncertainty

- **Uncertainty** describes the condition when the probabilities are *unknown*.
- Thus, if the probabilities of future outcomes are known, we have *risk*, and if the probabilities are unknown, we have *uncertainty*.

- In projects accompanied by normal risk and uncertainty, the MARR is used without adjustment.
- For projects with greater than average risk or uncertainty, most firms increase the MARR to determine the validity of an alternative.
- Companies under a normal level of risk have typical MARR rates of 12\% ~ 15\%.
- Much higher rates are common for different industries, such as technology start-ups short of capital or petroleum, where the risks maybe much higher.


## IRR Introduction

- Rate of return analysis is the most frequently used measure in industry. 
- It provides a measure of a project’s desirability in terms that are easily understood.
- In rate of return analysis, we compute a rate of return from the cash flow.
	- More precisely, ***internal rate of return***.
- The calculated rate of return can be compared with a pre-selected MARR.

### The Internal Rate of Return (IRR)

- We can measure the return from an investment as a rate of return per dollar invested.
	- As an interest rate.
- Rate of return calculated for a project is known as the internal rate of return (IRR).
	- "***internal***" means that the rate of return only depends on the cash flows due to investment.

$$\sum_{t=0}^T\frac{R_t-D_t}{(1+i^*)^t} = 0$$
$R_t$ = cash inflow per period, $D_t$ = cash outflow per period, $T$ = number of periods, $i^*$ = IRR.

- **IRR** is the interest rate at which the project “breaks even”.
- We solve for the discount rate in which: 
	1. $PW(\text{disbursements}) = PW(\text{receipts})$
	2. $AW(\text{disbursements}) = AW(\text{receipts})$
	3. $FW(\text{disbursements}) = FW(\text{receipts})$

### Plot of NPV versus Interest Rate $i$

![[Pasted image 20240616161949.png]]
1. Non-linearity due to non-linearity of discounting.
2. The **IRR** is located where the plot crosses the $\text{NPW} = 0$ point.

- The **IRR** is usually positive (otherwise project is losing money).
- The equation for the IRR is solved by:
	- Trial and error (with linear interpolation).
	- Built-in IRR function.


## Internal Rate of Return Comparisons for Independent Projects

- In a project, if **IRR** equals or exceeds **MARR**, then invest.
- Projects with IRR = MARR have a marginally acceptable rate of return.
- When performing rate of return comparison on mutually exclusive projects, the projects must have equal lives.

### If there are many independent projects
1. IRR for each is calculated separately.
2. Those having and IRR equal to or exceeding the MARR should be chosen.

### Opportunity Cost, in IRR Context 
The best reject project is called the: **Opportunity Cost**
- Net cost (or benefit) of best opportunity foregone.
- Net cost (or benefit) of next-best opportunity.
- **Rate of return on the best rejected property.**

If Capital Budget is \$1.2 million, the best rate of return is 20\%, the next best rate of return for this investment is 18\%. Hence, the opportunity cost is 18\%.


## IRR Comparisons for Mutually Exclusive Projects: Incremental Analysis

- Internal rate of return can be deceiving.
- Comparing strictly on the **IRR** on each project can provide incorrect results and disagree with present worth or annual worth analysis.
- The objective is to maximize the ***“return”*** **NOT** the ***“internal rate of return”***.
- This is why we use different techniques: such as Incremental Analysis.

### Incremental Analysis Algorithm

1. Calculate the rate of return for each alternative, and discard for any which IRR < MARR.
2. Arrange the remaining alternatives in ascending order of first cost.
3. The alternative with lowest first cost is you current champion.
4. Calculate the incremental IRR of upgrading from the current champion to the alternative with next-lowest first cost.
5. If the incremental IRR > MARR, upgrade; otherwise, stick with the current champion.
6. Repeat steps 4 and 5 until you run out of alternatives.


Example,
Projects:
1. Cost \$1 today, returns \$2 in one year.
2. Cost \$1000 today, returns \$1900 in one year.
	**MARR = 70\%.**

$$-1 + 2\cdot(P/F,i^*,1) = 0,\hspace{.2in} i^*=100\%$$
$$-1000+1900\cdot(P/F,i^{**},1) = 0, \hspace{.2in} i^{**}=90\%$$

Both exceed MARR but these are mutually exclusive projects gotta use incremental IRR analysis.
$$-(1000-1)+(1900-2)\cdot(P/F,i^*,1) = 0, \hspace{.2in} i^*=89.98\%$$
Considering Incremental IRR analysis, we can see that IRR > MARR so the new champion is project 2. Therefore, the second investment should be selected.


### Multiple IRRs
A project pays \$1000 today, costs \$5000 one year from now and pays \$6000 in two years. What is its IRR?

$$1000 - 5000\cdot(P/F,i^*,1) + 6000\cdot(P/F,i^*,2) = 0$$
$$1000-5000\cdot\frac{1}{(1+i^*)}+6000\cdot\frac{1}{(1+i^*)^2}= 0$$
$$i^{*^2}-3i^*+2 =0, \hspace{.2in}i^*=1,2$$
The project has two IRRs: 100\% and 200\%.

#### External Rate of Return Methods
To resolve the multiple IRRs, we need to consider what return is earned by money associated with a project that is not invested in the project.
- Assumption is that funds are invested elsewhere and earn an *explicit rate of return* equal to MARR.
- **External Rate of Return (ERR)**, denoted by $i^{*}_e$ , is the rate of return where any “excess” cash earns interest at an explicit rate, usually the MARR.

Same Example, from above + MARR is 25\%: The first \$1000 is not invested in the project immediately, so assume we invested outside the project for one year at MARR:

$$1000(F/P,20\%,1)-5000 = 1250-5000=-3750$$
$$-3750 + 6000(P/F,i^*_e,1)=0,\hspace{.2in}i^*_e=0.60=60\%$$
ERR = 60%.

## Equivalence of Rate of Return and Present/Annual Worth Methods

A comparison of Rate of Return and PW/AW methods leads to two important conclusions:
1. The two sets of methods, when properly used, gives the same decisions.
2. Each set of methods has its own advantages and disadvantages.
3. If an independent project has a unique IRR, the IRR method and the PW method give the same decision.

### Analysis Period
In internal rate of return analysis, the analysis period needs to be the same if we are examining the increments between alternatives. 

A common multiple of the alternative service lives may be used, assuming identical replacement.

### Sensitivity Analysis
It can often happen in engineering problems that we need to make tentative conclusions about a project while one or more important parameters remain undetermined.

We can compute how much an estimate can change and effect on a particular decision. (“sensitivity analysis”)

It is often possible to construct a graph showing what performance we would expect for a range of plausible values of the undetermined parameter(s).


## IRR vs. ROI

Return on Investment (ROI)
- ROI (sometimes called rate of return, ROR) is the percentage increase or decrease in an investment over a set period.
- $\text{ROI} = \frac{F-P}{P}$
- Not an annual rate: **Total return over entire time frame**.

## Levelized Cost
**Levelized Cost**: A method that calculates a product’s minimum selling price that still provides MARR. Often compared with the product’s market value.

- If market price is greater than the levelized cost.
	- Investment is considered acceptable.
- Levelized cost, $x$, can be calculated as follows: 
	$$x = \frac{PW(\text{costs}) - PW(\text{salvage})}{PW(\text{physical output})}$$

## Next Lecture [[Lecture 8]]
