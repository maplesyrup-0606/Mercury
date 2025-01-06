#### Gram-Schmidt Algorithm
In particular, let $\mathbf{u}_{1},\cdots,\mathbf{u}_{m}$ be any basis of $U \in \mathbb{R}^n$. We can construct an orthogonal basis iteratively subtracting the part of $\mathbf{u}_{k}$ in the span of $\mathbf{u}_{1},\cdots,\mathbf{u}_{k - 1}$.
That is, let us calculate $\mathbf{v}_{1},\cdots,\mathbf{v}_{m}$ as 
$$\mathbf{v}_{i}=\mathbf{u}_{i} - \sum_{j=1}^{ i- 1}\text{proj}_{\mathbf{v}_{j}}(\mathbf{u}_{i})$$

Let’s see why $\mathbf{v}_{1},\cdots,\mathbf{v}_{m}$ are orthogonal.

First, recall that $\mathbf{x}-\text{proj}_{U}(\mathbf{x})\in U^\perp$ for any subspace $U$. In view of the definition of $\mathbf{v}_{2}$, this states that
$$\mathbf{v}_{2}=\mathbf{u}_{2}-\text{proj}_{\mathbf{v}_{1}}(\mathbf{u}_{2}) \perp \mathbf{v}_{1}$$
for instance, $U=\text{span}\{ \mathbf{v}_{1} \}$ in this case.

Since $\mathbf{v}_{1},\mathbf{v}_{2}$ are orthogonal they form an orthogonal basis for the subspace $\text{span}\{ \mathbf{v}_{1},\mathbf{v}_{2} \}$. Then, we have that
$$\mathbf{v}_{3}=\mathbf{u}_{3}-\text{proj}_{\mathbf{v}_{3}}(\mathbf{u}_{3}) - \text{proj}_{\mathbf{v}_{1}}(\mathbf{u}_{3})$$
$$=\mathbf{u}_{3}-\text{proj}_{\text{span}\{ \mathbf{v_{1},\mathbf{v}_{2}} \}}(\mathbf{u}_{3})$$
$$\perp \text{span}\{ \mathbf{v}_{1},\mathbf{v}_{2} \}$$

We can then recursively show that $\mathbf{v}_{1},\cdots,\mathbf{v}_{m}$ are orthogonal vectors.

###### Exercise
Prove that $\text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}=\text{span}\{ \mathbf{v}_{1},\cdots,\mathbf{v}_{m} \}$.

Let $\mathbf{a} \in  \text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$. That is, $$\mathbf{a}=c_{1}\mathbf{u}_{1}+\cdots+c_{m}\mathbf{u}_{m},c_{i}\in \mathbb{R}$$
$$\mathbf{a}=c_{1}(\mathbf{v}_{1})+c_{2}(\mathbf{v}_{2}+\text{proj}_{\mathbf{v}_{1}}(\mathbf{u}_{2}))+\cdots+c_{m} (\mathbf{v}_{m}+\sum_{j=1}^{ m- 1}\text{proj}_{\mathbf{v}_{j}}(\mathbf{u_{m}}))$$
$$=d_{1}\mathbf{v}_{1}+\cdots+d_{m}\mathbf{v}_{m} \in \text{span} \{ \mathbf{v}_{1},\cdots,\mathbf{v}_{m} \}$$

Now, let $\mathbf{b} \in \text{span} \{ \mathbf{v}_{1},\cdots,\mathbf{v}_{m} \}$. Hence,
$$\mathbf{b}=c'_{1}\mathbf{v}_{1}+\cdots+c'_{m}\mathbf{v}_{m},c'_{i}\in \mathbb{R}$$
$$\mathbf{b}=c_{1}'\mathbf{u}_{1} + c_{2}'(\mathbf{u}_{2}-\text{proj}_{\mathbf{v}_{1}}(\mathbf{u}_{2})) + \cdots+c_{m}'(\mathbf{u}_{m}- \sum_{j=1}^{ m- 1}\text{proj}_{\mathbf{v}_{j}}(\mathbf{u_{m}}))$$
$$=e_{1}\mathbf{u}_{1}+\cdots+e_{m}\mathbf{u}_{m}\in \text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$$

Hence,
$$\therefore \text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}=\text{span}\{ \mathbf{v}_{1},\cdots,\mathbf{v}_{m} \}$$

