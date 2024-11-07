#### Definition of inner product
We define the inner product of vectors $\mathbf{x},\mathbf{y}\in \mathbb{R}^n$ to be
$$\langle \mathbf{x}, \mathbf{y} \rangle =\sum_{k=1}^nx_{k}y_{k}$$
where $$\mathbf{x}=\begin{bmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{bmatrix},\mathbf{y}=\begin{bmatrix}
y_{1} \\
\vdots \\
y_{n}
\end{bmatrix}$$

##### Properties of inner product
1. $$\langle \mathbf{x},\mathbf{y} \rangle =\langle \mathbf{y},\mathbf{x} \rangle $$
2. $$\langle \mathbf{x},\mathbf{y} \rangle =\mathbf{x}^T\mathbf{y}=\mathbf{y}^T \mathbf{x}$$
3. $$\langle a\mathbf{x}+\mathbf{y},\mathbf{z} \rangle = a\langle \mathbf{x},\mathbf{z} \rangle + \langle \mathbf{y},\mathbf{z} \rangle   $$
4. The $l_2$ norm of a vector $\mathbf{x}$ is $$\lvert \lvert \mathbf{x} \rvert  \rvert =\sqrt{ \langle \mathbf{x},\mathbf{x} \rangle  }=\sqrt{ x_{1}^2+\cdots+x_{n}^2 }$$
5. Let us have $A \in \mathbb{R}^{m \times n}, \mathbf{x}\in \mathbb{R}^n,\mathbf{y}\in \mathbb{R}^m$. Then, $$\langle A\mathbf{x}, \mathbf{y} \rangle=(A\mathbf{x})^T\mathbf{y}=\mathbf{x}^TA^T\mathbf{y} = \langle \mathbf{x},A^T\mathbf{y} \rangle  $$
6. Let us have $A=\begin{bmatrix}\mathbf{u}^T_{1} \\ \vdots \\ \mathbf{u}^T_{m}\end{bmatrix} \in \mathbb{R}^{m\times n}$, where $\mathbf{u}_{1},\cdots,\mathbf{u}_{m}\in \mathbb{R}^n$, that is, $\mathbf{u}^T_{i}$ is the $i$-th row of $A$. Then for any $\mathbf{x}\in \mathbb{R}^{n}$, we have $$A\mathbf{x}=\begin{bmatrix}
\langle \mathbf{u}_{1}, \mathbf{x} \rangle  \\
\vdots \\
\langle \mathbf{u}_{m}, \mathbf{x} \rangle
\end{bmatrix}$$

#### Definition of orthogonality
Vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ are orthogonal if $\langle \mathbf{x},\mathbf{y} \rangle=0$. A set of non-zero vectors $\{ \mathbf{x}_{1},\cdots,\mathbf{x}_{m} \} \in \mathbb{R}^n$ is an orthogonal set if $\langle \mathbf{x}_{i},\mathbf{x}_{j} \rangle = 0$ for all $i \neq j$ .

#### Theorem
If $\{ \mathbf{x}_{1},\cdots,\mathbf{x}_{m} \} \subseteq \mathbb{R}^n$ is an orthogonal set, the vectors $\mathbf{x}_{1},\cdots,\mathbf{x}_{m}$ are linearly independent.

[Proof]
To determine linear independence, we want to see if there exist non-zero $c_{1},\cdots,c_{m}$ such that $\mathbf{x}_{1}c_{1}+\cdots+\mathbf{x}_{m}c_{m}=\mathbf{0}$. Let us pick any $k \in \{ 1,\cdots,m \}$ and compute
$$\langle c_{1}\mathbf{x}_{1}+\cdots+c_{m}\mathbf{x}_{m},  \mathbf{x}_{k} \rangle = \langle 0, \mathbf{x}_{k} \rangle =0 $$
Also, $$\langle c_{1}\mathbf{x}_{1}+\cdots+c_{m}\mathbf{x}c_{m},  \mathbf{x}_{k} \rangle = c_{1}\langle \mathbf{x}_{1},\mathbf{x}_{k} \rangle + c_{2}\langle \mathbf{x}_{2},\mathbf{x}_{k} \rangle + \cdots+  c_{k}\langle \mathbf{x}_{k},\mathbf{x}_{k} \rangle + \cdots +  c_{n}\langle \mathbf{x}_{n},\mathbf{x}_{k} \rangle $$
$$=c_{k}\langle \mathbf{x}_{k},\mathbf{x}_{k} \rangle = c_{k}\lvert \lvert \mathbf{x}_{k} \rvert  \rvert  ^2$$

and this is due to that the set was an orthogonal set.

Since, $$ c_{k}\lvert \lvert \mathbf{x}_{k} \rvert  \rvert  ^2 = 0$$
But, since $\lvert \lvert \mathbf{x}_{k} \rvert \rvert^2 \neq 0$ we are only left with that $c_{k}=0$. And since $c_k$ is arbitrary we have the same for all $c_i$.

###### Exercise
Find a counter example for the other direction, that is write down a linearly independent set which is not orthogonal.

$$\{ \begin{bmatrix}
1 \\
0 \\
\end{bmatrix}, \begin{bmatrix}
-1  \\
1
\end{bmatrix} \}$$

#### Definition of orthogonal subspaces
Let $U_{1}\in \mathbb{R}^n$ and $U_{1}\in \mathbb{R}^n$ be a subspace. Then, $U_{1},U_{2}$ are orthogonal if $\langle \mathbf{u}_{1}, \mathbf{u}_{2} \rangle = 0$ for all $\mathbf{u}_{1}\in U_{1},\mathbf{u}_{2} \in U_{2}$.

We write that $U_{1} \perp U_{2}$ when $U_1$ and $U_2$ are orthogonal subspaces.

###### Exercise
Let $U=\text{span}\{ \begin{bmatrix}1 \\ 1\\ 1\end{bmatrix} \} \subseteq \mathbb{R}^3$. Describe all subspaces of $\mathbb{R}^3$ which are orthogonal to $U$.

Any vector in $U$ can be written as $c \begin{bmatrix}1\\1\\1\end{bmatrix},c\in \mathbb{R}$. We find a vector $\begin{bmatrix}x \\ y \\z\end{bmatrix}$ is orthogonal to $U$ if
$$\langle c \begin{bmatrix}
1\\1\\1
\end{bmatrix},\begin{bmatrix}
x\\y\\z
\end{bmatrix} \rangle =0 \iff x+y+z= 0$$
Then,
$$V=\{ \begin{bmatrix}
x\\y\\z
\end{bmatrix} : x+y+z=0 \} $$
is orthogonal to $U$.

Further notice that any vector in $V$ is in the form, 
$$\begin{bmatrix}
x\\y\\-x-y
\end{bmatrix}=x\begin{bmatrix}
1\\0\\-1
\end{bmatrix}+y\begin{bmatrix}
0\\1\\-1
\end{bmatrix}$$
this shows that the set $$\{ \begin{bmatrix}
1 \\
0 \\
-1
\end{bmatrix}, \begin{bmatrix}
0 \\
1 \\
-1
\end{bmatrix} \}$$ is the basis of $V$ and hence $\text{dim}(V)= 2$.

Also, addition to $V$ any line in $V$ is also orthogonal to $U$, for instance,
$$Y=\text{span}\{ \begin{bmatrix}
2 \\
-1 \\
-1
\end{bmatrix} \}$$
is orthogonal to $U$.

There are different kinds of subspaces that orthogonal to $U$. In $\mathbb{R}^3$, there are planes and lines that are orthogonal.

#### Definition of orthogonal complement
Let $U$ be a subspace, the orthogonal complement of $U$ is $$U^\perp=\{ \mathbf{x}\in \mathbb{R}^n:\langle \mathbf{x},\mathbf{u} \rangle =0,\forall \mathbf{u}\in U \}$$
To illustrate in words, it is the set that contains **all** the vectors $\mathbf{x}$ such that $\mathbf{x}$ is orthogonal to all vectors in $U$. 

#### Theorem
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be a basis of $U \subseteq \mathbb{R}^n$ and let $A=\begin{bmatrix}\mathbf{u}_{1}^T \\ \vdots \\ \mathbf{u}_{m}^T\end{bmatrix}$. Then, $U^\perp=N(A)$.

[Proof]
We use the definition of the basis to see how the infinitely many vectors of $U$ satisfy the above.

We know, for any $\mathbf{u}\in U$, we have
$$\mathbf{u}=c_{1}\mathbf{u}_{1}+\cdots+c_{m}\mathbf{u}_{m}$$
where $c_{1},\cdots,c_{m}\in \mathbb{R}$.

Now we search for all vectors $\mathbf{x}\in \mathbb{R}^n$ such that,
$$\langle \mathbf{x},\mathbf{u} \rangle =c_{1}\langle \mathbf{x},\mathbf{u}_{1} \rangle + \cdots+c_{m}\langle \mathbf{x},\mathbf{u}_{m} \rangle=0  $$
We have to show that both $U^\perp \subseteq N(A)$ and $N(A) \subseteq U^\perp$.

1. $N(A) \subseteq U^\perp$
This is immediate since if $\mathbf{x}\in N(A)$ then we have,
$$A\mathbf{x}=\begin{bmatrix}
\langle \mathbf{x},\mathbf{u}_{1} \rangle \\
\vdots \\
\langle \mathbf{x},\mathbf{u}_{m} \rangle  
\end{bmatrix}=\mathbf{0}\iff \langle  \mathbf{x},\mathbf{u}_{1} \rangle =\cdots=\langle  \mathbf{x},\mathbf{u}_{m} \rangle = 0$$

Then, we have that $\mathbf{x}$ is orthogonal to all $\mathbf{u}\in U$ and so $\mathbf{x} \in U^\perp$.

2. $U^\perp \subseteq N(A)$
Let $\mathbf{x}\in U^\perp$, then $\langle \mathbf{x},\mathbf{u} \rangle$ must be 0 for any choice of $\mathbf{u}\in U$. In particular,
$$\langle \mathbf{x},\mathbf{u}_{1} \rangle =0$$
$$\vdots$$
$$\langle \mathbf{x},\mathbf{u}_{m} \rangle =0$$

because $\mathbf{u}_{i} \in U$ for $i=1,2,\cdots,m$.

Thus, $\mathbf{x}\in N(A)$.

#### Theorem
Let $U \subseteq \mathbb{R}^n$ be a subspace. Then, $$\text{dim}(U) + \text{dim}(U^\perp)=n$$

[Proof]
Let $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ be a basis of $U$. Let us define $A$ as the theorem above. In particular,
$$A=\begin{bmatrix}
\mathbf{u}_{1}^T \\ \vdots \\ \mathbf{u}_{m}^T
\end{bmatrix}$$

Then, because of the theorem above, we know that
$$U^\perp = N(A)$$
Also, we know that
$$U=\text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$$
and $$R(A^T)=\text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$$
because
$$R(A^T) = \{ A^T\mathbf{x}:\mathbf{x}\in \mathbb{R}^m \}=\{ \mathbf{u}_{1}x_{1}+\cdots+\mathbf{u}_{m}x_{m}:\mathbf{x}=\begin{bmatrix}
x_{1} \\
\vdots \\
x_{m}
\end{bmatrix} \in \mathbb{R}^m\}$$

In other words,
$$U=R(A^T)$$
recall the rank-nullity theorem,$$\text{dim}(N(A))+\text{dim}(R(A))=n$$
And,
$$\text{dim}(R(A))=\text{rank}(A)=\text{rank}(A^T)=\text{dim}(R(A^T))$$

Thus,
$$\text{dim}(U^\perp)+\text{dim}(U)=n$$

###### Exercise
Show that $\text{rank}(A)=\text{rank}(A^T)$.

#### Next Lecture [[Lecture 12]]

