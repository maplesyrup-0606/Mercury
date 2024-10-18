## Template Matching
- How can we find a part of one image that matches another?
- How can we find instances of a pattern in an image?

***Use the pattern as a template!***

![[Screenshot 2024-10-17 at 8.54.20 PM.png]]
We can think of convolution / **correlation** as comparing a template (the filter) with each local image patch.
- Consider the filter and image patch as vectors.
- Applying a filter at an image location can be interpreted as computing the dot product between the filter and the local image patch.

$$\text{template }\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix} \implies \text{vector }\begin{bmatrix}
0 \\
0 \\
0 \\
0 \\
1 \\
1 \\
0 \\
0 \\
1
\end{bmatrix}$$

Given the two image patches,
$$\text{patch 1}=\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix},\text{ patch 2}=\begin{bmatrix}
1 & 0 & 1 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}$$

Since we are directly applying the filter to these image patches,
$$p_{1}\times f=\begin{bmatrix}
0 & 0 & 0  \\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix} = 3,\hspace{.2in}p_{2}\times f=\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix} =1$$
$$\times = \text{element wise multiplication (vector dot product)}$$
***The dot product maybe large simply because that region is bright → need to normalize.***
Response to filter is highest when image patch has more similarity.
#### Similarity measurements in template matching
Let the filter $\mathbf{J}$, the local image region $\mathbf{I}$.
- Correlation, $\text{CORR}=\mathbf{I}\cdot \mathbf{J}=\mathbf{I}^T\mathbf{J}$.
- Normalized Correlation, $\text{NCORR}=\frac{\mathbf{I}^T\mathbf{J}}{\lvert \mathbf{I} \rvert\lvert \mathbf{J} \rvert}=\cos \theta$.
	- *Normalize patch, image by norm, not the sum to 1.*
	- Normalized correlation varies between -1 and 1, attains the value when the filter and image region are identical (up to a scale factor).
		- Since images are positive, the range actually be 0 to 1.
- Sum Squared Difference, $\text{SSD}=\lvert \mathbf{I}-\mathbf{J} \rvert^2$

Minimizing SSD and maximizing NCORR are equivalent if $\lvert  \mathbf{I} \rvert =\lvert  \mathbf{J} \rvert=1$.

![[Screenshot 2024-10-17 at 9.16.24 PM.png]]The correlation map indicates similarity of the patch centered at the position to the template.

- If the threshold is relatively low.
	- We get multiple detections for a certain region (redundant detections).
	- False positives.
- If the threshold is very high.
	- In this case, it’s ok since we have a duplicate.
	- But in practice, we might not get any detections all.


Let $a$ and $b$ be vectors. Let $\theta$ be the angle between them. We know,
$$\cos \theta=\frac{a \cdot b}{\sqrt{ (a \cdot a)(b \cdot b) }} = \frac{a}{\lvert a \rvert } \frac{b}{\lvert b \rvert }$$

1. Normalize the template / filter $(b)$ in the beginning. Since we don’t change it.
2. Compute $\lvert  a \rvert$ by convolving squared image with a filter of all 1’s of equal size to the template and square-rooting the response.$$\begin{bmatrix}
1 & 17 & 3 & 5 \\
43 & 24 & 1 & 11 \\
13 & 24 & 8 & 15 \\
6 & 17 & 9 & 19
\end{bmatrix}\to_{\text{square}} \begin{bmatrix}
1 & 289 & 9 & 25 \\
1849 & 576 & 1 & 121 \\
169 & 576 & 64 & 225 \\
36 & 289 & 81 & 361
\end{bmatrix}\to_{\text{convolve}}\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 3378 & 1886 & 0  \\
0 & 3485 & 2294 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}$$$$\to_{\text{square root}}\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 58.12 & 43.43 & 0 \\
0 & 59.03 & 47.90 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}$$
3. Compute the dot product by correlation of image $(a)$ with normalized filter $(b)$.
4. Compute the normalized correlation by dividing element-wise result in step 3 by result in step 2.

##### Why might template matching fail?

- Different Scales
![[Screenshot 2024-10-17 at 9.32.36 PM.png]]

- Different Orientation
![[Screenshot 2024-10-17 at 9.32.43 PM.png]]

- Lighting Conditions
![[Screenshot 2024-10-17 at 9.32.48 PM.png]]

- Left vs. Right Hand
![[Screenshot 2024-10-17 at 9.32.53 PM.png]]

- Partial Occlusions
![[Screenshot 2024-10-17 at 9.33.02 PM.png]]

- Different Perspective

- Motion / blur

**Good News**:
- Works well in presence of noise.
- Relatively easy to compute.

**Bad News**:
- Sensitive to scale change.
- Sensitive to 2D rotation.

**More Bad News**:
- When imaging 3D worlds.
	- Sensitive to viewing direction and pose.
	- Sensitive to conditions of illumination.
#### Scaled Representations
![[Screenshot 2024-10-17 at 9.35.13 PM.png]]
We can either scale the image or scale the template.
But there exists a significant cost difference.

**Cost of Scaling Template**:
$$M^2N^2 + 4M^2N^2 + 16M^2N^2 + 64M^2N^2 = 85M^2N^2$$

**Cost of Scaling Image**:
$$M^2N^2+M^2\left( \frac{N}{2} \right)^2+M^2\left( \frac{N}{4} \right)^2+M^2\left( \frac{N}{8} \right)^2 \approx \frac{3}{2}M^2N^2$$

==The amount of computations when scaling the template is insanely huge compared to scaling the image!==

***How does a scaled representation help us?***
- to find template matches at all scales.
	- keep template size constant, scale image.
	- allows us to find hands or faces when we don’t know what size they are in the image.
- efficient search.
	- look first at coarse scales, refine at finer scales.
	- much less cost (but possibly miss best match).
- examine all levels of detail.
	- find edges with different amounts of blur.
	- find textures with different spatial frequencies (i.e. different levels of detail).


#### Gaussian Pyramid
![[Screenshot 2024-10-17 at 10.02.12 PM.png]]
- What happens to the details?
	- They get smoothed out as we move to higher levels.
- What is preserved at higher levels?
	- Mostly large uniform regions in the original image.
- Just with Gaussian images we cannot get back → So how can we reconstruct the image?

*Upper level → lower resolution.*
#### Laplacian Pyramid
![[Screenshot 2024-10-17 at 10.05.02 PM.png]]

![[Screenshot 2024-10-17 at 10.05.15 PM.png]]
The laplacian image stores the difference between the image at the level and the blurred version of that image at that level.

Why can we do this?
- According to the Nyquist sampling theorem, when blurred at a certain rate sub-sampling doesn’t lose any information.
- However, this blurring process itself causes a loss of information.
- So, we can track the difference when reconstructing later on.

**Building a Laplacian Pyramid**:
1. Create Gaussian Pyramid.
2. Take the difference between one Gaussian pyramid level and the next.

**Properties**:
- Computes a Laplacian / Difference-Of-Gaussian (DoG) function of the image at multiple scales.
- It is a **band-pass filter** – each level represents a different band of spatial frequencies.

*Last level of Gaussian is the same as the Last level of Laplacian.*

![[Screenshot 2024-10-17 at 10.09.05 PM.png]]

Algorithm:
```python
repeat:
	filter
	compute residual
	subsample
until min resolution reached
```

![[Screenshot 2024-10-17 at 10.12.37 PM.png]]


##### Reconstructing the Original Image
Algorithm:
```python
repeat:
	upsample
	sum with residual
until original resolution reached
```

![[Screenshot 2024-10-17 at 10.14.49 PM.png]]

