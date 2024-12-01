##### Exercise
Find the projection matrix $P$ that projects on $\mathbf{u}=\begin{bmatrix}1\\1\\1\end{bmatrix}$. Then, project $\mathbf{x}=\begin{bmatrix}-1\\0\\1\end{bmatrix}$.

We know that
$$P=\frac{1}{\langle \mathbf{u},\mathbf{u} \rangle }\mathbf{u}\mathbf{u^T}= \frac{1}{3}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}$$

For projecting $\mathbf{x}$, we have
$$\text{proj}_{\mathbf{u}}(\mathbf{x})=P\mathbf{x}=\begin{bmatrix}
0 \\
0 \\
0 
\end{bmatrix}$$
That is $\mathbf{x}$ is orthogonal to $\mathbf{u}$.

Instead, if we project $\mathbf{x}_{2}=\begin{bmatrix}1\\1\\0\end{bmatrix}$, we would get

$$P\mathbf{x}_{2}=\frac{1}{3}\begin{bmatrix}
2 \\
2 \\
2 \\
\end{bmatrix}$$

#### Projecting onto a subspace
Let $\mathbf{u}_{1},\cdots,\mathbf{u}_{m} \in \mathbb{R}^n$ be a basis of a subspace $U \subseteq \mathbb{R}^n$. Can we define the projection using the sum of projections onto each basis vector? That is:
$$\text{proj}_{U}(\mathbf{x})=\sum_{i=1}^m \frac{\langle \mathbf{x},\mathbf{u}_{i} \rangle }{\langle \mathbf{u}_{i},\mathbf{u}_{i} \rangle }\mathbf{u}_{i}$$

For this to give us the projection on the subspace, we need $\mathbf{u}_{i}$ to be the orthogonal basis so that $\mathbf{x}-\text{proj}_{U}(\mathbf{x})\in U^\perp$.

We want the projection to satisfy,
1. $\text{proj}_{U}(\mathbf{x})$ is orthogonal to $\mathbf{x}-\text{proj}_{U}(\mathbf{x})$.
2. $\text{proj}_{U}(\mathbf{u})=\mathbf{u}$ if $\mathbf{u}\in U$.

#### Definition of orthogonal basis
Let $U \subseteq \mathbb{R}^n$ be a subspace. Then $\{ \mathbf{u}_{i},\cdots, \mathbf{u}_{m}\}$ is an orthogonal basis of $U$ if
1. $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ is a basis of $U$.
2. $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ is an orthogonal set of vectors, that is $\langle \mathbf{u}_{i},\mathbf{u}_{j} \rangle = 0$ for all $i \neq j$.

Furthermore, if $\lvert \lvert \mathbf{u}_{i} \rvert \rvert=1$, then we call this an *orthonormal basis* of $U$.

#### Definition of Orthogonal projection.
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be an orthogonal basis of $U$. Then, the orthogonal projection of $\mathbf{x}$ on $U$ is $$\text{proj}_{U}(\mathbf{x})=\sum_{i=1}^m \text{proj}_{\mathbf{u}_{i}}(\mathbf{x})=\sum_{i=1}^m \frac{\langle \mathbf{x},\mathbf{u}_{i} \rangle }{\langle \mathbf{u}_{i},\mathbf{u}_{i} \rangle }\mathbf{u}_{i}$$$$=\sum_{i=1}^m \frac{1}{\mathbf{u}_{i}^T\mathbf{u}_{i}}\mathbf{u}_{i}\mathbf{u}_{i}^T\mathbf{x}$$
where the derivation is exactly the same as the derivation of $P$.

When the basis is orthonormal,
$$\text{proj}_{U}(\mathbf{x})=P\mathbf{x}=\begin{bmatrix}
\mathbf{u}_{1}  & \cdots  & \mathbf{u}_{m}
\end{bmatrix}\begin{bmatrix}
\mathbf{u}_{1}^T \\ \vdots \\ \mathbf{u}_{m}^T
\end{bmatrix}\mathbf{x}=\begin{bmatrix}
\mathbf{u}_{1}  & \cdots  & \mathbf{u}_{m}
\end{bmatrix}\begin{bmatrix}
\langle \mathbf{u}_{1}, \mathbf{x} \rangle \\ \vdots \\ \langle \mathbf{u}_{m}, \mathbf{x} \rangle 
\end{bmatrix}=\sum_{i=1}^m \langle \mathbf{u}_{i},\mathbf{x} \rangle \mathbf{u}_{i}$$

#### Theorem
Let $U\subseteq \mathbb{R}^n$ be a subspace. Let $P \in \mathbb{R}^{n\times n}$ be such that $\text{proj}_{U}(\mathbf{x})=P\mathbf{x}$.
Then,
1. $P^2=P$.
2. $P^T=P$.
3. $\text{rank}(P)=\text{dim}(U)$.

[Proof]
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be an orthonormal basis of $U$ and set $$Q_{1}=\begin{bmatrix}
\mathbf{u}_{1}  & \mathbf{u}_{2}  &  \cdots  & \mathbf{u}_{m}
\end{bmatrix}$$

