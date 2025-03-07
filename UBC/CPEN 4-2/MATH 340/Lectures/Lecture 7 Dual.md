##### Theorem (Degeneracy Recap)
$$\text{No Degeneracy → The simplex algorithm } \textbf{must} \text{ terminate.}$$

If we start from a feasible dictionary, and at each step the dictionary is non-degenerate. Then,
- The pivot moves to the next corner point (unless unbounded).
- When moving to the next corner point, the objective function will (strictly) increase.
- Hence, no corner point can be visited twice.
→ It MUST terminate.

##### Fundamental Theorem of LP
Every linear programming problem in standard form has the following properties:
- If it has *no optimal solution* then the either it is infeasible, or unbounded.
- If it has *feasible solutions*, then it has a feasible dictionary.
- If it has *an optimal solution*, then it has a basic optimal solution.

##### Duality
In duality we have a Primal LP as well as a Dual LP,
$$\begin{aligned}
\text{Primal LP}& \\ 
\text{maximize } & c_{1}x_{1} + c_{2}x_{2} + \cdots + c_{n}x_{n} \\
\text{subject to } &a_{11}x_{1}+a_{12}x_{2}+\cdots+a_{1n}x_{n} \leq b_{1} \\ 
&a_{21}x_{1}+a_{22}x_{2}+\cdots+a_{2n}x_{n} \leq b_{2} \\
&\vdots \\
&a_{m{1}}x_{1}+a_{m{2}}x_{2}+\cdots+a_{mn}x_{n} \leq b_{m} \\ 
& x_{1},x_{2},\cdots,x_{n} \geq 0
\end{aligned}$$

$$\begin{aligned}
\text{Dual LP}&\\
\text{minimize }& b_{1}y_{1}+\cdots+b_{m}y_{m} \\ 
\text{subject to }&a_{11}y_{1}+a_{21}y_{1} + \cdots + a_{m{1}}y_{m} \geq c_{1} \\ 
& a_{12}y_{1} + a_{22}y_{2} + \cdots + a_{m{2}}y_{m} \geq c_{2} \\ 
&\vdots \\ 
&a_{1n}y_{1}+ a_{2n}y_{2} + \cdots + a_{mn}y_{m} \geq c_{n}
\end{aligned}$$

In matrix form,
$$A= \begin{bmatrix}
a_{11} & a_{12} & \cdots  & a_{1n}  \\
\vdots &  &  & \vdots  \\
a_{m{1}} & a_{m{2}} & \cdots & a_{mn}
\end{bmatrix},\vec{x} = \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}, \vec{c}=\begin{bmatrix}
c_{1} \\
c_{2} \\
\vdots \\
c_{n} \\

\end{bmatrix}$$
$$\vec{y} = \begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots  \\
y_{m}
\end{bmatrix}, \vec{b} = \begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{bmatrix}$$

Hence, the primal LP is
$$\begin{aligned}
\text{maximize } & \vec{c} \cdot  \vec{x} \\ 
\text{subject to } &A \vec{x}\leq \vec{b} \\
& \vec{x} \geq \vec{0}
\end{aligned}$$
and the dual LP is
$$\begin{aligned}
\text{minimize } & \vec{b}^T \vec{y}\\ 
\text{subject to } &A^T \vec{y} \geq \vec{c} \\ 
& \vec{y} \geq \vec{0}
\end{aligned}$$

For instance,
[Primal]
$$\begin{aligned}
\text{maximize } &  4x_{1}+3x_{2}+x_{3}+x_{4} \\
\text{subject to } & x_{1}+2x_{2}-x_{4} \leq 3 \\
&2x_{1}+x_{2}-x_{3}+x_{4} \leq 2 \\ 
&x_{2}+x_{3} \leq 2\\ 
& x_{1},x_{2},x_{3},x_{4} \geq 0
\end{aligned}$$


[Dual]
$$\begin{aligned}
\text{minimize } & 3y_{1}+2y_{2}+2y_{3} \\ 
\text{subject to } & y_{1}+2y_{2} \geq 4 \\  
&2y_{1}+y_{2}+y_{3} \geq 3 \\ 
& -y_{2} +y_{3} \geq 1 \\ 
& -y_{1} + y_{2} \geq 1\\
&y_{1},y_{2},y_{3} \geq 0
\end{aligned}$$

Where does the duality come from? We consider the
- Penalty method for constraint optimization problem.

Let,
$$f: \text{function of } \vec{x} \in \mathbb{R}^n$$
$$C \subset \mathbb{R}^n \text{ Constraint}$$

$$\left\{ \begin{aligned}
&\text{maximize } f(\vec{x}) \\ 
&\text{subject to } \vec{x} \in C
\end{aligned} \right\} \iff \begin{aligned}
\text{maximize } & [f( \vec{x} ) + p(\vec{x})]  \\ 
\text{where } & p(\vec{x}) = \begin{cases}
0 \quad &\text{if } \vec{x} \in C  \\
-\infty \quad &\text{if } \vec{x} \not\in C
\end{cases}
\end{aligned}$$
$p(\vec{x})$ is the “hard penalty function”. 


Relaxation of penalty (soft penalty),
$$\begin{aligned}
\text{maximize } &f(\vec{x}) + g(\vec{x}) \\ 
\text{such that } & \begin{cases}
g(\vec{x}) \geq 0 \quad & \text{if } \vec{x} \in C \\
g(\vec{x}) < 0\quad & \text{if } \vec{x} \not\in C
\end{cases}
\end{aligned}$$
![[Screenshot 2025-02-27 at 11.24.27 AM.png]]


