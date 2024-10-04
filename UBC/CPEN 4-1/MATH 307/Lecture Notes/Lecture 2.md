
#### Definition of a pivot
A **pivot** is the first non-zero element (from the left)  at every non-zero row.

ex.
$$\begin{bmatrix}
 1 & 3 & 4 \\
0 & 9 & 8 \\
0 & 0 & 0 
\end{bmatrix}$$
There are two pivots, in the first and second rows, namely 1 and 9.

#### Definition of a rank of a matrix
The **Rank** of a matrix is defined as the number of pivots, or equivalently the number of non-zero rows, in its **ref form**.

The above example had a rank of 2: since it had two pivots.

## Proposition
Given a linear system,
$$A\mathbf{x}= \mathbf{b}, \hspace{.3in} A \in \mathbb{R}^{m \times n}, \mathbf{x}\in \mathbb{R}^n ,b\in \mathbb{R}^m

$$
we have the following properties.

1. If rank($A$) < rank($\begin{bmatrix}A\vert b\end{bmatrix}$), then the system is inconsistent and there are no solutions to the system.
	- In particular, when this occurs, by the definition of rank, we know that there is at least one row in the augmented matrix where we have,
		$$0 \hspace{.1in} 0 \cdots 0 \vert 1$$
		no $\mathbf{x}$ can satisfy this system. Since, $\mathbf{0}^\intercal \mathbf{x} = 1$ is not solvable.

2. If rank($A$) = rank($\begin{bmatrix}A\vert b\end{bmatrix}$), and if rank($A$) = $n$, then there is a unique solution.
3. If rank($A$) = rank($\begin{bmatrix}A\vert b\end{bmatrix}$), and if rank($A$) < $n$, then there are infinitely many solutions.

==These are all in “if and only if” statements.==

ex.
Consider the system with,
$$A= \begin{bmatrix}
1 & 2 & -2 \\
-1 & 2 & 7 \\
1 & 6 & 3
\end{bmatrix}, \hspace{.1in} \mathbf{b}=\begin{bmatrix} 8 \\
2 \\
18
\end{bmatrix}$$


And given the augmented matrix,
$$\begin{bmatrix}
A  & \vert & \mathbf{b}
\end{bmatrix} = \begin{bmatrix}
1 & 2 & -2 & \vert & 8 \\
-1 & 2 & 7 & \vert & 2 \\
1 & 6 & 33 & \vert & 18
\end{bmatrix}$$

We can apply Gaussian elimination to get,
$$\begin{bmatrix}
1 & 2 & -2 & \vert & 8 \\
0 & 4 & 5 & \vert & 10 \\
0 & 0 & 0 & \vert & 0
\end{bmatrix}$$


As a result, our simpler system is,
$$\begin{bmatrix}
1 & 2 & -2  \\
0 & 4 & 5 \\
0 & 0 & 0 
\end{bmatrix} \begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix} = \begin{bmatrix}
8  \\
10 \\
0
\end{bmatrix}$$

We have now two equations and three unknowns, also notice that 
$$\text{rank}(A) = \text{rank}(A\vert \mathbf{b}) = 2 < 3 = n.$$
Hence, there are an infinite amount of solutions.


ex.
Let’s see how $\alpha$ can affect the solution characteristics of the following linear system.
$$x_{1} +x_{2}-x_{3} = 0$$
$$\alpha x_{2}-x_{3}= 2$$
$$x_{1}+x_{2}+\alpha x_{3} =0 $$

Let’s apply gaussian elimination to the augmented matrix,
$$\begin{bmatrix}
1 & 2 & -1 & \vert & 0 \\
0 & \alpha & -1 & \vert  & 2 \\
1 & 1 & \alpha & \vert & 0
\end{bmatrix} \to \begin{bmatrix}1 & 1 & -1 & \vert & 0 \\
0 & \alpha & -1 & \vert & 2 \\
0 & 0 & \alpha+1 & \vert & 0\end{bmatrix}$$

There are a total of three cases,

1. $\alpha \neq 0$ and $\alpha \neq -1$:
	Then we have that the matrix in ref has rank of 3 along with the augmented matrix. Also, $n=3$ → Hence, a unique solution.
