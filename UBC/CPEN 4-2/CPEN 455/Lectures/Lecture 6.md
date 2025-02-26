#### 2D Transposed Convolution
We know convolution can reduce input size, e.g., with stride > 1. Can any convolution operator enlarge the input size? → Transposed Convolution.

Suppose we have a 2D convolution (3 x 3 kernel),
![[Screenshot 2025-02-11 at 6.43.40 PM.png]]
If we look at the left one, we’re applying a 3 x 3 filter with no padding and default stride of 1. Resulting a size of $(4 - 3 + 1) \times (4-3+1) = 2 \times 2$. On the other hand, if we look at the right one, we’re convolving with a 3 x 3 filter with stride 1 and padding 2 resulting in $\left(  \left\lfloor  \frac{2 + 2\cdot 2 - 3}{1}  \right\rfloor+1   \right) \times \left(  \left\lfloor  \frac{2 + 2\cdot 2 - 3}{1}  \right\rfloor+1   \right) = (4 \times 4)$.

- Convolution and its transposed are mutually inverse w.r.t. with the shapes of the output. **Not to the values!** 
- Convolution and Deconvolution are mutually inverse w.r.t. values of the input and output.

Or we can pad zeros in between the 3 x 3 shape below,
![[Screenshot 2025-02-11 at 7.01.56 PM.png]]
- In the above example, we are upsampling, but we can see that the same location is now a contribution of different cells. We are aggregating information. Specifically, in this example, each resultant cell is consisted of the computation of two cells at a time.
- In practice, we don’t pad zeros in between since it is computationally high in cost. We rather leverage the gradient of convolution.

Consider $$\mathbf{y}=W\mathbf{x}\quad\quad W\in \mathbb{R}^{m\times n},\mathbf{x}\in \mathbb{R}^n,\mathbf{y}\in \mathbb{R}^m$$
$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}}=W \to \hat{\mathbf{x}}=\left( \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \right)^T\mathbf{y} \in \mathbb{R}^{n \times m}\times \mathbb{R}^{m}=\mathbb{R}^n$$
as required!
- We need in general, to specify the stride and padding of convolution.
- For transposed convolution, stride is always 1 and we sometimes need (output) padding.

![[Screenshot 2025-02-11 at 7.34.27 PM.png]]
In both cases, the gradients have the same shape in im2patch implementation, so to distinguish them and output correct shapes in their transposed convolutions, output padding on one side is added in the 2nd case.

#### Dilated Convolution
We are aware that the kernel size decides what elements are used in convolution at one location, can we also enlarge the kernel size without increasing the number of parameters?

Suppose we have a 2D convolution,
![[Screenshot 2025-02-11 at 7.39.22 PM.png]]
with a 3 x 3 kernel → 9 weights. We want to enlarge the kernel without changing the number of parameters.

Now let’s assume dilation = 2, 
![[Screenshot 2025-02-11 at 7.41.32 PM.png]]
On the input, we are spacing out the kernel (effectively to a 5 x 5), and convolving. 
We can see that with dilating kernels, we are effectively increasing the receptive field (the region of input that affects the output).

#### Grouped Convolution
Our new question is can we maintain the shame shaped input and output with a fewer number of parameters?

Consider a convolutional layer applied to shape $H \times W \times c_{1}$
![[Screenshot 2025-02-11 at 7.50.31 PM.png]]
and we have $c_2$ filters with size $h_{1} \times w_{1} \times c_{1}$.

What are the total number of parameters here? 

We have $c_{1} \times w_{1} \times h_{1} + 1$ parameters per filter. Hence, with $c_{2}$ filters, we have a total of $$c_{2} \times (h_{1} \times w_{1} \times c_{1} + 1)$$
parameters.

Now let’s switch to a grouped convolutional layer applied to the same input.
![[Screenshot 2025-02-11 at 7.52.59 PM.png]]
Then, the number of parameters are
$$c_{2} \times \left( \frac{c_{1}}{2} \times h_{1} \times w_{1}  + 1\right)$$
hence we reduced the number of parameters while keeping the shape of the input and output.

Why would we do this?
- We can learn different features when applying two different features which a much more computationally efficient method!

Let’s say that we have $G$ groups, then the number of parameters become,
$$c_{2} \times \left( \frac{c_{1}}{G} \times h_{1} \times w_{1}  + 1 \right)$$

#### Separable Convolution
We can also incorporate separable convolution with group convolution to reduce the number of parameters while maintaining the shape of the input and the output.

If the filter is rank 1, we can separate into a matrix outer-product, for instance,
$$\begin{bmatrix}
3 & 6 & 9 \\
4 & 8 & 12 \\
5 & 10 & 15
\end{bmatrix}= \begin{bmatrix}
3 \\
4 \\
5
\end{bmatrix} \times \begin{bmatrix}
1 & 2 & 3
\end{bmatrix}$$
![[Screenshot 2025-02-11 at 8.10.16 PM.png]]

Spatial separable are rank one and cannot represent full-rank kernels → they are limited in terms of expressiveness.

##### Depth-wise Separable Convolution
**Depth-wise Spatial Convolution**
![[Screenshot 2025-02-11 at 8.17.34 PM.png]]

**Point-wise 1 x 1 Convolution**
![[Screenshot 2025-02-11 at 8.17.53 PM.png]]

The main purpose is the reduction of the number of parameters.

For instance, let’s look at the depth-wise case,
Each filter has $$5\times 5 \times 1 + 1 = 26 \text{ parameters}$$
So in total,
$$26 \times 3 = 78 \text{ parameters}$$

In the second case, we have a total of 256 filters,
$$256 \times (1 \times 1 \times 3 +1) = 1024 \text{ parameters}$$

#### Pooling
This is similar to convolution in a sense but differs in that we use a pooling operator (no weights),

Consider max pooling with stride 2,
$$\begin{bmatrix}
1 & 0 & 3 & 5 \\
3 & 4 & 2 & 2 \\
1 & 3 & 3 & 9 \\
5 & 7 & 8 & 4
\end{bmatrix} \to \begin{bmatrix}
4 & 5 \\
7 & 9
\end{bmatrix}$$
If we did mean pooling with stride 2,
$$\begin{bmatrix}
1 & 0 & 3 & 5 \\
3 & 4 & 2 & 2 \\
1 & 3 & 3 & 9 \\
5 & 7 & 8 & 4
\end{bmatrix} \to \begin{bmatrix}
2 & 3 \\
4 & 6
\end{bmatrix}$$

This gives us permutation invariance.

#### Example Architectures
Let’s look at an example CNN,
![[Screenshot 2025-02-11 at 8.36.04 PM.png]]

Consider the case that the background doesn’t change and one only shifts the foreground object, then pooling will give you shift-invariance.

![[Screenshot 2025-02-11 at 8.37.47 PM.png]]

