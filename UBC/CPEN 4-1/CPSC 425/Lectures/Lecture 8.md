## Edge Detection
The **Goal** is to identify sudden changes in image intensity. This is where most shape information is encoded. 
Think of a contour,
![[Screenshot 2024-10-18 at 12.00.16 PM.png]]

What Causes Edges?
- Depth Discontinuity (like objects in front of others).
- Surface Orientation Discontinuity.
- Reflectance Discontinuity (like change in surface material properties).
- Illumination Discontinuity (like shadows).

#### Derivatives
Recall, for a 2D function (continuous),
$$\frac{\delta f}{\delta x} = \lim_{ \epsilon \to 0 } \frac{f(x+\epsilon,y)-f(x,y)}{\epsilon}$$
A discrete approximation would be,
$$\frac{\delta f}{\delta X}\approx  \frac{F(X+1,Y)-F(X,Y)}{\Delta X}$$
Where this would represent **forward difference**, and $\Delta X =1$ for this case.
On the other hand, **backward difference** would look like,
$$\frac{\delta f}{\delta X}\approx  \frac{F(X,Y)-F(X-1,Y)}{\Delta X}$$
There is also **central difference**,
$$\frac{\delta f}{\delta X}\approx  \frac{F(X+1,Y)-F(X- 1,Y)}{\Delta X}$$
And in this case $\Delta X = 2$.


***Differentiation is linear and shift invariant, and therefore can be implemented as a convolution!***

![[Screenshot 2024-10-18 at 12.27.46 PM.png]]
[Remember that they are 180 degrees difference.]

Since the filter is not odd anymore, depending on what difference it is we will have a undefined on line on either sides.
![[Screenshot 2024-10-18 at 12.29.08 PM.png]]

For $Y$ dimension, it is similar, having filters like,
$$\begin{bmatrix}
1 \\
-1
\end{bmatrix},\begin{bmatrix}
-1 \\
1
\end{bmatrix}$$

An Example would be like the following,
![[Screenshot 2024-10-18 at 12.30.07 PM.png]]

![[Screenshot 2024-10-18 at 12.31.42 PM.png]]
If we look at the images above, the $X,Y$ derivatives clearly show a difference, where $Y$ derivative shows more vertical edges and the $X$ derivative shows more horizontal edges.

Let’s try a small example (using first forward difference),
$$\text{image}= \begin{bmatrix}
1  & 1 & 0.6 & 0.3 & 0 & 0 \\
1 & 1 & 0.6 & 0.3 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0  \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}$$
$$
\frac{\delta f}{\delta X}=\begin{bmatrix}
0 & -0.4 & -0.3 & -0.3  & 0 \\
0 & -0.4 & -0.3 & -0.3 & 0 \\
0 & 0 & 0 & 0 & 0 &  \\
0 & 0 & 0 & 0 & 0 & 
\end{bmatrix}, \frac{\delta f}{\delta Y}=\begin{bmatrix} \\
0 & 0 & 0 & 0 & 0 & 0 \\
1 & 1 & 0.6 & 0.3 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}$$


**Why, in general, should the weights of a filter used for differentiation sum to 0?**
=> Think of a constant image, $I(X,Y)=k$. The derivative is 0. Therefore, the weights of any filter used for differentiation needs to sum up to 0.

$$\sum_{i=1}^Nf_{i}\cdot k=k\sum_{i=1}^N f_{i} = 0 \implies \sum_{i=1}^N f_{i=}= 0$$

**Image noise tends to result in pixels not looking exactly like their neighbours, so simple “finite differences'“ are sensitive to noise.**
=> The usual way to deal with this problem is to **smooth** the image prior to derivative estimation.

#### Smoothing and Differentiation
An **Edge** is a location with high gradient (derivative). We need to smooth to reduce noise prior to taking the derivative. And we need two derivative $x$ and $y$.

We can use the **derivative of Gaussian filters**:
- Because differentiation is convolution.
- And, convolution is **associative**.

$$D \otimes (G \otimes I(X,Y)) = (D \otimes G) \otimes I(X,Y)$$
And this is more efficient to precompute.

Let’s consider a row of pixels in an image that contains noise:
![[Screenshot 2024-10-18 at 12.40.44 PM.png]]
In this case, can we determine an edge? Uh no..

