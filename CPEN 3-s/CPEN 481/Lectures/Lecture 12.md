
## Introduction
**Sensitivity Analysis** gives better understanding of how uncertainty affects outcome of the evaluation.
- The sensitivity of certain performance measures (as PW) to changes in the values of input parameters provide a manager with better decision making.

**Sensitivity Graphs** illustrate sensitivity of performance measures to changes in parameters.

**Decision Trees** allow probabilistic information about the outcome of a decision to be structured so that the best decision is made.

## Sensitivity Analysis
Used to assess the effect of one-at-a-time changes in key parameter values of a project on an economic performance measure.

Process:
1. Begin with a “base case” where all estimated parameter values are used to evaluate PW, AW or IRR, etc.
2. Vary parameters above and below the base case one at a time.
3. Plot Sensitivity Graph - Graph of changes in the performance measure due to one-at-a-time parameter changes.

**Sensitivity Analyses** assess economic performance, as key parameters are varied “one-at-a-time”.

***Advantages***:
- Amenable to “boardroom” communication.
- Shows parameters of significant impact (graphically).

***Disadvantages***:
- Only valid within parameter range of graph.
- Does not consider the possible interaction between two or more parameters.

## Break-Even Analysis
Process of varying *one* parameter whereby performance measure reaches “break-even” value.
Normally used for comparing two or more projects.

- How does the *impact* of changes in parameter values affect which project(s) are chosen?
	- For independent projects analysis, this can be carried out on each project independently.
	- For *mutually exclusive projects*, best choice will seldom stand out as clearly superior from all points of view.
	- Best choice may depend on a particular interest rate, level of output, or initial investment.
- **Break-even analysis** is a simple tool that can be used to extract insights from a modest amount of data.
- It communicates threshold (break-even) parameter values where
	- preference changes from one alternative to another.
	- project changes from being economically justified or not.
- Main **disadvantage** of break-even analysis:
	- It cannot easily capture interdependencies among variables.

## Structuring Decisions with Decision Trees
Formal methods aid engineers in evaluating complex problems where uncertainty/risk play role:
- Provide means of decomposing a large problem and structuring it into sequence of smaller components.
- Suggest a variety of decision criteria to help with the process of selecting a preferred course of action.
- Graphical means of structuring where uncertainties are characterized by probability distributions.
- Clarifies options decision maker has/provides framework with which to deal with the risk involved.

**Decision Tree**: A graphical representation of the logical structure of a decision problem in terms of the sequence of small and essential components.
- Clarifies the options a decision-maker has.
- Provides a framework with which to deal with the risk involved.


![[Pasted image 20240618120207.png]]

There are **four main** components in a decision tree:
1. A **decision node** represents a decision to be made by the decision maker - *denoted by a square*.
2. A **chance node** represents an event whose outcome is uncertain - *denoted by a circle*.
3. The branches connect nodes from left to right, depicting the sequence of possible decisions and chance events.
4. The leaves indicate the values, or payoffs, associated with each terminal (rightmost) branch of the tree. A decision tree grows from left to right.

From the figure above,
$$\mathbb{E}[\text{up}]= (0.6\cdot\$15) + (0.4\cdot \$7) =\$11.8$$
$$\mathbb{E}[\text{down}] = \$10$$

One criterion for selecting among risky alternatives is expected value, EB, carried out as follows:
1. **Structure the problem:** Develop a decision tree.
2. **Rollback**: Moving from right to left on the tree.
	1. At each chance node, compute the expected value of the possible outcomes.
	2. At each decision node, select the option with best expected value. This becomes the value associated with the decision node. Terminate option(s) not selected with “//” on their branch.
	3. Continue until the leftmost branch is reached.
3. **Conclude**: The expected value associated with the final node is the expected value of the overall decision.

