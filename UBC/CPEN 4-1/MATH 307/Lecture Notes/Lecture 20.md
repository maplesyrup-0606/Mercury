We’ve been using $A$ that was a square matrix. But what happens if $A$ was a rectangular matrix, hence $A \in \mathbb{R}^{m\times n}$.

==We can use the spectral theorem! → We can diagonalize real-symmetric matrices with real orthogonal and diagonal matrices.==

Let’s look at $AA^T$ and $A^TA$,
$$AA^T \in \mathbb{R}^{m\times m},A^TA\in \mathbb{R}^{n\times n}$$
they are symmetric.

Also,
$$AA^T=PD_{1}P^T$$
$$A^TA=QD_{2}Q^T$$
They share the same eigenvalues!

### SVD (Singular Value Decomposition)

#### Theorem
Let $A \in \mathbb{R}^{m\times n}$ be a real matrix. There exists orthogonal matrices $P \in \mathbb{R}^{m\times m}$ and $Q \in \mathbb{R}^{n\times n}$, a diagonal $\Sigma$ where
$$\Sigma=\begin{bmatrix}
\sigma_{1} & \cdots & 0 & 0 & 0 \\
0 & \sigma_{2} & 0 & 0 & 0 \\
 &  & \ddots &   \\  
0 & \cdots & 0 & \sigma_{r} & 0 \\
0 & \cdots & 0 & 0 & 0 \\
\vdots \\
0 & \cdots & 0 & 0 & 0
\end{bmatrix}$$
$$A=P\Sigma Q^T$$

#### Theorem
If $\lambda$ is a non-zero eigenvalue of $AA^T$, then it is also an eigenvalue of $A^TA$.

[Proof]
Given: $$AA^Tv=\lambda v$$
$$\implies A^T(AA^Tv)=\lambda A^Tv$$
$$\implies A^TAu=\lambda u \hspace{.1in}(\because A^Tv=u)$$
So, $\lambda$ is an eigenvalue of $A^TA$ if $u\neq {0}$. Because we know that $$AA^Tv=\lambda v\neq 0$$
We are for sure that $A^Tv=u \neq 0$

Now, let’s show that if $\lambda$ is a non-zero eigenvalue of $A^TA$ then $\lambda$ is an eigenvalue of $AA^T$.

Let, $$A^TAu=\lambda u$$
$$\implies AA^TAu=\lambda Au$$
$$\implies AA^Tv=\lambda v \hspace{.1in} (\because Au=v \neq 0)$$

#### Theorem
Eigenvalues of $AA^T$ (or $A^TA$) are non-negative.

[Proof]
Let $\lambda$ be an eigenvalue of $AA^T$ with eigenvector $v$.
$$\lvert \lvert A^Tv \rvert  \rvert ^2=\langle A^Tv,A^Tv \rangle =v^TAA^Tv=\langle v,AA^Tv \rangle  = \langle v,\lambda v \rangle $$
$$\to \lambda \langle v,v \rangle =\lambda \lvert \lvert v \rvert  \rvert ^2 \hspace{.1in} (v \neq 0)$$
$$\to \lambda = \frac{\lvert \lvert A^Tv \rvert  \rvert ^2}{\lvert \lvert v \rvert  \rvert^2 } \geq 0$$

#### Theorem
Let $\lambda$ be a positive eigenvalue of $AA^T$ with the unit eigenvector $p$. Then $\lambda$ is an eigenvalue of $A^TA$ with unit eigenvector
$$q= \frac{1}{\sigma}A^Tp,\hspace{.1in}\sigma=\sqrt{ \lambda }$$
Conversely, let $\lambda$ be a positive eigenvalue of $A^TA$ with (unit) eigenvector $q$. Then $\lambda$ is an eigenvalue of $AA^T$ with eigenvector
$$p= \frac{1}{\sigma}Aq, \hspace{.1in}\sigma=\sqrt{ \lambda }$$


[Proof]
Compute
$$A^TAq= A^TA\left(  \frac{1}{\sigma} A^Tp \right)= \frac{1}{\sigma} A^TAA^Tp = \frac{1}{\sigma}A^T(\lambda p)= \sqrt{  \lambda } A^Tp=\lambda q$$

Now compute,
$$AA^Tp=AA^T\left( \frac{1}{\sigma} Aq \right) = \frac{1}{\sigma} AA^TAq = \frac{1}{\sigma }A(\lambda q) = \sqrt{ \lambda }Aq = \lambda p$$


We can verify the norms,
$$\lvert \lvert q_{k} \rvert  \rvert ^2= \frac{1}{\sigma_{k}^2}\langle A^Tp_{k},A^Tp_{k} \rangle = \frac{1}{\sigma_{k}^2}\langle p_{k},AA^Tp_{k} \rangle = \frac{1}{\sigma_{k}^2}\langle p_{k},\lambda_{k}p_{k} \rangle = 1  $$

