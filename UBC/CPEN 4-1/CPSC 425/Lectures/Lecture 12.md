#### Re-cap
**Key-point** is an image location at which a descriptor is computed.
- Locally distinct points.
- Easily localizable and identifiable.

The feature **descriptor** summarizes the local structure around the key point.
- Allows unique matching of key-points in presence of object pose variations, image and photometric deformations.

#### Image Alignment
The aim is to warp one image to align with another using a 2D transformation.

Steps:
1. Find correspondences (matching points) across two images.
	1. **But**, not all points will match across two images, need to reject outliers.
		1. An actually match might not exist.
		2. Occlusions.
		3. Mismatches!
2. Compute the transformation to align the two images.

![[Screenshot 2024-11-28 at 12.12.51 PM.png]]

#### 2D transformations
We will look at a family that can be represented by 3 x 3 matrices.
![[Screenshot 2024-11-28 at 12.14.01 PM.png]]
This group represents perspective projections of **planar surfaces**.

##### Affine Transformation
It’s a linear function of the input points
$$\begin{bmatrix}
x' \\
y' 
\end{bmatrix}=\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}\begin{bmatrix}
x \\ y
\end{bmatrix} + \begin{bmatrix}
a_{13} \\
a_{23}
\end{bmatrix}$$

This can be written as a single matrix multiplication using *homogeneous* coordinates
$$\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}=\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
x_{1} \\
y_{1} \\
1
\end{bmatrix}$$
which is basically the same thing given initially with easier computation.

Consider the action of the unit square, under $\begin{bmatrix}3&1&0\\1&2&0\\0&0&1\end{bmatrix}$,
$$\begin{bmatrix}
3 & 1 & 0 \\
1 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
1 & 1 & 1 & 1
\end{bmatrix}=\begin{bmatrix}
0 & 1 & 3 & 4 \\
0 & 2 & 1 & 3 \\
1 & 1 & 1 & 1
\end{bmatrix}$$

![[Screenshot 2024-11-28 at 12.18.24 PM.png]]
The same thing happens to the images, we can have pixels as ‘coordinates’!

==Linear (or Affine) Transformations== can model translation, rotation, scale and shear.
→ Parallel lines (in the image) are preserved.

==Other transformations that are not affine== do not preserve parallel lines.
- We have more degrees of freedom to do better alignment.

For an affine transformation,
![[Screenshot 2024-11-28 at 12.21.48 PM.png]]
How many points are needed to solve for $a$?
We have 6 unknowns $a_{ij}$, and we get two constraints for one point.
→ We need two more points, hence three points to solve for the values $a_{ij}$.

**Depending on the type of transformation, we have a different number of constraints.**

###### Computing Affine Transformation
We can represent the matrix above in the same way like, rearranging the unknown into a vector
$$\begin{bmatrix}
x_{1}' \\
y_{1}'
\end{bmatrix}= \begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{21} & a_{22} & a_{23}
\end{bmatrix}\begin{bmatrix}
0 & x_{1} \\
0 & y_{1} \\
0 & 1 \\
x_{1} & 0 \\
y_{1} & 0 \\
1 & 0
\end{bmatrix}$$

And solve for the affine transformation as solving a matrix (since we need to know three points for an affine transformation),
$$\begin{bmatrix}
x_{1} & y_{1} & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_{1} & y_{1} & 1 \\
x_{2} & y_{2} & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_{2} & y_{2} & 1 \\
x_{3} & y_{3} & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_{3} & y_{3} & 1
\end{bmatrix}\begin{bmatrix}
a_{11} \\
a_{12} \\
a_{13} \\
a_{21} \\
a_{22} \\
a_{23}
\end{bmatrix}=\begin{bmatrix}
x_{1}' \\
y_{1}' \\
x_{2}' \\
y_{2}' \\
x_{3}' \\
y_{3}'
\end{bmatrix}$$

Once we solve for a transform, we can now **map any single pixel between two images** and stitch them!
![[Pasted image 20241128122948.png]]

We assume:
- **All matches are accurate**.
- **Matches have to be very close for the estimates to accurate**.
	- We can use many points to make an over-complete system.

###### Other forms of Linear transformations
Other linear transformations are special cases of **affine transform**.

- Translation
$$\begin{bmatrix}
1 & 0 & a_{13} \\
0 & 1 & a_{23} \\
0 & 0 & 1
\end{bmatrix}$$
We only need one point since there are two unknowns.

- Euclidean (translation + rotation)
$$\begin{bmatrix}
\cos \theta & \sin \theta & a_{13} \\
-\sin \theta & \cos \theta & a_{23} \\
0 & 0 & 1
\end{bmatrix}$$
We have three unknowns $\theta,a_{13},a_{23}$ we just need two points.

- Similarity (euclidean + scaling)
$$\begin{bmatrix}
s\cos \theta & s\sin \theta & a_{13} \\
-s\sin \theta & s\cos \theta & a_{23} \\
0 & 0 & 1
\end{bmatrix}$$
We also just need two points.

[Table]
![[Screenshot 2024-11-28 at 12.35.00 PM.png]]

We can use homographies when,
- The scene is planar.
- The scene is really far or has small depth variation → approximately planar.
- The scene is only captured under camera rotation.

#### Projective Transformation
Let’s consider the general 3 x 3 matrix transformation,
$$\begin{bmatrix}
x_{1}' \\
y_{1}' \\
1
\end{bmatrix}=\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}\begin{bmatrix}
x_{1} \\
y_{1} \\
1
\end{bmatrix}$$

