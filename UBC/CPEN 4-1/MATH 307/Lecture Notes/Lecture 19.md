#### Eigen values and Eigen vectors
Let use consider $A \in \mathbb{R}^{n\times n}$. A number $\lambda$ is an eigenvalue of $A$ with eigenvector $v$ if $Av=\lambda v$ where $v \neq 0$.

$$Av=\lambda v \iff Av-\lambda v=0 \iff(A - I\lambda)v=0$$

Since $v\neq0$ and $v \in N(A-\lambda I)$ has a nontrivial null space. This means that it has vectors in its null space that are not identically equal to zero. This also means that the matrix is not full rank (by rank nullity theorem and dimension of the range) and hence not invertible and has determinant 0.

→ To elaborate, since it has vectors that are non-zero that make a solution to the matrix, we have that the null space has at least dimension 1. Which means that the rank of the matrix is not full rank → making it non-invertible and has determinant 0.

#### Definition of characteristic polynomial
The characteristic polynomial of $A$ is 
$$c_{A}(x)=\det(A-xI)$$
The characteristic polynomial has degree $n$. Eigenvalues of $A$ are roots of $c_{A}(x)$.

#### Definition of Eigenspace
Let $A \in R^{n\times n}$ have an eigenvalue $\lambda$. The eigenspace for $\lambda$ is 
$$E_{\lambda}=\{ v \in \mathbb{R}^n :Av=\lambda v \}=N(A-\lambda I)$$

1. Calculate $c_{A}(x)$.
2. Find roots of $c_{A}(x)$.
3. Find a basis of $E_{\lambda}$ for each $\lambda$.

==This does not work with large $n$!==

#### Theorem
Let $\lambda_{1},\cdots,\lambda_{k}$ be distinct eigenvalues of $A$ with $k \leq n$. We have 
$$c_{A}(x)=\pm(x-\lambda_{1})^{\alpha_{1}}(x-\lambda_{2})^{\alpha_{2}}\cdots(x-\lambda_{k})^{\alpha_{k}}$$

We know that $\alpha_{1}+\cdots+\alpha_{k}=n$.
- Algebraic multiplicity of $\lambda_{i}$ is $\alpha_{i}$.
- Geometric multiplicity of $\lambda_{i}$ is $d_{i}=\text{dim}(E_{\lambda})$. This is the number of linearly independent eigenvectors for $\lambda_{i}$.
- An eigen value is defective if $d_{i}<\alpha_{i}$.

###### Exercise
Let, $$A=\begin{bmatrix}0&1&1 \\ 1&0&1 \\ 1&1&0\end{bmatrix}$$
$$c_{A}(x)=\det(A-xI)=\det(\begin{bmatrix}
-x & 1 & 1 \\
1 & -x & 1 \\
1 & 1 & -x
\end{bmatrix})$$
$$=-x(x^2-1)-(-x-1)+(1+x)=-x(x-1)(x+1)+2(x+1)$$
$$=(x+1)(-x^2+x+2)=-(x+1)^2(x-2)$$
giving us the eigenvalues
$$\lambda_{1}=-1,\lambda_{2}=2$$
with algebraic multiplicities
$$\alpha_{1}=2,\alpha_{2}=1$$
Now let’s find the eigenvectors, first for $\lambda_{1}$
$$\mathbf{y} \in N(A+I) \iff \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}\mathbf{y}=0$$
$$\mathbf{y}=\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}t+\begin{bmatrix}
-1 \\
1 \\
0
\end{bmatrix}l$$
$$E_{\lambda_{1}}= \text{span}\left\{ \begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}, \begin{bmatrix}
-1 \\
1 \\
0
\end{bmatrix} \right\}$$
Giving the eigenvectors,
$$\mathbf{v}_{1}=\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix},\mathbf{v}_{2}=\begin{bmatrix}
-1 \\
1 \\
0 
\end{bmatrix} \to d_{1}=\text{dim}(E_{\lambda_{1}})=2$$

