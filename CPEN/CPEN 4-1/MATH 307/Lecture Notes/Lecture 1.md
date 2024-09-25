## Linear System of Equations
A *linear system of equations* is defined by known coefficients $a_{i,j} \in \mathbb{R}$ and $b_i \in \mathbb{R}$ for $i,j \ge 1$ and unknown variables $x_i \in \mathbb{R}$ in the following way:
$$a_{1,1}x_1 + a_{1,2}x_2 + \dots a_{1,n}x_n = b_1$$
$$a_{2,1}x_1 + a_{2,2}x_2 + \dots a_{2,n}x_n = b_2$$
$$\vdots$$
$$a_{m,1}x_1 + a_{m,2}x_2 + \dots a_{m,n}x_n = b_m$$

We have above $m$ equations and $n$ unknowns. 

Given the above, we can re-write this into a compact form by using matrix-vector multiplication.


#### Convention
Given a matrix $A\in \mathbb{R}^{m \times n}$, we denote the $i$-th row and $j$-th column as $a_{i,j}$.

$$A = \begin{bmatrix} a_{1,1} & a_{1,2} & \dots & a_{1,n}
\\
a_{2,1} & a_{2,2} & \dots & a_{2,n}
\\
a_{m,1} & a_{m,2} & \dots & a_{m,n}
\end{bmatrix}$$

Similarly, given a vector $\mathbf{b} \in \mathbb{R}^b$, we denote the element at the $i$-th row as $b_i$.
$$\mathbf{b}=  \begin{bmatrix}b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}$$

Then, the compact form is exactly
$$A\mathbf{x} = \mathbf{b}$$

#### Definition of an augmented matrix
The *augmented matrix* corresponding to the linear system given above is,
$$\begin{bmatrix} A \hspace{.1in}\vert \hspace{.1in}b \end{bmatrix}$$

#### Definition of Row-echelon form
A matrix is in ***row echelon form (ref)*** if
1. All zero rows are at the bottom.
2. At each row, the first non-zero element (from the left) is to the right of the first non-zero elements in the rows above.

For instance, 

$$\begin{bmatrix}* & * & * & * \\ 0 & * & * & * \\ 0 & 0 & 0 & *\end{bmatrix}$$
is in ref form. And ,

$$\begin{bmatrix}1 & 2 & 4 & 4 \\ 0 & 2 & 7 & 3 \\ 0 & 0 & 0 & *4\end{bmatrix}$$
is in ref form. Whereas,
$$\begin{bmatrix}1 & 2 & 4 & 4 \\ 0 & 2 & 7 & 3 \\ 3 & 0 & 0 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
is not in ref form, since the 3rd row has a non-zero term left to the first non-zero term of the row above.


#### Definition of elementary row operations
An ***elementary row operation*** performs one of the three actions on a matrix,
1. Exchange two rows.
2. Multiply a row by a non-zero scalar.
3. Multiply a row by a non-zero scalar and then add it to another row.

==Be careful that this does not include multiplying a row by 0.==

#### Definition of Gauss Elimination
***Gauss Elimination*** is the process of converting the augmented matrix corresponding to a linear system to the row echelon form.

Let’s first see an example,
$$\begin{bmatrix} A \hspace{.1in}\vert \hspace{.1in}b \end{bmatrix} = \begin{bmatrix}
1 & 2 &  4 & \vert  & 2 \\
3 & 5 & 6 & \vert &  7  \\
-1 & 4 & 8 & \vert & 10
\end{bmatrix}
\to^{R_{2} \leftarrow (-3R_{1}) + R_{2}}_{R_{3} \leftarrow R_{1} + R_{3}}= \begin{bmatrix}
1 & 2 & 4 & \vert & 2  \\
0 & -1 & -6 & \vert & 1 \\
0 & 6 & 12 & \vert & 12
\end{bmatrix}
$$
$$\to^{R_{3} \leftarrow 6R_{2} + R_{3}} \begin{bmatrix}
1 & 2 &  4 & \vert & 2  \\
 0 & -1 & -6 & \vert & 1 \\
0 & 0 & -24 & \vert & 18
\end{bmatrix}$$

Which is the form of row echelon form, and this corresponds to the following linear system:
$$\begin{bmatrix}
1 & 2 & 4 \\
0 & -1 & -6 \\
0 & 0 & -24
\end{bmatrix}
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix}
= \begin{bmatrix}
2 \\
1 \\
18
\end{bmatrix}$$

Hence, more explicitly,
$$x_{1}+2x_{2}+4x_{3}=2 $$
$$-x_{2}-6x_{3}=1$$
$$-24x_{3}=18$$
And thus we can solve for the vector,
$$\mathbf{x}=\begin{bmatrix}
-2 \\
\frac{7}{2} \\
\frac{-3}{4}
\end{bmatrix}$$

### Equivalence of solution sets before / after elimination
Given a linear system, we use Gaussian elimination to obtain a simplified version. Then we solve the simple system and hence derive a solution for the original system (which is visible by plugging in the solution to the original system). 

**We need to understand why the elementary row operations do not change the solution set of the initial linear system.**

Maybe one way of seeing this is to notice that : **we are applying reversible elementary row operations on the system and hence can always go back to the original system.**

#### Proof  (another way)
Let,
$$\begin{bmatrix}
A' & \vert & \mathbf{b}'
\end{bmatrix}$$
denote the augmented matrix formed as a result of applying an elementary row operation to
$$\begin{bmatrix}
A  & \vert  & \mathbf{b}
\end{bmatrix}$$

The strategy is to verify such that, for $\mathbf{x}$ that satisfies $A\mathbf{x} = \mathbf{b}$, we want that such $\mathbf{x}$ to satisfy $A’\mathbf{x} = b’$ and vice versa. 

First, we want to show that an arbitrary vector $\bar{x}$  that satisfies $A\bar{\mathbf{x}} = \mathbf{b}$ also satisfies $A'\bar{\mathbf{x}} = \mathbf{b'}$ .
Second, we need to show that an arbitrary vector $\hat{x}$ that satisfies $A'\hat{x} =\mathbf{b}'$ also satisfies $A\hat{x}=\mathbf{b}$ 

**Operation 1: Exchanging rows**
- Exchanging rows mean that the order of equations is changed. Clearly a vector $\bar{x}$ satisfying one system satisfies another.
	This is since, the coefficients $x_{1},x_{2},x_{3},\dots,x_{n}$ are maintained in the same order.

**Operation 2: Multiplying a row with a scalar**
- Multiplying a row by a scalar only multiplies the coefficients by a scalar, for instance $a_{1} \to c\times a_{n}$.
- Again, if a vector $\hat{x}$ satisfies one system, it satisfies the other too.

**Operation 3: Adding a non-zero scalar multiplication of a row to another row**
Let’s see an example, following the above [[#Linear System of Equations]]

$$a_{1,1}x_{1}+a_{1,2}x_{2}+\dots_+a_{1,n}x_{n} = b_{1}$$
$$(2a_{1,1}+a_{2,1})x_{1}+\dots+(2a_{1,n}+a_{2,n})x_{n} = 2b_{1}+b_{2}$$
$$\vdots$$
$$a_{m,1}x_{1}+a_{m,2}x_{2}+\dots_+a_{m,n}x_{n} = b_{m}$$

It is straightforward to see that if $\bar{x}$ satisfies then it also satisfies the system above.
To see in the other direction, we can apply the row operations in reverse and prove in the same method.
#### Next Lecture [[CPEN/CPEN 4-1/MATH 307/Lecture Notes/Lecture 2|Lecture 2]]

