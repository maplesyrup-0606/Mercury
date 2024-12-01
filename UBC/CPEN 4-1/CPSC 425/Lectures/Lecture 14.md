### Stereo Vision
Determining depth using two images acquired from (slightly) different viewpoints.

Key idea: The 3D coordinates of each point imaged are constrained to lie along a ray. This is true also for a second image obtained from a (slightly) different viewpoint. Rays for the same point in the world intersect at the actual 3D location of that point.

We can do with SIFT, but it gives depth at certain points not every single pixel (Assuming they are correct too).

==We perceive **depth** based on **differences in the relative position of points** in the left image and the right image.==

Eyes further apart can determine depth better.

#### Binoculars
Binoculars enhance binocular depth perception in two distinct ways:
1. Magnification.
2. Longer baseline (distance between entering light paths) compared to the normal human inter-pupillary distance.

#### Stereo Vision
**Task**: Compute depth from two images from different viewpoints.
**Approach**: “Match” locations in one image to those in another.
**Sub-tasks**:
- Calibrate cameras and camera positions.
- Find all corresponding points (hardest).
- Compute depth and surfaces.

#### 2-view Geometry
How de find dense correspondences between two views?
![[Screenshot 2024-11-28 at 4.13.54 PM.png]]

In the planar case: the mapping can be obtained by homography
![[Screenshot 2024-11-28 at 4.15.45 PM.png]]
And we can get to dense correspondences since we know ho to warp every point.
==It only works when the world is planar, which is generally not the case.==

Non-planar case:
![[Screenshot 2024-11-28 at 4.16.41 PM.png]]
Under perspective projection, lines are still lines. The only correspondence that would be consistent would a line in the second view.
![[Screenshot 2024-11-28 at 4.17.32 PM.png]]
And that line is called the epipolar line.

#### Epipolar Constraint
If we have a point in one image, the corresponding point in the other image has to lie along a line.

This reduces the correspondence problem to 1D search along conjugate epipolar lines. →Greatly reduces cost and ambiguity of matching.
![[Screenshot 2024-11-28 at 4.23.53 PM.png]]
We form a ray between the cameras + the ray from the projection of the point in the camera to the scene as seen from the 2nd camera → Thus gives a epipolar line.

#### Improving RANSAC + Epipolar Geometry
Once we have SIFT features, look at matches closer to epipolar line and disregard those further away.

![[Screenshot 2024-11-28 at 4.27.50 PM.png]]

#### Simplest Case: Rectified Images
We can warp images in a way such that a few conditions hold.

- Image planes of cameras are parallel.
- Focal **points** are at same height.
- Focal **lengths** are same.

We can do this by warping each view by homography, we can solve for what the homography needs to be in order for the constraints to hold.

→ Then, **epipolar lines** fall along the ==horizontal scan lines== of the images.
- Simplifies algorithms.
- Improves efficiency.

*Essentially, rectify the views and compute more efficiently.*

#### Stereo Matching in Rectified Images
In standard stereo setup, where cameras are related by translation in the $x$ direction, epipolar lines are horizontal.
![[Screenshot 2024-11-28 at 6.48.13 PM.png]]
- Stereo algorithms search along scanlines for match.
- Distance along the scanline (difference in $x$ coordinate) for a corresponding feature is called **disparity**.
- Distance tells how far things are, $d$ small → things further away, $d$ large → close to us.

#### Rectified Stereo Pair
**Any** two camera views that overlap can be **rectified** so that epipolar lines correspond to scan lines (no special conditions much hold).

![[Screenshot 2024-11-28 at 6.59.44 PM.png]]
We can project both views into a common plane (between centers of camera views)

![[Screenshot 2024-11-28 at 7.00.34 PM.png]]
- Re-project image planes onto a common plane parallel to the line between camera centers (grey→yellow).
- Need two homographies (3 x 3 transform), one for each input image reprojection.

#### Depth Estimation
![[Screenshot 2024-11-28 at 7.06.27 PM.png]]
We have two cameras (origins denoted):
- We can shoot rays from center to pixel, we know the point has to form a line in 3D world.
	- The two lines intersect the point in the 3D world.
	- We assume that these points are in correspondence.

