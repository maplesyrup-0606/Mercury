For a given vector $x \in \mathbb{R}^n$ and subspaces $U,U^\perp \subseteq \mathbb{R}^n$, we have a unique presentation as the following:
$$\mathbf{x}=\mathbf{u}+\mathbf{v}, \mathbf{u}\in U,\mathbf{v}\in U^\perp$$

Let’s assume that there are two distinct decompositions,
$$\mathbf{x}=\mathbf{u}+\mathbf{v}=\mathbf{u}'+\mathbf{v}':\mathbf{u},\mathbf{u}'\in U,\mathbf{v},\mathbf{v}'\in U^\perp$$

By arrangement we get the equality,
$$\mathbf{u}-\mathbf{u}'=\mathbf{v}'-\mathbf{v}$$
Since, $\mathbf{u}-\mathbf{u}'\in U$ and $\mathbf{v}-\mathbf{v}'\in U^\perp$, both sides are orthogonal to each other. In order for this to be satisfied, both sides have to be 0 :
$$\mathbf{u}=\mathbf{u}',\mathbf{v}=\mathbf{v}'$$

Thus, both decompositions are not distinct.

#### Definition of fundamental subspaces
Let us given the matrix $A$ such that $A \in \mathbb{R}^{m\times n}$. The fundamental subspaces are,
$$N(A),R(A),N(A^T),R(A^T)$$
And these subspaces live in,
$$N(A)\subseteq \mathbb{R}^n,R(A)\subseteq \mathbb{R}^m,R(A^T)\subseteq \mathbb{R}^n,N(A^T)\subseteq \mathbb{R}^m$$

#### Theorem
Given the matrix $A \in \mathbb{R}^{m\times n}$ we have that,
$$N(A)=R(A^T)^\perp,R(A)=N(A^T)^\perp$$

[Proof]
Let us denote the rows of $A$ by using vectors $\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}$ where $\mathbf{u}_{i}\in R^n$ for any $i = 1,\cdots,m$. Since $\mathbf{u}_{i}$ are column vectors by our convention, we have the representations
$$A=\begin{bmatrix}
\mathbf{u}_{1}^T \\
\vdots \\
\mathbf{u}_{m}^T
\end{bmatrix},A^T=\begin{bmatrix}
\vert & \cdots & \vert \\
\mathbf{u}_{1} & \cdots & \mathbf{u}_{m} \\
\vert & \cdots & \vert
\end{bmatrix}$$

First, notice that $$U=R(A^T)$$
by definition. $R(A^T)$ is the set of all linear combinations of columns of $A^T$ which are vectors $\mathbf{u}_{1},\cdots,\mathbf{u}_{m}$. 

At the same time, we have that $$U^\perp = N(A)$$
Then, $N(A) = R(A^T)^\perp$ is claimed.

Another way to see this is
$$A\mathbf{x} =0 \iff \begin{bmatrix}
\langle \mathbf{x},\mathbf{u}_{1} \rangle  \\
\vdots \\
\langle \mathbf{x},\mathbf{u}_{m} \rangle 
\end{bmatrix}=0 \iff x \in \text{span}\{ \mathbf{u}_{1},\cdots,\mathbf{u}_{m} \}^\perp \iff x \in R(A^T)^\perp$$
Also,
$$N(A^T)=R(A)^\perp \iff N(A^T)^\perp=R(A)$$

since $(V^\perp)^\perp = V$, the above is asserted.
###### Exercise
Prove that $(V^\perp)^\perp = V$

[Proof]
Let $V=\text{span}\left\{ \mathbf{v}_{1}, \cdots, \mathbf{v}_{n} \right\}$. Then, $\forall \mathbf{v'} \in V^\perp, \forall \mathbf{v}\in V$ we have that $\langle \mathbf{v},\mathbf{v}' \rangle=0$.
In other words, all vectors in $V$ are orthogonal to all vectors in $V^\perp$. 
Thus, $(V^\perp)^\perp = V$.

###### Exercise
Suppose that $A=LU$ such that
$$L=\begin{bmatrix}
1 & 0 & 0 \\
* & 1 & 0 \\
* & * & 1
\end{bmatrix},U=\begin{bmatrix}
a & * & * & * & * \\
0 & 0 & b & * & * \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}$$

Find the dimensions of the fundamental subspaces.

