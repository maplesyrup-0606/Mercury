#### Problematic Cases of LP with Simplex
We’ve been considering the cases where the initial dictionary is feasible.
But what happens if the initial dictionary isn’t feasible?

For instance,
$$\begin{aligned}
\text{max }&x_{1} \\ \text{subjec to } & x_{1}-x_{2}\leq-10 \\ 
&x_{1},x_{2}\geq{0}
\end{aligned}$$
When setting $x_{3}=-10-x_{1}+x_{2}$, the initial basic solution isn’t feasible.

Or, we can just not have a feasible solution,
$$\begin{aligned}
\text{max }&x_{1}+x_{2} \\
\text{subject to }&x_{1}-x_{2}\leq_{1}\\
&x_{1}+x_{2}\leq -1\\
& -2x_{1}+x_{2} \leq -2\\
&x_{1},x_{2}\geq{0}
\end{aligned}$$
```functionplot
---
title: Feasible regions
xLabel: x_1
yLabel: x_2
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x) = -x-1
g(x) = x-1
h(x) = 2x-2

```

Then how can we check that the feasible set isn’t empty with a lot of variables?
→ Two phase simplex method!

e.g.
$$\begin{aligned}
z&=x_{1}+x_{2} \\ x_{3}&=-5+x_{1} \\ x_{4}&=1-x_{2}
\end{aligned}$$
When $x_{1}=x_{2}=0$, we get the basic solution $\left\{ x_{1},x_{2},x_{3},x_{4} \right\}=\left\{ 0,0,-5,1 \right\}$ which is not feasible.

We need some mechanism to help us!

#### Two Phase Simplex Method
**Phase 1**
- Solve an LP (the auxiliary problem) for **feasibility** and find a feasible dictionary (in the case it is a feasible LP problem for the original problem).

**Phase 2**
- Solve original LP problem, starting from the initial dictionary from phase 1.

Consider the following example,
$$\begin{aligned}
\text{max } &x_{1}-2x_{2}+x_{3}\\
\text{subject to } &2x_{1}+x_{2}-x_{3}\leq {5} \\
&-x_{1}+x_{3} \leq -2 \\ 
&x_{2}-x_{3} \leq -1 \\ 
&x_{1},x_{2},x_{3}\geq{0}
\end{aligned}$$

[Phase 1]
Consider the “auxiliary LP”. We introduce $x_{0}$ such that
$$\begin{aligned}
\text{max } &-x_{0} \\ 
\text{subject to } &2x_{1}+x_{2}-x_{3}-x_{0} \leq 5\\
& -x_{1} +x_{3} -x_{0} \leq -2 \\ 
&x_{2} - x_{3} - x_{0} \leq -1 \\
&x_{0},x_{1},x_{2},x_{3} \geq 0
\end{aligned}$$
The feasible region is non-empty, since we can set $x_{1},x_{2},x_{3}=0$ and have $x_{0}$ large enough to satisfy the constraints.

The **Idea** is to make $x_{0} \gg 1$ large & positive so that we can find $x_{1},\cdots,x_{n}\geq {0}$ such that the constraints are satisfied.
$$\left\{ \text{constraints of auxiliary LP} \cap x_{0} \right\} \to \left\{ \text{constraints of original L{P}} \right\}$$

*The auxiliary problem in phase 1 is always feasible!!!*

Given the feasible region of the auxiliary LP, we have two cases,

1. Intersection
![[Screenshot 2025-02-06 at 12.06.50 PM.png]]
Here the y-axis refers to the original space of the original LP Problem. The intersection with $\left\{ x_{0}=0 \right\}$ and the feasible region of the auxiliary problem is the original LP’s feasible region.

2. No intersection
![[Screenshot 2025-02-06 at 12.08.12 PM.png]]
In this case, the space of the original LP problem doesn’t intersect with the auxiliary space’s feasible region. → Showing that the original LP problem **is not feasible!**

[Let’s try it out]
$$\begin{aligned}
\text{max } &-x_{0} \\ 
\text{subject to } &2x_{1}+x_{2}-x_{3}-x_{0} \leq 5\\
& -x_{1} +x_{3} -x_{0} \leq -2 \\ 
&x_{2} - x_{3} - x_{0} \leq -1 \\
&x_{0},x_{1},x_{2},x_{3} \geq 0
\end{aligned}$$

Which is 
$$\begin{aligned}
w&=-x_{0} \\ 
x_{4} &= 5 +x_{0}-2x_{1}-x_{2}+x_{3} \\
x_{5}&= -2+x_{0}+x_{1}-x_{3}\\
x_{6} &= -1+x_{0}-x_{2}+x_{3} 
\end{aligned}$$
This is not a feasible dictionary, $\left\{ x_{0},x_{1},x_{2},x_{3},x_{4},x_{5},x_{6} \right\} = \left\{ 0,0,0,0,5,-2,-1 \right\}$ **yet**.
For the initial part, we need a special step ( for entering / leaving  variables) to find a feasible initial dictionary.

==This is different from checking the feasibility of the auxiliary LP problem!!==

- $x_{0}$ is our entering variable.
- Our leaving variable will be the *last* variable that becomes non-negative as $x_0$ increases wile other non-basic variables are 0.

Which in the example above is "$x_{5}$".

$$\begin{aligned}
w &= -2 +x_{1}-x_{3}-x_{5} \\ 
x_{0} &= 2-x_{1}+x_{3}+x_{5} \\ 
x_{4} &= 7-3x_{1}-x_{2}+2x_{3}+x_{5} \\ 
x_{6} &= 1-x_{1}-x_{2}+2x_{3}+x_{5}
\end{aligned}$$
Now, we use the usual simplex method to get the final dictionary.
Entering variable → $x_1$, Leaving variable → $x_{6}$.

…

And thus getting the final dictionary,
$$\begin{aligned}
w&=-x_{0} \\ 
x_{1}&=3-2x_{0}+x_{2}+x_{5}+x_{6} \\
x_{4}&=0 + 4x_{0}-2x_{2}-2x_{5}-x_{6} \\ 
x_{3}&=1-x_{0}+x_{2}+x_{6}
\end{aligned}$$

Since the optimal value for the auxiliary problem is 0, we can get a feasible dictionary of the original problem by setting $x_{0}=0$. (otherwise the original problem is not feasible and we end it.)

Thus,
$$z= x_{1}-2x_{2}+x_{3}$$
and 
$$\begin{aligned}
x_{1}&=3+x_{2}+x_{5}+x_{6} \\ 
x_{4}&=-2x_{2}-2x_{5}-x_{6} \\ 
x_{3} &= 1+x_{2}+x_{6}
\end{aligned}$$
with basic variables $x_{2},x_{5},x_{6}$ and non-basic variables $x_{1},x_{3},x_{4}$.

$$\begin{aligned}
z&=x_{1}-2x_{2}+x_{3} \\ 
&= (3+x_{2}+x_{5}+x_{6})-2x_{2}+(1+x_{2}+x_{6}) \\ 
&= 4+x_{5}+2x_{6}
\end{aligned}$$

and we get move on to get the optimal solution using the simplex method since we now have a feasible basic dictionary.