![[Screenshot 2024-10-18 at 12.41.15 PM.png]]
So if we smooth before taking the derivative, it is better for finding edges!
Also, as shown above, it is more efficient to differentiate the Gaussian filter first.
==And this is because the filter is smaller in size, we use less computation power than differentiating the whole image.==

#### Gradient Magnitude
Let $I(X,Y)$ be an image, and $I_x,I_y$ be estimates of the partial derivatives in the $x$ and $y$ directions, respectively.
Then the gradient is the vector $[I_{x},I_{y}]$ and the scalar $\sqrt{ I_{x}^2+I_{y}^2 }$ is the gradient magnitude.
This magnitude can gives us a sense of how strong the edge is. (when either derivatives are large → gradient magnitude becomes large → indicates existence of edge)

![[Screenshot 2024-10-18 at 12.54.05 PM.png]]
==Gradient points dark to light.==

The **gradient direction** is given by:
$$\theta = \arctan\left( \frac{\left( \frac{\delta f}{\delta y} \right)}{\left( \frac{\delta f}{\delta x} \right)} \right)$$
This is perpendicular to the direction of the edge.

The **gradient magnitude** is:
$$\lvert \lvert \nabla f \rvert  \rvert= \sqrt{ \left( \frac{\delta f}{\delta x} \right)^2 + \left( \frac{\delta f}{\delta y} \right)^2 } $$

==So we can use these quantities do reason about the strength / direction of the edge.==

![[Screenshot 2024-10-18 at 12.57.34 PM.png]]
The edges differ per $\sigma$, increase smoothing results in,
- eliminating noise edges.
- Makes edges smoother and thicker.
- Removes fine detail.

If we see the above images, we can see the result of padding, which at the end makes an edge itself.

### Edge Detecting

#### Sobel Edge Detector
1. Use central differencing to compute gradient image. More accurate.
2. Threshold to obtain edges. → Above threshold would be a edge pixel, vice versa.

![[Screenshot 2024-10-18 at 12.59.25 PM.png]]
If we look at the matrix,
$$\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}$$
We can see that it is taking the central difference horizontally and the Gaussian vertically.
=> Smoothing / differentiating. (other direction is 90 degrees rotation)

==Instead of smoothing by 2D gaussian, sobel only smooths in one direction orthogonal to the gradient → to improve localization.==

==Effort to apply **Gaussian-like smoothing** (or weighted averaging) in the direction **perpendicular to the edge detection** in order to **suppress noise**, while still calculating the **rate of change (derivative)** more accurately in the direction of interest.==

##### Comparing Edge Detectors
**Good Detection**: minimize probability of FP/FN edges.
**Good localization**: found edges should be as close to true image edge as possible.
**Single Response**: minimize the number of edge pixels around a single edge.

![[Screenshot 2024-10-18 at 1.02.38 PM.png]]
After smoothing, the edge becomes ambiguous and assign a whole set of pixels to an edge.
==We want a small thin line of pixels.==

In terms of the Sobel Edge Detector,

|       | Approach                     | Detection | Localization | Single Resp | Limitations            |
| ----- | ---------------------------- | --------- | ------------ | ----------- | ---------------------- |
| Sobel | Gradient Magnitude Threshold | Good      | Poor         | Poor        | Results in thick edges |
The problem with threshold is that, if we set a threshold, there would be a set of points that would be detected as an edge. => Hence, we would have poor single response and localization.
![[Screenshot 2024-10-18 at 1.05.47 PM.png]]

The idea is to take the 2nd derivative and find the zero-crossing, which tell us that single point where an edge exists.
![[Screenshot 2024-10-18 at 1.05.32 PM.png]]

The two generic approaches to edge point detection is:
- significant local extrema of first derivative operator.
- zero crossings of a second derivative operator.

#### Marr/Hildreth Laplacian of Gaussian
**A zero crossings of a second derivative approach!**

