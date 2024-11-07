###### Exercise
Find $P$ for $$U = \text{span}\left\{ \begin{bmatrix}
1\\1\\1\\1
\end{bmatrix},\begin{bmatrix}
1\\2\\0\\1
\end{bmatrix},\begin{bmatrix}
-1\\0\\1\\1
\end{bmatrix} \right\}$$

First, let’s set $A$ such that 
$$A=\begin{bmatrix}
\mathbf{u}_{1}^T \\ \mathbf{u}_{2}^T  \\ \mathbf{u}_{3}^T
\end{bmatrix}$$
And use the fact that $U^\perp = N(A)$.

$$A=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 2 & 0 & 1 \\
-1 & 0 & 1 & 1
\end{bmatrix}\to \begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & -1 & 0 \\
0 & 1 & 2 & 2
\end{bmatrix}\to \begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & -1 & 0 \\
0 & 0 & 3 & 2
\end{bmatrix}$$

The solution is then in the form,
$$t\begin{bmatrix}
\frac{1}{3} \\ -\frac{2}{3} \\-\frac{2}{3} \\ 1 
\end{bmatrix},t \in \mathbb{R}$$

thus,
$$U^\perp= \text{span}\left\{ \begin{bmatrix}
1  \\
-2 \\
-2 \\
3
\end{bmatrix} \right\} = \text{span}\left\{ \mathbf{w} \right\}$$

$$P_{\perp} = \frac{1}{\mathbf{w}^T\mathbf{w}}\mathbf{w}\mathbf{w}^T$$
$$=\frac{1}{18}\begin{bmatrix}
1 & -2 & -2 & 3 \\
-2 & 4 & 4 & -6 \\
-2 & 4 & 4 & -6 \\
3 & -6 & -6 & 9
\end{bmatrix}$$

$$P=I-P_{\perp} = \frac{1}{18}\begin{bmatrix}
17 & 2 & 2 & -3 \\
2 & 14 & -4 & 6 \\
2 & -4 & 14 & 6 \\
-3 & 6 & 6 & 9
\end{bmatrix}$$


###### Example
Find the shortest distance from
$$\mathbf{x}=\begin{bmatrix}
1\\1\\1\\-1\\1
\end{bmatrix}$$
to
$$U=\text{span}\left\{ \begin{bmatrix}
1\\1\\1\\1\\1
\end{bmatrix},\begin{bmatrix}
1\\0\\1\\0\\1
\end{bmatrix},\begin{bmatrix}
1\\-1\\0\\0\\1
\end{bmatrix},\begin{bmatrix}
0\\0\\1\\1\\-1
\end{bmatrix} \right\}$$

We can either,
1. Construct an orthogonal basis of $U$ with Gram-Schmidt then compute $\text{proj}_{U}(\mathbf{x})$ and $\lvert \lvert \mathbf{x}-\text{proj}_{U}(\mathbf{x}) \rvert \rvert$.
2. Construct an orthogonal basis of $U^\perp$ and then compute $\text{proj}_{U^\perp}(\mathbf{x})=\mathbf{x}-\text{proj}_{U}(\mathbf{x})$ and $\lvert \lvert \text{proj}_{U^\perp}(\mathbf{x}) \rvert \rvert$.

Since $\text{dim}(U^\perp)= 1$. We just need to find the basis of $U^\perp$.

$$A=\begin{bmatrix}
\mathbf{u}_{1}^T\\ \mathbf{u}_{2}^T\\\mathbf{u}_{3}^T\\\mathbf{u}_{4}^T
\end{bmatrix}=\begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 1 \\
1 & -1 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & -1
\end{bmatrix}$$
$$\to \begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
0 & -1 & 0 & -1 & 0 \\
0 & -2 & -1 & -1 & 0 \\
0 & 0 & 1 & 1 & -1
\end{bmatrix} \to \begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
0 & -1 & 0 & -1 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 1 & 1 & -1
\end{bmatrix}$$
$$\to \begin{bmatrix}
1 & 1 & 1 & 1 & 1 \\
0 & -1 & 0 & -1 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & 2 & -1
\end{bmatrix}$$

$$\therefore \mathbf{w}=\begin{bmatrix}
-3 \\ -1 \\ 1 \\ 1 \\ 2
\end{bmatrix}$$

$$\text{proj}_{U^\perp}(\mathbf{x})=\text{proj}_{\mathbf{w}}(\mathbf{x})=\frac{\langle \mathbf{w},\mathbf{x} \rangle}{\langle \mathbf{w},\mathbf{w} \rangle }\mathbf{w} = \frac{-2}{16} \mathbf{w} $$
$$\therefore \lvert \lvert \text{proj}_{U^\perp}(\mathbf{x}) \rvert  \rvert  = \frac{1}{8} \times 4 = \frac{1}{2}$$

#### Definition of Orthogonal Matrix
A matrix $Q$ is orthogonal if $$Q^TQ=I \hspace{.1in} \cap \hspace{.1in} QQ^T=I$$

