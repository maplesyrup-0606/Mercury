In Gram-Schmidt orthogonalization, if we normalize the result of each step, we will get an orthonormalization algorithm. That is, we can define $\mathbf{w}_{i}= \frac{\mathbf{v}_{i}}{\lvert \lvert \mathbf{v}_{i} \rvert \rvert}$ for any $i =1,2,\cdots,m$.

#### Theorem
Let $A\in \mathbb{R}^{m\times n}$ be matrix such that $\text{rank}(A)=n$ and $m \geq n$ (tall matrix). Then there exists an orthogonal matrix $Q$ and an upper triangular matrix $R$ such that
$$A=QR$$
*R is also a tall matrix $R \in \mathbb{R} ^{m \times n}$ since $Q \in \mathbb{R}^{m \times m}$.*

$$A\mathbf{x}=\mathbf{b} \iff QR\mathbf{x}=\mathbf{b} \iff R\mathbf{x}=Q^T\mathbf{b}$$
And this would mean that we would just need to solve using the upper triangular matrix, which is easy.

We get $Q$ and $R$ from Gram-Schmidt.

[Proof]
Let us denote by $a_i$ the columns of $A$:
$$A=\begin{bmatrix}
a_{1} & a_{2} &  \cdots & a_{n}
\end{bmatrix}$$
where $a_{i}\in \mathbb{R}^m$ for $i=1,2,\cdots,n$

Since $\text{rank}(A)=n$, we must have $n$ vectors in a basis of $R(A)$. So $\{ a_{1},\cdots,a_{n} \}$ is a basis of $R(A)$. We can then apply Gram-Schmidt to get an orthonormal basis $w_{1},\cdots,w_{n}$ of $R(A)$.

$$\mathbf{v}_{1}=\mathbf{a}_{1} \to \mathbf{w}_{1}= \frac{\mathbf{v}_{1}}{\lvert \lvert \mathbf{v}_{1} \rvert  \rvert }$$
$$\vdots$$
$$\mathbf{v}_{n}=\mathbf{a}_{n}- \frac{\langle \mathbf{a}_{n},\mathbf{v}_{1} \rangle }{\langle \mathbf{v}_{1}, \mathbf{v}_{1} \rangle }\mathbf{v}_{1}-\cdots- \frac{\langle \mathbf{a}_{n},\mathbf{v}_{n-1} \rangle  }{\langle \mathbf{v}_{n-1},\mathbf{v}_{n-1} \rangle }\mathbf{v}_{n-1} \to \mathbf{w}_{n}=\frac{\mathbf{v}_{n}}{\lvert \lvert \mathbf{v}_{n} \rvert  \rvert }$$

Recall that since $$\text{span}\left\{ a_{1},\cdots,a_{n} \right\}= \text{span}\left\{ v_{1},\cdots,v_{n} \right\} =\text{span}\left\{ w_{1},\cdots,w_{n} \right\}$$

We can have that each $a_{k} \in \text{span}\left\{ w_{1},\cdots,w_{n} \right\}$ by construction for any $k$.

Then, we can use Gram-Schmidt orthonormalization to get $\{ w_{1},\cdots,w_{n} \}$ and then project $a_{1},\cdots,a_{n}$ onto $w_{1},\cdots,w_{n}$:
$$a_{1}=\langle a_{1},w_{1} \rangle w_{1} $$
$$a_{2}=\langle w_{1},a_{2} \rangle w_{1}+\langle w_{2},a_{2} \rangle w_{2}$$
$$\vdots$$
$$a_{n}=\langle w_{1},a_{n} \rangle w_{1}+\langle w_{2},a_{n} \rangle w_{2}+\cdots+\langle w_{n},a_{n} \rangle w_{n}$$

Then, we can write the decomposition
$$A=\begin{bmatrix}
a_{1} & a_{2} & \cdots & a_{n}
\end{bmatrix}=\begin{bmatrix}
w_{1} & w_{2} & \cdots & w_{n}
\end{bmatrix}\begin{bmatrix}
\langle w_{1},a_{1} \rangle & \langle w_{1},a_{2} \rangle  &\cdots & \langle w_{1},a_{n} \rangle \\
0 & \langle w_{2},a_{2} \rangle & \cdots & \langle w_{2},a_{n} \rangle  \\
\vdots &  &  &  \\
0 & 0 & \cdots & \langle w_{n},a_{n} \rangle
\end{bmatrix}=Q_{1}R_{1}$$

This is the thin QR decomposition of A:
1. Columns of $Q_1$ form an orthonormal basis of $R(A)$.
2. $R_{1} \in \mathbb{R}^{n\times n}$ is a square matrix.

