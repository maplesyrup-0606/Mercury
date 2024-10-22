### Convolutional Neural Networks (CNN)
![[Screenshot 2024-10-15 at 11.45.58 AM.png]]

Basic operations in CNNs are convolutions (with learned linear filters) followed by non-linear functions. → Resulting in non-linear filters.


### Linear Filters: Matrix Form
$$\begin{bmatrix}
80 & 80 & 90 \\
80 & 80 & 90
\end{bmatrix} = \frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}\oplus \begin{bmatrix}
90 & 90 & 90 & 90 & 90 \\
90 & 90 & 90 & 90 & 90  \\
90 & 0 & 90 & 90 & 90  \\
90 & 90 & 90 & 90 & 90 
\end{bmatrix}$$

Where the first matrix on the RHS is the filter and the second matrix on the RHS is the image.

And this becomes,
![[Screenshot 2024-10-15 at 11.50.52 AM.png]]

For image, stack the rows into one column. 
For filter, make each row the same size as the vectorized image, and place the numbers based on how we compute the correlation.

#### Properties of Linear Filters
**Superposition**: Let $F_{1},F_{2}$ be digital filters,
$$(F_{1}+F_{2})\otimes I(X,Y)=F_{1}\otimes I(X,Y)+F_{2}\otimes I(X,Y)$$
**Scaling**: Let $k$ now be a scalar,
$$(kF)\otimes I(X,Y)=F\otimes (kI(X,Y))=k(F\otimes I(X,Y))$$
**Shift Invariance**: Output is local (no dependence on absolute position).

A shift invariant function would look like,
![[Screenshot 2024-10-15 at 11.55.53 AM.png]]

Where a shift variant function would look like,
![[Screenshot 2024-10-15 at 11.56.09 AM.png]]

An operation is **linear** if it satisfies both **superposition** and **scaling**. → ***Any linear, shift invariant operation can be expressed as convolution.***

**Summary**
==Any operation that satisfies superposition and scaling is linear. Any linear operation that is shift invariant can be expressed as a convolution (correlation as well). Convolution unlike correlation satisfies associativity and symmetry.==

## Smoothing
Smoothing (or blurring):
- Captured images are naturally **noisy**, smoothing allows removal of noise.
- It is important for **re-scaling** of images, to avoid sampling artifacts.
- Fake image **defocus** for artistic effects.

#### Smoothing with a Box Filter
$$\frac{1}{9}\begin{bmatrix}
1 & 1 & 1  \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}$$

**Filter has equal positive values that sum up to 1.**
→ Overall brightness doesn’t change.

Replaces each pixel with the average of itself and its local neighborhood.

A **Box Filter** is also referred to as **average / mean** filter.

If we make the box filter larger (width increases) → We average more with each pixels contribution being smaller and hence a blurrier image.
![[Screenshot 2024-10-15 at 12.15.53 PM.png]]

*However, smoothing with a box doesn’t model lens defocus well*
- Smoothing with a box filter depends on direction.
- Image in which the center point is 1 and every other point is 0 (simple point).

$$\frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}\otimes \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0  \\
0 & 0 & 0 & 0 & 0  \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}=\begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & \frac{1}{9} & \frac{1}{9} & \frac{1}{9} & 0 \\
0 & \frac{1}{9} & \frac{1}{9} & \frac{1}{9} & 0 \\
0 & \frac{1}{9} & \frac{1}{9} & \frac{1}{9} & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}$$

It is blurring in a rectangular matter, not representing the focus that well.
The box filter will enhance the vertical / horizontal aspect rather than blurring irrespective of its orientation.

***The box filter is not rotationally invariant. (At least for angles not in 90 degrees).***

#### Pillbox filter
Smoothing with a circular pillbox is a better model for defocus (in geometric options).