1. An orthogonal matrix is square and invertible with inverse $Q^{-1}=Q^T$. 
2. A matrix is orthogonal if the columns are orthonormal and rows are orthonormal. 
3. If $Q$ is orthogonal, then for $\mathbf{x}\in \mathbb{R}^n$, we have $\lvert \lvert Qx \rvert \rvert=\lvert \lvert x \rvert \rvert$.

[Proof]
Since $Q^TQ=I$ → $Q^T=Q^{-1}$.

Let $Q=\begin{bmatrix}\mathbf{q}_{1},\mathbf{q}_{2},\cdots,\mathbf{q}_{n}\end{bmatrix}$ and let’s compute $Q^TQ$.
$$Q^TQ=\begin{bmatrix}
\mathbf{q}_{1}^T\\\mathbf{q}_{2}^T \\ \vdots \\ \mathbf{q}_{n}^T
\end{bmatrix} \begin{bmatrix}\mathbf{q}_{1},\mathbf{q}_{2},\cdots,\mathbf{q}_{n}\end{bmatrix}=\begin{bmatrix}
\langle \mathbf{q}_{1},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{1},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{1},\mathbf{q}_{n} \rangle  \\
\langle \mathbf{q}_{2},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{2},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{2},\mathbf{q}_{n} \rangle  \\
\vdots \\
\langle \mathbf{q}_{n},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{n},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{n},\mathbf{q}_{n} \rangle 
\end{bmatrix} = I$$

Then, all columns are orthonormal.

Similarly, let $Q=\begin{bmatrix}\mathbf{q}_{1}  \\ \mathbf{q}_{2} \\ \vdots \\ \mathbf{q}_{n}\end{bmatrix}$
$$QQ^T=\begin{bmatrix}\mathbf{q}_{1}  \\ \mathbf{q}_{2} \\ \vdots \\ \mathbf{q}_{n}\end{bmatrix}\begin{bmatrix}\mathbf{q}_{1}^T  & \mathbf{q}_{2}^T  & \cdots &  \mathbf{q}_{n}^T\end{bmatrix}=\begin{bmatrix}
\langle \mathbf{q}_{1},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{1},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{1},\mathbf{q}_{n} \rangle  \\
\langle \mathbf{q}_{2},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{2},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{2},\mathbf{q}_{n} \rangle  \\
\vdots \\
\langle \mathbf{q}_{n},\mathbf{q}_{1} \rangle  & \langle \mathbf{q}_{n},\mathbf{q}_{2} \rangle &  \cdots  & \langle \mathbf{q}_{n},\mathbf{q}_{n} \rangle 
\end{bmatrix} = I$$

Thus, the rows are also orthonormal.

Now, for the last property,
$$\lvert \lvert Q\mathbf{x} \rvert  \rvert ^2=\langle Q\mathbf{x},Q\mathbf{x} \rangle = (Q\mathbf{x})^T(Q\mathbf{x})=\mathbf{x}^TQ^TQ\mathbf{x}=\mathbf{x}^T\mathbf{x}=\langle \mathbf{x},\mathbf{x} \rangle =\lvert \lvert \mathbf{x} \rvert  \rvert^2  $$
$$\therefore \lvert \lvert Q\mathbf{x} \rvert  \rvert =\lvert \lvert \mathbf{x} \rvert  \rvert $$

#### Definition of a reflection 
Let $U \subseteq \mathbb{R}^n$ be a subspace. The reflection of $\mathbf{x}$ through $U$ is
$$R\mathbf{x}=2P\mathbf{x}- \mathbf{x}$$

#### Theorem
Let $R$ be the reflection matrix through subspace $U$. Then, $R$ is orthogonal.

[Proof]
Let $P$ be the projection onto $U$. Then,
$$R=2P-I$$

Let’s check orthogonality by $R^TR$:
$$R^TR=(2P-I)^T(2P-I)=(2P^T-I)(2P - I)= 4P^TP-2P-2P^T+I$$
$$=4P^2-2P-2P + I=4P-4P+I = I$$

because $P^2=P,P^T=P$. 

Think of it this way,
$$\mathbf{x} - 2(\mathbf{x}-\text{proj}_{U}(\mathbf{x}))=2\text{proj}_{U}(\mathbf{x})-\mathbf{x}$$

==Note that $R$ is also symmetric.==

*But, is a projection matrix orthogonal?*
$$P^TP=P^2=P \neq I$$
*no!*


[Claim]
If $Q_{1},Q_{2},\cdots,Q_{m}$ are orthogonal, then $T=Q_{1}Q_{2}\cdots Q_{m}$ is orthogonal.

[Proof]
$$T^TT=(Q_{1}Q_{2} \cdots Q_{m})^T(Q_{1}Q_{2} \cdots Q_{m})$$
$$=Q_{m}^T \cdots Q_{2}^TQ_{1}^TQ_{1}Q_{2}\cdots Q_{m}$$
$$=I$$

#### Next Lecture [[Lecture 17]]