To get the full QR decomposition, we find $w_{n+1},\cdots,w_{m}$ as any orthonormal basis of $R(A)^\perp$. Finding a basis of $R(A)^\perp$ amounts to finding a basis of $N(A^T)$. Then, we have to perform Gram-Schmidt orthonormalization to get an orthonormal basis.

Then, we have $A=QR$ with
$$Q=\begin{bmatrix}
w_{1} & \cdots & w_{n} & w_{n+1} & \cdots & w_{m}
\end{bmatrix}$$
and
$$R=\begin{bmatrix}
\langle w_{1},a_{1} \rangle & \langle w_{1},a_{2} \rangle & \cdots & 
\langle w_{1},a_{n} \rangle \\
0 & \langle w_{2},a_{2} \rangle & \cdots & \langle w_{2},a_{n} \rangle \\
\vdots &  &  &  \\
0 & 0 & \cdots & \langle w_{n},a_{n} \rangle \\
0 & 0 & \cdots & 0 \\
\vdots &  &  &  \\
0 & 0 & \cdots & 0
\end{bmatrix}$$

Let $Q_2$ contain the orthonormal basis of $R(A)^\perp$:
$$Q_{2}=\begin{bmatrix}
w_{n+1} & \cdots & w_{m}
\end{bmatrix}$$

With this notation, we can write the QR decomposition as
$$A=QR \text{ where }Q=\begin{bmatrix}
Q_{1} & Q_{2}
\end{bmatrix}\begin{bmatrix}
R_{1} \\
0
\end{bmatrix}$$

[Normally thin is used for calculations and full is used for proofs.]

#### Theorem
Let $U=R(A)\subseteq \mathbb{R}^m$ where $A\in \mathbb{R}^{m\times n}$ and $\text{rank}(A)=n$. Let $A=Q_{1}R_{1}$ be the thin QR decomposition. Then,
$$\text{proj}_{R(A)}(x)=Q_{1}Q_{1}^Tx$$
$$\text{proj}_{R(A)^\perp}(x)=Q_{2}Q_{2}^Tx$$
for any $x \in \mathbb{R}^m$.

[Proof]
$$Q_{1}Q_{1}^Tx=\begin{bmatrix}
w_{1} & \cdots & w_{n}
\end{bmatrix}\begin{bmatrix}
w_{1}^T \\
\vdots \\
w_{n}^T
\end{bmatrix}x$$
$$=\begin{bmatrix}
w_{1} & \cdots & w_{n}
\end{bmatrix}\begin{bmatrix}
\langle w_{1},x \rangle  \\
\vdots \\
\langle w_{n},x \rangle 
\end{bmatrix}$$
$$=\text{proj}_{U}(x)=\text{proj}_{R(A)}(x)$$
since $w_{1},\cdots,w_{n}$ is an orthonormal basis of $U$.

We can also show that $\text{proj}_{U^\perp}(x)=Q_{2}Q_{2}^Tx$

$$Q_{2}Q_{2}^Tx=\begin{bmatrix}
w_{n+1} & w_{n+2} & \cdots & w_{m}
\end{bmatrix}\begin{bmatrix}
w_{n+1}^T \\
\vdots \\
w_{m}^T
\end{bmatrix}x=\begin{bmatrix}
w_{n+1} & w_{n+2} & \cdots & w_{m}
\end{bmatrix}\begin{bmatrix}
 \langle w_{n+1}^T,x \rangle  \\
\vdots \\
\langle w_{m}^T,x \rangle 
\end{bmatrix}=\text{proj}_{U^\perp}(x)$$

###### Example
Let
$$A=\begin{bmatrix}
1 & -1 \\
1 & 2  \\
1 & 1
\end{bmatrix}$$
Find the QR decomposition and projection of $x=\begin{bmatrix}2&1&1 \end{bmatrix}^T$ onto $R(A)$.

First, let’s set up an orthonormal basis by G-S. This gives,
$$v_{1}=a_{1},v_{2}=a_{2}- \frac{\langle v_{1},a_{2} \rangle }{\langle v_{1},v_{1} \rangle }v_{1}$$
$$\to v_{1}=\begin{bmatrix}
1  \\
1 \\
1
\end{bmatrix},v_{2}=\begin{bmatrix}
-1 \\
2 \\
1
\end{bmatrix}-\frac{2}{3}\begin{bmatrix}
1  \\
1 \\
1
\end{bmatrix}=\begin{bmatrix}
-\frac{5}{3} \\
\frac{4}{3} \\
\frac{1}{3}
\end{bmatrix}$$

We normalize to get,
$$w_{1}=\frac{1}{\sqrt{ 3 }}\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix},w_{2}= \frac{1}{\sqrt{ 42 }} \begin{bmatrix}
-5\\4\\1
\end{bmatrix}$$

