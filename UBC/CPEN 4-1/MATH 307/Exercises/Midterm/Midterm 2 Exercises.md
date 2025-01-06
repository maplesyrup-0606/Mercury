#### Exercise 1
Determine whether or not the set 
$$U=\left\{ \begin{bmatrix}
a\\ b \\ c
\end{bmatrix}:abc=0 \right\}$$
is a subspace.

[Solution]
First, let’s check if the origin is included.
$$\begin{bmatrix}
0\\0\\0
\end{bmatrix}\to 0\times 0\times 0 = 0$$
✅

Second, we check additivity. Let $$x_{1}=\begin{bmatrix}
a_{1}\\ b_{1}\\ c_{1}
\end{bmatrix},x_{2}=\begin{bmatrix}
a_{2}\\ b_{2}\\ c_{2}
\end{bmatrix}$$

Then, $a_{1}b_{1}c_{1}=0$ and $a_{2}b_{2}c_{2}=0$. 
$$x_{1}+x_{2}=\begin{bmatrix}
a_{1}+a_{2} \\ b_{1} + b_{2} \\ c_{1} + c_{2}
\end{bmatrix}$$
$$(a_{1}+a_{2})(b_{1}+b_{2})(c_{1}+c_{2})=(a_{1}b_{1}+a_{2}b_{1}+a_{1}b_{2}+a_{2}b_{2})(c_{1}+c_{2})$$
$$=a_{1}b_{1}c_{1}+a_{2}b_{1}c_{1}+a_{1}b_{2}c_{1}+a_{2}b_{2}c_{1}+a_{1}b_{1}c_{2}+a_{2}b_{1}c_{2}+a_{1}b_{2}c_{2}+a_{2}b_{2}c_{2}$$
$$=a_{2}b_{1}c_{1}+a_{1}b_{2}c_{1}+a_{2}b_{2}c_{1}+a_{1}b_{1}c_{2}+a_{2}b_{1}c_{2}+a_{1}b_{2}c_{2}$$
And this may not be zero for all cases.

==Hence, it is not a subspace.==

#### Exercise 2 
Determine whether $\text{span}\left\{ u_{1},u_{2} \right\}=\text{span}\left\{ u_{3},u_{4} \right\}$ where
$$u_{1}=\begin{bmatrix}
2\\-3\\1\\-1
\end{bmatrix},u_{2}=\begin{bmatrix}
-5\\1\\2\\-2
\end{bmatrix},u_{3}=\begin{bmatrix}
-1\\-5\\4\\-4
\end{bmatrix},u_{4}=\begin{bmatrix}
3\\-11\\6\\-10
\end{bmatrix}$$

$u_{1},u_{2},u_{4}$ are linearly independent, but $u_{3}=2u_{1}+u_{2}$ so $\text{span}\left\{ u_{1},u_{2} \right\}\neq \text{span}\left\{ u_{3},u_{4} \right\}$


#### Exercise 3
Let $U=\text{span}\left\{ u_{1},u_{2},u_{3},u_{4} \right\} \subseteq \mathbb{R}^4$ where
$$u_{1}=\begin{bmatrix}
2\\4\\4\\2
\end{bmatrix},u_{2}=\begin{bmatrix}
3 \\
5 \\
3 \\
1
\end{bmatrix},u_{3}=\begin{bmatrix}
3 \\
3 \\
-1 \\
-11
\end{bmatrix},u_{4}=\begin{bmatrix}
0 \\
3 \\
11 \\
-2
\end{bmatrix}$$

- Find a basis and the dimension of $U$.
- Is $\{ u_{1},u_{3},u_{4} \}$ a basis of $U$?

Let’s see if the vectors are linearly independent. Thus, compute for $Ax=0$ where $A=\begin{bmatrix}u_{1} & u_{2} & u_{3} & u_{4} \end{bmatrix}$.

$$ \begin{bmatrix}
A & | & 0
\end{bmatrix} =\begin{bmatrix}
2 & 3 & 3 & 0 \\
4 & 5 & 3 & 3 \\
4 & 3 & -1 & 11 \\
2 & 1 & -11 & -2
\end{bmatrix}$$
$$\to \begin{bmatrix}
2 & 3 & 3 & 0 \\
0 & -1 & -3 & 3 \\
0 & -3 & -7 & 11 \\
0 & -2 & -14 & -2
\end{bmatrix}\to \begin{bmatrix}
2 & 3 & 3 & 0 \\
0 & -1 & -3 & 3 \\
0 & 0 & 2 & 2 \\
0 & 0 & -8 & -8
\end{bmatrix}\to \begin{bmatrix}
2 & 3 & 3 & 0 \\
0 & -1 & -3 & 3 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

Since there are 3 pivots we can say that the basis of $U$ is $\{ u_{1},u_{2},u_{3} \}$ thus giving $\text{dim}(U)=3$.

We can also say that $\{ u_{1},u_{3},u_{4} \}$ is a basis of $U$.

#### Exercise 4
Let $A=LU$ be the LU decomposition of $A$. Determine whether the statement is **True** or **False**.

- $N(A)=N(U)$
Since $U$ is the ref form of $A$, they have the same solution set. Therefore, $N(A)=N(U)$.
**True**

- $\text{dim}(N(A))=\text{dim}(N(U))$
Since we said that from above $N(A)=N(U)$, they should be equal.

- $R(A)=R(U)$
Since $L$ is invertible,
$$A=LU$$
$$\text{let } y \in R(A) \to \exists x \text{ s.t. }Ax=y  $$
$$LUx=y \to w=Ux \to Lw=y$$
$$\therefore y \in R(L)$$
$$\text{let } y \in R(L) \to \exists w \text{ s.t. } Lw=y$$
$$\text{let } x=U^{-1}w \to Ax= LUx=LU(U^{-1}w)=Lw=y$$
$$y\in R(A)$$

$$(R(A) \subseteq R(L) )\cap (R(L) \subseteq R(A)) \to \therefore R(L)=R(A)$$

