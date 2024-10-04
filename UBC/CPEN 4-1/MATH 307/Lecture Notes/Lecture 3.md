# Continuing LU decomposition..

Let’s start with an example,
$$A = \begin{bmatrix}
 3  & -1 & 1 \\
1  & 3 & 2 \\
-1 & 3 & 4
\end{bmatrix}$$

We use the elimination as the same way we’ve been doing so far,
$$A = \begin{bmatrix}
 3  & -1 & 1 \\
1  & 3 & 2 \\
-1 & 3 & 4
\end{bmatrix} \to_{E^{(1)}}^{R_{2}\leftarrow R_{2}-\frac{R_{1}}{3}} \begin{bmatrix}
3 & -1 & 1  \\
 0 & \frac{10}{3} & \frac{5}{3} \\
-1 & 3 & 4
\end{bmatrix} \to_{E^{(2)}}^{R_{3}\leftarrow R_{3}+\frac{R_{1}}{3}} \begin{bmatrix}
3 & -1 & 1  \\
0  & \frac{10}{3} & \frac{5}{3}  \\
0 & \frac{8}{3} & \frac{13}{3}
\end{bmatrix} $$

$$\to_{E^{(3)}}^{R_{3}\leftarrow R_{3}-8\frac{R_{2}}{10}} \begin{bmatrix}
3 & -1 & 1 \\
0 & \frac{10}{3} & \frac{5}{3}  \\
0 & 0 & 3
		\end{bmatrix}$$

Since the last matrix is in ref form, we have
$$U = E^{(3)}E^{(2)}E^{(1)}A$$

The row operations correspond to the following elementary matrices, to obtain $L$:
$$A \coloneqq (E^{(1)})^{-1}(E^{(2)})^{-1}(E^{(3)})^{-1}U \eqqcolon LU$$


#### Facts
Let $E \in R^{m \times m}$ be the matrix that differs from the identity matrix only in the element in row $i$ and column $j$ for $i>j$:

$$E_{i,j} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & c_{i,j} &  &  \\
 &  &  &  & 1
\end{bmatrix}$$

Let $A\in R^{m\times m}$, then,

**1. The product $EA$ applies the elementary row operation “add $c_{i,j}$ times row $j$ to row $i$ to $A$”.**
**2. The inverse of E is given as**
$$E_{i,j} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & -c_{i,j} &  &  \\
 &  &  &  & 1
\end{bmatrix}$$
**3. Take the nonzero scalars $c_{i,j}, c_{k,l}$ with $i>j,k>l$ and $(i,j)\neq(k,l), k\geq i,l\geq j$ and matrices,**
$$E^{(1)} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & c_{i,j} &  &  \\
 &  &  &  & 1
\end{bmatrix},
E^{(2)} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & c_{k,l} &  &  \\
 &  &  &  & 1
\end{bmatrix}$$

**Then, we have that their product is in the following form**
$$E^{(1)}E^{(2)} =\begin{bmatrix}
1 &  &  &  &  \\
 & 1 &  &  &  \\
 &  & \cdots &  &  \\
 & c_{i,j} &  &  \\
 &  & c_{k,l} &  & 1
\end{bmatrix}$$

**That is, $E^{(1)}E^{(2)}$ is a unit lower triangular matrix where the elements below the diagonal in $E^{(1)}$ and $E^{(2)}$ sits at their respective locations in matrix $E^{(1)}E^{(2)}$.**


**4.  If a matrix $A\in \mathbb{R}^{m\times m}$ can be reduced to its row echelon form only with elementary row operations of the form “add $c_{i,j}$ times row $j$ to row $i$”, the LU decomposition of $A$ exists.** 
**The factor $U$ in the decomposition is the row echelon form of $A$ and the factor $L$ is given in the form**

$$L= \begin{bmatrix}
1 & 0 & 0  & \cdots & 0 \\
-c_{2,1} & 1 & 0 & \cdots  & 0 \\
-c_{3,1} & -c_{3,2} & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots  \\
-c_{m,1} & -c_{m,2} & \cdots-c_{m,m-1} & 1 
\end{bmatrix}$$

##### Remark
There are some cases where LU decomposition might not exist for a given matrix, to see a simple counter example,
$$A = \begin{bmatrix}
0 & 1   \\
1 & 0 
\end{bmatrix}$$
where we have to exchange rows to  put this matrix to its row echelon form.

To handle this issue, we use *pivoting* which allows exchanging rows. The idea is that given a permutation matrix $P$, we find the LU decomposition of $PA$, that is
$$PA = LU$$