2. $\alpha = 0$:
	rank($A$) = 2 < rank($\begin{bmatrix}A\vert \mathbf{b}\end{bmatrix}$) < $n$ = 3 → Hence, no solution.
3. $\alpha = -1$:
	rank($A$) = 2 = rank($\begin{bmatrix}A \vert \mathbf{b}\end{bmatrix}$) < $n$ = 3 → so there are infinitely many solutions.


## LU decomposition
We’ve learned Gaussian elimination for one linear system so far. What if we need to solve many linear systems with the same $A$ and different $\mathbf{b}$?

#### Definition of LU decomposition
The factorization(**When it exist**) of a given matrix in terms of  a lower triangular ($L$) and upper triangular($U$) matrix is called the **LU decomposition.**

That is,
$$A = LU, \hspace{.1in}L \in \mathbb{R}^{m \times n} , U \in \mathbb{R}^{m\times n},A\in \mathbb{R}^{m \times n}.$$

##### A bit more about upper/lower triangular matrices.
Given diagonal entries of $a_{i,i}$, when there are fully zeroes below or above the diagonal determines a upper/lower triangular matrix.

**Unit** lower (or upper) triangular matrices satisfy the above and they are additionally square and they have 1 as their diagonal entries.


## Definition of elementary matrices
An elementary matrix is a matrix that can be obtained by an **elementary row operation** on the **identity matrix**.

In particular, we will focus on *“add a scalar multiple of one row to another row”*.

ex.
$$E_{2,1} = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0  \\
2 & 0 & 1
\end{bmatrix}, \hspace{.1in} E_{3,2} = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 5 & 1
\end{bmatrix}, \hspace{.1in} E_{1,2} = \begin{bmatrix}
1 & 0 & 0 \\
4 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$$



- Elementary matrix for *”exchange two rows”*
$$E' = \begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}$$

- Elementary matrix for *”multiply row by a scalar”*
$$E'' = \begin{bmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}$$

### Multiply row j with c and add to row i elementary matrix
In particular, the matrix $E_{i,j} \in \mathbb{R}^{m \times m}$, describing such an operation is

$$E_{i,j} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & c_{i,j} &  &  \\
 &  &  &  & 1
\end{bmatrix}$$

where $c_{i,j}$ is at the intersection of row $i$ and column $j$ of $E_{i,j}$ and all the other entries are 0 (except the other diagonals being 1).

#### Proof (?)
If we let $\mathbf{a}$ such that,
$$\mathbf{a} = \begin{bmatrix}
a_{1,1}  & \cdots & a_{1,m}\\
a_{2,1}  & \cdots & a_{2,m} \\
\vdots \\
a_{m-1,1}  & \cdots & a_{m-1,m} \\
a_{m,1}  & \cdots & a_{m,m} \\
\end{bmatrix}$$

Then, 
$$E\mathbf{a} =\begin{bmatrix}
a_{1,1}  & \cdots & a_{1,m}\\
a_{2,1}  & \cdots & a_{2,m} \\
\vdots  &  & \vdots \\ c_{i,j}a_{j,1} +a_{i,1} &   \cdots  & c_{i,j}a_{j,m}+a_{i,m}\\
\vdots  &  & \vdots\\

a_{m-1,1}  & \cdots & a_{m-1,m} \\
a_{m,1}  & \cdots & a_{m,m} \\
\end{bmatrix} $$
as required.



## Proposition
Given $E^{-1}_{i,j}$, defined above, we can compute it as,
$$E^{-1}_{i,j}= \begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots  & &  \\
 & -c_{i,j}  &  &  &  \\
 &  &  &  & 1
\end{bmatrix}$$

with the same convention for $-c_{i,j}$.

Recall that,
$$E^{-1}_{i,j}E_{i,j}A = A$$ since $E^{-1}_{i,j}$ is the inverse of $E_{i,j}$. 

And this is true because,
- $E^{-1}_{i,j}$ is the inverse operation hence, multiply row $j$ by $-c_{i,j}$ and add to row $i$.
- If combine these two operations, then it would be multiply row $j$ and subtract then multiply row $j$ and add, hence recovering to the original matrix.

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 3|Lecture 3]]