Moreover,
$$\langle q_{i},q_{j} \rangle = \frac{1}{\sigma_{i}\sigma_{j}}\langle A^Tp_{i},A^Tp_{j} \rangle =\frac{1}{\sigma_{i}\sigma_{j}}\langle AA^Tp_{i},p_{j} \rangle  = \frac{\lambda_{i}}{\sigma_{i}\sigma_{j}}\langle p_{i},p_{j} \rangle = 0$$

#### Proposition
Let $A \in \mathbb{R}^{m\times n}$, then
$$N(AA^T)=N(A^T), N(A^TA)=N(A)$$

[Proof]
Let’s first show that $N(AA^T)=N(A^T)$, and let $v \in N(A^T)$
$$A^Tv=0$$
$$\to AA^Tv=A 0=0 \implies v \in N(AA^T)$$
$$\therefore N(A^T) \subseteq N(AA^T)$$

Now, let $v \in N(AA^T)$,
$$\lvert \lvert AA^Tv \rvert  \rvert ^2=\langle A^Tv,A^Tv \rangle =\langle AA^Tv,v \rangle = 0 \to A^Tv = 0 $$
$$\implies v \in N(A^T) \implies N(AA^T) \subseteq N(A^T)$$
$$\therefore N(AA^T)=N(A^T)$$

And replacing $$AA^T \to (AA^T)^T = A^TA, A^T \to (A^T)^T = A$$
we can show that the other direction is satisfied.

#### Full Construction
1. Calculate the nonzero eigenvalues of $AA^T$ (or $A^TA$): $\lambda_{1}\geq \cdots \geq \lambda_{r} > 0$, set $\sigma_{i}= \sqrt{ \lambda_{i} }$ and form $$\Sigma = \begin{bmatrix}
\sigma_{1} &  &  & 0 \\
 & \ddots &  & \vdots \\
 &  & \sigma_{r} & 0 \\
0 & \cdots & 0 & 0 
\end{bmatrix}$$
2. Calculate the orthonormal eigenvectors $p_{1},\cdots,p_{r}$ of $AA^T$ corresponding to $\lambda_{1},\cdots,\lambda_{r}$ and calculate $q_{i}= \frac{1}{\sigma_{i}}A^Tp_{i}$ for $i = 1,\cdots,r$.
3. Calculate the basis $p_{r+1},\cdots,p_{m}$ of $N(A^T)$.
4. Calculate the basis $q_{r+1},\cdots,q_{n}$ of $N(A)$.
5. Set$$P=\begin{bmatrix}
p_{1} & \cdots & p_{m}
\end{bmatrix}, \hspace{.2in}Q=\begin{bmatrix}
q_{1} & \cdots & q_{n}
\end{bmatrix}$$ Then, we have $$A=P\Sigma Q^T$$
Note that vectors $p_{1},\cdots,p_{m}$ form a basis of $\mathbb{R}^m$ and the vectors $q_{1},\cdots,q_{n}$ form a basis of $\mathbb{R}^n$.

Let’s check that,
$$AQ=P\Sigma$$
We have
$$AQ=\begin{bmatrix}
Aq_{1} & \cdots & Aq_{r} & Aq_{r+1} & \cdots & Aq_{n}
\end{bmatrix}$$
$$=\begin{bmatrix}
\sigma_{1} p_{1} & \cdots & \sigma_{r}p_{r} & 0 & \cdots & 0
\end{bmatrix}$$
$$P\Sigma=\begin{bmatrix}
p_{1} & \cdots & p_{m}
\end{bmatrix}\begin{bmatrix}
\sigma_{1} &  &  & 0 \\
 & \ddots &  & \vdots \\
 &  & \sigma_{r} & 0 \\
0 & \cdots & 0 & 0 
\end{bmatrix}=\begin{bmatrix}
\sigma_{1}p_{1} & \cdots & \sigma_{r}p_{r} & 0 & \cdots & 0
\end{bmatrix}$$

Note how one can also write this as 
$$A= \sum_{i=1}^r \sigma_{i}p_{i}q_{i}^T$$

###### Example
Calculate the SVD of 
$$A=\begin{bmatrix}
1 & 0 & 1 \\
-1 & 1 & 0
\end{bmatrix}$$