We can try one example,
$$\begin{bmatrix}
x_{1}' \\
y_{1}' \\
1
\end{bmatrix}=\mathbf{H}\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}=\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix}\begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1  \\
1 & 1 & 1 & 1
\end{bmatrix}=\begin{bmatrix}
0 & 0 & 1 & 1  \\
0 & 1 & 0 & 1 \\
1 & 2 & 1 & 2
\end{bmatrix}$$
						^points

The last row is no longer 1, in order to make it one we divide by the last row.
$$\begin{bmatrix}
0 & 0 & 1 & 0.5 \\
0 & 0.5 & 0 & 0.5 \\
1 & 1 & 1 & 1
\end{bmatrix}$$
Since it’s not linear anymore due to the dividing in the last step we use other solvers (such as SVD).

###### Image alignment
So far, for finding correspondence matches between two images we solved for $$\mathbf{u} = \mathbf{H}\mathbf{x}$$
and we needed
- 2 points for similarity.
- 3 points for affine.
- 4 points homography.

But in reality, we have many *noisy correspondences + outliers*.

So instead, we can have a really large linear system, for instance in affine, in the parameters
$$\begin{bmatrix}
x_{1} & y_{1} & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & x_{1} & y_{1} & 1 \\
 &  &  & \vdots & 0 & 0
\end{bmatrix}\begin{bmatrix}
a_{11} \\
a_{12} \\
a_{13} \\
a_{21} \\
a_{22} \\
a_{23}
\end{bmatrix}=\begin{bmatrix}
x_{1}' \\
y_{1}' \\
x_{2}' \\
y_{2}' \\
x_{3}' \\
y_{3}' \\
\vdots
\end{bmatrix}$$

It is **over-constrained** and subject to **outliers**:
- More equations than unknowns.
- Some rows are completely wrong.

#### Fitting and RANSAC
Suppose we are **fitting a line** to a dataset that consists of 50% outlier. We can fit a line using two points.

→ If we draw pairs of points uniformly at random, then about 1/4 of these pairs will consist entirely of good data points.

→ We can identify these good pairs by noticing that a large collection of other points lie close to the line fitted pair.

→ A better estimate of the line can be obtained by refitting the line to the points that lie close to the line.

**RANSAC Algorithm**
```
1. Randomly choose minimal subset of data points necessary to fit model (a sample)
2. Points within some distance threshold, t, of model are a consensus set.
	1. Size of consensus set is model's support.
3. Repeat for N samples; model with biggest support is most robust fit.
	- Points within distance t of best model are inliers.
	- Fit final model to all inliers.
```

How can we derive some constraints? We can’t be sampling for infinite times.

Let $\omega$ be the fraction of inliers (points on line).
Let $n$ be the number of points needed to define hypothesis ($n=2$ for a line in the plane).

Suppose $k$ samples are chosen → The probability that single sample of $n$ points is correct is 
$$\omega^n$$

The probability that all $k$ samples fail is
$$(1-\omega^n)^k$$

We choose $k$ large enough (to keep this below a target failure rate)

Consider this example,
![[Screenshot 2024-11-28 at 12.56.47 PM.png]]
This shows the number of iterations we should do so that for a certain sample size and the number of outliers we would have to do for a certain correctness.

###### After RANSAC
RANSAC divides the points into inliers and outliers and yields estimate computed from the minimal set of inliers.

Improve this initial estimate with estimation over inliers. But this may change inliers, so alternate fitting with re-classification as inlier/outlier

![[Screenshot 2024-11-28 at 1.00.33 PM.png]]
Consider the example above where we estimate the line with points $A,B$. Are inlier set is 4, consisting of $A,B,C,D$.

We can choose $A,B,C,D$ and re-estimate and get a better fit.

![[Screenshot 2024-11-28 at 1.02.07 PM.png]]

#### Image Alignment + RANSAC
Consider the RANSAC solution for Similarity Transform and we have the following matches.
![[Screenshot 2024-11-28 at 1.02.46 PM.png]]
Now let’s assume that we have the 4 inliers and 4 outliers,
$$\text{inliers}= \{\text{red, orange, yellow, brown} \}$$
$$\text{ouliers}=\{ \text{blue, light blue, purple, pink} \}$$

Next, with the 8 points of data, we choose two at random (since similarity needs two). And choose light blue and purple. → These are outliers 😱.

![[Screenshot 2024-11-28 at 1.04.28 PM.png]]
When we check match distances, we can see that the matching is very poor.

![[Screenshot 2024-11-28 at 1.05.01 PM.png]]
Thus, the number of our consensus set is 2 (only the numbers we sampled initially).

We pick two other points,
![[Screenshot 2024-11-28 at 1.06.53 PM.png]]

![[Pasted image 20241128130712.png]]
Now that we have more things that are aligning. So we have a new consensus set of 4. And we would prefer this over the previous. We can use all four points in this set to re-estimate.

RANSAC determines the best solution, so for in object recognition if we have more than one good match we might not get the best result.

#### Re-cap RANSAC
- RANSAC is a technique to fit model to data.
	- Divide data into inliers and outliers.
	- Estimate model from minimal set of inliers.
	- Improve model estimate using all inliers.
	- Alternate fitting with re-classification as inlier/outlier.

- RANSAC is general method suited for a wide range of model fitting problems.
	- Easy to implement.
	- Easy to estimate/control failure rate.
- RANSAC only handles a moderate percentage of outliers without cost blowing up.

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 13|Lecture 13]]
