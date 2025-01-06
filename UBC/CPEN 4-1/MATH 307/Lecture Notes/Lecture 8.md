###### Exercise
Determine if $\mathbf{v} \in \text{span}\{\mathbf{u}_{1},\cdots,\mathbf{u}_{m}\}$ where
$$ \mathbf{v} =\begin{bmatrix}
3 \\
4 \\
0 \\
1 
\end{bmatrix},\mathbf{u}_{1}=\begin{bmatrix}
1 \\
1 \\
0 \\
1
\end{bmatrix}, \mathbf{u}_{2} = \begin{bmatrix}
-1 \\
0 \\
-1 \\
1
\end{bmatrix},\mathbf{u}_{3}=\begin{bmatrix}
0 \\
2 \\
-1 \\
0
\end{bmatrix}$$
We want to find if a solution exists to the linear solution,
$$\begin{bmatrix}
1 & -1 & 0 \\
1 & 0 & 2 \\
0 & -1 & -1   \\
1 & 1 & 0
\end{bmatrix}\begin{bmatrix}
c_{1} \\ c_{2} \\ c_{3}
\end{bmatrix} = \begin{bmatrix}
3 \\
4 \\
0 \\
1
\end{bmatrix}$$
Let’s do the reduction,
$$\begin{bmatrix}
1 & -1 & 0 & | & 3 \\
0 & 1 & 2 & | & 1 \\
0 & 0 & 1 & | & 1 \\
0 & 0 & 0 & |  & 0
\end{bmatrix}$$

We have the rank of the augmented solution equal to the number of unknowns, giving a unique solution. As a result, we know that $\mathbf{v} \in \text{span}\{\mathbf{u}_{1},\mathbf{u}_{2},\mathbf{u}_{3}\}$.

###### Exercise
With the same $\mathbf{u}_{1},\mathbf{u}_{2},\mathbf{u}_{3}$ determine if $\mathbf{w}=\begin{bmatrix}3 \\ 4 \\ 0 \\ 2 \end{bmatrix}$ is in the same span consisting of the three vectors.

If we do the reduction we end up with
$$\begin{bmatrix}
1 & -1 & 0 & \vert  & 3 \\
0 & 1 & 2 & \vert & 1 \\
0 & 0 & 1 & \vert & 1 \\
0 & 0 & 0 & \vert & 1
\end{bmatrix}$$
We end up with an inconsistent system, meaning that no linear combination of the 3 vectors can form $\mathbf{w}$. Hence, $\mathbf{w}$ is not in the span.

#### Definition of linear independence
Vectors $\mathbf{u}_{1},\mathbf{u}_{2},\cdots,\mathbf{u}_{m} \in \mathbb{R}^n$ are **linearly independent** if 
$$c_{1}\mathbf{u}_{1}+c_{2}\mathbf{u}_{2}+\cdots+c_{m}\mathbf{u}_{m}=0 \iff c_{1}=c_{2}=\cdots=c_{m}=0$$

We say vectors are linearly dependent if they are not linearly independent. In other words, vectors $\mathbf{u}_{1},\mathbf{u}_{2},\cdots,\mathbf{u}_{m}$ are linearly independent if no $\mathbf{u}_{k}$ is in the span of $\mathbf{u}_{1},\mathbf{u}_{2},\cdots,\mathbf{u}_{k-1},\mathbf{u}_{k+1},\cdots,\mathbf{u}_{m}$. Equivalently no $\mathbf{u}_{k}$ can be written as the linear combination of the other vectors. 

To see the equivalence, assume that vectors $\mathbf{u}_{1},\cdots,\mathbf{u}_m$ are linearly dependent, then we would have, for $c_{k}\neq {0}$, that
$$\mathbf{u}_{k} = \frac{c_{1}}{c_{k}}\mathbf{u}_{1}+\cdots+\frac{c_{k-1}}{c_{k}}\mathbf{u}_{k-1}+ \frac{c_{k+1}}{c_{k}}\mathbf{u}_{k+1}+\cdots+ \frac{c_{m}}{c_{k}}\mathbf{u}_{m}$$

Given a set of vectors, how can we find out linear independence? 
$$c_{1}\mathbf{u}_{1}+c_{2}\mathbf{u}_{2}+\cdots+c_{m}\mathbf{u}_{m}=\mathbf{0} \iff \begin{bmatrix}
\vert  & \vert & \cdots & \vert \\
\mathbf{u}_{1}  & \mathbf{u}_{2} & \cdots  & \mathbf{u}_{m} \\
\vert & \vert & \cdots  & \vert
\end{bmatrix}\begin{bmatrix}
c_{1} \\
c_{2} \\
\vdots \\
c_{m}
\end{bmatrix}=\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}$$

Then, the linear system only admits $\mathbf{0}$ as the solution. A.k.a there are no non-trivial solutions to the system.