Steps:
1. Gaussian for smoothing.
2. Laplacian for differentiation where $$\nabla^2f(x,y)=\frac{\delta^2f(x,y)}{\delta x^2}+\frac{\delta^2f(x,y)}{\delta y^2}$$
3. Locate zero-crossings in the Laplacian of the Gaussian $\nabla^2G$ where $$\nabla^2G(x,y)=-\frac{1}{2\pi \sigma^4}\left[ 2- \frac{x^2+y^2}{\sigma^2} \right]e^{\frac{-(x^2+y^2)}{2\sigma^2}}$$
![[Screenshot 2024-10-18 at 1.10.26 PM.png]]

![[Screenshot 2024-10-18 at 1.11.34 PM.png]]

|                 | Approach                              | Detection | Localization | Single Resp | Limitations     |
| --------------- | ------------------------------------- | --------- | ------------ | ----------- | --------------- |
| Marr / Hidlreth | Zero-crossings of 2D derivative (LoG) | Good      | Good         | Good        | Smooths Corners |
We would not get a sharp corner since we apply a Gaussian that would smooth out the edge.

==The values for smoothing will be larger than sobel, because the second derivative is more susceptible to noise than the first derivative. And since we use a pre-convolved operator, no additional smoothing is needed.==

#### Canny Edge Detector
This is the significant local extrema approach.
1. Apply directional derivatives to Gaussian.
2. Compute Gradient magnitude and Gradient direction.
3. **Non-maximum suppression**.
	1. Thin multi-pixel wide “ridges” down to single pixel width.
4. **Linking** / Thresholding.
	1. Low, high edge-strength thresholds.
	2. Accept all edges over low threshold that are connected to edge over high threshold.

##### Non-maxima Suppression
The idea is to suppress near-by similar detections to obtain one “true” result.
![[Screenshot 2024-10-18 at 1.18.19 PM.png]]\
==Gradient direction is orthogonal edge.==
If we want to fill this out, is to look along the gradient direction to find the maxima and suppress the others.

***Select the maximum point across the width of the edge!***

![[Screenshot 2024-10-18 at 1.21.11 PM.png]]
For non-45 degree angles, interpolate the values.

![[Screenshot 2024-10-18 at 1.21.37 PM.png]]
Even though we find local extremas, some maybe large and some maybe small!
=> We can threshold!

##### Linking-Edge Points
Setting thresholds are hard. If we set some threshold, though may consist the same object in the image, some maybe treated as edges and some may not!
That’s why we use **Linking** → If we have some evidence that there is a strong edge somewhere and nearby are weaker edges, we link them to make elongated edges!

And this is possible for **gradient direction**, specifically the direction orthogonal to the gradient direction.

![[Screenshot 2024-10-18 at 1.26.30 PM.png]]
Assume the marked out point is an edge point. Take the normal to the gradient at that point and use this to predict continuation points (either r or s).

We will have two thresholds, $k_{\text{high}},k_{\text{low}}$:
- Gradient magnitude > $k_{\text{high}}$.
	- Definitely an edge pixel.
- $k_{\text{low}}$ < Gradient magnitude < $k_{\text{high}}$:
	- Maybe an edge pixel.
- Gradient magnitude < $k_\text{low}$:
	- Definitely not and edge pixel.

Typical ratio of threshold is (roughly): $\frac{k_{\text{high}}}{k_{\text{low}}}=2$.

Basically, starting at any point above $k_\text{high}$ we look in the orthogonal gradient direction to see if the pixels are above $k_\text{low}$ and link them up.


|       | Approach                        | Detection | Localization | Single Resp | Limitations |
| ----- | ------------------------------- | --------- | ------------ | ----------- | ----------- |
| Canny | Local extrema of 1st Derivative | Best      | Good         | Good        |             |

### Boundary Detection
We can formulate boundary detection as a high-level recognition taksk.
- Try to learn, from sample human-annotated images, which visual features or cues are predictive of a salient / significant boundary.
Many boundary detectors output a **probability or confidence** that a pixel is on a boundary.


- Consider circular windows of radii $r$ at each pixel $(x,y)$ cut in half by an oriented line through the middle.
- Compare visual features on both sides of the cut.
- If features are very **different** on the two sides, the cut line probably corresponds to a boundary.
- Notice this gives us an idea of the orientation of the boundary as well.

1. Compute non-parametric distribution for left side.
2. Same for right side.
3. Compare two histograms, on left and right, using statistical test.

![[Screenshot 2024-10-18 at 1.41.33 PM.png]]


#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 9|Lecture 9]]