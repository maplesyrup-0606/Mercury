### Question 1
Consider when designing a digital filter to use for differentiation,

(A) Filter values are normalized to sum to one.
**False**

(B) Filter values are normalized to sum to zero.
**True**

(C) Filter values are normalized so that the sum of the squared values is one.
**False**

(D) Filter values whatever they are. Normalization is not required.
**False**

### Question 2
Canny edge detection.

(A) Different thresholds are needed to select edge points when linking edges forward or backward from the starting location.
**False**, it’s always in the direction orthogonal to gradient direction (along the edge).

(B) The use of two thresholds prevents gaps that would otherwise appear in the linked edge points.
**True**

(C) The $X$ and $Y$ directional derivatives each require a threshold when linking to new edge points.
**False**, we need a threshold for gradient magnitude.

### Question 3
Which is the Harris corner direction stable under?

(A) Image scaling.
**False**, under scaling (say we zoomed in) the edge might not appear as an edge.

(B) Image translation.
**True**, no matter what the shift is we can still detect.

(C) Image rotation.
**True**, the eigen vectors record the rotation.

### Question 4
Name four scene properties that would cause an edge in an image.

1. Surface reflection discontinuity.
2. Illumination discontinuity.
3. Orientation discontinuity.
4. Depth discontinuity. (due to Occlusions)

### Question 5
Consider the matrix, $\mathbf{M}$, defined at each image point where
$$M=\begin{bmatrix}
I_{x}^2 & I_{x}I_{y}  \\
I_{x}I_{y} & I_{y}^2
\end{bmatrix}$$
Note that $\mathbf{M}$ is not a covariance matrix because it is computed at a pixel and not over the neighborhood of a pixel. $\mathbf{M}$ can also be written as the outer product of the image gradient with itself,
$$\mathbf{M}=\begin{bmatrix}
I_{x} \\
I_{y}
\end{bmatrix}\begin{bmatrix}
I_{x} & I_{y}
\end{bmatrix}$$

(A) Assuming $I_x$ and $I_y$ are not both zero, what is the rank of $\mathbf{M}$.
We can make into row-echelon form with rank 1. Thus, rank is 1.

(B) Write expressions for the eigenvalues, $\lambda_{1},\lambda_{2}$ of $\mathbf{M}$.
$$\det(\mathbf{M}-\lambda I)=\det(\begin{bmatrix}
I_{x}^2-\lambda & I_{x}I_{y} \\
I_{x}I_{y} & I_{y^2}-\lambda
\end{bmatrix}) = (I_{x}^2-\lambda)(I_{y}^2-\lambda)-(I_{x}I_{y})^2$$
$$=\lambda^2-(I_{x}^2+I_{y}^2)\lambda=0$$
Therefore, $$\lambda_{1}=I_{x}^2+I_{y}^2,\hspace{.1in}\lambda_{2}=0$$
(C) Is the computation of $\mathbf{M}$ at each image point a linear operation? Is it shift invariant?
It is indeed shift invariant, but it is not linear.

Both $I_{x}^2,I_{x}I_{y},I_{y}^2$ are not linear.

(D) Could the computation of $\mathbf{M}$ at each image point be used for edge detection?
By using $\lambda_{1}$ we can develop a mechanism such that if $\lambda_{1}$ is below a certain threshold than it can detected as an edge. Since it is the magnitude of the gradient.

### Question 6
Consider constructing an $\mathbf{x}$-derivative filter of size 5. 

I would suggest,
$$\begin{bmatrix}
-0.5 & -1 & 0 & 1 & 0.5
\end{bmatrix}$$
First, of all it is symmetric and sums up to 0.
Second, the impact of closer pixels should be higher than further ones.