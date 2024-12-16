### Question 1: True / False

(A) A 2D (circular) pillbox filter is separable.
**False**, consider the following box filter,
$$\begin{bmatrix}
0 & 1 & 0 \\
1 & 1 & 1 \\
0 & 1 & 0
\end{bmatrix}$$
The rank is not 1, it is not separable.

(B) A 2D (circular) pillbox filter is rotationally invariant.
**True**, regardless of the rotation of the image it is invariant.
==But, a box filter is rotation variant.==

(C) Smoothing with a 2D (circular) pillbox models “blurring” that occurs when the lens it out of focus.
**True**, but a box filter isn’t.

==Not only a box filter, but Gaussian is also not a good model. Since it does a weighted evaluation based on distance, it would not model it properly.==

### Question 2

(A) Give a 3 x 3 linear filter that shifts an image 1 pixel downwards and also reduces the image brightness by 50%. Assume the filter is to be implemented as a correlation.

$$\frac{1}{2} \begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}$$
If we apply this filter, as a correlation, we fetch only the pixel above and reduce the intensity to half.

(B) Using the answer to part (A), what is the 3 x 3 linear filter if it is to be implemented as a convolution?

$$\frac{1}{2} \begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 1 & 0 
\end{bmatrix}$$

It is just a 180 degree rotation of the correlation filter.

### Question 3
Describe the situation where the filter values are

(A) normalized to sum one.
This would be the case when we do image smoothing, it is needed since we need to keep the overall intensity maintained.

(B) normalized to sum to zero.
This would be the case where we applying differentiation to find rate of change within an image, mainly for either edge detection or corner detection. This is needed since we are trying to get the change.

(C) normalized so that the filter magnitude is one.
This would be the case that the filter is used for template matching. In template matching, if we just do auto correlation, due to different intensities the value just might be high if we correlate with a high intensity patch. Thus, to reduce this and to find the similarity we would normalized to the l2-norm of the filter.

### Question 4

(A) Let $S$ be the number of multiplication operations required to convolve a Gaussian filter with an image of size $n \times n$ pixels. Assume that we use two separable 1D filters, each of length $6\sigma$. Give an expression for $S$ in terms of $\sigma$ and $n$.

We convolve twice with each 1D filter hence being,
$$2 \times 6\sigma \times n^2 = 12\sigma n^2$$

(B) Let $R$ be the number of multiplication operations required to convolve the equivalent single 2D Gaussian filter with an image of size $n \times n$ pixels, rather than using the two separable 1D filters. Give an expression for $R$ in terms of $\sigma$ and $n$.

$$(6\sigma)^2 \times n^2 = 36\sigma^2n^2$$

(C) Let $Q$ be the number of multiplication operations required to convolve a Gaussian filter with an image of size $n \times n$ pixels. Assuming we want to apply a single 2D Gaussian filter in FFT space, in accordance with Convolution Theorem, give an expression for $Q$ in terms of $\sigma$ and $n$. (Ignore the cost of converting to and from FFT space)

$$Q=n^2$$
In FFT space, it no longer depends on the filter.

### Question 5

(A) We can smooth an image by convolving the 1D vector [0.25, 0.5, 0.25] with the rows and then the columns of the image. Instead give the 2D matrix that combines these row and column operations into a single 3 x 3 filter that can be convolved with the image.

$$\begin{bmatrix}
0.25 \\
0.5 \\
0.25
\end{bmatrix} \otimes \begin{bmatrix}
0.25 & 0.5 & 0.25
\end{bmatrix}=\begin{bmatrix}
\frac{1}{16} & \frac{1}{8} & \frac{1}{16} \\
\frac{1}{8} & \frac{1}{4} & \frac{1}{8}  \\
\frac{1}{16} & \frac{1}{8} & \frac{1}{16}
\end{bmatrix}$$

(B) Following this smoothing, we wish to use the 1D filter [-1, 0, 1], applied to the rows of the image, to calculate the first central difference in the horizontal direction and thus estimate image gradients corresponding to vertical edges. Combine this 1D filter with your answer from part (a) to generate a single 2D filter that estimates the horizontal derivative of the smoothed image.

Let’s try convolving the two,
$$\begin{bmatrix}
1 & 0 & -1
\end{bmatrix} \otimes \begin{bmatrix}
\frac{1}{16} & \frac{1}{8} & \frac{1}{16} \\
\frac{1}{8} & \frac{1}{4} & \frac{1}{8}  \\
\frac{1}{16} & \frac{1}{8} & \frac{1}{16}
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0  & 0\\
0 & 0 & 0 & 0 & 0 & 0  & 0\\
0 & 0 & 1 & 0 & -1 & 0  & 0\\
0 & 0 & 0 & 0 & 0 & 0  & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix} \text{convolve} \begin{bmatrix}
\frac{1}{16} & \frac{1}{8} & \frac{1}{16} \\
\frac{1}{8} & \frac{1}{4} & \frac{1}{8}  \\
\frac{1}{16} & \frac{1}{8} & \frac{1}{16}
\end{bmatrix}$$
$$\begin{bmatrix}
\frac{1}{16}  & \frac{1}{8} & 0 & -\frac{1}{8} & -\frac{1}{16} \\
\frac{1}{8} & \frac{1}{4} & 0 & -\frac{1}{4} & -\frac{1}{8} \\
\frac{1}{16} & \frac{1}{8} & 0 & -\frac{1}{8} & -\frac{1.}{16}
\end{bmatrix}$$
For convolution.