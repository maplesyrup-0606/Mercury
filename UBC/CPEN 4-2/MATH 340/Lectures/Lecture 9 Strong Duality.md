#### Theorem
**If** the primal problem has an optimal solution, say $\vec{x}^*$, then
- The dual problem also has an optimal solution $\vec{y}^*$.
- $\vec{c} \cdot  \vec{x}^* =\vec{b} \cdot   \vec{y}^*$. 

Moreover, from the row of the objective function of the optimal final dictionary of the primal problem,
$$\begin{aligned}
z&= z^* + \sum_{k=1}^{n+m} c_{k}^*x_{k} \\ 
&= z^* + c_{1}^* x_{1} + \cdots + c_{n}x_{n}^* +c_{n+1}x_{n+1}^* + \cdots +c_{n+m}x_{n+m}^*
\end{aligned}$$

(If $x_{k}$ is basic, then $x_{k} = 0$, then the optimal solution $z^*$ comes from setting the non-basic variables to 0.)

**Then**,
$$\vec{y}^*_{i} = -c^*_{n+1} \leftarrow \text{coefficients of the slack variables}$$
where $1 \leq i \leq m$, is a dual problem solution.

e.g.
$$ \vec{c} =\begin{bmatrix}
4 \\
3 \\
1 \\
1
\end{bmatrix}, \vec{b} = \begin{bmatrix}
3 \\
2 \\
2
\end{bmatrix}, A=\begin{bmatrix}
1 & 2 & 0 & -1 \\
2 & 1 & -1 & 1 \\
0 & 1 & 1 & 0
\end{bmatrix}$$

$$\begin{aligned}
\text{primal}& \\
\text{max} \quad&4x_{1}+3x_{2}+x_{3}+x_{4} \\
\text{s.j.t}\quad &x_{1}+2x_{2}-x_{4}\leq 3 \\ 
&2x_{1}+x_{2}-x_{3}+x_{4} \leq 2\\ 
&x_{2}+x_{3} \leq 2\\
&x_{1},x_{2},x_{3},x_{4} \geq 0
\end{aligned}$$
$$\begin{aligned}
\text{dual}& \\
\text{min} \quad &3y_{1} + 2y_{2} + 2y_{3} \\
\text{s.j.t}\quad &y_{1}+ 2y_{2} \geq 4 \\ 
&2y_{1}+ y_{2} + y_{3} \geq 3\\ 
&-y_{2}+ y_{3} \geq 1\\
&-y_{1} +y_{2} \geq 1\\
&y_{1},y_{2},y_{3}\geq 0
\end{aligned}$$

For the primal, after doing the simplex method, we get the final dictionary,
$$\begin{aligned}
z &= 10-2x_{2} -x_{4}-2x_{6}-3x_{4} \\ 
x_{1} &= 2-x_{2}- 0.5x_{4} - 0.5x_{6} - 0.5 x_{7} \\ 
x_{3} &= 2-x_{2} \\ 
x_{5} &= 1 - x_{2} + 1.5x_{4} + 0.5x_{6} + 0.5x_{7}
\end{aligned}$$

The primal optimal solution is,
$$\vec{x}^* = (\underbrace{ 2,0,2,0 }_{ \text{decision} },\underbrace{ 1,0,0 }_{ \text{slack} }),\quad \vec{c}^* = (\underbrace{ 0,-2,0,-1 }_{ \text{decision} },\underbrace{ 0,-2,-3 }_{ \text{slack} })$$
hence from the theorem, the optimal solution to the dual is,
$$\vec{y}^*  = (0,2,3)$$

So, if we find an optimal dual solution (with the simplex method - with standard form), we can use the final dictionary to find the optimal primal solution.

##### Complementary Slackness
Let,
$$\begin{aligned}
\vec{x}^* &= (x_{1}^*,\cdots,x_{n}^*) \\ \vec{y}^* &= (y_{1}^*,\cdots,y_{n}^*)
\end{aligned}$$
be feasible for the primal / dual problem respectively.

Then, the following are equivalent,
$$\begin{aligned}
&x_{j}^*y_{m+j}^* = 0 \quad j=1,\cdots,n \\
&y_{i}^*x_{n+i}^*= 0\quad i=1,\cdots,m
\end{aligned}$$
where $x_{n+i}^*,y_{m+j}^*$ are slack variables.

Note that,
$$\begin{aligned}
x_{n+i} &= b_{i} - \sum_{j=1}^n a_{ij}x_{j} \leftarrow \text{primal slack}\\ 
y_{n+j} &= \sum_{i=1}^n a_{ij}y_{i} -c_{j} \leftarrow \text{dual slack}
\end{aligned}$$
then,
$$\begin{aligned}
&y_{i}^*\left( b_{i} - \sum_{j=1}^n a_{ij}x_{j}^* \right) = 0 \\ 
&x_{j}^* \left( \sum_{i=1}^na_{ij}y_{i}^* - c_{j} \right)=0
\end{aligned}$$
complementary slackness can be used to check *optimality* of a solution.

Let’s prove, from weak duality,
$$\begin{aligned}
\sum_{j}c_{j}x_{j} &\leq \sum_{j}\left( \sum_{i}y_{i}a_{ij} \right)x_{j} \\
&=\sum_{i} \left( \sum_{j}x_{j}a_{ij} \right)y_{i} \\
&\leq \sum_{i}b_{i}y_{i}
\end{aligned}$$

The first inequality will only be held if $x_{j} =0$ or $c_{j} = \sum_{i}y_{i}a_{ij}$. Then the alternative to $x_j=0$, is simply $0 = c_{j} - \sum_{i}y_{i}a_{ij}$, but since $z_{j}=c_{j}-\sum_{i}y_{i}a_{ij}$ where $z_j$ is the slack variable. We apply the same method for the dual LP problem.

e.g.
$$\vec{c} = \begin{bmatrix}
4 \\
3 \\
1 \\
1
\end{bmatrix}, \vec{b} = \begin{bmatrix}
3 \\
2 \\
2
\end{bmatrix},A=\begin{bmatrix}
1 & 2 & 0 & -1 \\
2 & 1 & -1 & 1 \\
0 & 1 & 1 & 0
\end{bmatrix}$$
$$\begin{aligned}
\text{primal}& \\
\text{max} \quad&4x_{1}+3x_{2}+x_{3}+x_{4} \\
\text{s.j.t}\quad &x_{1}+2x_{2}-x_{4}\leq 3 \\ 
&2x_{1}+x_{2}-x_{3}+x_{4} \leq 2\\ 
&x_{2}+x_{3} \leq 2\\
&x_{1},x_{2},x_{3},x_{4} \geq 0
\end{aligned}$$
$$\begin{aligned}
\text{dual}& \\
\text{min} \quad &3y_{1} + 2y_{2} + 2y_{3} \\
\text{s.j.t}\quad &y_{1}+ 2y_{2} \geq 4 \\ 
&2y_{1}+ y_{2} + y_{3} \geq 3\\ 
&-y_{2}+ y_{3} \geq 1\\
&-y_{1} +y_{2} \geq 1\\
&y_{1},y_{2},y_{3}\geq 0
\end{aligned}$$
$$\vec{x}^* = (\underbrace{ 2,0,2,0 }_{ \text{decision} },\underbrace{ 1,0,0 }_{ \text{slack} }),\quad \vec{c}^* = (\underbrace{ 0,-2,0,-1 }_{ \text{decision} },\underbrace{ 0,-2,-3 }_{ \text{slack} })$$
Then, 
$$\vec{y}^* = (0,2,3)$$
and we can see that the complementary slack variable relation holds.

