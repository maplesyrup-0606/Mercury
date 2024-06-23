## Types of Property

- Tangible Property
	- Can be seen, touched, and felt.
- Real Property
	- Land, buildings, and all things growing on, built upon, constructed on, or attached to the land.
- Personal Property
	- Equipment, furnishings, vehicles, and any other tangible property that is **NOT** real property.
- Intangible Property
	- Value to the owner but cannot be seen or touched; patents, copyrights, trademarks, trade names, and franchises.

## Depreciation and Expenses

- Most businesses obtain physical assets to help generate revenue. These physical assets typically lose value, or depreciate, over time.
- Capital assets are considered different from supplies (inventory goods), because they last longer, and usually wear out over time.
- Expenses are consumed over the normal course of business and over a short period of time.
	- Labour, materials, insurance etc.
- In contrast, capital assets are not fully written off (considered of no value) when they are purchased.
- They are depreciated over an extended period of time because they have a longer life.

### Depreciation

- Projects involve investment in *assets*, such as buildings and equipment, that are put to productive use.
- Assets lose value, or depreciate, over time.
- **Depreciation** is taken into account when:
	- A firm states the value of its assets in a Financial Statement.
	- Making decisions as to when to replace an aging asset.
	- Dealing with issues related to taxation.
- Assets depreciate for a variety of reasons:
	- **Use-related physical loss**:
		- As something is used, parts wear out.
		- Usually measured in units of production, km driven, hours of use.
	- **Time-related physical loss**
		- Even if something is not actively in use, physical loss can occur over time.
		- Usually measured in units of time as an unused car will rust and lose value over time.
	- **Functional loss (obsolescence)**
		- Losses can occur without any physical changes.
		- Usually expressed in terms of function lost including fashion, legislative (i.e., pollution control, safety devices) and technical changes.
- **Value of an Asset**
	- Depreciation models are used to:
		- model value of an asset over time.
		- determine the remaining value of an asset at any point in time.
	- Remaining value is referred to as:
		- **Market value**
			- The actual value an asset can be sold for in an open market (estimated)
		- **Book value**
			- The value of an asset calculated from a depreciation model for accounting purposes.
				- Might differ from market value.
				- May be several book values given for the same asset.
		- **Scrap value**
			- Either actual or estimated value at end of its physical life.
		- **Salvage value** 
			- Either actual or estimated value at end of its useful life (usually when sold).


To state the book value of an asset, a good model of depreciation is desirable:
- To make managerial decisions it’s important to know the value of owned assets.
- One needs an estimate of the value of assets for planning purposes.
	- Either to keep or replace an asset.
- Tax legislation requires company tax to be paid on profits.


### Depreciation and Expenses
Depreciation is a **non-cash cost** (no actual exchange of dollars) that causes **real cash impacts** (because it affects profits and taxes).

To be depreciable, assets must:
- Be used for business purposes to produce income.
- Have useful life that can be determined and that is longer than one year.
- Be an asset that decays, gets used up, wears out, becomes obsolete, or loses value to the owner from natural causes.

*Exceptions to depreciation*:
1. Land is never depreciated.
2. Leased property: it does where out → but not firm’s problem.
3. Factory inventory.


### Asset Depreciation Concept

- Cost Basis = “First Cost” = Total cost of acquiring and putting an asset into use.
- Total cost is assumed to be **equal** to the total value of the asset.
- That value declines over time, so the cost of buying it is also *spread out* over time - over the life of the asset.
- The *spread-out* costs are depreciation expenses.

**Book Value**
$$\text{Book value} = \text{Cost basis} - \text{Depreciation charges made to date}$$
- Each year, the amount that the book value drops is the depreciation expense.
- The remaining value is the “book value”.
- Continues until the asset is of no value.
- Largely separate from the physical condition of the asset.

![[Pasted image 20240620143129.png]]

### Straight-Line Depreciation
**Straight line depreciation** assumes the rate of loss of the asset’s value is constant over its useful life.
- The book value of an asset is determined by drawing a straight line between its first cost and its salvage or scrap value.

$$\text{Annual Depreciation Charge} = d_t = \frac{B-S}{N}$$
$B$: Cost basis, $S$: Salvage value, $N$: depreciable life.

*Depreciation and Book Value*
$$D(n) = \frac{P-S}{N}$$
$$BV(n) = P - n\cdot\frac{P-S}{N}$$
$P$: Purchase price ← a.k.a Cost basis

Advantage 
- Easy to calculate and understand.

Disadvantage
- Most assets do not depreciate at a constant rate.

### Declining-Balance Method

![[Pasted image 20240620143907.png]]

