### Example of cubic spline interpolation 1
Given the following coefficient matrix for a cubic spline with $t_0 = 1,t_1=1,\cdots,t_5=5$, find the unknowns.
$$C=\begin{bmatrix}
1 & -2 & 1 & a_{4} & 1 & 1 \\
0 & 3 & -3 & b_{4} & -6 & -3 \\
1 & 4 & 4 & c_{4} & -5 & -14  \\
1 & 3 & 8 & 10 & 9 & -1 
\end{bmatrix}$$

First, we use the equations given by using the continuity of $p''(t)$ evaluated at $k=3$ to get
$$6a_{3}+2b_{3}=2b_{4}$$

from,
$$p'_{3}(t_{3})=6a_{3}(t_{3}-t_{2})+2b_3=6a_{3}+2b_{3}$$
$$p'_{4}(t_{3})=6a_{4}(t_{3}-t_{3})+2b_{4}=2b_{4}$$

Resulting in $b_{4}=0$ since $a_{3}=1,b_{3}=-3$.

Second, we use the equations by using the continuity of $p'(t)$ evaluated at $k=3$ to get 
$$3a_{3}+2b_{3}+c_{3}=c_{4}$$
from,
$$p'_{3}(t_{3})=3a_{3}(t_{3}-t_{2})^2+2b_{3}(t_{3}-t_{2})+c_{3}=3a_{3}+2b_{3}+c_{3}$$
$$p'_{4}(t)=3a_{4}(t_{4}-t_{3})^2+2b_{5}(t_{3}-t_{3})+c_{4}$$

Resulting in $c_{4}=1$ since $a_{3}=1,b_{3}=-3,c_{3}=4$.

Third,= we use the equations given by using the continuity of $p''(t)$ evaluated at $k=4$ to get
$$6a_{4}+2b_{4}=2b_{5}$$
from,
$$p'_{4}(t_{4})=6a_{4}(t_{4}-t_{3})+2b_4=6a_{4}+2b_{4}$$
$$p'_{5}(t_{4})=6a_{5}(t_{4}-t_{4})+2b_{5}=2b_{5}$$

Resulting in $a_{4}=-2$ since $b_{4}=0,b_{5}=-6$.


### Example of cubic spline interpolation 2
If we have 5 data points $(t_{0},y_{0}),\cdots,(t_{4},y_{4})$, can we define a function $p(t)$ which has two pieces with
$$p_{1}(t)=a_{1}+b_{1}t+c_{1}t^2+d_{1}t^3,t \in[t_{0},t_{2}]$$
$$p_{2}(t)=a_{2}+b_{2}t+c_{2}t^2+d_{2}t^3,t\in[t_{2},t_{4}]$$
such that $p(t)$ interpolates the data and $p(t),p’(t)'$ are continuous? Write the linear system for finding the coefficients. Is $p(t)$ unique?

$$p_{1}(t_{0})=y_{0} \leftrightarrow a_{1}+b_{1}t_{0}+c_{1}t_{0}^2+d_{1}t_{0}^3=y_{0}$$
$$p_{1}(t_{1})=y_{1} \leftrightarrow a_{1}+b_{1}t_{1}+c_{1}t_{1}^2+d_{1}t_{1}^3=y_{1}$$
$$p_{1}(t_{2})=y_{2} \leftrightarrow a_{1}+b_{1}t_{2}+c_{1}t_{2}^2+d_{1}t_{2}^3=y_{2}$$
$$p_{2}(t_{2})=y_{2} \leftrightarrow a_{2}+b_{2}t_{2}+c_{2}t_{2}^2+d_{1}t_{2}^3=y_{2}$$
$$p_{2}(t_{3})=y_{3} \leftrightarrow a_{2}+b_{2}t_{3}+c_{2}t_{3}^2+d_{1}t_{3}^3=y_3$$
$$p_{2}(t_{4})=y_{4} \leftrightarrow a_{2}+b_{2}t_{4}+c_{2}t_{4}^2+d_{1}t_{4}^3=y_{4}$$

This gives us 6 equations. Let us also note that,
$$p'_{1}(t)=b_{1}+2c_{1}t+3d_{1}t^2$$
$$p_{2}'(t)=b_{2}+2c_{2}t+3d_{2}t^2$$