![[Screenshot 2024-11-28 at 7.09.01 PM.png]]
Let $X$ be the distance from the point to the origin $O$. Then, 
$$\frac{X-b}{Z}= \frac{x'}{f}$$
$$\frac{X}{Z}=\frac{x}{f}$$
hence,
$$\frac{X-b}{Z}=\frac{X}{Z}-\frac{b}{Z}=\frac{x}{f}-\frac{b}{Z}=\frac{x'}{f}$$
$$d=x-x'= \frac{b}{Z}f$$
and we can see that it is inversely proportional to depth.
We already know $b,f$ so depending on disparity $d$, we can compute for depth $Z$.

#### (simple) Stereo Algorithm
```
1. Rectify images (make epipolar lines horizontal)
2. For each pixel
	a. Find epopolar line
	b. Scan line for best match
	c. Compute depth from disparity
```

#### Pixel Matching
```
For each epipolar line
	For each pixel in the left image
		compare with every pixel on same epipolar line in right image
		pick pixel with minimum match cost
```
Not the best..

Define the window function by,
$$\mathbf{W}_{m}(x,y)=\left\{ (u,v)\vert x-\frac{m}{2} \leq u \leq x + \frac{m}{2}, y-\frac{m}{2}\leq v\leq y+\frac{m}{2} \right\}$$

SSD measures intensity difference as a function of disparity:
$$C_{R}(x,y,d)=\sum_{(u,v) \in \mathbf{W}_{m}(x,y)}[I_{L}(u,v)-I_{R}(u -d,v-d)]^2$$


#### Image Normalization
Average Pixel:
$$\bar{I}= \frac{1}{\lvert \mathbf{W}_{m}(x,y) \rvert }\sum_{(u,v)\in \mathbf{W}_{m}(x,y)}I(u,v)$$
Window Magnitude:
$$\lvert \lvert I \rvert  \rvert _{\mathbf{W}_{m}(x,y)}=\sqrt{ \sum_{(u,v) \in \mathbf{W}_{m}(x,y)}[I(u,v)]^2 }$$
Normalized pixel:
$$\hat{I}(x,y)= \frac{ I(x,y)-\bar{I}}{\lvert \lvert I-\bar{I} \rvert  \rvert _{\mathbf{W}_{m}(x,y)}}$$

We can also use normalize correlation,
$$C_{NC}(d)= \sum_{(u,v)\in \mathbf{W}_{m}(x,y)}\hat{I}_{L}(u,v)\hat{I}_{R}(u-d,v)=\mathbf{w}_{L} \cdot \mathbf{w}_{R}(d)=\cos \theta$$

For carefully chosen $d$, we get the same results for both cases.

#### Effect of Window Size
If we have a small window:
- We have more detail (+) depth estimate.
- We have more noise (-).
	- Higher sensitivity to noise due to small window size.

If we have a large window:
- Smoother disparity maps (+).
	- Contrast to smaller windows.
- Less detail (-).
- Fails near boundaries (-).
	- In one view, there’s going to be occlusions and dis-occlusions.
		- In one view, some pixels are present. In other, pixels won’t be there.
			- Discontinuity between depth.
![[Screenshot 2024-11-28 at 7.32.26 PM.png]]

#### Ordering Constraints
Irrespective of patch size, we will have problems in regions that have uniform color.
→ Matching is kind of arbitrary.

![[Screenshot 2024-11-28 at 7.35.25 PM.png]]
The idea is that the correspondences would be in the same order in both views.
$$c\to b \to a \text{ and } c'\to b'\to a'$$
Works for convex objects.

We also have a failure case,
![[Screenshot 2024-11-28 at 7.36.35 PM.png]]

#### Block Matching Techniques
![[Screenshot 2024-11-28 at 7.39.10 PM.png]]
We can see that compared to the ground truth that the block matching has discontinuity in depth.

We can assume that “depth should change smoothly” (for most regions, maybe except boundaries).

We can apply energy minimization,
$$E(d) =E_{d}(d)+\lambda E_{s}(d)$$
Where $E(d)$ is the energy function for one pixel, $E_{d}(d)$ is a data term, $E_{s}(d)$ is smoothness term.

- First term is from the cost function (SSD etc.).
- Second term is Smoothness term, penalizes pixels for which nearby disparity is too different from one another.

We can do various smooth terms,
- L1 distance

And this can be optimized via dynamic programming.
![[Pasted image 20241128194859.png]]

#### Using More Cameras
![[Screenshot 2024-11-28 at 8.01.55 PM.png]]
Adding another camera reduces ambiguity.
1. Compute disparity and depth from two views, and re-project on third view to verify.
2. Optimize 3D position directly, ensuring correspondence across all three views are satisfied. 

##### Structured light imaging
Instead of having two cameras, we can replace the other camera with a projector.![[Screenshot 2024-11-28 at 8.08.07 PM.png]]
Instead of other camera doing matches, we can have a projector.
We know which pixels we are projecting, we just need to find the pixels in the camera view and then find correspondence and then find for depth. 

Projectors actively generate a signal that is easy to detect on the left. 
For instance, Microsoft Kinect.

We can emit (unique) random patterns, that are easy to pick up, and we know correspondence between IR emitter and depth sensor. We can compute disparity and know the depth.

Essentially,
- We know the pattern projected, we can directly warp them to the other camera.
- With the depth sensors, we can directly compare the projected pattern.
	- We augment the world with easily detectable patterns.

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 15|Lecture 15]]
