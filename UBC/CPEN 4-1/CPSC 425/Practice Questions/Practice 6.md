#### Question 1
Consider conditions under which an epipolar constraint used in stereo matching holds between images from two cameras. Which of the following conditions are true? Which are false? (Assume standard perspective projection)

What were the constraints to have horizontal epipolar lines?
→ Same focal length
→ Same height of camera setup
→ Parallel image planes

Epipolar constraint → the object will be on a epipolar line on the other camera.

- The two cameras must have coplanar projection planes.
**False**, they don’t need to. We can rectify to hold this.

- The two cameras must face in the same direction.
**False**, similar to above. We don’t NEED this.

- The two images must be rectified.
**False**, not necessarily.

- There are no restrictions on camera locations or orientations, an epipolar constraint always applies.
**True**

#### Question 2
Stereo matching can be performed by correlating windows of pixels between two images. But, it is difficult to know what window size to use. The following statements identify problems when the window size is too large. Which is true? Which are false?

- There will be more false images due to ambiguity and image noise.
**False**, this would refer to a small window size.

- Places where depth is discontinuous will be poorly matched.
**True**, especially on the corners.

- The epipolar constraint is not as effective to limit the number of matches.
**False**, epipolar constraint is enough to reduce from the whole image to a single line on an image.

#### Question 3
The Lucas-Kanade method makes several assumptions about motion and optical flow. Which assumptions are ture?

- Corresponding points in a sequence of images of a moving object have exactly the same brightness value.
**True**, $\frac{dI}{dt}= 0$ for pixels on a stream of time.

- Sampling in $x,y$ and $t$ is frequent enough that the partial derivative $I_{x},I_{y}$ and $I_t$ are well-defined.
**True**, we want smooth derivatives so the matrix doesn’t blow up.

- The motion, $[u,v]$, is constant in the selected window about each image point, $[x,y]$.
**True**, this has to be constant for solving the least squares solution.

- The matrix$$A^TA=\begin{bmatrix}
\sum I_{x}^2 & \sum I_{x}I_{y} \\
\sum I_{x}I_{y} & \sum I_{y}^2
\end{bmatrix}$$ has rank 2 in the selected window about each image point.
**True**

#### Question 4
As we have seen, determining corresponding points in the left image and in the right image is the hardest part of stereo vision. A variety of things can go wrong in stereo matching. In a sentence or two for each, give a specific example of a scene where

- there are not enough locally distinct features that match.
A plane region with not much change, plain grey wall.

- there are too many locally distinct features that match.
Closely space objects that are visually similar.

- locally distinct features match incorrectly.
Objects that are different but are visually similar.

#### Question 5
Lucas–Kanade estimate the 2-D motion, [u, v], at a given point, [x, y], in an image by computing the partial derivatives, Ix, Iy, It, in a window centered at the given [x, y]. Their method assumes all points in the window are “inliers” with respect to the estimation of a single motion, [u, v]. Suppose, instead, that there are multiple, distinct motions occuring within the window. Describe, in a few sentences, how you might use a Hough transform  
approach to detect and determine the multiple motions.

We essentially want to solve for 
$$uI_{x}+vI_{y}+I_{t}=0$$
and we are given values of $I_{x},I_{y},I_{t}$ for a given window. 

We can use the parameter space of $u,v$ and set them to have a max and min value of $s$ for instance. 

For each pair of $I_{x},I_{y},I_{t}$ we use that line in $uv$ space to vote in the quantized bins. We can then get the maxima to find the most dominant movement.

