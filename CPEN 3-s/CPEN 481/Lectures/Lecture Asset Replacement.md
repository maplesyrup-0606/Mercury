## Introduction
Survival of businesses require regular evaluation of assets (plant \& equipment) used in production.

When an asset is evaluated, there are one of four mutually exclusive choices:
1. Keep the asset in use without change (do nothing).
2. Overhaul the asset to improve its performance.
3. Remove it from use without replacement.
4. Replace the current asset with another asset.

When and why should you replace a physical asset? Let’s set up the analysis structure and cases we need to assess:
- The existing physical asset is called the **defender**.
- The potential replacement is called the **challenger**.
- Challenger and defender do not always have to be the same.
- Cases that need to be considered:
	- When a defender and challenger are the same.
	- When a defender is different from the challenger.
	- When a defender is different from the challenger, which is itself different from another replacing it in the future.

## Reasons for Retirement of Replacement

**Reasons for retirement**:
- An existing asset is retired if it is removed from use without being replaced, because the service that the asset provides is no longer needed.

**Reasons for replacement**:
- Replacement becomes worthwhile if there is a cheaper way to get the service provided.
- **Use-related physical loss**:
	- As something is used, parts wear out.
	- Usually measured in units of production, km driven, hours of use.
- **Time-related physical loss**:
	- Even if something is not actively in use, physical loss can occur over time.
	- Usually measured in units of time as an unused car will rust and lose value over time.
- **Functional loss**:
	- Losses can occur without physical changes.
	- Usually expressed in terms of function lost including fashion, legislative and technical changes.
- **Capacity limit reached**
- **Technological improvements**: replacement is less expensive.


## Capital Costs and Other Costs

- Purchasing assets is a decision to acquire **capacity**.
	- Capacity is the ability to produce.
- Just acquiring the capacity entails costs that are incurred whether or not there is actual production.

Relevant costs associated with owning assets:
1. **Capital costs (P)**: difference between price paid and what it can be sold for later (usually expressed as EAC).
2. **Installation costs (I)**: not reversable after the fact.
	- Includes lost production time and lost output.
3. **Operating and maintenance (O\&M) costs**:
	- The cost of using the asset to produce goods/services. Might include the cost of electricity, gasoline etc.

Different types of costs being discussed can be related to:
- Fixed costs:
	- Remain the same regardless of actual units of production.
- Variable costs:
	- Costs that change depending on the number of units produced.

Three different replacement cases will be examined:
1. Defender and challenger are **identical** and the need for the asset repeats indefinitely.
2. Challenger repeats indefinitely but is **different** from the defender.
3. Defender and challenger are different and challenger does not repeat.

### Estimating Salvage Values and Scrap Values

- When an operating asset is replaced, its salvage value greatly depends on what was done with it.
- To make a good replacement decision, it is desirable to have an accurate estimate of the actual salvage value of the asset.
- If the asset is scrapped:
	- Value can be estimated from posted values for metal scrap available on the web.

#### Defender and Challenger Are Identical

- Assumptions (relative to time horizon):
	- The defender / challenger are technologically identical.
	- Lives of these identical assets are assumed to be short.
	- Relative prices / interest rates are assumed constant.
- We model the replacement decision as if it were to take place a large number of times (**cyclic replacement**).
- Then determine the minimum-cost lifetime of the assets.


- Capital costs decrease (per period) while O&M generally increases (per period) over time.
	- Rise in O&M costs is initially offset by the decrease in capital costs per year that occurs at the asset life is extended.
		- Capital costs are spread over a greater number of years.
- Changes in the two sets of costs work in the opposite direction as the life of the asset is extended.
- There usually is a lifetime that will minimize EAC. This is the **economic life** of the asset.

![[Screenshot 2024-06-21 at 12.37.07 AM.png]]

$$\text{EAC} = (P-S)\cdot (A/P,i,n)+S\cdot i$$
Calculate $EAC$’s separately!

#### Challenger is Different from Defender; Challenger Repeats Indefinitely

1. Determine the Economic Life of the challenger and its associated EAC.
2. Determine the remaining Economic life of the defender and its associated EAC.
3. If the EAC (defender) > EAC (challenger), replace now. Otherwise, do not replace now.
- ==For assets “in place”== for many years, annual capital costs will be low in comparison to O&M costs and EAC (total) will be increasing each $N$.
- Use **One year principle**: When ==above== exists and the yearly operating costs are monotonically increasing, the economic life of the defender is one year and total EAC is the cost of using the defender for one more year.

	- This implies:
		1. Treat EAC of Defender as the cost of operating it for one more year (ignore capital part).
		2. If EAC of keeping Defender one more year exceeds the EAC of Challenger at its economic life, replace defender immediately.

![[Screenshot 2024-06-21 at 12.54.35 AM.png]]


## The Irrelevance of Sunk Costs

- Once an asset has been installed and has been operating for some time, the costs of installation, and all other costs incurred up to that time are no longer relevant to any decision to replace the current asset.
- These costs are called **sunk costs**.
- Only those costs that will be incurred in keeping operating the asset from this time on are relevant.

#### When Capital or Operating Costs are Non-Monotonic
Sometimes operating and/or capital costs do not increase smoothly (monotonically) over time.
- Then the one year principle does not apply because there may be one-time or periodic costs that occur over the course of the next year.
- Such costs may make the costs of keeping the defender for one more year greater than installing / using the challenger over its economic life.
	- However, there may be a life longer than one year over which the cost of using the defender is less than the cost of installing and using the challenger.

#### Challenger is Different from Defender; Challenger Does Not Repeat

- We no longer assume that challengers are alike.
- We recognize future challengers will be available and we expect them to be better than the current challenger.
- We must decide whether the current challenger must replace the defender.
- If the defender is to be replaced by the current challenger, when should the replacement occur?

It is reasonable to consider only the combinations of the period of length of one year.

To choose among the possible alternatives, information about the defender and challengers are needed:
1. Costs of installing the challengers.
2. Salvage values for different possible lives for all three.
3. Operating and maintenance costs for all possible ages of three.

==”three” as in referring to example 7.10==

