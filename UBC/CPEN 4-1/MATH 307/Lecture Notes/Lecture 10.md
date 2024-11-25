#### Definition of range
Let $A \in \mathbb{R}^{m \times n}$. The range of $A$ is defined as 
$$R(A) = \{ \mathbf{y}\in \mathbb{R}^m  s.t. \hspace{.1in} A\mathbf{x} =\mathbf{y} : \mathbf{x}\in \mathbb{R}^n\} = \{ A\mathbf{x}:\mathbf{x} \in \mathbb{R}^n\}$$

##### R(A) is a subspace
We verify the requirements for a subspace.
1. The set $R(A)$ contains $\mathbf{0}$ since $A\mathbf{0}=\mathbf{0}$.
2. Let $\mathbf{y}_{1}=A\mathbf{x}_{1}$ and $\mathbf{y}_{2}=A\mathbf{x}_{2}$ be arbitrary. Then, we have $\mathbf{y}_{1}+\mathbf{y}_{2}= A(\mathbf{x}_{1}+\mathbf{x}_{2}) \in R(A)$.
3. The set $R(A)$ is closed under scalar multiplication because if $\mathbf{y}_{1}=A\mathbf{x}_{1}$, then $c \mathbf{y}_{1}=cA\mathbf{x}_{1}=A(c \mathbf{x}_{1}) \in R(A)$.

###### Remark
1. The range of $A$ is also called the image of $A$, sometimes denoted as $\text{im}(A)$. This is because we can view the matrix-vector multiplication as a function.
2. If $\mathbf{u}_{1},\cdots,\mathbf{u}_{n} \in \mathbb{R}^m$ are columns of $A$, then $A\mathbf{x}$ is the subspace of all linear combinations of columns of $A$. This is the span of the columns, that is, the *column space* of the matrix.$$R(A) = \text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}=\text{col}(A)$$ To see this,$$A\mathbf{x}=\begin{bmatrix}
\vert &  & \vert \\
\mathbf{u}_{1}  & \cdots & \mathbf{u}_{2} \\
\vert &  & \vert
\end{bmatrix}\begin{bmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{bmatrix}=x_1\mathbf{u}_{1}+\cdots+x_{n}\mathbf{u}_{n}$$

###### Example
Find the basis and dimension of the range of
$$A=\begin{bmatrix}
1 & 3 & 1 & -1  \\
-2  & -4 & 0 & -2 \\
1 & 4 & 2 & -3
\end{bmatrix}$$
Recall that $R(A) = \text{span}\{ \mathbf{u}_{1},\mathbf{u}_{2},\mathbf{u}_{3},\mathbf{u}_{4} \}$. But this does not mean that they are linearly independent. Let’s reduce $A$,
$$\begin{bmatrix}
1 & 3 & 1 & -1 \\
0 & 2 & 2 & -4 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

This shows that the two columns are linearly independent, so they form the basis of the column space. That is,
$$R(A) = \text{span}\{ \begin{bmatrix}
1 \\
-2 \\
1
\end{bmatrix},\begin{bmatrix}
3 \\
-4\\
4
\end{bmatrix} \}$$
Since we have two vectors, $\text{dim}(R(A)) = 2$.

#### Proposition
Let $U \in \mathbb{R}^{m \times n }$ be the row echelon form of $A \in \mathbb{R}^{m \times n}$, where we use the following notation for their columns,
$$U=\begin{bmatrix}
\vert &  & \vert \\
\mathbf{u}_{1} & \cdots & \mathbf{u}_{n} \\
\vert &  & \vert
\end{bmatrix}, \text{ and } A=\begin{bmatrix}
\vert &  & \vert \\
\mathbf{a}_{1} & \cdots & \mathbf{a}_{n} \\
\vert &  & \vert
\end{bmatrix}$$

Let $I \subseteq \{ 1,2,\cdots,n \}$ be the index set containing the indices of columns of $U$ that have a pivot and let $I(i)$ denote the $i$-th element of set $I$.

Then, the vectors $\mathbf{a}_{I(1)},\mathbf{a}_{I(2)},\cdots,\mathbf{a}_{I(r)}$ form a basis of $R(A)$.

[Proof]
Since the set $\{ \mathbf{u}_{I(1)},\cdots,\mathbf{u}_{I(r)} \}$ contains the pivot columns in $U$, it is a basis of $R(U)$.
Then we can write any other column of $U$ as the linear combination of these vectors. 
That is, for any $k \in \{ 1,2,\cdots,n \}$ such that $k \not\in I$ we have,
$$\mathbf{u}_{k}=l_{1}\mathbf{u}_{I(1)}+\cdots+l_{r}\mathbf{u}_{I(r)}$$
This means that the following vector is the solution to the linear system $U\mathbf{c}=0$:
$$c_{I(1)}=l_{1}$$
$$c_{I(2)}=2$$
$$\vdots$$
$$c_{I(r))}=l_{r}$$
$$c_{k}= - 1$$
$$c_{i} = 0 \text{ if }i \neq k \text{ and } i \not\in I$$

