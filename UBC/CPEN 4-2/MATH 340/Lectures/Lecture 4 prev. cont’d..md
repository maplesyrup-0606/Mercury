#### Gradient of Objective Function
The gradient $\nabla f$ is defined as,
$$\nabla f = \left( \frac{\partial f}{\partial x_{1}}, \frac{\partial f}{\partial x_{2}},\cdots,\frac{\partial f}{\partial x_{n}} \right)$$
The direction of the gradient, $\nabla f(\vec{x})$ is the vector which as the direction where $f$ increases the most at $\vec{x}$.
- It’s magnitude is the maximum rate of change.

For the function $f(\vec{x})=\vec{a}\cdot\vec{x}$, it 
- increases, if you move in $\vec{u}$ where $\vec{u} \cdot  \vec{a} >0$
- decreases, if you move in $\vec{u}$ where $\vec{u}\cdot  \vec{a} < 0$


#### Simplex Method
We know that the maximum occurs at a vertex, hence we simply move along the vertices to find the maximum.

We can move from one vertex to the other by changing the set of variables with zero value.

![[Screenshot 2025-01-31 at 9.19.21 PM.png]]

**But, how do we choose the variables that we change from zero → non-zero or vice versa, in a way the value of the objective function increase?**

E.g.

$$\text{maximize } 4x_{1}+3x_{2}$$
$$\text{s.t. } 2x_{1}+x_{2}\leq{4}0$$
$$x_{1}+x_{2} \leq 30$$
$$x_{1} \leq 15$$
$$x_{1},x_{2} \geq 0$$

[**Step 0**]
Form a dictionary by introducing slack variables,
$$z=4x_{1}+3x_{2}$$
$$x_{3} = 40 -2x_{1}- x_{2}$$
$$x_{4} = 30 -x_{1} -x_{2}$$
$$x_{5} = 15-x_{1}$$
And we know $x_{1},x_{2},x_{3},x_{4},x_{5} \geq 0$.

**Basic Variables**: Variables on the left. → Not necessarily slack variables.
**Non-basic Variables**: Variables on the right.

###### Terminologies
- Basic solution of dictionary: Solution where all non-basic variables have zero value.$$z=4x_{1}+3x_{2}$$$$x_{3}=40-2x_{1}-x_{2}$$$$x_{4}=30-x_{1}-x_{2}$$$$x_{5}=15-x_{1}$$The basic solution is $(x_{1},x_{2},x_{3},x_{4},x_{5}) = (0,0,40,30,15)$
	- This basic solution is feasible → The dictionary is feasible.
- Feasible solution: A solution that satisfies all constraints.
- Feasible basic solution: A basic solution that is also feasible.
- Feasible dictionary: A dictionary where the basic solution if feasible.
	- All $x_{i} \geq 0$. (both original and slack variables)


[Fact]
**A feasible dictionary gives a feasible basic solution, which is a vertex of the feasible region → Each vertex of the feasible region is the basic solution of a feasible dictionary.**
- Hence, “moving along corner points” is the same as “re-writing dictionaries in equivalent form”.

###### When to stop?
After iterations, we will eventually find a final expression of the objective function,
$$z = 100 -x_{3}-2x_{4}$$
from the example above.

What is the point of such a final expression?
We had $x_{3},x_{4} \geq {0}$. So, if we change them in the feasible region $z$ will decrease.
→ $z \leq 100$, at $z = 100$ we have $x_{3},x_{4} = 0$.

The goal is to find a “good” feasible dictionary for the LP problem, which has such a “good” expression of the objective function.

###### Step-by-step procedure
[**Step 1**]
Start with a “feasible” dictionary (some vertex of the feasible region).

$$z=4x_{1}+3x_{2}$$$$x_{3}=40-2x_{1}-x_{2}$$$$x_{4}=30-x_{1}-x_{2}$$$$x_{5}=15-x_{1}$$
Basic variables: $x_{3},x_{4},x_{5}$
Non-basic variables: $x_{1},x_{2}$

The basic solution here is $x_{1}=0,x_{2}=0,x_{3}=40,x_{4}=30,x_{5}=15$.
- The basic solution is feasible.
- The dictionary is feasible.

[**Step 2**]
We have two important steps to do,
- *Choose an entering variable from the non-basic ones.*
- *Choose a leaving variable fro the basic variables.*
in a way that in the updated dictionary the corresponding feasible basic solution has a bigger objective function value than before.

**Entering variable:**
Choose a non-basic variable whose increase makes $z$ increase.

**Leaving variable:**
The basic variable that becomes zero first as the entering variable increases.

We have the objective function,
$$z=4x_{1}+3x_{2}$$
both $x_{1},x_{2}$ make the objective function increase, so we choose the one with the lower index.

Now, considering that $x_{1}$ leaves, by setting $x_{2}=0$,
$$x_{3} = 0 \to x_{1}=20$$
$$x_{4}=0 \to x_{1}=30$$$$x_{5}=0 \to x_{1}= 15$$
$x_5$ becomes zero the first as $x_1$ increases → $x_5$ is our leaving variable!