Then, $P=Q_{1}Q^T_{1}$ and we can now compute $P^2$ as
$$P^2=Q_{1}Q_{1}^TQ_{1}Q^T_{1}$$

Let’s see $Q_{1}^TQ_{1}$,
$$Q_{1}^TQ_{1}=\begin{bmatrix}
\mathbf{u}_{1}^T \\ \mathbf{u}_{2}^T \\ \vdots \\ \mathbf{u}_{m}^T
\end{bmatrix}\begin{bmatrix}
\mathbf{u}_{1} &  \mathbf{u}_{2}  &  \cdots   & \mathbf{u}_{m}
\end{bmatrix}$$
$$=\begin{bmatrix}
\langle \mathbf{u}_{1},\mathbf{u}_{1} \rangle & \langle \mathbf{u}_{1},\mathbf{u}_{2} \rangle  & \cdots & \langle \mathbf{u}_{1},\mathbf{u}_{m} \rangle \\
\langle \mathbf{u}_{2},\mathbf{u}_{1} \rangle  & \langle \mathbf{u}_{2},\mathbf{u}_{2} \rangle & \cdots & \langle \mathbf{u}_{2},\mathbf{u}_{m} \rangle \\
\vdots \\
\langle \mathbf{u}_{m},\mathbf{u}_{1} \rangle  & \langle \mathbf{u}_{m},\mathbf{u}_{1} \rangle  & \cdots & \langle \mathbf{u}_{m},\mathbf{u}_{m} \rangle
\end{bmatrix} = I$$

because $\langle \mathbf{u}_{i},\mathbf{u}_{j} \rangle = 1$ if $i = j$ and $\langle \mathbf{u}_{i},\mathbf{u}_{j} \rangle = 0$ if $i\neq j$.

Plugging this back into the above $P^2$ gives,$$P^2=Q_{1}Q^T_{1}Q_{1}Q^T_{1}=Q_{1}IQ_{1}^T=P$$
Now, with the same setup of $P$,
$$P^T=(Q_{1}Q_{1}^T)^T=Q_{1}Q_{1}^T=P$$

Lastly, for
$$\text{rank}(P)=\text{dim}(U)=m$$


considering the orthonormal basis of $U$ as the same set above.

Let’s show that $R(P)= U$, first let $y \in R(P), Px=y$
$$Px=y= \sum_{i=1}^m \frac{\langle u_{i},x \rangle }{\langle u_{i},u_{i} \rangle } u_{i}  \in U \to y \in U$$
Now let $y \in U$,
$$y=\sum_{i=1}^m c_{i}u_{i}$$
Then let $Px=\sum_{i=1}^m c_{i}u_{i}$, we can see that
$$Px=\sum _{i=1}^m c_{i}u_{i}=y \in R(P)$$
Hence,
$$\therefore R(P)=U$$
$$\text{rank}(P)=\text{dim}(R(P))=\text{dim}(U) = m$$

#### Theorem
Let $U \subseteq \mathbb{R}^n$ be a subspace and $P$ be the projection matrix onto $U$. Then,
$$\mathbf{x}-\text{proj}_{U}(\mathbf{x})\in U^\perp$$

[Proof]
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be an orthonormal basis of $U$. Then,
$$\text{proj}_{U}(\mathbf{x}) = \langle \mathbf{u}_{1},\mathbf{x} \rangle\mathbf{u}_{1} +\cdots+\langle \mathbf{u}_{m},\mathbf{x} \rangle\mathbf{u}_{m}$$

Pick any $k \in \{ 1,\cdots,m \}$. Then,
$$\langle \mathbf{x}-\text{proj}_{U}(\mathbf{x}),\mathbf{u}_{k} \rangle = \langle \mathbf{x}- (\langle \mathbf{u}_{1},\mathbf{x} \rangle\mathbf{u}_{1} +\cdots+\langle \mathbf{u}_{m},\mathbf{x} \rangle\mathbf{u}_{m}), \mathbf{u}_{k} \rangle $$
$$=\langle \mathbf{x},\mathbf{u}_{k} \rangle-\langle \mathbf{u}_{1},\mathbf{x} \rangle\langle \mathbf{u}_{1},\mathbf{u}_{k} \rangle - \cdots-  \langle \mathbf{u}_{m},\mathbf{x} \rangle\langle \mathbf{u}_{m},\mathbf{u}_{k} \rangle$$
$$=\langle \mathbf{x},\mathbf{u}_{k} \rangle  - \langle \mathbf{u}_{k},\mathbf{x} \rangle \langle \mathbf{u}_{k},\mathbf{u}_{k} \rangle $$
$$=\langle \mathbf{x},\mathbf{u}_{k} \rangle - \langle \mathbf{u}_{k},\mathbf{x} \rangle  = 0$$

As a result, $\mathbf{x}-\text{proj}_{U}(\mathbf{x})$ is orthogonal to any $\mathbf{u}_{k}$ in the basis of $U$ and hence $$\therefore \mathbf{x}-\text{proj}_{U}(\mathbf{x})\in U^\perp$$
#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 14]]