Since $A\mathbf{c}=0$ will have the same solution set, this means that for any $k \not\in I$, we have
$$\mathbf{a}_{k} = l_{1}\mathbf{a}_{I(1)}+\cdots+l_{r}\mathbf{a}_{I(r)}$$

where $\mathbf{a}_i$ is the $i$-th column of A. We showed that any column of $A$ is in $\text{span}\{ \mathbf{a}_{I(1)},\cdots,\mathbf{a}_{I(r)} \}$. To conclude that the vectors $\mathbf{a}_{I(1)},\cdots,\mathbf{a}_{I(r)}$ form a basis for $R(A)$, we have to verify that they are linearly independent.

Because that the vectors $\mathbf{u}_{I(1)},\cdots,\mathbf{u}_{I(r)}$ are linearly independent, we have that 
$$\mathbf{0}=l_{1} \mathbf{u}_{I(1)}+\cdots+l_{r}\mathbf{u}_{I(r)} \iff l_{1}=\cdots=l_{r}=0$$
In view of this, we consider the solutions of $U\mathbf{c}=0$. For any solution $\mathbf{c}$ to this system such that $$c_{i} = 0 \text{ if } i \not\in I$$
We need to have that $c_{i}=0$ for $i\in I$.

Since the solution sets to $U\mathbf{c}=0$ and $A\mathbf{c}=0$ are equivalent, this means that
$$\mathbf{0} = l_{1}\mathbf{a}_{I(1)}+\cdots+l_{r}\mathbf{a}_{I(r)} \iff l_{1} = \cdots = l_{r} = 0$$
That is, the vectors are linearly independent.

#### Theorem
Let us have a matrix $A$ such that $A \in \mathbb{R}^{m \times n}$. Then, we have that $\text{rank}(A)=\text{dim}(R(A))$.

[Proof]
$$\text{rank}(A) = \text{number of nonzero rows in ref form}$$
$$ = \text{ number of columns with pivot}$$
$$= \text{ number of linearly independent columns in ref}$$
$$=\text{dim}(R(A))$$


#### Theorem
Let $A \in \mathbb{R}^{m \times n}$ admit the LU decomposition $A=LU$ and let $\text{rank}(A) = r$. Then the first $r$ columns of $L$ forms a basis of $R(A)$.

[Proof]
First, let $L \in \mathbb{R}^{m\times n}$ and $U \in \mathbb{R}^{m \times n}$. That is,
$$A=LU=\begin{bmatrix}
\vert &  & \vert \\
\mathbf{l}_{1}  & \cdots & \mathbf{l}_{m} \\
\vert &  & \vert
\end{bmatrix}\begin{bmatrix}
*   & a & \cdots & b \\
0 & * & \cdots & c \\
\vdots &  &  & \vdots \\
0 & 0 & \cdots & * \\
0 & 0 & \cdots & 0 \\
\vdots &  &  &  \\
0 & 0 & \cdots & 0
\end{bmatrix}$$