Ex)
![[Pasted image 20240618121859.png]]
**(1)**
$$\hspace{.1in}\mathbb{E}[\text{2}] = (0.6\cdot\$15) +(0.4\cdot\$7) = \$11.8,\hspace{.2in} \mathbb{E}[\text{3}] = (0.3\cdot\$8)+(0.55\cdot\$10)+(0.15\cdot\$12) = \$9.4$$

**(2)**
Roll back $\mathbb{E}[1]$ = the higher of the two possibilities hence $\mathbb{E}[2]$. Thus, the best option.

**(3)**
Conclusion, the expected value of the overall decision is \$11.80/unit.

## Risk
Risk is the chance of getting an outcome other than the expected value.
A common measure is standard deviation.
$$\sigma = \sqrt{(\mathbb{E[X - \mu]})^2}$$
Standard deviation is used instead of variance since it has the same units as the expected value.



Ex)
Suppose a potential project has a **capital cost of \$25,000**, and the borrowing cost will be **\%10**. The most likely value of the annual benefit of a potential project is **\$8,000**, with a probability of **\%60**. There is a **30\%** probability it will be **\$5,000**, and a **10\%** probability it will be **\$10.000**. Independent of a that information, a life of 6 years is twice as likely as a life of 9 years.


| Saving per year | Probability | Useful Life | Probability | Joint Probability | Expected Value |
| --------------- | ----------- | ----------- | ----------- | ----------------- | -------------- |
| 5000            | 0.3         | 6           | 0.667       | 0.2               | 1000           |
| 8000            | 0.6         | 6           | 0.667       | 0.4               | 3200           |
| 10000           | 0.1         | 6           | 0.667       | 0.0667            | 667            |
| 5000            | 0.3         | 9           | 0.333       | 0.1               | 500            |
| 8000            | 0.6         | 9           | 0.333       | 0.2               | 1600           |
| 10000           | 0.1         | 9           | 0.333       | 0.0333            | 333            |
$$\mathbb{E} = \$7,300$$

| Capital Cost            | -25000         |             |  |      |          |             |
|-------------------------|----------------|-------------|--|------|----------|-------------|
| interest rate           | 10%            |             |  |      |          |             |
|                         |                |             |  | year | cashflow | present     |
|                         | Annual benefit | Probability |  | 0    | -25000   | -25000      |
| lower                   | 5000           | 0.3         |  | 1    | 7300     | 6636.363636 |
| most likely             | 8000           | 0.6         |  | 2    | 7300     | 6033.057851 |
| higher                  | 10000          | 0.1         |  | 3    | 7300     | 5484.598047 |
|                         |                |             |  | 4    | 7300     | 4985.998224 |
| Expected Annual Benefit |                | 7300        |  | 5    | 7300     | 4532.725658 |
|                         |                |             |  | 6    | 7300     | 4120.659689 |
|                         | Useful Life    | Probability |  | 7    | 7300     | 3746.054263 |
| 6 years                 | 6              | 0.67        |  |      |          |             |
| 9 years                 | 9              | 0.33        |  |      |          |             |
|                         |                |             |  | IRR  | 22%      |             |
| Expected useful life    |                | 7           |  | NPW  |          | 10539.45737 |



Ex) A large firm is discontinuing an older product, and therefore some facilities are becoming available for other uses. The following table summarizes eight potential new projects that would use the facilities. Considering expected return and risk, which projects are good candidates? The firm believes it can earn 4\% on a risk-free investment in government securities (labelled as “Project F”).

![[Pasted image 20240618125940.png]]

![[Pasted image 20240618130044.png]]

We can plot the possibilities, since *larger expected return is better* we want to choose projects that are as **high up on the graph as possible**. Since a *lower risk is better*, we want to choose projects **that are as far left as possible**. 

- Projects 4 and 5 are dominated → they can be eliminated.
- Projects 1 and 8 also appear to be inferior.
- The remaining is an efficient frontier.


## Risk Preference
There are three options for risk preference.
1. Risk-averse
2. Risk-neutral
3. Risk-seeking
Based of the preference is how you internalize expected value comparisons.


## Next Lecture [[Lecture Accounting]]