Hence, we have
$$Q_{1}=\begin{bmatrix}
\frac{1}{\sqrt{ 3 }} & -\frac{5}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{4}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 42 }}
\end{bmatrix}$$

We now need $Q_2$. That is, the orthonormal basis of $R(A)^\perp=N(A^T)$ which gives
$$w_{3}=\frac{1}{\sqrt{ 14 }}\begin{bmatrix}
-1\\-2\\3
\end{bmatrix}=Q_{2}$$

Next, we need $R_1$:
$$R_{1}=\begin{bmatrix}
\langle w_{1},a_{1} \rangle & \langle w_{1},a_{2} \rangle \\
0 & \langle w_{2},a_{2} \rangle 
\end{bmatrix}=\begin{bmatrix}
\sqrt{ 3 } & \frac{2}{\sqrt{ 3 }} \\
0 & \frac{14}{\sqrt{ 42 }}
\end{bmatrix}$$

We now have the full QR decomposition by padding below $R_1$.
$$A=QR=\begin{bmatrix}
\frac{1}{\sqrt{ 3 }} & -\frac{5}{\sqrt{ 42 }} & -\frac{1}{\sqrt{ 14 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{4}{\sqrt{ 42 }}  & -\frac{2}{\sqrt{ 14 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 42 }}  & \frac{3}{\sqrt{ 14 }}
\end{bmatrix}\begin{bmatrix}
\sqrt{ 3 } & \frac{2}{\sqrt{ 3 }} \\
0 & \frac{14}{\sqrt{ 42 }} \\
0 & 0
\end{bmatrix}$$

Finally, we find the projection of $x$ onto $R(A)$:
$$\text{proj}_{R(A)}(x)=Q_{1}Q_{1}^Tx=\begin{bmatrix}
\frac{1}{\sqrt{ 3 }} & -\frac{5}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{4}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 42 }}
\end{bmatrix}\begin{bmatrix}
\frac{1}{\sqrt{ 3 }} &\frac{1}{\sqrt{ 3 }} &\frac{1}{\sqrt{ 3 }}  \\
  -\frac{5}{\sqrt{ 42 }} & \frac{4}{\sqrt{ 42 }} & \frac{1}{\sqrt{ 42 }}

\end{bmatrix}\begin{bmatrix}
2 \\
1 \\
1
\end{bmatrix}$$
$$=\begin{bmatrix}
\frac{1}{\sqrt{ 3 }} & -\frac{5}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{4}{\sqrt{ 42 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 42 }}
\end{bmatrix}\begin{bmatrix}
\frac{4}{\sqrt{ 3 }} \\ -\frac{5}{\sqrt{ 42 }}
\end{bmatrix} = \begin{bmatrix}
\frac{4}{3}+\frac{25}{42} \\ \frac{4}{3}-\frac{20}{42} \\ \frac{4}{3} -\frac{5}{42} 
\end{bmatrix}=\begin{bmatrix}
\frac{81}{42} \\ \frac{36}{42} \\ \frac{51}{42}
\end{bmatrix}= \frac{1}{14} \begin{bmatrix}
27 \\ 12 \\ 17
\end{bmatrix}$$

###### Exercise
Show that $N(A^T)=N(Q_{1}^T)$.

[Proof]
$$A=\begin{bmatrix}
Q_{1} & Q_{2}
\end{bmatrix}\begin{bmatrix}
R_{1} \\
0
\end{bmatrix}$$
Then,
$$A^T=\begin{bmatrix}
R_{1}^T & 0
\end{bmatrix}\begin{bmatrix}
Q_{1}^T \\
Q_{2}^T
\end{bmatrix}$$

Assume (for now?) that $A=Q_{1}R_{1}$,
Then,
$$A^T = R_{1}^TQ_{1}^T $$

Let $x \in \mathbb{R}^m$ and assume $x \in N(A^T)$ a.k.a $A^Tx=0$
We know that $R_{1}^T$ is invertible, hence $(R_{1}^T)^{-1}A^T=Q_{1}^T$.
$$(R_{1}^T)^{-1}A^Tx=(R_{1}^T)^{-1}0=0=Q_{1}^Tx \to x \in N(Q_{1}^T)$$

Now assume that $x \in N(Q_{1}^T)$,
$$A^Tx=R_{1}^TQ_{1}^Tx=R_{1}^TQ_{1}^Tx=0 \to x \in N(A^T)$$

$$\left( N(A^T) \subseteq N(Q_{1}^T)  \right)\cap \left(N(Q_{1}^T) \subseteq N(A^T)  \right) \to \hspace{.1in} \therefore N(A^T)=N(Q_{1}^T)$$
#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 18]]