[**Step 3**]
Now we update the dictionary.
$$x_{5}=15-x_{1} \to x_{1}=15-x_{5}$$
$$z = 4x_{1}+3x_{2} =60+3x_{2}-4x_{5}$$
$$x_{3}=40-2x_{1}-x_{2}= 10 -x_{2}+2x_{5}$$
$$x_{4} = 30-x_{1}-x_{2} = 15-x_{2}+x_{5}$$


Let’s look at the basic solution,
$$x_{1}=15,x_{2}=0,x_{3}=10,x_{4}=15,x_{5}=0$$
*It’s feasible!*

[**Step 4**]
Iterate “pivoting”!

Our new entering variable is $x_{2}$ given that we can see that $x_{3}$ reaches it’s 0 first.

Thus,
$$x_{2}=10-x_{3}+2x_{5}$$
$$x_{4}= 5+x_{3}-x_{5}$$
$$x_{1}=15-x_{5}$$
$$z=90-3x_{3} + 2x_{5}$$

One more time, where $x_5$ enters and $x_{4}$ leaves.

$$x_{5} = 5+x_{3}-x_{4}$$
$$x_{2}= 20+x_{3}-2x_{4}$$
$$x_{1}=10-x_{3}+x_{4}$$
$$z=100 -x_{3} -2x_{4}$$

Now, we finally reached the form we’ve desired.
The maximum of $z$ occurs when $x_{3}=x_{4}=0$ where $z=100$. At this point,
$$x_{1}=10,x_{2}=20$$


==This is our final dictionary since the objective function value decreases with the leaving variables.==

#### Special Cases of the Simplex Method

When we start with a feasible dictionary,
- What if there is no choice for entering / leaving variables? e.g. $$z=100-x_{3}-2x_{4}$$$$x_{2}=20+x_{3}-2x_{4}$$$$x_{1}=10-x_{3}+x_{4}$$$$x_{5}=5+x_{3}-x_{4}$$None of the leaving variables can be an entering variable despite having a feasible solution. This point it is just the max.
- What if we have an entering variable but no leaving variable?           Geometrically speaking,![[Screenshot 2025-01-31 at 10.44.37 PM.png]] We have no leaving variable in the gradient direction means that the LP is **unbounded**. For instance, $$z=10+x_{3}-x_{5}-2x_{6}$$$$x_{4}=1-x_{5}-x_{6}$$$$x_{2}=1+2x_{3}-x_{6}$$$$x_{1}=1+x_{3}+x_{5}-x_{6}$$In this case, we have the entering variable $x_3$, but none of the non-basic variables will leave! There are unbounded. Let $x_{3}=t,x_{5}=0,x_{6}=0$, $$x_{1}=1+t,x_{2}=1+2t,x_{3}=t,x_{4}=1,x_{5}=0,x_{6}=0$$which will give us $$z=10+t \to \infty$$**There is no optimal solution!**

###### Anstee’s Rule
- For the entering variable choose the one with the largest positive coefficient in the objective function.
	- For a tie, pick the one with the smaller index.
- For the leaving variable, if there is a tie.
	- Choose the one with the smaller index.

###### Example
$$\text{maximize }2x_{2}+x_{3}$$
$$\text{s.t. }x_{1}-x_{2}+x_{3} \leq 5$$
$$-2x_{1}+x_{2} \leq 3$$
$$x_{2}-2x_{3}\leq{5}$$
$$x_{1},x_{2},x_{3} \geq 0$$

[Initial Dictionary]
$$z=2x_{2}+x_{3}$$
$$x_{4}= 5-x_{1}+x_{2}-x_{3}$$
$$x_{5}=3+2x_{1}-x_{2}$$
$$x_{6}=5-x_{2}+2x_{3}$$

NBV: $x_{1},x_{2},x_{3}$
BV: $x_{4},x_{5},x_{6}$

EV: $x_2$
LV: $x_{5}$ reaches 0 first.

---
[update]
$$x_{2}=3+2x_{1}-x_{5}$$
$$x_{4}=8+x_{1}-x_{3}-x_{5}$$
$$x_{6}=2-2x_{1}+2x_{3}+x_{5}$$
$$z=6+4x_{1}+x_{3}-2x_{5} $$
BV: $x_{2},x_{4},x_{6}$
NBV: $x_{1},x_{3},x_{5}$

EV: $x_1$
LV: $x_{6}$

---
$$x_{1}=1+x_{3}+\frac{1}{2}x_{5}- \frac{1}{2}x_{6}$$
$$z=10+5x_{3}-2x_{6}$$
$$x_{4}= 9-\frac{1}{2}x_{5} - \frac{1}{2}x_{6}$$
$$x_{2}=5+2x_{3}-x_{6}$$

[update]
BV: $x_{1},x_{2},x_{4}$
NBV: $x_{3},x_{5},x_{6}$

EV: $x_{3}$
LV: none

It is unbounded!!


#### Next Lecture [[Lecture 5 Two Phase Simplex Method|Lecture 5 Two Phase Simplex Method]]


  