Since there are two pivots in $U$, we see that there are two linearly independent columns in$U$ and also in $A$. Since the range of $A$ is the span of the columns and that there are 2 linearly independent columns, we get that $$\text{dim}(R(A)) = 2$$
Since there are three columns in $U$ without pivots, we have three free variables leading to$$\text{dim}(N(A))=3$$
Then,
$$\text{dim}(N(A^T))=\text{dim}(R(A)^\perp)=3-\text{dim}(R(A))=1$$
$$\text{dim}(R(A^T))=\text{dim}(N(A)^\perp)=5-\text{dim}(N(A))=2$$


###### Exercise
Find the fundamental subspaces for 
$$A=\begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix}\begin{bmatrix}
2 & 3 & 1 & 4 \\
0 & -1 & 0 & 1 \\
0 & 0 & -2 & 2
\end{bmatrix}$$

According to one of the theorems we learned, since there are three pivots in $U$, we pick the first three columns of $L$ and they form a basis for $R(A)$, that is
$$R(A)=\text{span}\{ \begin{bmatrix}
1 \\
1 \\
0
\end{bmatrix}, \begin{bmatrix}
0 \\
1 \\
-2
\end{bmatrix}, \begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}\}$$

since $\text{dim}(R(A))=3$ and that $R(A)\subseteq \mathbb{R}^3$, we actually have that $R(A)=\mathbb{R}^3$. As a result, we have alternative choices of basis, such as
$$\{ \begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix} ,\begin{bmatrix}
0  \\
1 \\
0 
\end{bmatrix},\begin{bmatrix}
0  \\
0 \\
1
\end{bmatrix} \}$$

We can easily get $N(A^T)$ easily since
$$N(A^T)=(R(A))^\perp \iff N(A^T)=\{ \mathbf{0} \}$$

Next, we find $N(A)$. We have to find all $\mathbf{x}$ such that $U\mathbf{x}=0$ since $L$ is invertible. This gives us,
$$N(A)=\text{span}\{ \begin{bmatrix}
-4 \\
1 \\
1 \\
1 
\end{bmatrix} \}$$

Finally, we have that
$$R(A^T)=(N(A))^\perp$$

That is, we want to find all $\mathbf{x}\in \mathbb{R}^4$ such that $\mathbf{x}$ is orthogonal to all vectors in $N(A)$. All vectors in $N(A)$ are characterized as $c \begin{bmatrix}-4\\1\\1\\1\end{bmatrix}$ for any $c \in \mathbb{R}$. Then we solve,
$$\langle \begin{bmatrix}
-4 \\
1 \\
1 \\
1
\end{bmatrix},\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_4
\end{bmatrix} \rangle = 0 $$


Which is essentially solving the linear system,
$$\begin{bmatrix}
-4 & 1 & 1 & 1
\end{bmatrix}\begin{bmatrix}
x_{1}  \\
x_{2} \\
x_{3} \\
x_{4}
\end{bmatrix} = \mathbf{0}$$

As a result we obtain,
$$R(A^T)=\text{span}\left\{  \begin{bmatrix}
\frac{1}{4} \\
1 \\
0 \\
0 \\

\end{bmatrix} , \begin{bmatrix}
\frac{1}{4} \\

0 \\ 1 \\
0 \\

\end{bmatrix} , \begin{bmatrix}
\frac{1}{4} \\

0 \\
0 \\1 \\

\end{bmatrix}  \right\}$$


#### Definition of projection
The projection of $\mathbf{x}\in \mathbb{R}^n$ onto $\mathbf{u}\in \mathbb{R}^n$ is
$$\text{proj}_{\mathbf{u}}(x)=\frac{\langle \mathbf{x},\mathbf{u} \rangle }{\langle \mathbf{u},\mathbf{u} \rangle } \mathbf{u}$$

1.  We have $\text{proj}_{\mathbf{u}}(\mathbf{x})=c \mathbf{u}$ for some $c \in \mathbb{R}$, that is the projection is the span of $\mathbf{u}$.
2. We have that $\mathbf{x}-\text{proj}_{\mathbf{u}}(\mathbf{x})$ is orthogonal to $\mathbf{u}$. This results in $$\langle \mathbf{x}-c \mathbf{u},\mathbf{u} \rangle=0 \iff \langle \mathbf{x},\mathbf{u} \rangle - c \langle \mathbf{u},\mathbf{u} \rangle \iff c = \frac{\langle \mathbf{x},\mathbf{u} \rangle }{\langle \mathbf{u},\mathbf{u} \rangle }  $$


