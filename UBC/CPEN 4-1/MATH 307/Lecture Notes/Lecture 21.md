### Principal Component Analysis (PCA)
The setup is when we have data points $x_{1},\cdots,x_{n} \in \mathbb{R}^p$ where we generally have $n \gg p\gg 2$. We also assume that $\sum_{i=1}^nx_i=0$. We wish to find the direction $w_{1}\in \mathbb{R}^p$ that captures the **most information**.

That is, we want to find $w_{1}$ such that
$$\sum_{i=1}^n \lvert \lvert \text{proj}_{w_{1}}(x_{i}) \rvert  \rvert ^2=\sum_{i=1}^n \lvert \langle w_{1},x_{i} \rangle  \rvert ^2$$
is maximized.

==The idea is that if we have a dataset in 2d where most of the variation of the dataset is on one direction, we might as well focus on the variability of the data on this direction.==

$$\sum_{i=1}^n \lvert \lvert \text{proj}_{w_{1}}(x_{i}) \rvert  \rvert ^2 = \sum_{i=1}^n\lvert \langle w_{1},x_{i} \rangle  \rvert ^2 = \left\lvert \left\lvert \begin{bmatrix}
\langle w_{1},x_{1} \rangle  \\
\langle w_{1},x_{2} \rangle   \\
\vdots \\
\langle w_{1},x_{n} \rangle 
\end{bmatrix} \right\rvert  \right\rvert^2 $$
$$=\left\lvert \left\lvert \begin{bmatrix}
x_{1}^T \\
x_{2}^T \\
\vdots \\
x_{n}^T
\end{bmatrix}w_{1} \right\rvert  \right\rvert^2=\lvert \lvert Aw_{1} \rvert  \rvert ^2 $$

#### Definition of first weight vector
The first weight vector of $A$, denoted as $w_{1}\in \mathbb{R}^p$ is the unit vector that maximizes $\lvert \lvert Aw_{1} \rvert \rvert^2$.

#### Theorem
Let $A=P\Sigma Q^T$. Then $w_{1}=q_{1}$ where $q_{1}$ is the first column of $Q$.

[Proof]
We know that $\lvert \lvert A \rvert \rvert= \text{max}_{\lvert \lvert x \rvert \rvert=1}\lvert \lvert Ax \rvert \rvert=\sigma_{1}$ and we wish to find such $x$. By orthonormality of the columns of $Q$, we have $Q^Tq_{1}=\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}$. Then, we calculate
$$Aq_{1}=P\Sigma Q^Tq_{1}=\sigma_{1}p_{1}$$

Since $\lvert \lvert p_{1} \rvert \rvert=1$, we have that $\lvert \lvert Aq_{1} \rvert \rvert=\sigma_{1}\lvert \lvert p_{1} \rvert \rvert=\sigma_{1}$. As a result, $q_1$ is the vector that maximizes $\lvert \lvert Aq_{1} \rvert \rvert$ and we are done.

Given weight vectors $w_{1},\cdots,w_{k-1} \in \mathbb{R}^p$ of $A$, the k-th weight vector $w_k$ is the vector that maximizes $\lvert \lvert A_{k-1}w_{k} \rvert \rvert$ where $A_{k-1}$ is the projection of $A$ onto $\text{span}\left\{ w_{1},\cdots,w_{k-1} \right\}^\perp$. That is for each vector in the rows of $A$, we project it on $\text{span}\left\{ w_{1},\cdots,w_{k-1} \right\}^\perp$, then we put the resulting vectors to the rows of $A_{k-1}$. This is equal to 
$$A_{k-1}=A-A\begin{bmatrix}
w_{1} & \cdots & w_{k-1}
\end{bmatrix}\begin{bmatrix}
w_{1} & \cdots & w_{k-1}
\end{bmatrix}^T$$

###### Example
Find $w_{1}$ for data points
$$(-1,-2),(-1,-1),(-1,1),(0,0),(1,-1),(1,1),(1,2)$$