**False**

- $\text{dim}(R(A))=\text{dim}(R(U))$
Since both $A,U$ have the same number of pivot columns we can say that $\text{rank}(A)=\text{rank}(U)$.
$$\text{rank}(A)=\text{rank}(U)\to \text{dim}(R(A))=\text{dim}(R(U))$$
**True**

#### Exercise 5
Let $A$ be a matrix such that its LU decomposition is of the form
$$A=LU=\begin{bmatrix}
1 & 0 & 0 \\
*  & 1 & 0 \\
* & * & 1
\end{bmatrix}\begin{bmatrix}
* & * & * & * \\
0 & * & * & * \\
0 & 0 & * & *
\end{bmatrix}$$
where * denotes a non-zero number. Find the dimension of each subspace $N(A),R(A),N(A^T),R(A^T)$.

$$N(A) = N(U) \to \text{dim}(N(A))=\text{dim}(N(U))=1$$
$$\text{dim}(R(A))=\text{dim}(R(U))=3$$
$$\text{dim}(N(A^T))=\text{dim}(R(A)^\perp)= 3-\text{dim}(R(A))=3-3=0$$
$$\text{dim}(R(A)^T)=\text{dim}(N(A)^\perp)=4-\text{dim}(N(A))=4-1=3$$

#### Exercise 6
Determine whether the statement is **True** or **False**.

- Let $U\subseteq \mathbb{R}^n$ be a subspace. If $u\in \mathbb{R}^n$ such that $u\neq {0}$ then either $u \in U$ or $u \in U^\perp$.
**False**, let
$$U=\text{span}\left\{ \begin{bmatrix}
1\\ 0
\end{bmatrix} \right\},U^\perp=\text{span}\left\{ \begin{bmatrix}
0 \\
1
\end{bmatrix} \right\}$$
Then $u=\begin{bmatrix}1\\1\end{bmatrix}$ is neither in $U$ nor $U^\perp$.

- Let $L_{1} \subset \mathbb{R}^2$ be a line through the origin. There is a unique line $L_{2} \subset \mathbb{R}^2$ through the origin such that $L_{1} \perp L_{2}$.

**True**, Since $\text{dim}(L_{1})+\text{dim}(L_{1}^\perp)=2$ and $\text{dim}(L_{1})=1$ we have that $\text{dim}(L_{2})=1$, hence there is a unique line passing through the origin so that they are orthogonal.

- Let $L_{1} \subset \mathbb{R}^3$ be a line through the origin. There is a unique line $L_{2} \subset \mathbb{R}^3$ through the origin such that $L_{1} \perp L_{2}$.

**False**, $\text{dim}(L_{1})=1$ then in order to be unique $\text{dim}(L_{2})=3-1=2$ but if $L_{2}$ is a line through the origin, its dimension should be 1.

- Let $U_{1} \subset \mathbb{R}^4$ be a 2-dimensional subspace. There is a unique 2-dimensional subspace $U_{2} \subset \mathbb{R}^4$ through the origin such that $U_{1} \perp U_{2}$.

**True**,
$$4=\text{dim}(U)+\text{dim}(U^\perp)=2+2$$
hence, there should be a unique $U_{2}$ such that $U_{2}=U^\perp$.

#### Exercise 7
Let $A=LU$ be the LU decomposition of $A$. Determine whether the statement is **True** or **False**.

- $N(A^T)=N(U^T)$
$$A^T=U^TL^T$$
Then, now we have to different upper and lower triangle matrices. Then, $A^T$ and $L^T$ have the same solution set, thus 
$$N(A^T)=N(L^T)$$
**False**

- $R(A^T)=R(U^T)$

$$A^T=U^TL^T$$
$$\text{let }y \in R(A^T)\to \exists x \text{ s.t. } A^Tx=y \to U^TL^Tx=y$$
$$\text{let }w=L^Tx\to U^Tw=U^TL^Tx=y$$
$$\therefore y \in R(U^T)$$

$$\text{let }y \in R(U^T) \to \exists w \text{ s.t. }U^Tw=y$$
$$\text{let }x=(L^T)^{-1}w \to A^Tx=U^TL^Tx=U^TL^T(L^T)^{-1}w=U^Tw=y$$
$$\therefore y \in R(A^T)$$

$$(R(U^T)\subseteq R(A^T)) \cap (R(A^T) \subseteq R(U^T)) \to \therefore R(A^T)=R(U^T)$$
**True**

#### Exercise 8
Determine whether the statement is **True** or **False**.

- If $A^TA$ is a diagonal matrix, then the columns of $A$ are orthogonal.

Assume that $A$’s columns are orthogonal, $A=\begin{bmatrix}\vert & \cdots & \vert \\ a_{1} & \cdots & a_{n} \\ \vert & \cdots & \vert\end{bmatrix}$

$$A^TA=\begin{bmatrix}
- & a_{1} &  - \\
 & \vdots &  \\
- & a_{n} & - 
\end{bmatrix}\begin{bmatrix}
\vert & \cdots & \vert \\
a_{1} & \cdots & a_{n} \\
\vert & \cdots & \vert
\end{bmatrix} = \begin{bmatrix}
\langle a_{1},a_{1} \rangle  & \cdots & \langle a_{1},a_{n} \rangle \\
\langle a_{2},a_{1} \rangle  & \cdots & \langle a_{2},a_{n} \rangle \\
\vdots &  & \vdots \\
\langle a_{n},a_{1} \rangle & \cdots & \langle a_{n},a_{n} \rangle
\end{bmatrix}$$
$$\to \begin{bmatrix}
\langle a_{1},a_{1} \rangle & 0 & 0 & \cdots & 0 \\
0 & \langle a_{2},a_{2} \rangle & 0 & \cdots & 0 \\
\vdots \\
0 & 0 & 0 & \cdots & \langle a_{n},a_{n} \rangle
\end{bmatrix}$$
**True**

- If $AA^T$ is a diagonal matrix, then the columns of $A$ are orthogonal.

