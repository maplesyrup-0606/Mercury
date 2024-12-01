Recall that,$$P=\begin{bmatrix}
\mathbf{u}_{1}  & \cdots  & \mathbf{u}_{m}
\end{bmatrix}\begin{bmatrix}
\mathbf{u}_{1}^T \\ \vdots \\ \mathbf{u}_{m}^T
\end{bmatrix} = Q_{1}Q_{1}^T$$

also, recall when the basis $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ is orthonormal:
$$\text{proj}_{U}(\mathbf{x})=\langle \mathbf{x},\mathbf{u}_{1} \rangle \mathbf{u}_{1} + \cdots+ \langle \mathbf{x},\mathbf{u}_{m} \rangle \mathbf{u}_{m}$$

Let us calculate,
$$Q_{1}^T\mathbf{x}= \begin{bmatrix}
\mathbf{u}_{1}^T \\ \vdots \\ \mathbf{u}_{m}^T
\end{bmatrix}\mathbf{x}=\begin{bmatrix}
\langle \mathbf{u_{1}},\mathbf{x} \rangle \\ \langle \mathbf{u}_{2}, \mathbf{x} \rangle \\ \vdots \\ \langle \mathbf{u}_{m},\mathbf{x} \rangle   
\end{bmatrix}$$

Then,
$$Q_{1}(Q_{1}^T\mathbf{x})=\begin{bmatrix}
\mathbf{u}_{1}  & \cdots  & \mathbf{u}_{m}
\end{bmatrix}\begin{bmatrix}
\langle \mathbf{u_{1}},\mathbf{x} \rangle \\ \langle \mathbf{u}_{2}, \mathbf{x} \rangle \\ \vdots \\ \langle \mathbf{u}_{m},\mathbf{x} \rangle   
\end{bmatrix} = \langle \mathbf{u_{1}},\mathbf{x} \rangle\mathbf{u}_{1}  \cdots + \langle \mathbf{u_{m}},\mathbf{x} \rangle\mathbf{u}_{m} = \text{proj}_{U}(\mathbf{x})=P\mathbf{x}$$
Hence, *given an orthonormal basis for a subspace, we can decompose the projection matrix onto the subspace*.

###### Example
Let us have the subspace,
$$U=\text{span}\left\{ \begin{bmatrix}
1\\0\\0
\end{bmatrix}, \begin{bmatrix}
1\\1\\0
\end{bmatrix} \right\}$$

where $\mathbf{u}_{1}=\begin{bmatrix}1\\0\\0\end{bmatrix}, \mathbf{u}_{2}=\begin{bmatrix}1\\1\\0\end{bmatrix}$. Let us project $\mathbf{u}_{1}$ onto $U$. Since $\mathbf{u}_{1}$, we expect $\text{proj}_{U}(\mathbf{u}_{1})= \mathbf{u}_{1}$.

Note that $\mathbf{u}_{1},\mathbf{u}_{2}$ are not orthogonal since $\langle \mathbf{u}_{1},\mathbf{u}_{2} \rangle = 1\neq {0}$. Let us see what happens when we still apply the formula:
$$\text{proj}_{U}(\mathbf{u}_{1})=\text{proj}_{\mathbf{u}_{1}}(\mathbf{u}_{1})+\text{proj}_{\mathbf{u}_{2}}(\mathbf{u}_{1})$$
$$=\frac{\langle \mathbf{u}_{1},\mathbf{u}_{1} \rangle }{\langle \mathbf{u}_{1},\mathbf{u}_{1} \rangle }\mathbf{u}_{1} + \frac{\langle \mathbf{u}_{1},\mathbf{u}_{2} \rangle }{\langle \mathbf{u}_{2},\mathbf{u}_{2} \rangle }\mathbf{u}_{2}$$
$$=\mathbf{u}_{1} + \frac{1}{2}\begin{bmatrix}
1\\1\\0
\end{bmatrix} \neq \mathbf{u}_{1}$$

Hence, we get a result that is contradictory to what we expect. ==This is because the projection formula is not valid without an orthogonal basis, so we cannot use it without an orthogonal basis.==


#### Theorem
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{n} \}$ be an orthogonal basis of $\mathbb{R}^n$. Then we have,
$$\mathbf{x}= \frac{\langle \mathbf{u}_{1},\mathbf{x} \rangle}{\langle\mathbf{u}_{1},\mathbf{u}_{1}\rangle}\mathbf{u}_{1} + \cdots+\frac{\langle \mathbf{u}_{n},\mathbf{x} \rangle }{\langle \mathbf{u}_{n},\mathbf{u}_{n} \rangle }\mathbf{u}_{n}$$

[Proof]
Since $\mathbf{x}\in \mathbb{R}^n$ and $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{n} \}$ is a basis, we have that,
$$\mathbf{x}=c_{1}\mathbf{u}_{1}+\cdots+c_{n}\mathbf{u}_{n}$$

and we want to find values of $c_{1},c_{2},\cdots,c_{n} \in \mathbb{R}$. Pick any $k \in \{ 1,2,\cdots,n \}$ and compute
$$\langle \mathbf{x},\mathbf{u}_{k} \rangle = \langle c_{1}\mathbf{u}_{1} +c_{2}\mathbf{u}_{2}+\cdots+c_{n}\mathbf{u}_{n}, \mathbf{u}_{k} \rangle $$
$$=c_{1}\langle \mathbf{u}_{1},\mathbf{u}_{k} \rangle + c_{2}\langle \mathbf{u}_{2},\mathbf{u}_{k} \rangle +\cdots+c_{n}\langle \mathbf{u}_{n},\mathbf{u}_{k} \rangle  $$
$$=c_{k}\langle \mathbf{u}_{k},\mathbf{u}_{k} \rangle $$