Next, for $\lambda_{2}=2$,
$$\mathbf{y} \in N(A-2I) \iff \begin{bmatrix}
-2 & 1 & 1 \\
1 & -2 & 1 \\
1 & 1 & -2
\end{bmatrix}$$
Giving us,
$$\mathbf{v}_{3}=\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix} \to d_{2}=\text{dim}(E_{\lambda_{2}})=1$$

###### Example
$$A=\begin{bmatrix}
1 & 0 & 1 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}$$

$$\det(A- \lambda I)=(1-\lambda)^2(2-\lambda)$$

We have $\lambda_{1}=1,\alpha_{1}=2$ and $\lambda_{2}=2,\alpha_{2}=1$.  Then, $\text{dim}(E_{\lambda_{1}})=1$ so $\lambda_{1}$ is defective.

#### Diagonalization
An $n\times n$ matrix is diagonizable if there exists invertible $P$ and diagonal $D$ such that $A=PDP^{-1}$. Even when $A$ is real, $P,D$ can be complex and not all matrices are diagonalizable.

We have that,
$$A=PDP^{-1} \iff AP=PD$$
$$AP=A\begin{bmatrix}
v_{1} & v_{2} & \cdots & v_{n}
\end{bmatrix}=\begin{bmatrix}
Av_{1} & Av_{2} & \cdots & Av_{n}
\end{bmatrix}$$

We also have,
$$PD=\begin{bmatrix}
v_{1} & v_{2} & \cdots & v_{n}
\end{bmatrix}\begin{bmatrix}
\lambda_{1} \\
 & \lambda_{2} \\
 &  & \ddots \\
 &  &  & \lambda_{n}
\end{bmatrix}=\begin{bmatrix}
\lambda_{1}v_{1} & \lambda_{2}v_{2} & \cdots & \lambda_{n}v_{n} 
\end{bmatrix}$$

Thus, we have that
$$Av_{1}=\lambda_{1}v_{1}$$
$$\vdots$$
$$Av_{n}=\lambda_{n}v_{n}$$

#### Theorem
$A$ is diagonizable iff it has $n$ linearly independent vectors. This means no eigenvalue is defective. A matrix need not be invertible to be diagonizable.

#### Theorem
Let $A$ be symmetric and real and let $\lambda_{1},\lambda_{2}$ be distinct eigenvalues. Then corresponding eigenvectors are orthogonal. That is $E_{1} \perp E_{2}$.

Let us check
$$\langle Av_{1},v_{2} \rangle=\lambda_{1} \langle v_{1},v_{2} \rangle  $$
$$\langle Av_{1},v_{2} \rangle =\langle v_{1},A^Tv_{2} \rangle =\langle v_{1},Av_{2} \rangle =\lambda_{2}\langle v_{1},v_{2} \rangle $$

For this to be equal
$$(\lambda_{1}-\lambda_{2})\langle v_{1},v_{2} \rangle=0 $$
But since $\lambda_{1}\neq \lambda_{2}$, we have that $\langle v_{1},v_{2} \rangle$ hence $v_{1}$,$v_{2}$ are orthogonal.

For symmetric and real $A$, the eigenvalues are real.

#### Theorem (Spectral)
Let $A \in \mathbb{R}^{n\times n}$ be symmetric and real. Then there exists a real orthogonal matrix $P \in \mathbb{R}^{n\times n}$ and real diagonal matrix $D \in \mathbb{R}^{n\times n}$ such that $A=PDP^T$.

1. Eigenvalues are real, they for the diagonal entries of $D$. $$D=\begin{bmatrix}
\lambda_{1} \\
 & \lambda_{2}  \\
 &  & \ddots \\
 &  &  & \lambda_{n}
\end{bmatrix}$$
2. Matrix is diagonalizable (there are $n$ linearly independent eigenvectors of $A$ $\iff$ algebraic multiplicity is equal to geometric multiplicity for each eigenvalue). These eigenvectors form the columns of $P$. $$P=\begin{bmatrix}
\mathbf{v}_{1} & \mathbf{v}_{2} & \cdots & \mathbf{v}_{n}
\end{bmatrix}$$
3. Eigenvectors for distinct eigenvalues are orthogonal. Assuming that the eigenvectors $\mathbf{v}_{1},\mathbf{v}_{2},\cdots,\mathbf{v}_{n}$ that are in the columns of $P$ are normalized, we have that $P$ is a matrix with orthonormal rows, hence it is orthogonal and hence $P^{-1}=P^T$, giving us the decomposition $$A=PDP^T=PDP^{-1}$$