Assume that $A$’s columns are orthogonal, $A=\begin{bmatrix}\vert & \cdots & \vert \\ a_{1} & \cdots & a_{n} \\ \vert & \cdots & \vert\end{bmatrix}$

$$AA^T=\begin{bmatrix}
\vert & \cdots & \vert \\
a_{1} & \cdots & a_{n} \\
\vert & \cdots & \vert
\end{bmatrix} \begin{bmatrix}
- & a_{1} &  - \\
 & \vdots &  \\
- & a_{n} & - 
\end{bmatrix}$$
Then the columns are not orthogonal, rather the rows are.
**False**

- If $A^TA$ is a diagonal matrix, then the rows of $A$ are orthogonal.
**False**, we showed that the columns are.

- If $AA^T$ is a diagonal matrix, then the rows of $A$ are orthogonal.
$$A=\begin{bmatrix}
 & a_{1} &  \\
 & \vdots &  \\
 & a_{n} & 
\end{bmatrix}$$
$$AA^T=\begin{bmatrix}
 & a_{1} &  \\
 & \vdots &  \\
 & a_{n} & 
\end{bmatrix}\begin{bmatrix}
\vert &  & \vert \\
a_{1} & \cdots & a_{n} \\
\vert &  & \vert
\end{bmatrix}=\begin{bmatrix}
\langle a_{1},a_{1} \rangle & \langle a_{1},a_{2} \rangle  & \cdots & \langle a_{1},a_{n} \rangle \\
\langle a_{2},a_{1} \rangle & \langle a_{2},a_{2} \rangle & \cdots & \langle a_{2},a_{n} \rangle \\
\vdots \\
\langle a_{n},a_{1} \rangle & \langle a_{n},a_{2} \rangle  & \cdots & \langle a_{n},a_{n} \rangle
\end{bmatrix}$$
$$=\begin{bmatrix}
\langle a_{1},a_{1} \rangle  & 0 & \cdots & 0 \\
0 & \langle a_{2},a_{2} \rangle & \cdots & 0 \\
\vdots \\
0 & 0 & \cdots & \langle a_{n},a_{n} \rangle
\end{bmatrix}$$

**True**

#### Exercise 9
Determine whether the statement is **True** or **False**.

Let $u_{1},u_{2},u_{3}\in \mathbb{R}^3$ be non-zero vectors. If $u_{1}$ is orthogonal to $u_{2}$, and $u_{2}$ is orthogonal to $u_{3}$, then $u_{1}$ is orthogonal to $u_{3}$.

For instance, let 
$$u_{1}=\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix},u_{2}=\begin{bmatrix}
0  \\
1 \\
0
\end{bmatrix},u_{3}=\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}$$

Then, 
$$\langle u_{1},u_{2} \rangle =0,\langle u_{2},u_{3} \rangle =0$$
But,
$$\langle u_{1},u_{3} \rangle=1 $$
**False**

#### Exercise 10
Let $A$ be a $m \times n$ matrix and let $\{ u_{1},u_{2} \} \subset \mathbb{R}^n$ be a basis of the nullspace $N(A)$. 
Determine $\text{dim}(R(A^T))$ and $\text{dim}(N(A^T))$.

$$\text{dim}(R(A^T))=\text{dim}(N(A)^\perp)=n-\text{dim}(N(A))=n - 2$$
$$\text{dim}(R(A^T))+\text{dim}(N(A^T)) = m \to \text{dim}(N(A^T)) = m-(n-2)=m-n+2$$

#### Exercise 11
Let $A$ be a $4\times 4$ matrix such that
$$A=LU=\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
0 & 2 & 1 & 1
\end{bmatrix}\begin{bmatrix}
1 & -1 & 2 & -1 \\
0 & 1 & -3 & 4 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

Find a basis of $N(A^T)$ and find a basis of $R(A^T)$.

$$N(A^T) = R(A)^\perp$$

Now use the fact that since we have $\text{rank}(A)=3$ the first $3$ columns of $L$ form the basis of $R(A)$.

$$R(A)=\text{span}\left\{ \begin{bmatrix}
1 \\
1 \\
0 \\
0
\end{bmatrix},\begin{bmatrix}
0  \\
1 \\
1 \\
2
\end{bmatrix},\begin{bmatrix}
0 \\
0 \\
1 \\
1
\end{bmatrix} \right\}$$
Also,
$$\text{dim}(R(A)^\perp)=4-\text{dim}(R(A))=4-3=1$$
Then we just need to find one vector orthogonal to all vectors in $R(A)$. Therefore,
$$N(A^T)=R(A)^\perp=\text{span}\left\{ \begin{bmatrix}
1 \\
-1 \\
-1 \\
1
\end{bmatrix} \right\}$$

Again, we use that
$$R(A^T)=N(A)^\perp$$
We can see easily from above that 
$$N(A)=\text{span}\left\{ \begin{bmatrix}
1\\3\\1\\0
\end{bmatrix} \right\}$$

Also,
$$\text{dim}(N(A)^\perp)= 4-\text{dim}(N(A))=4-1=3$$
So, we find three vectors orthogonal to $N(A)$,
$$N(A)^\perp=\text{span}\left\{ \begin{bmatrix}
3 \\
-1 \\
0 \\
0
\end{bmatrix}, \begin{bmatrix}
0 \\
1 \\
-3 \\
0
\end{bmatrix},\begin{bmatrix}
0 \\
0 \\
0 \\
1
\end{bmatrix} \right\}$$

as required.

#### Exercise 12
Let $A$ be a matrix such that its LU decomposition is of the form 
$$A=LU=\begin{bmatrix}
1 & 0 & 0 \\
* & 1 & 0 \\
* & * & 1
\end{bmatrix}\begin{bmatrix}
* & * & * & * \\
0 & * & * & * \\
0 & 0 & 0 & *
\end{bmatrix}$$
where * denotes a non-zero number. Determine the dimension of $R(A^T)$ and the dimension of $N(A^T)$.

