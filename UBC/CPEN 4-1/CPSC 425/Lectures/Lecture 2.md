##### Projection + Thin Lens Example
The perspective projection gives the location where a 3D world point projects.
And the thin lens equation gives the depth of the imaging plane itself where this point will be in focus.

Where would the focusing plane be for various positions of the object?
$$\frac{1}{z'}-\frac{1}{z}=\frac{1}{f},\hspace{.3in}z'=\frac{zf}{z+f}$$


If we move the object further and further from the lens,
$$\lim_{ z \to -\infty } \frac{zf}{z+f}=f$$
The focusing plane will form at focal length.

Let say the object is at 2 x focal length,
$$z'=\frac{zf}{z+f}=-\frac{2f^2}{-2f+f}=2f$$

##### Effect of Aperture Size
A smaller aperture => smaller blur, larger depth of field.
![[Screenshot 2024-10-14 at 10.59.36 PM.png]]

##### Real Lenses
Of course, real lenses are much more complicated. There are multiple stages of lenses included.

Some real phenomenas,
- Spherical Aberration. - Blur happens.
	- Lenses are not perfect, refraction will change as you get off the center.
	- Have to place where the blur is minimized.
- Vignetting. - Some light is missed when multiple lenses are used.
	- Darkening on the edges.
- Chromatic Aberration. - Different wavelengths of light follow different paths and blurring across some colors happen.
	- Not all colours can be equal in focus.
- Scattering.
- Distortion.

##### Human eye
The Human eye acts much like a pinhole camera.
- pupil = pinhole.
	- Change of pupil → changes focal length.
- retina = imaging plane / sensor.

## Image as a 2D Function
![[Screenshot 2024-10-14 at 11.07.39 PM.png]]
For a grey scale, the intensity is quantified between the range [0,255].
And intensity is unsigned since there is no negative brightness (0 ≤ photons).
### Adding Two Images
![[Screenshot 2024-10-14 at 11.08.42 PM.png]]
Since images are functions, we can perform operations on them such as average (above).

But,
![[Screenshot 2024-10-14 at 11.10.01 PM.png]]
These two option would provide a different result.

For instance, say that $I(X,Y)=98,G(X,Y)=200$.
Then the first would be,
$$\frac{98}{2}+\frac{200}{2}=149$$
where as the second would be,
$$\frac{\left\lfloor  298  \right\rfloor}{2} = \frac{255}{2} = 127 $$

$$\therefore a > b$$

#### Other Types of Transformations
![[Screenshot 2024-10-14 at 11.26.50 PM.png]]

#### Types of Filtering we can do
- Point operation
- Neighborhood Operation
##### Brightness vs. Contrast
- Brightness: All pixels get lighter/darker, relative difference between pixels stay the same.
- Contrast: Relative difference between pixel values becomes higher / lower.

![[Screenshot 2024-10-14 at 11.32.05 PM.png]]

#### Neighborhood Operations (Filtering)
There exists Linear / Non-linear filtering but let’s look at linear for now.
Let $I(X,Y)$ be an $n \times n$ image, and the filter (kernel) be another $m \times m$ image $F(X,Y)$.

Let $k = \left\lfloor  \frac{m}{2}  \right\rfloor$, compute the new image $I’(X,Y)$ as follows:
$$I'(X,Y)=\sum_{j=-k}^{k}\sum_{i=-k}^k F(i,j)I(X+i,Y+j)$$
For a given $X$ and $Y$, superimpose the filter on the image centered at $(X,Y)$.
Compute the new pixel value $I’(X,Y)$ as the sum of the product original value and filter values.

![[Screenshot 2024-10-14 at 11.36.28 PM.png]]

For every pixel we do $m \times m$ multiplications, and we have $n \times n$ pixels,
$$\therefore O(n^2m^2)$$
##### Boundary Effects (What do we do with boundaries?)
1. **Ignore Locations**: Make computation undefined for the top and bottom $k$ rows and leftmost and rightmost $k$ columns. → Resulting image shrinks with multiple filters, the image will be much more smaller than the original.
2. **Pad the image with zeros**: Return zero whenever a value of $I$ is required at some position outside the defined limits of $X$ and $Y$. → Boundary becomes darker.
3. **Assume periodicity**: The top row wraps around to the bottom row; the leftmost column wraps around to the rightmost column.
4. **Reflect Boarder**: Copy rows/columns locally by reflecting over the edge.
	1. Some pixels in the border neighborhood will contribute 2x as much to the weighted sum.

### Linear Filters: Correlation vs. Convolution.

**Correlation**:
$$I'(X,Y)=\sum_{j=-k}^{k}\sum_{i=-k}^k F(i,j)I(X+i,Y+j)$$

**Convolution**:
$$I'(X,Y)=\sum_{j=-k}^{k}\sum_{i=-k}^k F(i,j)I(X-i,Y-j)$$
$$=\sum_{j=-k}^{k}\sum_{i=-k}^k F(-i,-j)I(X+i,Y+j)$$

So let’s say we have the image and the filter as the following,
$$\text{filter}=\begin{bmatrix}
a & b & c  \\
d & e & f \\
g & h & i
\end{bmatrix},\text{   image}=\begin{bmatrix}
1 & 2 & 3  \\
4 & 5 &  6 \\
7 & 8 & 9
\end{bmatrix}$$

Then correlation would result in,
$$\text{correlation} = a+2b+3c+4d+5e+6f+7g+8h+9i$$
And convolution would result in,
$$\text{convolution } = 9a+8b+7c+6d+5e+4f+3g+2h+i$$

So it turns out that we are applying a filter that is rotated by 180 degrees.

If,
$$F(X,Y)=F(-X,-Y)$$
then correlation = convolution.

###### Exercise
$$I'(X,Y)=\frac{1}{4}\begin{bmatrix}
1 & 2 & 1
\end{bmatrix}\otimes \begin{bmatrix}
9 & 5 & 2 & 1 & 3 & 4 & 6 & 2 & 4
\end{bmatrix}$$
$$\frac{1}{4} \begin{bmatrix}
. & 12 & 10 & 7 & 11 & 17 & 18 & 14 & .
\end{bmatrix}$$
#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 3|Lecture 3]]