We can write the projection as matrix multiplication,
$$\text{proj}_{\mathbf{u}}(x)=\frac{\langle \mathbf{x},\mathbf{u} \rangle }{\langle \mathbf{u},\mathbf{u} \rangle } \mathbf{u} =\frac{1}{\langle \mathbf{u},\mathbf{u} \rangle }\mathbf{u\langle \mathbf{u,\mathbf{x}} \rangle }=\frac{1}{\langle \mathbf{u},\mathbf{u} \rangle} \mathbf{u}(\mathbf{u}^T\mathbf{x})=P\mathbf{x} $$
where $P$ is so-called the outer product of $\mathbf{u}$. 

$$P=\frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^2 }\begin{bmatrix}
u_{1}^2 & u_{1}u_{2} & \cdots & u_{1}u_{n} \\
u_{2}u_{1} & u_{2}^2 & \cdots & u_{2}u_{n} \\
\vdots \\
u_{n}u_{1} & u_{n}u_{2} & \cdots & u_{n}^2
\end{bmatrix}$$

#### Theorem
Let $P$ be as defined above, then we have,
1. $P^2=P$
2. $P^T = P$
3. $\text{rank}(P)=1$

###### Exercise
1.
$$P^2=PP= \frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^4 }\begin{bmatrix}
(u_{1}^4+u_{1}^2u_{2}^2+\cdots+u_{1}^2u_{n}^2) & \cdots & (u_{1}^3u_{n}+u_{1}u_{2}^2u_{n}+\cdots+u_{1}u_{n}^3) \\
\vdots &  & \vdots \\
(u_{n}u_{1}^3+u_{1}u_{2}^2u_{n}+\cdots+u_{1}u_{n}^3) & \cdots & (u_{1}^2u_{n}^2+u_{2}^2u_{n}^2+\cdots+u_{n}^4)
\end{bmatrix}$$
$$=\frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^4 }\begin{bmatrix}
u_{1}^2\lvert \lvert \mathbf{u} \rvert  \rvert ^2 & \cdots & u_{1}u_{n}\lvert \lvert \mathbf{u} \rvert  \rvert ^2 \\
\vdots &  & \vdots \\
u_{1}u_{n}\lvert \lvert \mathbf{u} \rvert  \rvert ^2 & \cdots & u_{n}^2\lvert \lvert \mathbf{u} \rvert  \rvert ^2
\end{bmatrix}=\frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^2 }\begin{bmatrix}
u_{1}^2 & u_{1}u_{2} & \cdots & u_{1}u_{n} \\
u_{2}u_{1} & u_{2}^2 & \cdots & u_{2}u_{n} \\
\vdots \\
u_{n}u_{1} & u_{n}u_{2} & \cdots & u_{n}^2
\end{bmatrix}=P$$

2.
$$P^T=\frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^2 }\begin{bmatrix}
u_{1}^2 & u_{1}u_{2} & \cdots & u_{1}u_{n} \\
u_{2}u_{1} & u_{2}^2 & \cdots & u_{2}u_{n} \\
\vdots \\
u_{n}u_{1} & u_{n}u_{2} & \cdots & u_{n}^2
\end{bmatrix}^T=P$$

3.
$$P=\frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert^2 }\begin{bmatrix}
u_{1}^2 & u_{1}u_{2} & \cdots & u_{1}u_{n} \\
u_{2}u_{1} & u_{2}^2 & \cdots & u_{2}u_{n} \\
\vdots \\
u_{n}u_{1} & u_{n}u_{2} & \cdots & u_{n}^2
\end{bmatrix}$$

If we subtract each row such as the following:
$$R_{k} \leftarrow R_{k}-R_{1}\times \frac{u_{k}}{u_{1}}$$
We have all zeros in all the rows below the first row.
$$P'= \frac{1}{\lvert \lvert \mathbf{u} \rvert  \rvert ^2}\begin{bmatrix}
u_{1}^2 & u_{1}u_{2} & \cdots & u_{1}u_{n} \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots &  & \vdots \\
0 & 0 & \cdots & 0
\end{bmatrix}$$
$$\therefore \text{rank}(P)=1$$
#### Next Lecture [[Lecture 13]]