## Applications of LU decomposition

#### rank($A$) = rank($U$)
The proof comes from the fact that $U$ is the Gauss elimination of $A$ 

#### For a square matrix, say A, we have det($A$) = det($U$)
Recall that,
$$\det(A) = \det(L)\det(U)$$


##### Determinant of a matrix product
$$\det(AB) = \det(A)\det(B)$$

For diagonal matrices, the determinant is the product of diagonal entries, also since the diagonal entries of $L$ are all 1, $\det(L) =1$.

$$\det(A)= \det(L)\det(U) = \det(U) = u_{1,1}u_{2,2}\cdots u_{n,n}$$

#### Solving systems
LU decomposition lets us solve multiple linear systems where we have the same $A$ but different  $\mathbf{b}$ without having to do a Gaussian elimination for every $\mathbf{b}$. 
In particular, for a series of systems
$$A\mathbf{x}^{(1)}=\mathbf{b}^{(1)}$$
$$A\mathbf{x}^{(2)}=\mathbf{b}^{(2)}$$
$$A\mathbf{x}^{(3)}=\mathbf{b}^{(3)}$$
$$\vdots$$

we ideally want to do Gaussian decomposition once, and solve for each linear system in an easier way when a new $\mathbf{b}^{(i)}$ is given to us.

Given $L$ and $U$, such that $A=LU$, the idea is to define a new unknown $\mathbb{y}$ such that $U\mathbf{x}=\mathbf{y}$ and write 
$$A\mathbf{x}=\mathbf{b}$$
$$\implies LU\mathbf{x}=\mathbf{b}$$
$$\implies L\mathbf{y}=\mathbf{b},\hspace{.1in}\mathbf{y}=U\mathbf{x}$$

We know $L$ and $\mathbf{b}$ and also that $L$ is lower triangular. We can solve for $\mathbf{y}$ in $L\mathbf{y}=\mathbf{b}$ first, and then we can use the value of $\mathbf{y}$ to write down the system
$$U\mathbf{x}=\mathbf{y}$$


### Example
Suppose that we have,
$$A=\begin{bmatrix}
2 & 3 & -1 & 1 \\
4  & 5 & -1 & 4 \\
-2 & -6 & 1  & 6 \\
2 & -1 & 9 & 9
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0  \\
-1 & 3 & 1 & 0 \\
1 & 4 & -2 & 1
\end{bmatrix}\begin{bmatrix}
2 & 3 & -1 & 1 \\
0 & -1 & 1 & 2 \\
0 & 0 & -3 & 1 \\
0 & 0 & 0 & 2
\end{bmatrix}=LU$$

Say for,
$$A\mathbf{x}=\mathbf{b},\mathbf{b}=\begin{bmatrix}
0 \\
-3 \\
-1 \\
-30
\end{bmatrix}$$

The idea is to define $\mathbf{y}=U\mathbf{x}$ and write our system equivalently as $A\mathbf{x}=\mathbf{b}\leftrightarrow LU\mathbf{x}=\mathbf{b}\leftrightarrow L\mathbf{y}=\mathbf{b}$. Then we will solve for $\mathbf{y}$ in the system and use to solve the original system in terms of $U\mathbf{x}=\mathbf{y}$
.
In the first step,
$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
-1 & 3 & 1 & 0 \\
1 & 4 & -2 & 1
\end{bmatrix}\begin{bmatrix}
y_{1} \\
y_{2} \\
y_{3} \\
y_{4}
\end{bmatrix}=\begin{bmatrix}
0 \\
-3 \\
-1 \\
-30
\end{bmatrix}$$

Which leads us to,
$$y_{1}=0,y_{2}=-3,y_{3}=8,y_{4}=-2 \implies \mathbf{y}=\begin{bmatrix}
0 \\
-3 \\
8 \\
-2
\end{bmatrix}$$
We can then write $U\mathbf{x}=\mathbf{y}$ as,
$$\begin{bmatrix}
 2  & 3 & -1 & 1 \\
0 & -1 & 1 & 2 \\
0 & 0 & -3 & 1 \\
0 & 0 & 0 & 2
\end{bmatrix}\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{bmatrix}=\begin{bmatrix}
0 \\
-3 \\
8 \\
-2
\end{bmatrix}$$

Which gives us the eventual solution as,
$$\mathbf{x}=\begin{bmatrix}
2\\-2\\-3\\-1
\end{bmatrix}$$

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 4|Lecture 4]]