since for $i \neq k$ we have that $\langle \mathbf{u}_{i},\mathbf{u}_{k} \rangle =0$. Then, solving for $c_k$ gives
$$c_{k} = \frac{\langle \mathbf{x}, \mathbf{u}_{k} \rangle }{\langle \mathbf{u}_{k},\mathbf{u}_{k} \rangle },k=1,2,\cdots,n$$ 
#### Theorem
Let $U \subseteq \mathbb{R}^n$ be a subspace. Let $P$ be the projection onto $U$ and let $P_\perp$ be the projection onto $U^\perp$. Then, we have
$$P_{\perp}=I-P$$

[Proof]
First, recall that
$$\text{dim}(U)+\text{dim}(U^\perp) = n$$

Let, $\text{dim}(U)=m$, this means that the number of vectors in a basis of $U$ is $m$ and the number of the vectors in a basis of $U^\perp$ is $n-m$.

Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be the orthogonal basis for $U$ and $\{ \mathbf{v}_{1},\cdots,\mathbf{v}_{n - m} \}$ be the orthogonal basis for $U^\perp$. Since $U$ and $U^\perp$ are orthogonal subspaces, we have that the sets $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ and $\{ \mathbf{v}_{1},\cdots,\mathbf{v}_{n - m} \}$ are orthogonal. 

This gives us a set of $n$ orthogonal vectors, that is
$$\{ \mathbf{u}_{1}, \mathbf{u}_{2},\cdots,\mathbf{u}_{m},\mathbf{v}_{1},\mathbf{v}_{2},\cdots,\mathbf{v}_{n-m} \}$$

Then it follows that this set is an orthogonal basis of $\mathbb{R}^n$.
Thus, for any vector $\mathbf{x}\in \mathbb{R}^n$,
$$\mathbf{x}= \frac{\langle \mathbf{x}, \mathbf{u}_{1} \rangle }{\langle \mathbf{u}_{1},\mathbf{u}_{1} \rangle }\mathbf{u}_{1} + \cdots+ \frac{\langle \mathbf{x}, \mathbf{u}_{m} \rangle }{\langle \mathbf{u}_{m},\mathbf{u}_{m} \rangle }\mathbf{u}_{m} + \frac{\langle \mathbf{x}, \mathbf{v}_{1} \rangle }{\langle \mathbf{v}_{1},\mathbf{v}_{1} \rangle }\mathbf{v}_{1} + \cdots + \frac{\langle \mathbf{x}, \mathbf{v}_{n-m} \rangle }{\langle \mathbf{v}_{n-m},\mathbf{v}_{n-m} \rangle }\mathbf{v}_{n-m}$$

$$= \text{proj}_{U}(\mathbf{x})+\text{proj}_{U^\perp}(\mathbf{x})$$

Hence, we derive that
$$\text{proj}_{U^\perp}(\mathbf{x})= \mathbf{x}-\text{proj}_{U}(\mathbf{x})=(I-P)\mathbf{x}$$
$$\therefore P_{\perp} = I - P$$

*Depending on whether $n-m \geq m$ or $m \geq n - m$, we can decide if it is easier to compute $P$ or $P_{\perp}$.*

###### Example
Calculate the projection matrix onto $U$ and $U^\perp$ where $U = \text{span}\left\{ \begin{bmatrix}1\\ 0 \\ 0\end{bmatrix}, \begin{bmatrix} 0 \\ 1\\ -1 \end{bmatrix} \right\}$.

Notice that $\mathbf{u}_{1},\mathbf{u}_{2}$ are orthogonal to each other (also linearly independent).

To calculate the projection matrix $P$ onto $U$,  we have
$$P= \frac{1}{\mathbf{u}_{1}^T\mathbf{u}_{1}}\mathbf{u}_{1}\mathbf{u}_{1}^T+\frac{1}{\mathbf{u}_{2}^T\mathbf{u}_{2}}\mathbf{u}_{2}\mathbf{u}_{2}^T$$

From the theorem above, we can calculate $P$ from $P_{\perp}$ as 
$$P = I - P_{\perp}$$

For this, we have to find an orthogonal basis to $U_\perp$. We can see that
$$U^\perp = \text{span} \left\{ \begin{bmatrix}
0   \\ 1 \\ 1
\end{bmatrix} \right\}$$

We can now calculate $P_{\perp}$ by using one vector,
$$P_{\perp}= \frac{1}{\mathbf{u}_{3}^T\mathbf{u}_{3}}\mathbf{u}_{3}\mathbf{u}_{3}^T$$
From the first method using $P$,
$$P= \frac{1}{\mathbf{u}_{1}^T\mathbf{u}_{1}}\mathbf{u}_{1}\mathbf{u}_{1}^T+\frac{1}{\mathbf{u}_{2}^T\mathbf{u}_{2}}\mathbf{u}_{2}\mathbf{u}_{2}^T=\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix} + \frac{1}{2}\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & -1 \\
0 & -1 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0 \\
0 & \frac{1}{2} & -\frac{1}{2} \\
0 & -\frac{1}{2} & \frac{1}{2}
\end{bmatrix}$$
Then,
$$P_{\perp}= I - P=\begin{bmatrix}
0 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2} \\
0 & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}$$

Or using the orthogonal basis of $U^\perp$ from above,
$$P_{\perp}= \frac{1}{\mathbf{u}_{3}^T\mathbf{u}_{3}}\mathbf{u}_{3}\mathbf{u}_{3}^T=\frac{1}{2} \begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 1  \\
0 & 1 & 1
\end{bmatrix}$$
which is the same as above.

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 15]]