
## Problem 1

| **Initial capital cost**      | 1,200,000 |
| ----------------------------- | --------- |
| **Annual benefit to users**   | 500,000   |
| **Annual cost to users**      | 50,000    |
| **Annual cost to government** | 125,000   |
| **Project life**              | 35 years  |
| **Interest rage**             | 10\%      |
Given the table, let’s calculate the conventional benefit-cost ratio,

$PW(\text{user benefit})$,
$$500000 \cdot\frac{1.1^{35}-1}{0.1\cdot1.1^{35}} - 50000\cdot\frac{1.1^{35} - 1}{0.1\cdot1.1^{35}} = 4822079.486 - 482207.9486 = 4339871.537$$

$PW(\text{sponsor cost})$,
$$1200000 + 125000\cdot\frac{1.1^{35}-1}{0.1\cdot1.1^{35}} = 2405519.872$$

$$\text{conventional benefit-cost ratio} = \frac{4339871.527}{2405519.872} = 1.8$$

Now let’s calculate the modified benefit-cost ratio,
$PW(\text{user benefit})$, remains the same, we just need to get $PW(\text{sponsor capital cost})$ and $PW(\text{sponsor operating cost})$.

$$PW(\text{sponsor capital cost}) = 1200000$$
$$PW(\text{sponsor operating cost}) = 125000 \cdot\frac{1.1^{35}-1}{0.1\cdot1.1^{35}} = 1205519.872$$

$$\text{modified benefit-cost ratio} = \frac{4339871.527 - 1205519.872}{1200000} = 2.6$$

## Problem 2

**(Gravity Plan)**

$$PW(\text{sponsor’s cost}) = \text{Initial Investment} + PW(\text{operation, maintenance}) + PW(\text{annual power cost})$$
$$=2800000 + 10000\cdot\frac{1.07^{40}-1}{0.07\cdot1.07^{40}}=2933317.088$$
$$PW(\text{user's benefits}) = 200000\cdot\frac{1.07^{20} - 1}{0.07\cdot 1.07^{20}} + \frac{400000}{1.07^{20}}\cdot\frac{1.07^{20}-1}{0.07\cdot1.07^{20}}=3213880.688$$
$$\text{conventional benefit-cost ratio} = \frac{3213880.688}{2933317.088} = 1.10$$

(**Pumping Plan**)

$$PW(\text{sponsor’s cost}) = \text{Initial Investment} + PW(\text{operation, maintenance}) + PW(\text{annual power cost})$$
$$=1500000 +300000\cdot\frac{1}{1.07^{10}} + 25000\cdot\frac{1.07^{40}-1}{0.07\cdot1.07^{40}} + 70000\cdot \frac{1.07^{10}-1}{0.07\cdot1.07^{10}} + \frac{100000}{1.07^{10}}\cdot\frac{1.07^{30} - 1}{0.07\cdot1.07^{30}}$$
$$=3108260.947$$
$PW(\text{user's benefits})$ is the same from the gravity plan, 3213880.688

Thus,
$$\text{conventional benefit-cost ratio} = \frac{3213880.688}{3108260.947} = 1.03$$
We can recommend the **Gravity Plan**, since it has a higher benefit-cost ratio.

Since the benefit of both projects are equal, it does not make sense to use incremental B/C analysis.


## Problem 3

**(a)**
The initial cost is \$7000 and by leasing for \$3000 a year, the annual saving compared to the other plan is \$2000/year.

$$\text{payback period} = \frac{\$7000}{\$2000/\text{year}} = 3.5\text{years}$$
**(b)**
$i = 0.1$, and there is a salvage value of \$500 in six years.

$$\text{conventional benefit-cost ratio} = \frac{500\cdot\frac{1}{1.1^6} + 2000\cdot\frac{1.1^6-1}{0.1\cdot1.1^6}}{7000 + 3000 \cdot \frac{1.1^6-1}{0.1\cdot1.1^6}} = \frac{8992.758364}{20065.7821} = 0.45$$

## Problem 4

**(a)**
New Buses :
$$\text{conventional benefit-cost ratio} = \frac{18000000}{4500000+12000000} = 1.09$$
Road Improvement :
$$\text{conventional benefit-cost ratio} = \frac{26000000}{15000000+5000000+4000000}= 1.08$$
From the benefit-cost ratio, the **New Buses option** is better. And both projects are individually viable.

**(b)**
Since both benefit-cost ratios are bigger than 1, we can use the incremental benefit-cost ratio,
And because $C_{\text{Road Improvement}} > C_{\text{New Buses}}$,
$$\text{incremental benefit-cost ratio} = \frac{B_{\text{Road Improvement}} - B_{\text{New Buses}} }{C_{\text{Road Improvement}} - C_{\text{New Buses}}}$$
$$ = \frac{26000000 - 18000000}{(15000000+5000000+4000000) - (12000000+4500000)} = 1.07$$
The better alternative is the **Road Improvement option** in this case.

**(c)**
$$PW(\text{New Buses}) = 18000000-12000000-4500000=1500000$$
$$PW(\text{Road Improvement}) = 26000000-15000000-5000000-4000000 = 2000000$$
The present worth analysis indicates that the **Road Improvement option** is better.

**(d)**
By comparing the decisions above, for most analyses the **Road Improvement option** is better.
Thus, we can see that the **Road Improvement option** is the best alternative.