We first check that the data is centered and form
$$A=\begin{bmatrix}
-1 & -2 \\
-1 & -1 \\
-1 & 1 \\
0 & 0 \\
1 & -1 \\
1 & 1 \\
1 & 2
\end{bmatrix}$$

columns of which sums to zero. 

$$A^TA=\begin{bmatrix}
-1 & -1 & -1 & 0 & 1 & 1 & 1 \\
-2 & -1 & 1 & 0 & -1 & 1 & 2
\end{bmatrix}\begin{bmatrix}
-1 & -2 \\
-1 & -1 \\
-1 & 1 \\
0 & 0 \\
1 & -1  \\
1 & 1 \\
1 & 2
\end{bmatrix}=\begin{bmatrix}
6 & 4 \\
4 & 12
\end{bmatrix}$$

$$\det(A^TA-\lambda I)=(6-\lambda)(12-\lambda)-16 = \lambda^2-18\lambda+56$$
$$\sigma_{1}=\sqrt{ 14 }$$
$$N(A^TA - 14I) = N\left(\begin{bmatrix}
-8 & 4 \\ 4 & -2
\end{bmatrix}\right
) \to w_{1}=\frac{1}{\sqrt{ 5 }} \begin{bmatrix}
 1\\2
\end{bmatrix}$$

### Power Method
We can use the power method to find the largest eigenvalue. The idea is to use the property
$$A^k=PD^kP^{-1}$$

Let $\lambda_{1}$ be the dominant eigenvalue, which means that $\lvert \lambda_{1} \rvert > \lvert \lambda_{2} \rvert \geq \cdots$. We pick a random $x_{0} \in \mathbb{R}^n$. Then iterate for $k \geq 0$:
$$x_{k+1}= Ax_{k}$$
where $x_k$ should converge to the eigenvector corresponding to the dominant eigenvalue. But why? → Let $x_{0}=c_{1}v_{1}+\cdots+c_{n}v_{n}$ where $v_{1},\cdots,v_{n}$ are the eigenvectors of $A$. Then,
$$Ax_{0}=c_{1}\lambda_{1}v_{1}+\cdots+c_{n}\lambda_{n}v_{n}$$

Equivalently, then,
$$x_{k}=Ax_{k-1}=A^kx_{0}=c_{1}\lambda_{1}^kv_{1}+\cdots+c_{n}\lambda_{n}^kv_{n}$$
and since $\lvert \lambda_{1} \rvert^k \gg \lvert \lambda_{i} \rvert^k$ for any $i\neq {1}$, we will have that
$$x_{k}\approx c_{1}\lambda_{1}^kv_{1}$$

When we normalize at each step, like
$$x_{k+1}= \frac{Ax_{k}}{\lvert \lvert Ax_{k} \rvert  \rvert_{\infty} }$$
we approximate the eigenvector corresponding to the dominant eigenvalue

###### Example
Approximate the dominant eigenvalue of $A=\begin{bmatrix}1&1&0 \\ 1&1&1 \\ 0&1&1\end{bmatrix}$. Let $x_{0}=\begin{bmatrix}1\\1\\1\end{bmatrix}$. 

$$x_{1} =Ax_{0}=\begin{bmatrix}
2 \\
3 \\
2
\end{bmatrix}$$
$$x_{2}=Ax_{1}=\begin{bmatrix}
5\\7\\5
\end{bmatrix}$$
$$x_{3}=Ax_{2}=\begin{bmatrix}
12\\17\\12
\end{bmatrix}$$
$$x_{4}=Ax_{3}=\begin{bmatrix}
29\\41\\29
\end{bmatrix}$$
$$x_{5}=Ax_{4}=\begin{bmatrix}
70\\99\\70
\end{bmatrix}$$
$$\vdots$$

After normalizing,
$$v_{1}=\begin{bmatrix}
\frac{70}{99} \\
1 \\
\frac{70}{99}
\end{bmatrix}$$
Then,
$$Av_{1}=\begin{bmatrix}
1.7\\2.7\\1.7
\end{bmatrix}$$

And hence $\lambda_{1} \approx 2.7$

#### Next Lecture [[Lecture 22]]