$$\text{dim}(R(A^T))=\text{dim}(N(A)^\perp) = 4-\text{dim}(N(A))=4-1=3$$
$$\text{dim}(N(A^T))=\text{dim}(R(A))=3-\text{dim}(R(A))=3-3=0$$

#### Exercise 13
Let $u$ and $v$ be non-zero column vectors in $\mathbb{R}^n$ such that $\langle u,v \rangle=0$ and let 
$$P= \frac{1}{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert }vu^T$$
Determine whether the statement is **True** or **False**.

- $\text{rank}(P)=1$
$$vu^T=\begin{bmatrix}
v_{1} \\
v_{2} \\
\vdots \\
v_{n}
\end{bmatrix}\begin{bmatrix}
u_{1} & u_{2} & \cdots & u_{n}
\end{bmatrix}$$
$$= \begin{bmatrix}
v_{1}u_{1} & v_{1}u_{2} & \cdots & v_{1}u_{n} \\
v_{2}u_{1} & v_{2}u_{2} & \cdots & v_{2}u_{n} \\
\vdots  &  &  & \vdots \\
v_{n}u_{1} & v_{n}u_{2} & \cdots & v_{n}u_{n}
\end{bmatrix} \to \begin{bmatrix}
v_{1}u_{1} & v_{1}u_{2} & \cdots & v_{1}u_{n} \\
0 & 0 & \cdots & 0 \\
\vdots &  &  & \vdots \\
0 & 0 & \cdots & 0
\end{bmatrix}$$
$$\to \text{rank}(P)=1$$
**True**

- $P^2$ is the identity matrix
$$P^2=\frac{1}{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert }vu^T\frac{1}{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert }vu^T = \frac{1}{\lvert \lvert u \rvert  \rvert ^2 \lvert \lvert v \rvert  \rvert^2 }vu^Tvu^T=\frac{1}{\lvert \lvert u \rvert  \rvert ^2 \lvert \lvert v \rvert  \rvert^2 }v\langle u,v \rangle u^T = 0$$
Zero-matrix! **False**

- $P^2$ is the zero matrix
**True**

- $Px$ is the projection $x$ onto $u$
$$Px=\frac{1}{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert }vu^Tx$$
This is nor a projection $x$ onto $u$ neither a projection $x$ onto $v$.

**False**

- $Px$ is the projection $x$ onto $v$

**False**

- $Pu= cv$ for some non-zero number $c$
$$Pu= \frac{1}{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert }vu^Tu = \frac{\langle u,u \rangle }{\lvert \lvert u \rvert  \rvert \lvert \lvert v \rvert  \rvert } v = cv$$
**True**

#### Exercise 14
Let $U \subset \mathbb{R}^n$ be a subspace. Let $P_1$ be a orthogonal projector onto $U$ and let $P_2$ be the orthogonal projector onto the orthogonal complement $U^\perp$. Determine whether the statement is **True** or **False**.

- $I=P_{1}+P_{2}$
$$P_{\perp}=I-P\to P_{2}=I-P_{1} \to P_{1}+P_{2}=I$$
**True**

- $P_{1}P_{2}=P_{2}P_{1}=0$

$$P_{1}P_{2}=P_{1}(I-P_{1})=P_{1}-P_{1}^2=P_{1}-P_{1}=0$$
$$P_{2}P_{1}=P_{2}(I-P_{2})=P_{2}-P_{2}^2=P_{2}-P_{2}=0$$

#### Exercise 15
Let $U \subset \mathbb{R}^3$ be the subspace spanned by 
$$u_{1}=\begin{bmatrix}
1\\1\\1
\end{bmatrix},u_{2}=\begin{bmatrix}-1\\1\\1
\end{bmatrix}$$
Find the vector in $U$ which is closest to the vector 
$$x=\begin{bmatrix}
1\\2\\1
\end{bmatrix}$$

Since $\lvert \lvert \text{proj}_{U}(x)-x \rvert \rvert$ is the minimum distance between $U$ and $x$, we just need to get $\text{proj}_{U}(x)$.
Since $\text{dim}(U)=2$ we also know that $\text{dim}(U^\perp)=1$ hence it’s easier to get $\text{proj}_{U^\perp}(x)$.

A vector $u_{3}$ that is orthogonal to $u_{1},u_{2}$ is
$$u_{3}=\begin{bmatrix}
0 \\1\\-1
\end{bmatrix}$$

Then, $P_\perp$ is
$$P_{\perp}=\frac{1}{\lvert \lvert u_{3} \rvert  \rvert ^2}u_{3}u_{3}^T$$
$$=\frac{1}{2} \begin{bmatrix}
0\\1\\-1
\end{bmatrix}\begin{bmatrix}
0 & 1 & -1
\end{bmatrix}=\frac{1}{2}\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & -1 \\
0 & -1 & 1
\end{bmatrix}$$

Thus,
$$\text{proj}_{U^\perp}(x)=\frac{1}{2}\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & -1 \\
0 & -1 & 1
\end{bmatrix}\begin{bmatrix}
0 \\
2 \\
1
\end{bmatrix}=\frac{1}{2}\begin{bmatrix}
0 \\
1 \\
-1
\end{bmatrix}$$
$$\text{proj}_{U}(x)=x-\text{proj}_{U^\perp}(x)=\begin{bmatrix}
1 \\
2 \\
1
\end{bmatrix}-\begin{bmatrix}
0 \\
\frac{1}{2} \\
-\frac{1}{2}
\end{bmatrix}=\begin{bmatrix}
1 \\
\frac{3}{2}  \\
\frac{3}{2}
\end{bmatrix}$$
#### Exercise 16
Let $U \subset \mathbb{R}^3$ be the subspace spanned by
$$u_{1}=\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix},u_{2}=\begin{bmatrix}
1 \\
2 \\
1
\end{bmatrix}$$
Find the shortest distance from $x$ to $U$ where
$$x=\begin{bmatrix}
1 \\
1 \\
2
\end{bmatrix}$$