*Depreciation and Book Values*
$$BV(0) = P \hspace{.1in}(\text{Purchase Price of Asset})$$
$$D(n)=BV(n-1)\cdot d$$
$d$: depreciation rate.
$$BV(n) = P\cdot(1-d)^n, \hspace{.1in} \forall d\in \mathbb{Z}^+$$

Declining balance rate that relates P and S: 
$$d=1-^n\sqrt{\frac{S}{P}}$$
$S$: Salvage Value, $P$: Asset’s current value.


Useful features:
- Matches observable loss in value that many assets have over time.
- Rate of loss is expressed on one parameter.
- Often the standard approach used for taxation purposes.

### Double-Declining Balance Rate
$$D=\frac{2}{N}$$
$D$: Depreciation Rate.

Suppose original cost of asset = \$1,000, and asset expected to last 7 years ($N=7$).
Deprecation rate $D=\frac{2}{7}=28.6\%$. 
Depreciation in year $t = d_t = D \cdot BV(t-1)$.

Then,
$$\text{Year 1} : \hspace{.1in} d_1 =  1000\cdot 28.6\% = 286$$
$$BV(1) = 1000 - 286 = 714$$
$$\text{Year 2} : \hspace{.1in}d_2 = 714 \cdot 28.6\% = 204$$
$$BV(2) = 714 - 204 = 510$$
etc.

- Note that the asset **will NEVER fully** depreciate by this method (not important though).
- Salvage value not used in calculation.
- Other variants are possible. Such as 150\% declining balance $\frac{1.5}{N}$.


### Sum-of-Years’-Digits Depreciation

![[Pasted image 20240620145829.png]]
$$d_t = \frac{N-t+1}{\text{SOYD}}\cdot(B-S)$$
$\text{SOYD}$: sum of year’s digits, $\frac{N(N+1)}{2}$.

Ex)
An asset costs \$12,000 and has a salvage value of \$2,000 after 5 years. If you use sum-of-years’-digit method of depreciation, find the book value at the end of year 2.

$$d_1 = \frac{5-1+1}{15}\cdot(12000-2000) = 3333$$
$$d_2 = \frac{5 - 2 + 1}{15}\cdot(12000-2000) = 2667$$
$$BV(2) = B - d_1-d_2 = 6000$$

### Unit-of-Production Depreciation

$$\text{UOP depreciation} = \frac{\text{Production for Year}}{\text{Total lifetime production}}\cdot (B-S)$$
- Based on physical use of the asset, not time.
- The remaining value of the asset = the remaining physical amount of the asset.
- Works well for supplies that you intend to use over many years.

Ex)
Capital cost \$900,000, Project life 5 years, Salvage value \$70,000. 40,000m^3 of sand to be used:

| Year  | Sand Required (m^3) |
| ----- | ------------------- |
| 1     | 4000                |
| 2     | 8000                |
| 3     | 16000               |
| 4     | 8000                |
| 5     | 4000                |
| Total | 40000               |

Calculate UOP depreciation schedule.

$$d_1 = \frac{4000}{40000}\cdot(900000-70000) = 83000$$
And if we calculate the depreciation,

| Year | UOP depreciation |
| ---- | ---------------- |
| 1    | 83000            |
| 2    | 166000           |
| 3    | 332000           |
| 4    | 166000           |
| 5    | 83000            |

## The Capital Cost Allowance System
In Canada, most assets are depreciated using a more complex declining-balance method.
The depreciation rate depends on the type of asset. 
Regulations are set out in the **capital cost allowance (CCA)** system.

- Canada has legislation on how assets are depreciated.
- The terms used in Income Tax Act are different.
- There are different rates for different types of assets.
- The maximum capital cost allowance a company can take in one year is what would be sufficient to reduce taxable income to zero.
- Generally, **only half of a given rate can be applied during the year that an asset is purchased (the first year of depreciation)** - but exceptions exist.
- The remaining value in each pooled account is called the **Undepreciated Capital Cost (UCC)**

![[Pasted image 20240620153026.png]]
- Capital cost of asset is total acquisition cost (including installation, transportation, legal, accounting, etc.).
- As asset is depreciated, company keeps track of **undepreciated capital cost (UCC)** which may differ from market or salvage value.
- The Canadian tax system uses the **half-year rule**. In the year of purchase and salvage only half the usual depreciation is applied.
- $\text{UCC}_{\text{opening}} + \text{additions} - \text{disposals} - \text{CCA} = \text{UCC}_{\text{ending}}$ 


### Natural Capital Assets
Natural capital can be defined as the world’s stocks of natural assets which include geology, soil, air, water and all living things.

It is from this natural capital that humans derive a wide range of services, often called ecosystem services, which make human life possible.

Examples: land (food), forests (building materials), watersheds (water), insects (pollination).

Interest is growing in incorporating such assets into traditional accounting frameworks.


## Next Lecture [[Lecture WACC]]
