#### Correspondence Problem
It’s about establishing matches (correspondences) between images.
- Rigid / non-rigid tracking.
- Object recognition.
- Image registration.
- Structure from motion.
- etc.

What are **good features** and **how do we match them**?

We want some invariance,

- Lighting Invariance: Edges are invariant
![[Screenshot 2024-11-26 at 9.01.34 PM.png]]

- Scale / Rotation / Translation Invariance
![[Screenshot 2024-11-26 at 9.01.55 PM.png]]


Since Harris and Blob are locally distinct, we minimally need them.
![[Screenshot 2024-11-26 at 9.02.56 PM.png]]

How do we know which **Blob** goes with which? → How do we match them?

![[Screenshot 2024-11-26 at 9.03.22 PM.png]]

We can extract patches around locally and use methods such as normalized correlation to get similarity among the patches.

###### Intensity Image
![[Screenshot 2024-11-26 at 9.04.09 PM.png]]

If geometry and appearance changes (particularly with lighting) → This is not really useful.
We can use edges (that are lighting invariant) or gradients (within the patch).
→ This is less sensitive to the actual lighting conditions.

![[Screenshot 2024-11-26 at 9.05.17 PM.png]]

But there are still problems → We are invariant to lighting (at least in shifts) but there are very sparse. When taking a photo from a different view point, then the edges wouldn’t align geometrically (geometric invariance isn’t held).

What can we do? 
![[Screenshot 2024-11-26 at 9.07.03 PM.png]]
We can use local coordinate frames that follow surface transformation (covariant) and compute feature descriptors in them. (Estimate rotation and scale, and undo those so that the features align better)

##### Strategies
- Detecting Scale / Orientation
![[Screenshot 2024-11-26 at 9.08.56 PM.png]]
We detect a local scale and orientation for each feature point.
e.g. Extract Harris at multiple scales and align to the local gradient.

![[Screenshot 2024-11-26 at 9.09.54 PM.png]]
Orient it so that the axes align and match the scale → Canonical Scale Matching!

**But, even if we do this in terms of really aligning edges. → We build a distribution over edges (despite they don’t align perfectly, more tolerant), since the distribution would still be the same. **

- Represent Distributions over Gradients
![[Screenshot 2024-11-26 at 9.13.30 PM.png]]

#### Invariant Local Features
The task is to identify objets or scenes and determine their pose and model parameters.

Applications:
- Industrial automation and inspection.
- Mobile robots, toys, user interfaces.
- Location recognition.
- etc.

**David Lowe’s Invariant Local Features**
![[Screenshot 2024-11-26 at 9.15.43 PM.png]]

Image content is transformed into local feature coordinates that are invariant to translation, rotation, scale and other imaging parameters.

**Advantages of Invariant Local Features**
- Locality: Features are local, so robust to occlusion and clutter. 
- Distinctiveness:  individual features can be matched to a large database of objects.
- Quantity: Many features can be generated for even small objects.
- Efficiency: Close to real-time performance.

#### SIFT (Scale Invariant Feature Transform)

SIFT describes both a *detector* and *descriptor*,
1. Multi scale extrema detection. *detector*
2. Key-point localization. *detector*
3. Orientation assignment. *detector*
4. Key-point descriptor. *descriptor*

###### Multi Scale Extrema Detection
![[Screenshot 2024-11-26 at 9.20.36 PM.png]]
We create levels in between as continuous blurring sometimes with same scale and sometimes sub-sample.

And the difference of Gaussian gives the Laplacian, with a high laplacian response → We have a blob.

![[Screenshot 2024-11-26 at 9.22.12 PM.png]]
If we know that the loonie here is responsive at $\sigma$, then when we scale the loonie, we know what $\sigma$ will respond highly at that scale.
→ When we know what $\sigma$ the response is high at, we know the factor to scale down at.

For instance, in the second example at $s = 0.5$, if we found a loonie at the $\sigma$ that means the original scale was bigger $\frac{1}{\sigma} = 2$ so we know that the scale is 2 times up.

![[Screenshot 2024-11-26 at 9.30.51 PM.png]]
It includes intermediate steps as if we created a Gaussian Pyramid with a sampling rate of 2.
$s$ is the number of intermediate scales (so in the picture above $s=4$).

![[Screenshot 2024-11-26 at 9.33.04 PM.png]]

![[Screenshot 2024-11-26 at 9.33.47 PM.png]]
We can do a sub-maxima suppression at every octave by choosing a good response among neighbouring levels.

