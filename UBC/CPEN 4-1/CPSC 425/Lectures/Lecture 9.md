## Corner  Detection

#### Bit of a Recap on Derivative Stuff
![[Screenshot 2024-10-18 at 1.58.54 PM.png]]

In terms of Gradient Direction, we can use the inverse tangent. And in this case, since it was a convolution we follow the grid (shown on the top left of the image) and get the directions such as the following,
![[Screenshot 2024-10-18 at 2.02.28 PM.png]]

If we think of Canny Edge Detection, we can do the following:
![[Screenshot 2024-10-18 at 2.05.04 PM.png]]
What we do is, first take a pixel, and look at the gradient magnitude along with the gradient direction. In terms of the pixel 95 at (4,3), we look at the gradient direction (along it) and see that 96 is higher, thus no longer making 95 an edge pixel. And continue..

Then,
![[Screenshot 2024-10-18 at 2.10.28 PM.png]]
We label those based on the thresholds $k_\text{high}, k_\text{low}$. For those, that are definitely an edge or not are fine. But we have to look at those that might be an edge or not. Based on the orthogonal direction of each “definite” pixel if we encounter an ambiguous one we can simply mark that one as an edge.

**In summary,**
1. Identify definite local maximas based on gradient direction.
2. Mark definite edge (non-edge)s, in-definite edge (non-edge)s.
3. Look at each definite edge pixel, and mark those ambiguous ones to be an edge if they are along the orthogonal gradient direction.

#### Image Matching
What are good features?
- Local: robust to occlusion and clutter.
- Accurate: precise localization.
- Robust: noise, blur, compression, etc. do not have big impact on the feature.
- Distinctive: individual features can be easily matched.
- Efficient: close to real-time performance.

**General Setup**:
- Use **small neighborhoods** of pixels to do feature detection. - find locations in image that MAY be able to match.
- Use **larger neighborhoods** around the feature detections to characterize the region well, using a **feature descriptor**, in order to do matching.

##### Corner
We thank of a corner as any **locally distinct** 2D image feature that (hopefully) corresponds to a distinct position on an 3D object of interest in the scene.

![[Screenshot 2024-10-18 at 2.26.02 PM.png]]

###### Why are Corners distinct?
![[Screenshot 2024-10-18 at 2.27.22 PM.png]]

A corner can localized reliably.
- Place a small window over a patch of constant image value. If you slide the window in any direction, the image in the window will not change.
- Place a small window over an edge. If you slide the window in the direction of the edge, the image in the window will not change.
	- Cannot estimate location along an edge **aperture problem**.
		- **aperture problem**: locally distinct in one direction but not along the edge.
- Place a small window over a corner. If you slide the window in any direction, the image in the window changes.

###### What kind of structures are present in the image locally?
- **0D Structure**: not useful for matching.
- **1D Structure**: edge, can be localized in one direction (aperture problem).
- **2D Structure**: Corner, or interest point, can be localized in both directions, good for matching.

==Look for Corners!!!==

#### Autocorrelation
This is the correlation of the image with itself. (Shift the patch just around its neighborhood)
- Windows centered on an edge point will have an autocorrelation that falls off slowly in the direction along the edge and rapidly in the direction perpendicular to the edge.
- Windows centered on a corner point will have autocorrelation that falls of rapidly in all directions.

==This is possible because correlation shows similarity.==

![[Screenshot 2024-10-18 at 2.37.00 PM.png]]
These show the result of autocorrelation in a small neighborhood, they represent the similarity from the pixel of choice and the neighborhood.

##### Local SSD Function
Consider the SSD of a patch with its local neighborhood,
$$\text{SSD}=\sum_{\mathcal{R}}\lvert I(\mathbf{x}) - I(\mathbf{x}+\Delta \mathbf{x}) \rvert^2 $$
![[Screenshot 2024-10-18 at 2.39.03 PM.png]]

![[Screenshot 2024-10-18 at 2.39.14 PM.png]]

##### Harris Corners
If we apply a first order approximation to the local SSD function
$$\text{SSD}=\sum_{\mathcal{R}}\lvert I(\mathbf{x}) - I(\mathbf{x}+\Delta \mathbf{x}) \rvert^2 =\Delta \mathbf{x}^T\mathbf{H}\Delta \mathbf{x}$$
where,
$$\mathbf{H}=\sum_{\mathcal{R}}\begin{bmatrix}
I_{x}^2 & I_{y}I_{x} \\
I_{x}I_{y} & I_{y}^2
\end{bmatrix}$$
which is a covariance matrix.

The ssd function must be large for all shift $\Delta \mathbf{x}$ for a corner / 2D structure. This implies that both eigenvalues of $\mathbf{H}$ must be **large**.

###### Harris Corner Detection
```python
1. Compute image gradients over small region.
2. Compute the covariance matrix.
3. Compute the eigenvectors and eigenvalues.
4. Use threshold on eigenvalues to detect corners.
```
==Eigen values are big => Corner!==

