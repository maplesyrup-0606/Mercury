###### Example
Find a basis and dimension of $N(A)$ for
$$A=\begin{bmatrix}
1 & 3 & 1 & -1 \\
-2 & -4 & 0 & -2 \\
1 & 4 & 2 & -3
\end{bmatrix}$$

We wish to find $\mathbf{x}\in \mathbb{R}^n$ such that $A\mathbf{x}=0$. That is, we will find the solutions to $A\mathbf{x}=0$. 
$$\begin{bmatrix}
A & \vert & \mathbf{0}
\end{bmatrix}=\begin{bmatrix}
1 & 3 & 1 & -1 & \vert & 0 \\
-2 & -4 & 0 & -2 & \vert & 0 \\
1 & 4 & 2 & -3 & \vert & 0
\end{bmatrix} \to \begin{bmatrix}
1 & 3 & 1 & -1 & \vert & 0 \\
0 & 2 & 2 & -4 & \vert & 0 \\
0 & 0 & 0 & 0 & \vert & 0
\end{bmatrix}$$

Let $x_{3}=t_{1},x_{4}=t_{2}$. Then,
$$\mathbf{x}=\begin{bmatrix}
2t_{1}-5t_{2} \\
-t_{1}+2t_{2} \\
t_{1} \\
t_{2}
\end{bmatrix} = \begin{bmatrix}
2 \\
-1 \\
1 \\
0
\end{bmatrix}t_{1}+\begin{bmatrix}
-5 \\
2 \\
0 \\
1
\end{bmatrix}t_{2}$$

That means $N(A)$ consists of all linear combination of $\begin{bmatrix}2 \\ -1 \\ 1\\0\end{bmatrix},\begin{bmatrix} -5 \\ 2 \\ 0 \\ 1\end{bmatrix}$, that is, the span of these two vectors. Moreover, these two vectors are linearly independent. As a result, they form a basis for $N(A)$ and $\text{dim}(N(A))=2$.

#### Theorem
For $A \in \mathbb{R}^{m\times n}$ assume that $A=LU$. Then we have that $N(A)= N(U)$.

[Proof]
Recall that $L$ is invertible, which is another way of saying that row operations are reversible. Then, we have the equivalences
$$\mathbf{x} \in N(A) \iff A\mathbf{x}=0 \iff LU\mathbf{x}=0 \iff L^{-1}LU\mathbf{x}=L^{-1}0 \iff U\mathbf{x}=0 \iff \mathbf{x} \in N(U)$$

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 10|Lecture 10]]