###### Example
Determine if the following vectors are linearly independent,
$$\mathbf{u}_{1}=\begin{bmatrix}
1 \\
-1 \\
1
\end{bmatrix},\mathbf{u}_{2}=\begin{bmatrix}
2 \\
0 \\
3
\end{bmatrix},\mathbf{u}_{3}=\begin{bmatrix}
0 \\
2 \\
1
\end{bmatrix}$$
We set up an augmented matrix that would only accept the solution $\mathbf{0}$.
$$\begin{bmatrix}
1 & 2 & 0 & \vert & 0 \\
-1 & 0 & 2 & \vert & 0 \\
1 & 3 & 1 & \vert & 0
\end{bmatrix} \to \begin{bmatrix}
1 & 2 & 0 & \vert & 0 \\
0 & 2 & 2 & \vert & 0 \\
0 & 0 & 0 & \vert & 0
\end{bmatrix}$$

This system gives the equations,
$$c_{1}+2c_{2}=0,c_{2}+c_{3}=0$$
If we let $c_{3}$ be a free variable, as a result we have that,
$$\mathbf{c}=\begin{bmatrix}
2  \\
-1 \\
1
\end{bmatrix}t,t\in \mathbb{R}$$

Since we can find a non-zero $\mathbf{c}$ that satisfies the system, it is not linearly independent.

#### Definition of basis
Let $U \subseteq \mathbb{R}^n$ be a subspace. A set of vectors $\{ u_{1}, \cdots, u_{m} \} \subseteq U$ forms a basis of $U$ if,
1. $\text{span}\{ u_{1},\cdots,u_{m} \} = U$.
2. $u_{1},\cdots,u_{m}$ are linearly independent.

The dimension of $U$, denoted as $\text{dim}(U)$, is the number of vectors in a basis.

==There are infinitely many choices for a basis for a non-zero subspace but they all have the same number of vectors.==

###### Example
Find a basis and the dimension of,
$$U=\text{span}\{ \begin{bmatrix}
1 \\
1 \\
1 \\
1
\end{bmatrix},\begin{bmatrix}
2 \\
-3 \\
1 \\
0
\end{bmatrix}, \begin{bmatrix}
1 \\
-1 \\
1 \\
-1
\end{bmatrix}, \begin{bmatrix}
2 \\
-1 \\
1 \\
2
\end{bmatrix} \} \subseteq \mathbb{R}^4$$

First, let’s check if the vectors are linearly independent,
$$\begin{bmatrix}
1 & 2 & 1 & 2 & \vert & 0 \\
1 & -3 & -1 & -1 & \vert & 0 \\
1 & 1 & 1 & 1 & \vert & 0 \\
1 & 0 & -1 & 2 & \vert & 0
\end{bmatrix} \to \begin{bmatrix}
1 & 2 & 1 & 2 & \vert & 0 \\
0 & -5 & -2 & -3 & \vert & 0 \\
0 & 0 & \frac{2}{5} & -\frac{2}{5} & \vert & 0 \\
0 & 0 & 0 & 0 & \vert & 0
\end{bmatrix}$$

If we set $c_{4}=t$, then the solution is,
$$\mathbf{c}=\begin{bmatrix}
-1  \\
-1 \\
1 \\
1

\end{bmatrix}t$$

If we set $t=1$, $\mathbf{u}_{4}=\mathbf{u}_{1}+\mathbf{u}_{2}-\mathbf{u}_{3} \in \text{span}\{ \mathbf{u}_{1},\mathbf{u}_{2},\mathbf{u}_{3} \}$

Hence, we have the first requirements for a basis. Now let’s check if these vectors are linearly independent. Given the reduction from above, we can see that the only solution for the vectors in the span is $c_{1}'=c_{2}'=c_{3}'=0$ hence they are linearly independent.

Thus,$$\text{dim}(U) = 3$$

#### Definition of null space
Let $A \in \mathbb{R}^{m \times n}$. The null space of $A$ is $$N(A) = \{ \mathbf{x} \in \mathbb{R}^n : A\mathbf{x}=0\}$$
In words, this means the set of all $\mathbf{x} \in \mathbb{R}^n$ such that $A\mathbf{x}=0$ holds. (Also known as the kernel of A, $ker(A)$)

###### Exercise
Prove that $N(A)$ is a subspace for any A.

To prove that it’s a subspace, we first check if the zero-vector is included. And secondly check multiplicity and associativity.

$$A\mathbf{0} = 0 ,\text{ by definition.}$$
$$A\mathbf{x}_{1}+A\mathbf{x}_{2}=0+0=A(\mathbf{x}_{1}+\mathbf{x}_{2})$$
$$A\mathbf{x}=0 \to A(c \mathbf{x})=0$$

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 9|Lecture 9]]