$$f(x,y)=\frac{1}{\pi r^2}
\{\begin{array}{ll}
  
      0 & x^2+y^2 \leq r^2 \\
      1 & \text{otherwise} \\
  
\end{array}
$$

The scaling constant ensures that the area of the filter is one.
![[Screenshot 2024-10-15 at 3.20.15 PM.png]]
It smooths out in all directions equally.

***Pillbox is rotationally symmetric, but not separable. And does model geometric out-of-focus blurring well.***

Even though the function is normalized to 1, in the continuous domain, sampling and evaluating a discrete set of points corresponding to the filter will not produce an array that sums up to 1. → Need to normalize the filter.
## Gaussian Filter
The **Gaussian** is a good general smoothing model.
- For phenomena.
- Whenever the Central Limit Theorem applies.

***Idea: Weight contributions of pixels by spatial proximity (nearness).***

And is often used for resizing as well.

![[Screenshot 2024-10-15 at 3.23.33 PM.png]]
$$G_{\sigma}(x,y)=\frac{1}{2\pi \sigma^2}e^{-(x^2+y^2)/2\sigma^2}$$

The standard deviation, $\sigma$, tells how much function is spread out.
- Defines a continuous 2D function.
- Discretize it by evaluating this function on the discrete pixel positions to obtain a filter.

If,
- $\sigma$ is larger: there is more blur since the center loses concentration and outer gains more.
- $\sigma$ is smaller: there is less blur since the center has way more concentration than the outer.

**Gaussian filter vs. Box filter**
![[Screenshot 2024-10-15 at 3.27.27 PM.png]]

What is the problem of this filter?
![[Screenshot 2024-10-15 at 3.28.39 PM.png]]
- Filter does not sum up to 1 → due to discretization, need to normalize.
- Truncated too much, 
  ![[Screenshot 2024-10-15 at 3.29.20 PM.png]]

So it needs to be **normalized** and capture $\pm 2\sigma$ to reliable.
In general, we want the Gaussian filter to capture $\pm 3\sigma$, for $\sigma=1 \implies 7\times {7} \text{ filter}$.


For instance, with $\sigma = 5$ what filter size would be appropriate?
We want $5\times 3$ on both top bottom and left right → $31\times 31$.

Trick, if $\sigma$ is given the filter would be $6 \times \sigma$ rounded up to the next odd integer.

## Efficiency
A 2D function of $x$ and $y$ is **separable** if it can be written as the product of two functions, one a function only of $x$ and the other a function of only $y$.

**Both** the **2D box filter** and the **2D Gaussian filter** are separable.

Both can be implemented as two 1D convolutions:
- First, convolve each row with a 1D filter.
- Then, convolve each column with a 1D filter.

==2D Gaussian is the only (non trivial) 2D function that is both separable and rotationally invariant. Also, convolving two Gaussians would result in another Gaussian.==

![[Screenshot 2024-10-15 at 3.36.00 PM.png]]

##### How to know separability
If a 2D filter can be expressed as an outer product of two 1D filters → it is separable. Alternatively, if the rank of the filter is 1, then the filter is separable.
![[Screenshot 2024-10-15 at 3.38.06 PM.png]]

#### Separability of Gaussian Filter
$$G_{\sigma}(x,y)=\frac{1}{2\pi \sigma^2}e^{-(x^2+y^2)/2\sigma^2}$$
$$=\left( \frac{1}{\sqrt{ 2\pi }\sigma} e^{-x^2/2\sigma^2} \right)\left(\frac{1}{\sqrt{ 2\pi }\sigma} e^{-y^2/2\sigma^2}\right)$$
Can be expressed of two functions, respectively in $x$ and $y$.
![[Screenshot 2024-10-15 at 4.19.29 PM.png]]

Ex)
$$\frac{1}{16}\begin{bmatrix}
1 \\
4 \\
6 \\
4 \\
1
\end{bmatrix} \otimes  \frac{1}{16}\begin{bmatrix}
1 & 4 & 6 & 4 & 1
\end{bmatrix} =\frac{1}{256}\begin{bmatrix}
1 & 4 & 6 & 4 & 1 \\
4 & 16 & 24 & 16 & 4 \\
6 & 24 & 36 & 24 & 6 \\
4 & 16 & 24 & 16 & 4 \\ 
1 & 4 & 6 & 4 & 1 
\end{bmatrix}$$

Now using separability, at each pixel there are only $2m$ multiplications and there are $n^2$ pixels.
$$\therefore O(2m\times n^2)$$

other separable filters,
![[Screenshot 2024-10-15 at 4.21.36 PM.png]]


|                    | Box Filter | Pillbox Filter | Gaussian Filter |
| ------------------ | ---------- | -------------- | --------------- |
| Rotation Invariant | ❌          | ✅              | ✅               |
| Separable          | ✅          | ❌              | ✅               |


#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 4|Lecture 4]]