Again, $\text{dim}(U^\perp)=3-\text{dim}(U)=3-2=1$, hence we proceed with getting $\text{proj}_{U^\perp}(x)$.
$$u_{3}=\begin{bmatrix}
1 \\
0 \\
-1
\end{bmatrix}$$

$$P_{\perp}= \frac{1}{\lvert \lvert u_{3} \rvert  \rvert^2 }u_{3}u_{3}^T$$
$$=\frac{1}{2} \begin{bmatrix}
1 \\
0 \\
-1
\end{bmatrix}\begin{bmatrix}
1 & 0 & -1
\end{bmatrix}=\frac{1}{2} \begin{bmatrix}
1 & 0 & -1 \\
0 & 0 & 0 \\
-1 & 0 & 1
\end{bmatrix}$$

$$\text{proj}_{U^\perp}(x)= \frac{1}{2}\begin{bmatrix}
1 & 0 & -1 \\
0 & 0 & 0 \\
-1 & 0 & 1
\end{bmatrix}\begin{bmatrix}
1 \\
1 \\
2
\end{bmatrix}=\frac{1}{2}\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}$$

Then the distance is 
$$\lvert \lvert \text{proj}_{U^\perp}(x) \rvert  \rvert =\left\lvert  \left\lvert  \begin{bmatrix}
-\frac{1}{2} \\ 0\\ \frac{1}{2}
\end{bmatrix}  \right\rvert   \right\rvert =\frac{1}{\sqrt{ 2 }}$$
==This method is ok, but if we were to get the projection matrix from $u_1,u_2$ we need to get the orthogonal basis.==

So then let’s try with the orthogonal basis,
$$u_{1}=\begin{bmatrix}
1\\1\\1
\end{bmatrix},u_{2}=\begin{bmatrix}
1\\2\\1
\end{bmatrix}$$

Let’s get the orthogonal basis,
$$v_{1}=\begin{bmatrix}
1\\1\\1
\end{bmatrix}$$

$$v_{2}=u_{2}-\text{proj}_{v_{1}}(u_{2})=\begin{bmatrix}
1\\2\\1
\end{bmatrix} - \frac{\langle v_{1},u_{2} \rangle }{\langle v_{1},v_{1} \rangle }v_{1}=\begin{bmatrix}
1\\2\\1
\end{bmatrix}- \frac{4}{3}\begin{bmatrix}
1\\1\\1
\end{bmatrix}=\begin{bmatrix}
-\frac{1}{3} \\ \frac{2}{3} \\ -\frac{1}{3}
\end{bmatrix}$$
Then,
$$P=\frac{1}{\lvert \lvert v_{1} \rvert  \rvert ^2}v_{1}v_{1}^T + \frac{1}{\lvert \lvert v_{2} \rvert  \rvert ^2}v_{2}v_{2}^T$$
$$=\frac{1}{3}\begin{bmatrix}
1\\1\\1
\end{bmatrix}\begin{bmatrix}
1 & 1 & 1
\end{bmatrix} + \frac{3}{2}\begin{bmatrix}
-\frac{1}{3}\\ \frac{2}{3} \\ -\frac{1}{3}
\end{bmatrix}\begin{bmatrix}
-\frac{1}{3} & \frac{2}{3} & -\frac{1}{3}
\end{bmatrix}$$
$$=\frac{1}{3}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix} + \frac{3}{2} \begin{bmatrix}
\frac{1}{9} & -\frac{2}{9} & \frac{1}{9} \\
-\frac{2}{9} & \frac{4}{9} & -\frac{2}{9} \\
\frac{1}{9} & -\frac{2}{9}  &  \frac{1}{9}
\end{bmatrix}$$
$$ = \begin{bmatrix}
\frac{1}{2} & 0 & \frac{1}{2} \\
0 & 1 & 0 \\
\frac{1}{2} & 0 & \frac{1}{2}
\end{bmatrix}$$
$$P_{\perp}=I-P= \begin{bmatrix}
\frac{1}{2} & 0 & -\frac{1}{2} \\
0 & 0 & 0 \\
-\frac{1}{2} & 0 & \frac{1}{2}
\end{bmatrix}$$

$$\text{proj}_{U^\perp}(x)=P_{\perp}x=\begin{bmatrix}
\frac{1}{2} & 0 & -\frac{1}{2} \\
0 & 0 & 0 \\
-\frac{1}{2} & 0 & \frac{1}{2}
\end{bmatrix}\begin{bmatrix}
1 \\
1 \\
2
\end{bmatrix}=\begin{bmatrix}
-\frac{1}{2}\\0\\ \frac{1}{2}
\end{bmatrix} $$
$$\therefore \lvert \lvert \text{proj}_{U^\perp}(x) \rvert  \rvert =\frac{1}{\sqrt{ 2 }}$$
==WAY TOO MUCH WORK!!!==

#### Exercise 17
Let $u \subset \mathbb{R}^n$ be a non-zero vector and let 
$$H=I-\frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^T$$
The matrix $H$ is called an elementary reflector. Determine whether the statement is **True** or **False**.

- There is a unique unit vector $v$ such that $Hv=v$
$$Hv=\left( I-\frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^T \right)v$$
$$=v- \frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^Tv$$

In order for the following relation to be established,
$$v- \frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^Tv=v$$
Then, we need that 
$$\frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^Tv=0$$

Since we know that $u$ is a non-zero vector, we need that $u^Tv=0$. That being said, there is not a **unique** vector that is orthogonal to $u$.

**False**

- $Hv=v$ for all $v \in \text{span}\left\{ u \right\}^\perp$
As we said above, all $v$ is any vector orthogonal to $u$. Hence, $v \in \text{span}\left\{ u \right\}^\perp$.
**True**

#### Exercise 18
Compute the QR decomposition of the matrix
$$A=\begin{bmatrix}
1 & 1 & 1 \\
0 & 1 & 1 \\
1 & 1 & 0
\end{bmatrix}$$

