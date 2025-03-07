Consider the following LP problem,
$$\begin{aligned}
z &= \frac{8}{3} + \frac{4}{3}x_{3} + \frac{1}{3}x_{4} \\ 
x_{1} &= \frac{7}{3} - \frac{1}{3}x_{3} + \frac{2}{3}x_{4} \\ 
x_{2} &= \frac{1}{3} - \frac{1}{3}x_{3} + \frac{2}{3}x_{4} \\ 
x_{5} &= \frac{7}{3} - \frac{7}{3}x_{3} - \frac{1}{3}x_{4}
\end{aligned}$$
The entering variable is $x_3$, and when we choose the leaving variable, among $x_{2},x_{5}$ we choose $x_2$ due to Anstee’s rule.

The next dictionary is then,
$$\begin{aligned}
z &= 4-4x_{2}  +3x_{4}  \\
x_{1} &= 2+x_{2}-x_{4} \\ 
x_{3} &= 1-3x_{2} +2x_{4}  \\ 
x_{5} &= 0 + 7x_{2} - 5x_{4}
\end{aligned}$$
This dictionary is *degenerate*, **one of the basic variables of the corresponding basic solution is zero.**

From the previous step, for the same entering variable $x_3$, if we chose $x_5$ as the leaving variable, then the next dictionary would be different, *but the corresponding basic solution would still be the same.*


==Note that, for the basic solution, its non-basic variables are already zero. But for the degenerate case, the basic solution has an additional zero variable. 
→ Geometrically, the vertex of the feasible region has more than $n$ (the number of basic variables) hyperplanes of $\left\{ x_{k}=0 \right\}$ passing through it.==


- The basic feasible solution may not be changed after a “pivot” if the dictionary is degenerate.
	- If a “zero” basic variable leaves, the basic solution does not change.
	- If a “non-zero” basic variable leaves, the basic solution changes.

Essentially, you might get stuck in a loop.


==If a dictionary is feasible and non-degenerate and has an entering variable (i.e. not yet at the optimal dictionary), then “pivot” moves us out of the current corner point.==
→ And this is because for a non-degenerate feasible dictionary, an entering variable can be strictly increased. Thus, the pivot has to move us out of the current corner point.

Also, in LP, there are finitely many variables and finitely many constraints, therefore the feasible region has only a finite number of corner points.

e.g. 
If there are $n$ variables and $m + n$ constraints. The number of corner points is at most$$m+n \choose n$$

Why do we talk about degeneracy? In reality, in the worst case,
- The algorithm may get stuck at the degenerate corner point and does not move from the current corner.
	- This is called “cycling”.

For instance, using Anstee’s rule,
$$D_{1}\to D_{2}\to D_{3}\to \cdots\to D_{6}\to D_{1}\to D_{2}$$
Aft er 6 pivots, we get the same pattern again.

###### Theorem
If the simplex method fails to terminate, then is **must cycle**. In other words, **cycling** is the only case where the simplex method does not terminate.

- There are only finitely many dictionaries.
	- We have only finitely many variables.
	- A dictionary of an LP is completely determined by the set of non-basic variables.
	- So only finitely many possible sets of non-basic variables and thus finitely many possible dictionaries.

Hence, after infinitely many steps in the algorithm then a dictionary should occur more than once → thus cycling happens.

##### How do we avoid cycling? 
**Smallest Subscript Rule (Bland’s Rule)**

At each iteration, among the variables eligible for entering / leaving, we choose the one with the smallest subscript.
→ Under the smallest subscript rule, the simplex method terminates in finite number of iterations.

#### Next Lecture [[Lecture 7 Dual]]