==What happens if we have more levels per octave, is it better?==
![[Screenshot 2024-11-26 at 9.35.02 PM.png]]
Just because more matches exist → not necessarily more accurate matches.
The optimal is at about 2 or 3 (3 or 4 laplacian levels).

###### Key-point Localization
After key-points are detected, we remove those that have ==low contrast== or are ==poorly localized== along an edge (not strong blobs).

Blobs respond to edges AND blobby regions (and since edges are not **locally unique** we really don’t want them)

We distinguish them via **Covariance Matrix (+ Eigen Values)**, we combine blobs with Harris and leave those that have **high corner-ness!!!**.

![[Screenshot 2024-11-26 at 9.39.05 PM.png]]

###### Orientation Assignment
![[Screenshot 2024-11-26 at 9.39.32 PM.png]]
==Harris would just compute the eigen vectors based on the just covariance matrix, but here we actually use the gradients themselves.==

- Create a **histogram** of local gradient directions computed at selected scale. Find the dominant orientation.
![[Pasted image 20241126214209.png]]
So we get a distribution of orientations, and we can assign a dominant orientation per key-point (strength of vote is magnitude, and also we have a gaussian weighted voting).

But, what happens if we don’t have a dominant orientation?
![[Screenshot 2024-11-26 at 9.43.48 PM.png]]
We create two different key-points with two different dominant orientations (same scale)

- Assign **canonical orientation** at peak of smoothed histogram.
- Each key specifies stable 2D coordinates (x, y, scale, orientation).

###### Key-point description
We have seen in **key-point detection** on how to assign location, scale and orientation to each key-point.

The next step is to compute a **key-point descriptor**: It should be robust to local shape distortions, changes in illumination or 3D view point (as mentioned in the very first part).

==It differs from key-point detection.==

- Image gradients are sampled over 16 x 16 array of locations in scale space (weighted by a Gaussian with sigma half size of the window).
- Create array of orientation histograms.
- 8 orientations x 4 x 4 histogram array.

![[Screenshot 2024-11-26 at 9.50.07 PM.png]]

We have 4 x 4 regions, 4 x 4 pixels, for each region create a histogram similar to the way we did orientation. 

==We then have 4 x 4 x 8 = 128 dimensional descriptors.==

If lighting changes (a shift in grey scale), in this representation it doesn’t change at all (gradients change). If contrast happens, gradients are scaled and since we’re voting this histogram will also be scale as well.
→ So we normalize the descriptor.

Descriptor is **normalized** to unit length to reduce effect of illumination change.
- If brightness is scaled (multiplied), the grades are scaled with same constant, and normalization cancels this change.
- If brightness values are translated (additive), the gradients do not change at all.


#### SIFT Matching
Now that we identified all descriptors all we have to do is match among different images.
We extract and match all SIFT descriptors from each image.

- Each SIFT feature is represented by a 128 dimensional vector.
- Feature matching becomes the task to finding the closest 128 dimensional vector.
- We can do Nearest Neighbour Matching: $$N N(j)=\text{arg min}_{i}\lvert x_{i}-x_{j} \rvert, i\neq j $$
	- But this is expensive (linear time), good approximation algorithms exist.

###### Match Ratio Test
So far we are trying to match things that were locally unique (not globally) → if we have an edge of a window, we would not have a global unique match.

We can thus compare the ratio between the best match and the second best matching neighbour.

A rule of thumb: d(1NN) < 0.8 * d(2NN) for a good match.
![[Screenshot 2024-11-26 at 10.10.00 PM.png]]

###### Feature Stability of Noise / Affine Change
Match features after random change in image scale & orientation, with differing levels of image noise.

![[Screenshot 2024-11-26 at 10.12.31 PM.png]]

![[Screenshot 2024-11-26 at 10.12.00 PM.png]]
Since we just compare the distribution of the histograms we can still match pretty accurately (it is robust).

#### Other descriptor algorithms
- HOG (Histogram of Oriented Gradients) Features
![[Screenshot 2024-11-26 at 10.16.13 PM.png]]
Instead of computing among non-overlapping regions, we compute along overlapping regions (thus having a larger dimension among descriptors). But similar idea, also a bit slower.

- SURF (Speeded Up Robust Features)
![[Screenshot 2024-11-26 at 10.17.38 PM.png]]
We don’t compute histogram but statistically measure → we get smaller dimensionality among descriptors.

#### Key-point Detectors vs Descriptors
**Detectors**
- Harris
- Blob
- SIFT (mix of two above)

**Descriptors** (similar idea of gradient used distributions but different design choices)
- SIFT
- HoG 
- SURF

Any combination of the two categories would work!


#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 12|Lecture 12]]