Let’s apply G-S to get the orthonormal basis of $R(A)$.

$$v_{1}=a_{1}=\begin{bmatrix}
1  \\
0 \\
1
\end{bmatrix}\to w_{1}=\frac{1}{\sqrt{ 2 }} \begin{bmatrix}
1 \\0\\1
\end{bmatrix}$$
$$v_{2}=a_{2} - \text{proj}_{v_{1}}(a_{2}) = \begin{bmatrix}
1\\1\\1
\end{bmatrix}-\frac{2}{2}\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}=\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix}=w_{2}$$
$$v_{3}=a_{3}-\text{proj}_{v_{1}}(a_{3})-\text{proj}_{v_{2}}(a_{3})$$
$$=\begin{bmatrix}
1\\1\\0
\end{bmatrix}-\frac{1}{2}\begin{bmatrix}
1\\0\\1
\end{bmatrix}-\begin{bmatrix}
0\\1\\0
\end{bmatrix}=\begin{bmatrix}
\frac{1}{2}\\0\\ -\frac{1}{2}
\end{bmatrix}$$
$$w_{3}=\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} \\ 0 \\ -\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$

Then, we construct $Q_{1}$,
$$Q_{1}= \begin{bmatrix}
\frac{1}{\sqrt{ 2 }} & 0 & \frac{1}{\sqrt{ 2 }} \\
0 &  1 & 0 \\
\frac{1}{\sqrt{ 2 }} & 0 & -\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$
Now $R_{1}$,
$$R_{1}= \begin{bmatrix}
\langle w_{1},a_{1} \rangle  & \langle w_{1},a_{2} \rangle  & \langle w_{1},a_{3} \rangle  \\
0 & \langle w_{2},a_{2} \rangle  & \langle w_{2},a_{3} \rangle  \\
0 & 0 & \langle w_{3},a_{3} \rangle 
\end{bmatrix}$$
$$=\begin{bmatrix}
\sqrt{ 2 } & \sqrt{ 2 } & \frac{1}{\sqrt{ 2 }} \\ 
0 & 1 & 1 \\
0 & 0 & \frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$

#### Exercise 19
Compute the thin QR decomposition of the matrix 
$$A=\begin{bmatrix}
1  & 1 \\
1 & -1  \\
1 & 1 \\
1 & 1
\end{bmatrix}$$
Let’s first get the orthonormal basis of $R(A)$.
$$v_{1}=a_{1}=\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}\to w_{1}=\frac{1}{2} \begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}$$
$$v_{2}=a_{2}-\text{proj}_{v_{1}}(a_{2})=\begin{bmatrix}
1\\-1\\1\\1
\end{bmatrix}-\frac{2}{4}\begin{bmatrix}
1\\1\\1\\1
\end{bmatrix}=\begin{bmatrix}
\frac{1}{2}  \\
-\frac{3}{2}  \\
\frac{1}{2} \\
\frac{1}{2}
\end{bmatrix}$$
$$\to w_{2}= \begin{bmatrix}
\frac{1}{2\sqrt{ 3 }} \\
-\frac{\sqrt{ 3 }}{2} \\
\frac{1}{2\sqrt{ 3 }} \\
\frac{1}{2\sqrt{ 3 }}
\end{bmatrix}=\begin{bmatrix}
\frac{\sqrt{ 3 }}{6} \\
\frac{-\sqrt{ 3 }}{2} \\
\frac{\sqrt{ 3 }}{6} \\
\frac{\sqrt{ 3 }}{6}
\end{bmatrix}$$

Also, we can get $\langle w_{1},a_{1} \rangle,\langle w_{1},a_{2} \rangle,\langle w_{2},a_{2} \rangle$.

$$\langle w_{1},a_{1} \rangle =2$$
$$\langle w_{1},a_{2} \rangle =1$$
$$\langle w_{2},a_{2} \rangle = \sqrt{ 3 }$$
$$A=Q_{1}R_{1}=\begin{bmatrix}
\frac{1}{2} & \frac{\sqrt{ 3 }}{6} \\
\frac{1}{2}  & -\frac{\sqrt{ 3 }}{2} \\
\frac{1}{2} & \frac{\sqrt{ 3 }}{6} \\
\frac{1}{2} & \frac{\sqrt{ 3 }}{6}
\end{bmatrix}\begin{bmatrix}
2 & 1 \\
0 & \sqrt{ 3 }
\end{bmatrix}$$


#### Exercise 20
Let $A=QR$ where
$$Q=\begin{bmatrix}
0 & 0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1
\end{bmatrix},R=\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

Find the least squares approximation $Ax \approx b$ where
$$b=\begin{bmatrix}
-2 \\
-1 \\
0 \\
1 \\
2
\end{bmatrix}$$

We need to find the solution of $R_{1}x=Q_{1}^Tb$,
$$R_{1}=\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix},Q_{1}=\begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

$$\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix}x=\begin{bmatrix}
0 & 0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
-2 \\
-1 \\
0 \\
1 \\
2
\end{bmatrix}=\begin{bmatrix}
1 \\
-1 \\
0 \\
-2
\end{bmatrix}$$

$$x=\begin{bmatrix}
2 \\ -1 \\ 2 \\ -2
\end{bmatrix}$$

#### Exercise 21
Set up (but do not solve) a linear system $Ac=y$ where the solution is the coefficient vector
$$c=\begin{bmatrix}
c_{0} \\
c_{1} \\
c_{2}
\end{bmatrix}$$
such that the function
$$f(t)=c_{0}+c_{1}\cos(2\pi t)+c_{2}\sin(2\pi t)$$
best fits the data $(0,1),\left( \frac{1}{4},3 \right), \left( \frac{1}{2},2 \right) ,\left( \frac{3}{4},-1 \right),(1,0)$

$$A=\begin{bmatrix}
1 & 1 & 1 \\ 
1 & 0 & 1 \\  
1 & -1 & 0 \\
1 & 0 & -1 \\
1 & 1 & 0
\end{bmatrix},y=\begin{bmatrix}
1 \\ 
3 \\
2 \\
-1 \\
0
\end{bmatrix}$$