$$AA^T=\begin{bmatrix}
1 & 0 & 1 \\
-1 & 1 & 0
\end{bmatrix}\begin{bmatrix}
1 & -1 \\
0 & 1 \\
1 & 0
\end{bmatrix} = \begin{bmatrix}
2 & -1 \\
-1 & 2
\end{bmatrix}$$
$$\det(AA^T-\lambda I) = (2-\lambda)^2-1=\lambda^2-4\lambda+3 = 0$$
$$\lambda_{1}=3,\lambda_{2}=1 \to \sigma_{1}=\sqrt{ 3 },\sigma_{2}=1$$
$$p_{1} : N(AA^T-3I) = N \left( \begin{bmatrix}
-1 & -1 \\
-1 & -1
\end{bmatrix}\right) = \text{span}\left\{ \begin{bmatrix}
1  \\
-1
\end{bmatrix} \right\}  \to p_{1}= \begin{bmatrix}
\frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }}
\end{bmatrix} $$
$$p_{2}:N(AA^T-I) = N\left( \begin{bmatrix}
1 & -1 \\
-1 & 1
\end{bmatrix} \right) = \text{span}\left\{ \begin{bmatrix}
1\\1
\end{bmatrix} \right\} \to p_{2}=\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$
$$q_{1}= \frac{1}{\sigma_{1}}A^Tp_{1}=\frac{1}{\sqrt{ 3 }}\begin{bmatrix}
1 & -1 \\
0 & 1  \\
1 & 0
\end{bmatrix}\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }}
\end{bmatrix} = \frac{1}{\sqrt{ 3 }} \begin{bmatrix}
\sqrt{ 2 } \\
-\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{bmatrix} = \begin{bmatrix}
\frac{2}{\sqrt{ 6 }} \\
-\frac{1}{\sqrt{ 6 }} \\
\frac{1}{\sqrt{ 6 }}
\end{bmatrix}$$
$$q_{2}= \frac{1}{\sigma_{2}}A^Tp_{2}=\begin{bmatrix}
1 & -1 \\
0 & 1  \\ 
1 & 0
\end{bmatrix}\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{bmatrix} = \begin{bmatrix}
0 \\
\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$
$$q_{3}=\begin{bmatrix}
-\frac{1}{\sqrt{ 3 }} \\
-\frac{1}{\sqrt{ 3 }} \\
\frac{1}{\sqrt{ 3 }}
\end{bmatrix}$$

Then,
$$P=\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }}
\end{bmatrix},\Sigma=\begin{bmatrix}
\sqrt{ 3 } & 0 & 0 \\
0 & 1 & 0
\end{bmatrix},Q=\begin{bmatrix}
\frac{2}{\sqrt{ 6 }} & 0 & -\frac{1}{\sqrt{ 3 }} \\
-\frac{1}{\sqrt{ 6 }} & \frac{1}{\sqrt{ 2 }} & -\frac{1}{\sqrt{ 3 }} \\
\frac{1}{\sqrt{ 6 }} & \frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 3 }}
\end{bmatrix}$$

##### Properties of SVD

- $R(A) =\text{span}\left\{ p_{1},\cdots ,p_{r} \right\}$
Since $\Sigma$ only has the first $r$ rows as non-zeros in the diagonal.

 - $R(A)^\perp = \text{span}\left\{ p_{r+1},\cdots,p_{m} \right\}$
Since $\text{span}\left\{ p_{r+1},\cdots,p_{m} \right\}$ is the orthogonal complement of $\text{span}\left\{ p_{1},\cdots,p_{r} \right\}$ we can see that $R(A)^\perp = \text{span}\left\{ p_{1},\cdots,p_{r} \right\}^\perp=\text{span}\left\{ p_{r+1},\cdots,p_{m} \right\}$.

- $N(A)=\text{span}\left\{ q_{r+1},\cdots,q_{n} \right\}$
Since only the first $r$ columns of $\Sigma$ is non-zero we have to have the first $r$ rows to be zero. This can be formulated from making the first $r$ rows of $Q^Tv$ be zero.
Thus, $N(A)=\text{span}\left\{ q_{r+1},\cdots,q_{n} \right\}$.

- $R(A^T)=N(A)^\perp=\text{span}\left\{ q_{1},\cdots,q_{r} \right\}$
Similar to the second argument, the orthogonal complement of $N(A)$ would be $\text{span}\left\{ q_{r+1},\cdots,q_{n} \right\}^\perp=\text{span}\left\{ q_{1},\cdots,q_{r} \right\}$.

- $\text{rank}(A)=r$
$\text{dim}(A)=\text{rank}(R(A)) = \text{rank}(R(P\Sigma Q^T)) =\text{dim}(R(P))=\text{dim}(P)=r$.

#### Theorem
We have that $\lvert \lvert A \rvert \rvert=\sigma_{1}$, that is, the largest singular value. If $A$ is invertible, then $\lvert \lvert A^{-1} \rvert \rvert = \sigma_{n}^{-1}$ and $\text{cond}(A) = \frac{\sigma_{1}}{\sigma_{n}}$.

[Proof]
We have that
$$A=\text{max}_{{\lvert \lvert x \rvert  \rvert =1}}\lvert \lvert Ax \rvert  \rvert =\text{max}_{\lvert \lvert x \rvert  \rvert =1}\lvert \lvert P\Sigma Q^Tx \rvert  \rvert = \text{max}_{\lvert \lvert y \rvert  \rvert =1}\lvert \lvert \Sigma y \rvert  \rvert =\sigma_{1}$$
$$A^{-1}=\text{max}_{\lvert \lvert x \rvert  \rvert =1}\lvert \lvert A^{-1}x \rvert  \rvert  = \frac{1}{\text{min}_{\lvert \lvert y \rvert  \rvert =1}\lvert \lvert Ay \rvert  \rvert }=\frac{1}{\sigma_{n}}=\sigma_{n}^{-1}  $$

And thus,
$$\text{cond}(A) = \frac{\sigma_{1}}{\sigma_{n}}$$

#### Next Lecture [[Lecture 21]]
