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
$$A=PDP^{-1} \iff PA=PD$$
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

#### Theorem
$A$ is diagonizable iff it has $n$ linearly independent vectors. This means no eigenvalue is defective. A matrix need not be invertible to be diagonizable/

#### Theorem
Let $A$ be symmetric and real and let $\lambda_{1},\lambda_{2}$ be distinct eigenvalues. Then corresponding eigenvectors are orthogonal. That is $E_{1} \perp E_{2}$.

Let us check
$$\langle Av_{1},v_{2} \rangle=\lambda \langle v_{1},v_{2} \rangle  $$
$$\langle Av_{1},v_{2} \rangle =\langle v_{1},A^Tv_{2} \rangle =\langle v_{1},Av_{2} \rangle =\lambda_{2}\langle v_{1},v_{2} \rangle $$

For this to be equal
$$(\lambda_{1}-\lambda_{2})\langle v_{1},v_{2} \rangle=0 $$
But since $\lambda_{1}\neq \lambda_{2}$, we have that $\langle v_{1},v_{2} \rangle$ hence $v_{1}$,$v_{2}$ are orthogonal.

For symmetric and real $A$, the eigenvalues are real.

#### Theorem (Spectral)
Let $A$ be symmetric and real. Then there exists a real orthogonal matrix $P$ and real diagonal matrix $D$ such that $A=PDP^T$.

1. Eigenvalues are real.
2. Matrix is diagonalizable (there are $n$ linearly independent eigenvectors of $A$ $\iff$ algebraic multiplicity is equal to geometric multiplicity for each eigenvalue).
3. Eigenvectors for distinct eigenvalues are orthogonal.

###### Example
Find $P$ and $D$ for $A=\begin{bmatrix}0&1&0 \\ 1&1&-1 \\ 0 & -1 & 0\end{bmatrix}$. 