#### Exercise 22
Determine whether the statement is **True** or **False**.

- Let $v_{1},v_{2} \in \mathbb{R}^2$ be linearly independent vectors. Let $\lambda_{1},\lambda_{2}$ be real numbers. There exists a unique $2\times {2}$ matrix $A$ with eigenvalues $\lambda_{1},\lambda_{2}$ and corresponding vectors $v_{1},v_{2}$.

$$A=\begin{bmatrix}
a & b \\
c & d
\end{bmatrix},v_{1}=\begin{bmatrix}
x_{1} \\
y_{1}
\end{bmatrix},v_{2}=\begin{bmatrix}
x_{2} \\
y_{2} 
\end{bmatrix}$$
We need to satisfy $Av_{1}=\lambda_{1}v_{1}$ and $Av_{2}=\lambda_{2}v_{2}$. Therefore,
$$Av_{1}=\begin{bmatrix}
ax_{1}+by_{1} \\
cx_{1}+dy_{1}
\end{bmatrix}=\begin{bmatrix}
\lambda_{1}x_{1} \\
\lambda_{2}y_{1}
\end{bmatrix}$$

$$Av_{2}=\begin{bmatrix}
ax_{2}+by_{2} \\
cx_{2}+dy_{2}
\end{bmatrix}=\begin{bmatrix}
\lambda_{2}x_{2} \\
\lambda_{2}y_{2}
\end{bmatrix}$$

Then we have four unknowns $a,b,c,d$ and four equations. Thus, it is unique. **True**.


 - Suppose $A$ and $B$ are symmetric $n\times n$ matrices. the eigenvectors of $AB$ corresponding to distinct eigenvalues are orthogonal.

Let $v_{i},u_{j}$ be the eigenvectors for $\lambda_{i},\lambda_{j}$ 
$$ABv_{i}=\lambda_iv_{i}$$
$$ABu_{j}=\lambda_{j}u_{j}$$
Then,
$$\langle \lambda_{i}v_{i},u_{j} \rangle =\langle ABv_{i},u_{j} \rangle $$
$$=\langle v_{i},B^TA^Tu_{j} \rangle $$
$$\langle v_{i},\lambda_{j}u_{j} \rangle = \langle v_{i},ABu_{j} \rangle  $$
 $$\to (\lambda_{i}-\lambda_{j})\langle v_{i},u_{j} \rangle = \langle v_{i},(AB-B^TA^T)u_{j} \rangle  =\langle v_{i},(AB - BA)u_{j} \rangle$$
Only if $AB=BA$, then this would be true. **False**.

#### Exercise 23
Let $A$ be a $m\times n$ matrix. Determine whether the statement is **True** or **False**.
- If $\lambda$ is an eigenvalue of $AA^T$ then $\lambda \in \mathbb{R}$.
$$(AA^T)^T=AA^T$$
so $AA^T$ is symmetric, hence the eigenvalues are real numbers. **True**.

- If $v_{1},v_{2}$ are eigenvectors of $AA^T$ for distinct eigenvalues $\lambda_{1},\lambda_{2}$ then $\langle v_{1},v_{2} \rangle=0$.
$$\lambda_{1}\langle v_{1},v_{2} \rangle =\langle \lambda_{1}v_{1},v_{2} \rangle = \langle AA^Tv_{1},v_{2} \rangle  = \langle v_{1},AA^Tv_{2} \rangle =\langle v_{1},\lambda_{2}v_{2} \rangle $$
$$(\lambda_{1}-\lambda_{2})\langle v_{1},v_{2} \rangle= 0 $$

And since $\lambda_{1} \neq \lambda_{2}$, thus $\langle v_{1},v_{2} \rangle=0$. **True**.
#### Exercise 24
Let $U \subset \mathbb{R}^n$ be a subspace with $\text{dim}(U)=m$ such that $0 < m < n$ and let $P$ be the orthogonal projection matrix onto $U$. Determine the characteristic polynomial of $P$.

$$c_{P}(x)=\det(P-xI)$$
Let’s consider $x=0$,
$$P - 0I=P \to \text{rank}(P)=\text{dim}(U)=n-\text{dim}(N(P)) =m$$
$$\text{dim}(N(P)) = n-m$$

for $x=1$,
$$P-I=-P_{\perp} \to \text{rank}(P_{\perp}) = \text{dim}(U^\perp)= n-m = n - \text{dim}(N(P_{\perp}))$$
$$\text{dim}(N(P_{\perp}))=m$$

Thus,
$$\therefore c_{P}(x)= \pm x^{n-m}(x-1)^m$$

#### Exercise 25
Let $u \in \mathbb{R}^n$ be a nonzero vector and let 
$$H=I- \frac{2}{\lvert \lvert u \rvert  \rvert ^2}uu^T$$
be the corresponding elementary reflector. Determine the characteristic polynomial of $H$.

$$H = I - 2P , c_{H}(x)=\det(I-2P-x I)$$

Let’s consider $x = 1$,
$$\det(-2P)=-2\det (P)=0 \text{ since } \text{rank}(P)=1$$
Then when $x=-1$,
$$\det(I-2P+I) =\det(2I-2P)=2\det(P_{\perp})= 0$$
$$\text{rank}(P_{\perp})=n-1$$
Thus,
$$\therefore c_{H}(x) = \pm (x-1)(x+1)^{n-1}$$

#### Exercise 26
Let $\lambda$ be an eigenvalue of an invertible matrix $A$. Determine whether the statement is **True** or **False**.

- $\lambda^{-1}$ is an eigenvalue of $A^{-1}$.
$$Av=\lambda v \to v = A^{-1}\lambda v \to \frac{1}{\lambda}v=A^{-1}v$$
**True**

- $\lambda$ is an eigenvalue of $A^T$.
$$\det((A-\lambda I)^T)=\det(A^T-\lambda I)=\det(A-\lambda I)$$
**True**