where the rows after the $r$-th row contain only zeros in $U$, because rank is $r$. Here the * denotes a non-zero value and the constants can be any value. As a result, for any $\mathbf{x} \in \mathbb{R}^n$, we have that
$$U\mathbf{x}=\begin{bmatrix}
* \\
* \\
\vdots \\
* \\
0 \\
\vdots \\
0
\end{bmatrix}$$
that is, only the first $r$ elements of $U\mathbf{x}$ can be non-zero. As a result,
$$A \mathbf{x} = \begin{bmatrix}
\vert &  & \vert \\
\mathbf{l}_{1}  & \cdots & \mathbf{l}_{m} \\
\vert &  & \vert
\end{bmatrix}U\mathbf{x}=* \mathbf{l}_{1}+\cdots+*\mathbf{l}_{r}$$
This means that $R(A) = \text{span}\{  \mathbf{l}_{1},\cdots,\mathbf{l}_{r} \}$. Linear independence of the vectors $\mathbf{l}_{1},\cdots,\mathbf{l}_{r}$ follows from $L$ being a unit lower triangular matrix.

#### Theorem (Rank nullity theorem)
Let $A \in \mathbb{R}^{m \times n }$, then
$$\text{dim}(N(A)) + \text{dim}(R(A)) = n$$
[Proof]
$\text{dim}(R(A))$ is the number of columns with a pivot in the row echelon form of $A$ and $\text{dim}(N(A))$ is the number columns without a pivot in the row echelon form of $A$. As a result, their sum is the number of columns, which is $n$.

###### Exercise
Let $A$ be such that $A=LU$ where
$$L=\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
2 & 1 & 1 & 0 \\
1 & 0 & -1 & 1
\end{bmatrix},U=\begin{bmatrix}
1 & -2 & 0 & 5 & 1 \\
0 & 0 & 2 & -1 & 0 \\
0 & 0 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}$$

1. Find the basis and determine the dimension of $R(A)$ and $N(A)$.

On the matrix $U$, we observe that the two columns do not have a pivot and 3 columns have pivots, so $\text{dim}(R(A)) = 3$ and $\text{dim}(N(A)) = 2$. Note that $\text{rank}(A)= 3$. 

We then know that the set,
$$\left\{ \begin{bmatrix}
1 \\
-1 \\
2 \\
1
\end{bmatrix}, \begin{bmatrix}
0 \\
1 \\
1 \\
0
\end{bmatrix}, \begin{bmatrix}
0 \\
0 \\
1 \\
-1
\end{bmatrix} \right\}$$
is a basis for $R(A)$.

To find the basis of $N(A)$, we have to solve $A\mathbf{x}=0$, or equivalently $U\mathbf{x}=0$. 
$$\left\{  \begin{bmatrix}
2 \\
1 \\
0 \\
0 \\
0
\end{bmatrix} , \begin{bmatrix}
5 \\
0 \\
\frac{1}{2} \\
-1 \\
0
\end{bmatrix}  \right\}$$

2. Determine if $R(A) = \text{span}\{ \mathbf{a}_{1},\mathbf{a}_{2}, \mathbf{a}_{3} \}$ where, $$A=\begin{bmatrix}
\vert & \vert & \vert & \vert & \vert \\
\mathbf{a}_{1} & \mathbf{a}_{2} & \mathbf{a}_{3} & \mathbf{a}_{4}
 & \mathbf{a}_{5} \\
\vert & \vert & \vert\ & \vert & \vert\end{bmatrix}$$ Notice that $\text{dim}(\text{span}\{ \mathbf{a}_{1},\mathbf{a}_{2},\mathbf{a} _{3}\}) = 2$. As a result, the set $\{ \mathbf{a}_{1},\mathbf{a}_{2},\mathbf{a}_{3} \}$ cannot be a basis of $R(A)$.

Since we know that $\text{dim}(R(A)) = 3$ any 3 linearly independent columns of $A$ would form a basis of $R(A)$. We can use the linearly independent columns of $U$ to find the linearly independent columns of $A$. ← Because elementary row operations don’t change linear dependence / independence relations.

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 11|Lecture 11]]