###### Example
Find an orthogonal basis and the projection matrix for the subspace defined as
$$U = \text{span}\left\{ \begin{bmatrix}
1\\1\\1\\1
\end{bmatrix},\begin{bmatrix}
1\\0\\0\\1
\end{bmatrix},\begin{bmatrix}
1\\1\\-1\\1
\end{bmatrix} \right\}$$
Let’s apply the Gram-Schmidt orthogonalization to obtain
$$\mathbf{v}_{1}=\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}$$
$$\mathbf{v}_{2}=\begin{bmatrix}
1\\0\\0\\1
\end{bmatrix}- \frac{2}{4}\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}=\begin{bmatrix}
\frac{1}{2} \\ -\frac{1}{2}\\ -\frac{1}{2}\\ \frac{1}{2}
\end{bmatrix}$$
$$\mathbf{v}_{3}=\begin{bmatrix}
1\\1\\-1\\1
\end{bmatrix}- \begin{bmatrix}
\frac{1}{2} \\ -\frac{1}{2} \\ -\frac{1}{2} \\ \frac{1}{2}
\end{bmatrix}-\frac{1}{2}\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}=\begin{bmatrix}
0 \\ 1 \\ -1 \\ 0
\end{bmatrix}$$

$$P= \frac{1}{\lvert \lvert \mathbf{v}_{1} \rvert  \rvert^2 }\mathbf{v}_{1}\mathbf{v}_{1}^T + \frac{1}{\lvert \lvert \mathbf{v}_{2} \rvert  \rvert^2 }\mathbf{v}_{2}\mathbf{v}_{2}^T + \frac{1}{\lvert \lvert \mathbf{v}_{3} \rvert  \rvert^2 }\mathbf{v}_{3}\mathbf{v}_{3}^T$$
$$= \frac{1}{4} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1
\end{bmatrix} + \begin{bmatrix}
\frac{1}{4} & -\frac{1}{4} & -\frac{1}{4} & \frac{1}{4} \\
-\frac{1}{4} & \frac{1}{4}  & \frac{1}{4} & -\frac{1}{4}  \\
-\frac{1}{4} & \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \\
\frac{1}{4} & -\frac{1}{4} & -\frac{1}{4} & \frac{1}{4}
\end{bmatrix} + \frac{1}{2} \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 1 & -1 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} $$
$$=\frac{1}{4} \begin{bmatrix}
2 & 0 & 0 & 2 \\
0 & 4 & 0 & 0 \\
0 & 0 & 4 & 0 \\
2 & 0 & 0 & 2
\end{bmatrix}$$

Then, we can calculate $P_{\perp}=I - P$.

For $P_{\perp}$, we have to find an orthogonal basis for $U^\perp$. If we set up a matrix $A$ that has the vectors $\mathbf{u}_{1}^T,\mathbf{u}_{2}^T,\mathbf{u}_{3}^T$ in its rows, then $U^\perp = N(A)$.

$$A=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 0 & 0 & 1 \\
1 & 1 & -1 & 1
\end{bmatrix} \to \begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & -1 & -1 & 0 \\
0 & 0 & -2 & 0
\end{bmatrix}$$

Hence, solving $A\mathbf{x}=0$ gives
$$N(A)= \text{span}\left\{ \begin{bmatrix}
1\\0\\0\\-1
\end{bmatrix} \right\} = \text{span}\left\{ \mathbf{w} \right\}$$

Then, alternatively we can calculate $P_\perp$ using $\mathbf{w}$.

$$P_{\perp} =\frac{1}{\mathbf{w}^T\mathbf{w}}\mathbf{w}\mathbf{w}^T= \frac{1}{2} \begin{bmatrix}
1 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
-1 & 0 & 0 & 1
\end{bmatrix}$$
$$\therefore P = I - P_{\perp} = \frac{1}{2} \begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 2 & 0 & 0 \\
0 & 0 & 2 & 0 \\
1 & 0 & 0 & 1
\end{bmatrix}$$

#### Theorem
Let $U \subseteq \mathbb{R}^n$ be a subspace and let $\mathbf{x} \in \mathbb{R}^n$. Then,
$$\lvert \lvert \mathbf{x}- \text{proj}_{U}(\mathbf{x}) \rvert  \rvert \leq \lvert \lvert \mathbf{x} - \mathbf{u} \rvert  \rvert $$
for any $\mathbf{u} \in U$.

[Proof]
When we have $\mathbf{x}_{1},\mathbf{x}_{2}$, pythagorean theorem tells us that when we have $\langle \mathbf{x}_{1},\mathbf{x}_{2} \rangle = 0$, then $\lvert \lvert \mathbf{x}_{1} + \mathbf{x}_{2} \rvert \rvert^2 = \lvert \lvert \mathbf{x}_{1} \rvert \rvert^2+\lvert \lvert \mathbf{x}_{2} \rvert \rvert^2$.

$$\lvert \lvert \mathbf{x}-\mathbf{u} \rvert  \rvert ^2 =\lvert \lvert \mathbf{x}-\text{proj}_{U}(\mathbf{x}) \rvert  \rvert^2 + \lvert \lvert \text{proj}_{U}(\mathbf{x})-\mathbf{u} \rvert  \rvert ^2 $$

But since, $\lvert \lvert \text{proj}_{U}(\mathbf{x})-\mathbf{u} \rvert  \rvert ^2  \geq 0$ the proof is complete.

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 16|Lecture 16]]