- $\lambda^2$ is an eigenvalue of $AA^T$.
$$\det(AA^T-\lambda^2I)=\det((A+\lambda I)(A^T-\lambda I))=\det(AA^T+\lambda(A^T-A)-\lambda^2I)$$
if and only if $A^T = A$. **False**.


- $\lambda$ is an eigenvalue of $BAB^{-1}$ for any invertible matrix $B$.
$$\det(BAB^{-1} - \lambda I) = \det(BAB^{-1} - \lambda BB^{-1})$$
$$=\det(B(A-\lambda I)B^{-1})= \det(B)\det(A-\lambda I)\det(B^{-1})$$
$$=\det(A - \lambda I)=0$$
**True**

#### Exercise 27
Suppose $A$ is a symmetric $3 \times {3}$ matrix with distinct eigenvalues $\lambda_{1},\lambda_{2},\lambda_{3}$ and eigenvectors
$$v_{1}=\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix},v_{2}=\begin{bmatrix}
1 \\
0 \\
-1
\end{bmatrix}$$

Find an eigenvector $v_{3}$ for eigenvalue $\lambda_{3}$.

If $A$ has distinct eigenvalues then $A$ is diagonalizable. Thus, $A=PDP^{-1}$. But $A$ is symmetric hence $P^{-1} = P^T$ making $P$ an orthogonal matrix.

We just need to find $v_3$ such that $v_{1},v_{2},v_{3}$ are orthonormal.
$$\therefore v_{3}=\begin{bmatrix}
1 \\
-2 \\
1
\end{bmatrix}$$

#### Exercise 28
Let $A$ and $B$ be $n\times n$ matrices. Then $R(BA)=R(A)$. **True** or **False**.

For instance, let
$$B=\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix},A=\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}$$

Then,
$$BA=\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}$$

Thus, $R(BA)= 0,R(A)=\mathbb{R}^2$. **False**.

#### Exercise 29
Let $U$ and $V$ be two subspaces of $\mathbb{R}^n$. Their union is also a subspace of $\mathbb{R}^n$.
Let,
$$U=\left \{ t\begin{bmatrix}
1 \\
0 \\
0 \\
\vdots \\
0
\end{bmatrix} : t\in \mathbb{R} \right \},V= \left \{ s\begin{bmatrix}
1 \\
1 \\
1 \\
\vdots \\
1
\end{bmatrix}:s \in \mathbb{R} \right \}$$

and also let,
$$u=\begin{bmatrix}
1 \\
0 \\
0 \\
\vdots \\
0
\end{bmatrix},v=\begin{bmatrix}
1 \\
1 \\
1 \\
\vdots \\
1
\end{bmatrix} \to u +v = \begin{bmatrix}
2 \\
1 \\
1 \\
\vdots \\
1
\end{bmatrix} \not\in U \cup V$$
Hence, it is not a subset. It is not closed under addition.

#### Exercise 30
Let $A$ be a non-zero $n \times n$ **orthogonal projection matrix**. If $y$ is a non-zero vector in $R(A)$, then $y$ is not in $N(A)$.

Let $y \in R(A)$ and $y\neq {0}$, then $Au=y$ for some $u\in \mathbb{R}^n$. 
$$Au=y \to A^2u=Ay \to u = Ay$$
but we know that $u\neq {0}$,
$$\therefore y \not\in N(A)$$

OR,
$$y\in R(A)=N(A^T)^\perp=N(A)^\perp$$
and since $y \neq 0$, and $N(A) \cap N(A)^\perp = \{ 0 \}$ hence $y \not\in N(A)$.

#### Exercise 31
Let $A$ be an $n \times n$ matrix. If all eigenvalues of $A$ are positive real numbers, $\lvert \lvert A \rvert \rvert$ equals its largest eigenvalue.

For instance, let $$A=\begin{bmatrix}
1 & 2024 \\
0 & 2
\end{bmatrix}$$

Then,
$$\det(A-\lambda I)=(\lambda - 1)(\lambda - 2) \to \lambda_{1}=1,\lambda_{2}=2$$

$$\lvert \lvert A \rvert  \rvert \geq \lvert\lvert A\begin{bmatrix}
0 \\ 1
\end{bmatrix} \rvert\rvert =\lvert\lvert \begin{bmatrix}
1 & 2024 \\
0 & 2
\end{bmatrix}\begin{bmatrix}
0 \\
1
\end{bmatrix}\rvert\rvert=\begin{bmatrix}
2024 \\
2
\end{bmatrix} \rvert \rvert > \lambda_{2}=2$$
**False!!**

#### Exercise 32
Let $U=\text{span}\left\{ \mathbf{x} \right\} \subseteq \mathbb{R}^3$ where $\mathbf{x}=\begin{bmatrix}1\\1\\-1\end{bmatrix}$.

(a) Construct an orthogonal projection matrix which projects onto $U$.

$$P= \frac{1}{\lvert \lvert \mathbf{x} \rvert  \rvert^2 }\mathbf{x}\mathbf{x}^T=\frac{1}{3}\begin{bmatrix}
1 \\
1 \\
-1
\end{bmatrix}\begin{bmatrix}
1 & 1 & -1
\end{bmatrix}= \frac{1}{3} \begin{bmatrix}
1 & 1 & -1 \\
1 & 1 & -1 \\
-1 & -1 & 1
\end{bmatrix}$$

(b) Find an orthogonal projection matrix $P$ such that $N(P)=U$.

$$N(P)=R(P^T)^\perp=R(P)^\perp=U^\perp$$
$$P=I-P_{\perp}=\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}-\frac{1}{3} \begin{bmatrix}
1 & 1 & -1 \\
1 & 1 & -1 \\
-1 & -1 & 1
\end{bmatrix}= \frac{1}{3} \begin{bmatrix}
2 & -1 & 1 \\
-1 & 2 & 1 \\
1 & 1 & 2
\end{bmatrix}$$