Step 1,
![[Screenshot 2024-10-18 at 2.44.32 PM.png]]
![[Screenshot 2024-10-18 at 2.45.08 PM.png]]
![[Screenshot 2024-10-18 at 2.45.37 PM.png]]
- Distribution reveals the **orientation** and **magnitude**.
- How shall we quantify the orientation and magnitude for this?

Step 2,
Compute the Covariance matrix,
$$C=\begin{bmatrix}
\sum_{p \in P}I_{x}I_{x} & \sum_{p \in P}I_{x}I_{y} \\
\sum_{p \in P} I_{y}I_{x} & \sum_{p \in P}I_{y}I_{y}
\end{bmatrix}$$

$p \in P$ denotes that we’re are getting the sum over a small region around the corner.
Also, the matrix is symmetric.

==We are fitting a quadratic to the gradients over a small image region.==

###### Simple case
Consider this image, what would $I_x$ and $I_y$ look like?
![[Screenshot 2024-10-18 at 2.50.30 PM.png]]
![[Screenshot 2024-10-18 at 2.50.50 PM.png]]

Then if we take the dot product of these two images to get the covariance matrix,
$$C=\begin{bmatrix}
\sum_{p \in P}I_{x}I_{x} & \sum_{p \in P}I_{x}I_{y} \\
\sum_{p \in P} I_{y}I_{x} & \sum_{p \in P}I_{y}I_{y}
\end{bmatrix}=\begin{bmatrix}
\lambda_{1}  & 0 \\
0 & \lambda_{2}
\end{bmatrix}=R^{-1}\begin{bmatrix}
\lambda_{1} & 0  \\
0 & \lambda_{2}
\end{bmatrix}R$$
How strong of a corner it is will determine the value of $\lambda_{1},\lambda_{2}$.
In particular, if the gradient is scaled by a factor of 2. → The matrix is scaled by a factor of 4.

Step 3, (computing eigen values and eigen vectors)
$$Ce=\lambda e  \implies (C-\lambda I)e=0$$
$$\det(C-\lambda I) = 0 \implies \lambda!?$$

###### Visualization as Ellipse
Since $C$ is symmetric, we have $$C=R^{-1}\begin{bmatrix}
\lambda_{1} & 0 \\
0 & \lambda_{2}
\end{bmatrix}R$$
We can visualize $C$ as an ellipse with axis lengths determined by the eigenvalues and orientation determined by $R$.

$$f(x,y)= \begin{bmatrix}
x & y
\end{bmatrix}\begin{bmatrix}
1 & 0  \\
0 & 1
\end{bmatrix}\begin{bmatrix}
x \\
y
\end{bmatrix}=\text{const}$$

![[Screenshot 2024-10-18 at 2.59.37 PM.png]]
We know that for flat patches that the eigen values are small, and for edges only one of them would be large. Also, for a corner both would be large. Hence, when fitting a quadratic we will get something like the above.

And depending on the shape of the corner we can get the shapes as the following.
![[Screenshot 2024-10-18 at 3.01.41 PM.png]]

But how do quantize the corners, how can we set the threshold to determine a corner??
The simplest form is $min(\lambda_{1},\lambda_{2})$.

![[Screenshot 2024-10-18 at 3.02.27 PM.png]]
But then this has to be done by computing the eigen values for every single image and it is not efficient.

Thus, we have the alternative function,
$$\lambda_{1}\lambda_{2}-\mathcal{k}(\lambda_{1}+\lambda_{2})^2$$
$$=\det(C)-\mathcal{k}\text{trace}^2(C)$$
which removes the need of actually calculating the eigen values.
![[Screenshot 2024-10-18 at 3.06.52 PM.png]]


##### Review of Harris Corner Detection
1. Filter image with Gaussian.
2. Compute magnitude of $x,y$ gradients at each pixel.
3. Construct $C$ in a window around each pixel.
	1. Harris uses a Gaussian Window rather than a box filter.
4. Solve for product $\lambda$’s.
5. If both eigen values are big (above threshold) => we have a corner.
	1. Harris also checks that $\lambda$’s are not too high.

###### Exercise
![[Screenshot 2024-10-18 at 3.13.00 PM.png]]
Considered a corner.

![[Screenshot 2024-10-18 at 3.13.20 PM.png]]
Not considered a corner.

![[Screenshot 2024-10-18 at 3.13.29 PM.png]]
Considered a corner.

##### Properties of Edges
- Rotational Invariance.
	- Eigen values are same, but eigen vectors represent rotation.
- Intensity shift invariance.
	- Only derivatives are used → invariant to shifts.
	- Scaling intensity does change eigen values → Get squared.
- Scale could effect performance.
	- ![[Screenshot 2024-10-18 at 3.16.49 PM.png]]


#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 10|Lecture 10]]