By continuity of $p’$,
$$p_{1}'(t_{2})=p_{2}'(t_{2})\leftrightarrow b_{1}+2c_{1}t_{2}+3d_{1}t_{2}^2=b_{2}+2c_{2}t_{2}+3d_{2}t_{2}^2$$
And by re-arranging,
$$b_{1}+2c_{1}t_{2}+3d_{1}t_{2}^2-b_{2}-2c_{2}t_{2}-3d_{2}t_{2}^2=0$$

At the end we have 7 equations and 8 unknowns, if the equations are consistent, then the solution is not unique. The linear system is,
$$\begin{bmatrix}
1 & t_{0} & t_{0}^2 & t_{0}^3 & 0 & 0 & 0 & 0 \\
1 & t_{1} & t_{1}^2 & t_{1}^3 & 0 & 0 & 0 & 0 \\ 
1 & t_{2} & t_{2}^2 & t_{2}^3 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 &  1 & t_{2} & t_{2}^2 & t_{2}^3 \\
0 & 0 & 0 & 0 & 1 & t_{3} & t_{3}^2 & t_{3}^3  \\
0 & 0 & 0 & 0 & 1 & t_{4} & t_{4}^2 & t_{4}^3 \\
0 & 1 & 2t_{2} & 3t_{2}^2 & 0 & -1 & -2t_{2} & -3t_{2}^2
\end{bmatrix}\begin{bmatrix}
a_{1} \\
b_{1} \\
c_{1} \\
d_{1} \\
a_{2} \\
b_{2} \\
c_{2} \\
d_{2}
\end{bmatrix}=\begin{bmatrix}
y_{0} \\
y_{1} \\
y_{2} \\
y_{3} \\
y_{4} \\
0
\end{bmatrix}$$

For a unique solution, we need to add $p’’$ to be continuous as well.

## Subspaces
#### Definition of a subspace
A subset $U\subseteq \mathbb{R}^n$ is a subspace if,
1. $U$ contains the all-zero vector $\mathbf{0}\in \mathbb{R}^n$.
2. $U$ is closed under addition. That is,  if $\mathbf{u_{1}}\in U$ and $\mathbf{u_{2}}\in U$ then $\mathbf{u_{1}}+\mathbf{u_{2}}\in U$.
3. $U$ is closed under scalar multiplication. If $\mathbf{u}\in U$ and $c \in \mathbb{R}$, then $c \mathbf{u}\in U$.

### Examples of subspaces
Subspaces on $\mathbb{R}^2$: origin, the whole space and any line through the origin.

$$U=\{\begin{bmatrix}x_{1}
 \\
x_2 \end{bmatrix}\in \mathbb{R}^2:x_{1}+x_{2}=1 \}$$
is not a subspace. It does not contain the zero vector and not closed under addition. 

ex. Take,
$$\mathbf{u_{1}}=\begin{bmatrix}
1 \\
0 
\end{bmatrix},\mathbf{u_{2}}=\begin{bmatrix}
0  \\
1
\end{bmatrix}$$

Then,
$$\mathbf{u_1}+\mathbf{u_{2}}=\begin{bmatrix}
1 \\
1
\end{bmatrix}\not\in U$$

#### Definition of a linear combination
A *linear combination* of vectors $\mathbf{u_{1}},\cdots,\mathbf{u_{m}}\in \mathbb{R}^n$ is,
$$c_{1}\mathbf{u_{1}}+c_{2}\mathbf{u_{2}}+\cdots+c_{m}\mathbf{u_{m}}$$
where $c_{1},c_{2},\cdots,c_{m}\in \mathbb{R}$.

#### Definition of a span
The span of $\mathbf{u_{1}},\cdots,\mathbf{u_{m}}\in \mathbb{R}^n$ is, the set of all linear combinations,
$$\text{span}\{\mathbf{u_{1}},\cdots,\mathbf{u_{m}}\}=\{c_{1}\mathbf{u_{1}}+\cdots+c_{m}\mathbf{u_{m}}:c_{1},\cdots,c_{m}\in \mathbb{R}\}$$


#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 8|Lecture 8]]


