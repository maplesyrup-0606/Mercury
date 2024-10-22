### Speeding up Convolution
Let $z$ be the product of two numbers, $x$ and $y$,
$$z=xy$$
Then taking logarithms of both sides gives us,
$$\ln z=\ln x+\ln y$$
Therefore,
$$z=e^{\ln z}=e^{\ln x+\ln y}$$
So at the expense of $ln$ and $e$ computations, multiplication can be reduced to addition.

Similarly, image processing operations can become cheaper in a transform domain,
![[Screenshot 2024-10-17 at 2.34.09 PM.png]]

#### Convolution Theorem
Let,
$$i'(x,y)=f(x,y)\otimes i(x,y)$$
then,
$$\mathcal{I}'(w_{x},w_{y})=\mathcal{F}(w_{x},w_{y})\cdot \mathcal{I}(w_{x},w_{{y}})$$

At the expense of **Fourier** transforms, and inverse Fourier transform, convolution can be reduced to (complex) multiplication.

A general implementation of convolution, would have a runtime of $O(m^2 \times n^2)$.
Convolution in a Fast Fourier Transform space:
- Cost of FFT/IFFT for image: $O(n^2\log n)$.
- Cost of FFT/IFFT for image: $O(m^2\log m)$.
- Cost of convolution: $O(n^2)$. ← ==Not a function of filter size anymore!==

### Low-pass / High-pass Filtering
Any filter that smooths out the image is at the end a low-pass filter.

![[Screenshot 2024-10-17 at 2.48.14 PM.png]]
- Low pass filter filters out all of the high frequency content of the image → only low frequencies remain.

*Wait but how should we interpret low / high frequencies?*
- **Low Frequencies**: Slow, gradual changes (smooth changes). 
- **High Frequencies**: Small-scale, rapid changes (details, edges, noise etc.).

So these filters tend do smooth out the image → Less detail in images → Low-pass.

#### Linear Filter Properties
Let $\otimes$ denote convolution, let $I(X,Y)$ be a digital image. Let $F$ and $G$ be digital filters,
- Convolution is **associative**. $$G\otimes(F \otimes I(X,Y)) = (G \otimes F)\otimes I(X,Y)$$
- Convolution is **symmetric**.$$(G\otimes F)\otimes I(X,Y)= (F\otimes G)\otimes I(X,Y)$$
Convolving $I(X,Y)$ with filter $F$ and then convolving the result with filter $G$ can be achieved in a single step, namely convolving $I(X,Y)$ with filter $G\otimes F=F \otimes G$. (Pre-convolution)

==Correlation, in general, is not associative!==

Ex)
```python
filter = boxfilter(3)
signal.correlate2d(filter,filter,'full')
```

$$\frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix} \otimes \frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}=\frac{1}{81}\begin{bmatrix}
1 & 2 & 3 & 2 & 1 \\
2 & 4 & 6 & 4 & 2 \\
3 & 6 & 9 & 6 & 3 \\
2 & 4 & 6 & 4 & 2 \\
1 & 2 & 3 & 2 & 1
\end{bmatrix}$$

$$\to \frac{1}{9}\begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 0 & 0 \\
0  & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix} \otimes \frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}= \frac{1}{81}\begin{bmatrix}
1 & 2 & 3 & 2 & 1 \\
2 & 4 & 6 & 4 & 2 \\
3 & 6 & 9 & 6 & 3 \\
2 & 4 & 6 & 4 & 2 \\
1 & 2 & 3 & 2 & 1
\end{bmatrix}$$
==Convolving a box filter of a larger size != Convolving box filters together.==

Ex. Separable Gaussian Filter
$$\frac{1}{16}\begin{bmatrix}
1 & 4 & 6 & 4 & 1
\end{bmatrix}\otimes \frac{1}{16}\begin{bmatrix}
1 \\
4 \\
6 \\
4 \\
1
\end{bmatrix}=\frac{1}{256}  \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
1 & 4 & 6 & 4 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}\otimes \begin{bmatrix}
1 \\
4 \\
6 \\
4 \\
1
\end{bmatrix}$$
$$\therefore \frac{1}{256}\begin{bmatrix}
1 & 4 & 6 & 4 & 1 \\
4 & 16 & 24 & 16 & 4 \\
6 & 24 & 36 & 24 & 6 \\
4 & 16 & 24 & 16 & 4 \\
1 & 4 & 6 & 4 & 1
\end{bmatrix}$$

##### Additional property of Gaussian Filter
Let $\otimes$ denote convolution. Let $G_{\sigma_1}(x)$ and $G_{\sigma_{2}}(x)$ be two 1D Gaussians,
$$G_{\sigma_{1}}(x) \otimes G_{\sigma_{2}}(x)=G_{\sqrt{ \sigma_{1}^2+\sigma_{2}^2 }}(x)$$

==Convolution of two Gaussians is another Gaussian (Only for Gaussian)!==

## Non-Linear Filters
We’ve seen that linear filters can perform a variety of image transformations:
- shifting
- smoothing
- sharpening

In some applications, better performance can be obtained using **non-linear filters**.
There are non-linear since they can’t be represented in a linear function / matrix.

#### Median Filter
The median filter takes the **median value** of the pixels under the filter.
![[Screenshot 2024-10-17 at 3.47.50 PM.png]]
```java
[4, 5, 5, 7, 13, 16, 24, 34, 54]

Then the median '13' is chosen.
```

- Effective at reducing certain kinds of noise, such as impulse noise (salt and pepper noise / shot noise).
- Forces points with distinct values to be more like their neighbours.
- Is not linear but **shift invariant**.
- Doesn’t have blurring effect.

#### Bilateral Filter
A bilateral filter is an edge-preserving non-linear filter.

**Like** a Gaussian filter:
- The filter weights depend on spatial distance from the center pixel.
- Pixels nearby should have greater influence than pixels far away.

**Unlike** a Gaussian filter:
- The filter weights also depend on range distance from the center pixel.
- Pixels with similar brightness value should have greater influence than pixels with dissimilar brightness values.

==Pixels that are near + similar have more contribution whereas pixels that are far + less similar have less contribution.==

$$e^{\frac{-(x^2+y^2)}{2\sigma_{d}^2}}e^{\frac{-(I(X+x,Y+y) - I(X,Y))^2}{2\sigma_{r}^2}}$$
We have both a **domain kernel** and a **range kernel**.
- If the color is too different, the range kernel tends to 0 and becomes less contributing.
- If the distance is too apart, the domain kernel tends to 0 and becomes less contributing.

![[Screenshot 2024-10-17 at 4.00.02 PM.png]]
- The domain kernel is the same all over the place.
- However, the range kernel is different depending on the neighborhood.

![[Screenshot 2024-10-17 at 4.01.11 PM.png]]
Suppose we want to smooth a noisy step function. 
A Gaussian kernel performs a weighted average of points over a spatial neighborhood.
→ But this averages points both at the top and bottom of the step (drastically changing part).
The bilateral filter looks at the **distances in range as well as space** to preserve the color edges.
##### Flash Photography
Non-flash images taken under low light conditions often suffer from excessive **noise** and **blur**.

But there are problems with **flash images**:
- Color is often unnatural.
- There may be strong shadows, specularities.

The solution is to combine flash and non-flash images to achieve better exposure and colour balance, and to reduce noise.

We can define the range kernel based on the flash image and smooth out the non-flash image using the range kernel. → **Joint / Cross Bilateral**: Compute Range kernel using separate guidance image.

![[Screenshot 2024-10-17 at 4.06.33 PM.png]]

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 5|Lecture 5]]