Let’s discover the rationale of all this non-sense (cuz I wasn’t understanding a thing just from this bs.).

Let’s assume we have the following LP problem (Primal),
$$\begin{aligned}
z &= 3x_{1}+ 4x_{2}  \\ 
&\frac{1}{2}x_{1} + 2x_{2} \leq 30 \\ 
&3x_{1} + x_{2} \leq 25 \\ 
&x_{1}, x_{2} \geq 0
\end{aligned}$$

Then, we know try a couple linear combinations of the constraints,
$$\begin{aligned}
6\left( \frac{1}{2}x_{1} + 2x_{2} \right) &= 3x_{1} + 12x_{2} \leq 180 \to z \leq 180 \\ 
4 (3x_{1}+x_{2}) &= 12x_{1} + 4x_{2} \leq 100 \to z \leq 100 \\ 
2\left( \frac{1}{2}x_{1} + 2x_{2} \right) + (3x_{1}+x_{2}) &= 4x_{1} + 5x_{2} \leq 85 \to z\leq 85
\end{aligned}$$
Since $x_{1},x_{2} \geq 0$, we can see that we can keep on finding the lower bound of the maximization fro the constraints. In other words, given $y_{1},y_{2} \geq 0$,
$$\begin{aligned}
&y_{1}\left( \frac{1}{2}x_{1} + 2x_{2} \right) + y_{2} ( 3x_{1} + x_{2}) \\ 
&=\left( \frac{1}{2}y_{1} + 3y_{2} \right)x_{1} + (2y_{1} + y_{2})x_{2} \leq  30y_{1} + 25y_{2}
\end{aligned}$$

Our goal is now to find the minimum of $30y_{1}+25y_{2}$, where $\frac{1}{2}y_{1} + 3y_{2}  \geq{3}$ and $2y_{1} + y_{2} \geq 4$. 

Thus, giving us the **Dual Problem**,
$$\begin{aligned}
\text{minimize } &30y_{1}+25y_{2} \\ 
\text{subject to }  & \frac{1}{2}y_{1} + 3y_{2} \geq 3 \\ 
&2y_{1}+y_{2} \geq 4 \\ 
&y_{1},y_{2} \geq 0
\end{aligned}$$

Fun stuff hehe 😼.

Now back to penalization,

- In the relaxed penalization, it is OK not to satisfy the constraint, but still it is preferable to stay in or near the constraint.
- The optimal solution in the relaxed problem can still be close to the optimal solution of the un-relaxed problem, if an appropriate relaxation is made.

Consider the LP, to maximize $\vec{c}^T \cdot \vec{x}$ subject to $A \vec{x} \leq \vec{b}, \vec{x} \geq \vec{0}$ which is $m+n$ constraints. 

Now, consider the Lagrange multiplier
$$\vec{y} \in \mathbb{R}^m, \vec{y} \geq 0\quad \cap\quad \vec{w} \in  \mathbb{R}^n , \vec{w} \geq \vec{0}$$
then the relaxed penalty is,
$$g_{\vec{y}, \vec{w}}(\vec{x}) = \vec{y}^T (\vec{b} - A \vec{x}) + \vec{w}^T \vec{x}$$
and note that $\vec{y}, \vec{w} \geq \vec{0}$ and $g_{\vec{y}, \vec{w}}( \vec{x}) \geq 0$ only if $\vec{x}\geq \vec{0} \quad \cap \quad A \vec{x} \leq \vec{b}$.

For the given constraints above, the relaxed problem is then,
$$\text{maximize }_{\vec{x}} [ \vec{c}^T \vec{x} + g_{\vec{y}, \vec{w}}(\vec{x}) ]$$
with no extra constraints.

Therefore,
$$\vec{c}^T \vec{x}+ g_{\vec{y}, \vec{w}}(\vec{x}) \geq \vec{c}^T \vec{x}$$ if $\vec{x} \geq \vec{0},  A \vec{x} \leq \vec{b}$.

Let $F( \vec{y}, \vec{w}) = \text{max }_{\vec{x}} [ \vec{c}^T \vec{x} + g_{\vec{y}, \vec{w}}(\vec{x})],$ the maximum of the relaxed problem for fixed $\vec{y}, \vec{w}$.

Then, for any $\vec{y}, \vec{w} \geq \vec{0}$,
$$\begin{aligned}
F(\vec{y}, \vec{w}) 
& \geq  \text{max }_{\vec{x}}\; [ \vec{c}^T \vec{x} + g_{\vec{y}, \vec{w}}(\vec{x})]\\
 & \geq \text{max}_{A \vec{x} \leq \vec{b}, \vec{x} \geq\vec{0}} \; [ \vec{c}^T \vec{x} + g_{\vec{y}, \vec{w}}(\vec{x})]  \\
&\geq \text{max }_{A \vec{x} \leq \vec{b}, \vec{x} \geq\vec{0}} \; \vec{c}^T \vec{x}
\end{aligned}$$

Thus, we want to solve for,
$$\begin{aligned}
\text{minimize } &F(\vec{y}, \vec{w}) \\
\text{subject to } &\vec{y},\vec{w} \geq \vec{0} 
\end{aligned}$$


#### Next Lecture [[Lecture 8 Weak Duality]]
