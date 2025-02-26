#### Invariance & Equivariance
- Invariance: a mathematical object remains unchanged after operations or transformations of a certain type are applied to the objects. $$f(X)=f(g(X))$$
- Equivariance: Applying a transformation and computing the function produces the same result as computing the function and applying the transformation. $$g(f(X))=f(g(X))$$

#### Convolution
##### 1D Convolutions
Consider the following,
$$\begin{aligned}
x\quad &=\underbrace{ \begin{bmatrix}
1 & 4 & 0 & 2 & 1 & 3
\end{bmatrix} }_{ n } \\ 
h\quad &= \underbrace{ \begin{bmatrix}
2 & 0 & -1
\end{bmatrix} }_{ m } \\ 
y\quad&= \underbrace{ \begin{bmatrix}
2 & 6 & -1 & 1
\end{bmatrix} }_{ n-m+1 }
\end{aligned}  $$
Convolution in Deep-Learning is actually Cross-Correlation in Math:
$$(h * t)(t) = \int_{-\infty}^\infty h(\tau)x(t+\tau)d\tau$$
thus the above would be represented as,
$$y=h*x \quad y[i] =\sum_{j=1}^m h_{j}x_{i+j-1}$$

What if we want to maintain the same shape as the input? ==Padding!==
$$\begin{aligned}
x\quad&=\begin{bmatrix}
\mathbf{0} & 1 & 4 & 0 & 2 & 1 & 3 & \mathbf{0} 
\end{bmatrix} \\ 
h\quad &= \begin{bmatrix}
2 & 0 & -1 
\end{bmatrix} \\ 
y\quad&= \begin{bmatrix}
-4 & 2 & 6 & -1 & 1 & 2
\end{bmatrix}
\end{aligned}$$



What if we want to make the output smaller compared to the input? ==Stride==
$$\begin{aligned}
x\quad&=\begin{bmatrix}
\mathbf{0} & 1 & 4 & 0 & 2 & 1 & 3 & \mathbf{0} 
\end{bmatrix} \\ 
h\quad &= \begin{bmatrix}
2 & 0 & -1 
\end{bmatrix} \\ 
y\quad&= \begin{bmatrix}
-4 & 6 & 2
\end{bmatrix}\quad \text{stride= } 3
\end{aligned}$$

Given input size $n$, and filter size $m$, padding $P$ and stride $S$,
$$\text{output: } \left\lfloor  \frac{n+2P-m}{S}  \right\rfloor + 1$$

##### Matrix Multiplication View
$$y=h*x=\begin{bmatrix}
h_{1} & \cdots & h_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & h_{m} & 0 & \cdots & \cdots & \cdots & 0 \\
0 & h_{1} & \cdots & h_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & h_{m-1} & h_{m} & \cdots & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots  \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
0 & 0 & \cdots & \cdots & h_{1} & \cdots & h_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & h_{m} & 0 \\
0 & 0 & \cdots & \cdots & 0 & h_{1}\cdots & \cdots & h_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & h_{m}
\end{bmatrix}\begin{bmatrix}
0 \\
\vdots \\
x_{1} \\
x_{2} \\
\vdots\\
x_{n} \\
\vdots \\
0
\end{bmatrix}$$

or we can do this which gives a Toeplitz matrix,
$$y^T = (h*x)^T$$
$$=\begin{bmatrix}
h_{1} & \cdots & h_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & h_{m}
\end{bmatrix}\begin{bmatrix}
0 & 0 & \cdots & x_{1}&\cdots & x_{n-\left\lfloor  \frac{m}{2}  \right\rfloor -1} & x_{n-\left\lfloor  \frac{m}{2}  \right\rfloor } \\
\vdots & \vdots & \cdots & \vdots & \cdots & \vdots & \vdots \\
0 & x_{1} & \cdots & x_{\left\lfloor  \frac{m}{2}  \right\rfloor } &  \cdots & x_{n-2} & x_{n-1} \\
x_{1} & x_{2} & \cdots & x_{\left\lfloor  \frac{m}{2}  \right\rfloor +1} & \cdots & x_{n-1} & x_{n} \\
x_{2} & x_{3} & \cdots & x_{\left\lfloor  \frac{m}{2}  \right\rfloor +2} & \cdots & x_n & 0 \\
\vdots & \vdots & \cdots & \vdots & \cdots & \vdots & \vdots  \\
x_{m-\left\lfloor  \frac{m}{2}  \right\rfloor } & x_{m-\left\lfloor  \frac{m}{2}+1  \right\rfloor } & \cdots & x_{m} & \cdots & 0 & 0
\end{bmatrix}$$
==This equivalence is the same for 2D+ convolutions, and this version is typically implemented on GPUs.==

##### Translation Equivariance
Consider a Toeplitz matrix: circulant matrix that must be a squared matrix.
![[Screenshot 2025-02-11 at 6.05.26 PM.png]]
Convolution with padding will look like the above.

![[Screenshot 2025-02-11 at 6.08.09 PM.png]]

If this is applied to the Filter,
![[Screenshot 2025-02-11 at 6.10.01 PM.png]]
we can see that circulant matrices are commutative.  → $\textbf{C(w)S}^T=\textbf{S}^T\textbf{C(w)}$.

==Convolution is translation equivariant, which also holds for higher dimensions as well.==

##### 2D Convolution
![[Screenshot 2025-02-11 at 6.15.37 PM.png]]

With no padding, the output would reduce the dimensionality $\left\lfloor  \frac{K}{2}   \right\rfloor$ on both sides, hence 
$$\mathbf{y}_{i,j}=\sum_{m=1}^K\sum_{n=1}^K W_{m,n}\mathbf{x}_{i+m-\left\lfloor  \frac{K}{2}  \right\rfloor ,j+n-\left\lfloor  \frac{K}{2}  \right\rfloor }$$

2D Convolution with multiple input channels,
![[Screenshot 2025-02-11 at 6.23.02 PM.png]]

What would the dimensionality of the output be? Since we convolve around $c$ channels the output would have a depth of $1$.

Also, considering no padding our width would become $W \to W-w+1$. And similarly for height, $H \to H-h+1$.
![[Screenshot 2025-02-11 at 6.24.30 PM.png]]
$$(W-w+1)\times(H-h+1)\times{1}$$

If were to have multiple filters (kernels),
![[Screenshot 2025-02-11 at 6.25.07 PM.png]]
since we apply the $D$ filter (kernels), we have a depth of $D$ on the output,
$$(W-w+1) \times (H-h+1) \times D$$

If we take a look at the effects of convolution,
![[Screenshot 2025-02-11 at 6.27.57 PM.png]]

#### Next Lecture [[Lecture 6]]