###### Example
Find $P$ and $D$ for $A=\begin{bmatrix}0&1&0 \\ 1&1&-1 \\ 0 & -1 & 0\end{bmatrix}$. 

$$\det(A-\lambda I)=\det(\begin{bmatrix}
-\lambda & 1 & 0 \\
1 & 1-\lambda & -1 \\
0 & -1 & -\lambda
\end{bmatrix})=-\lambda(\lambda^2-\lambda-1)+\lambda$$
$$=-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda^2-\lambda-2)=-\lambda(\lambda+1)(\lambda-2)= 0$$
$$\therefore \lambda_{1}=-1,\lambda_{2}=0,\lambda=2$$

$$E_{\lambda_{1}} =N(A+I)=N  \left(   \begin{bmatrix}
1 & 1 & 0 \\  
1 & 2 & -1 \\
0 & -1 & 1
\end{bmatrix}  \right) = \text{span}\left\{ \begin{bmatrix}
-1\\1\\1
\end{bmatrix} \right\}$$
$$E_{\lambda_{2}}=N(A)=N\left( \begin{bmatrix}
0 & 1 & 0 \\
1 & 1 & -1 \\
0 & -1 & 0
\end{bmatrix} \right) = \text{span}\left\{ \begin{bmatrix}
1 \\ 0 \\ 1
\end{bmatrix} \right\}$$
$$E_{\lambda_{3}}=N(A-2I)=N\left( \begin{bmatrix}
-2 & 1 & 0 \\
1 & -1 & -1 \\
0 & -1 & -2
\end{bmatrix} \right) = \text{span}\left\{ \begin{bmatrix}
-1 \\
-2 \\
1
\end{bmatrix} \right\}$$

$$\therefore P=\begin{bmatrix}
-1 & 1 & -1 \\
1 & 0 & -2 \\
1 & 1 & 1
\end{bmatrix},D=\begin{bmatrix}
-1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 2
\end{bmatrix}$$

#### Theorem
Eigenvalues of real-symmetric matrices are real.

[Proof]
Let $u \in \mathbb{C}^n$, then by definition of the complex inner-product,
$$\langle u,v \rangle =u^T \bar{v}=\begin{bmatrix}
u_{1} & u_{2} & \cdots & u_{n}
\end{bmatrix}\begin{bmatrix}
\bar{v_{1}} \\
\bar{v_{2}} \\
\vdots \\
\bar{v_{n}}
\end{bmatrix}$$

$$\langle v,Av \rangle =\langle v,\lambda v \rangle =v^T (\bar{\lambda v})=\bar{\lambda}v^T \bar{v}=\bar{\lambda}\langle v,v \rangle =\bar{\lambda}\lvert \lvert v \rvert  \rvert ^2$$
also,
$$v^T \bar{(Av)} =v^T \bar{A}\bar{v}=v^TA \bar{v}=(A^Tv)^T \bar{v}= \langle A^Tv,v \rangle $$
$$=\langle Av,v \rangle =\langle \lambda v,v \rangle=(\lambda v)^T \bar{v} = \lambda \langle v,v \rangle =\lambda \lvert \lvert v \rvert  \rvert ^2 $$
$$\therefore \lambda \lvert \lvert v \rvert  \rvert ^2= \bar{\lambda}\lvert \lvert v \rvert  \rvert ^2 \to \lambda \in \mathbb{R}$$

#### Remarks
-  $A$ is invertible iff 0 is not an eigenvalue.
	→ If 0 is an eigenvalue, $Av=0v =0,v\neq {0}$. Then, $A$ is not full rank and is not invertible.
	
- Determinant of $A$ = product of eigenvalues.
	→ $\det(A) = \det(PDP^-1)=\det(P)\det(A)\det(P^{-1})=\det(D)$.
	
- $A^k=PD^kP^{-1}$.
#### Next Lecture [[Lecture 20]]
