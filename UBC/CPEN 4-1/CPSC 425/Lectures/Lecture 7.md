#### Detection Performance
- TP = True Positive
- FP = False Positive
- TN = True Negative
- FN = False Negative

###### Recall & Precision
$$\text{Precision} = \frac{TP}{TP+ FP }$$
$$\text{Recall} = \frac{TP}{TP + FN}$$

Depending on where we set the threshold, we can trade off between True positives and False positives.
![[Screenshot 2024-10-18 at 10.55.13 AM.png]]

We can easily aim to get 100% True Positives, IF we are prepared to also get 100% False Positives as well. TP vs. FP!

We can plot a curve of all TP rates vs. FP rates by varying the classifier threshold and this is called the **Receiver Operating Characteristic (ROC)**.
![[Screenshot 2024-10-18 at 10.57.07 AM.png]]


#### Image Blending
![[Screenshot 2024-10-18 at 11.19.57 AM.png]]

1. Define a mask of how much we want to keep from the left and the same for the right.
	1. Each side will be an inverse of each other.
2. Blend lower frequency bands over larger spatial ranges, high frequency bands over small spatial ranges.
	1. Basically for abrupt changes, we pick one or another and for gradual changes we choose how much proportion we want to allocate from one another.

Algorithm:
```python
1. Build Laplacian pyramid LA and LB from images A and B.
2. Build a Gaussian pyramid GR from mask image R.
3. From a combined Laplacian pyramid LS, using nodes of GR as weights:
	LS(i,j) = GR(i,j) * LA(i,j) + (1 - GR(i,j)) * LB(i,j)
```

**Alpha blending is more sensitive to alignment.**

#### Improving Template Matching
Image detection can get much noisier with images that don’t have the exact template within the image.

![[Screenshot 2024-10-18 at 11.32.57 AM.png]]

We can try getting a number of templates and iteratively run for each template to match better → but this is inefficient, and the template batch size would have to be significantly high.


##### Template Matching with HoG
Template matching can be improved by using better features, e.g., Histograms of Gradients.
We can used a Learning-based-approach (SVM) to find an optimally weighted template.
![[Screenshot 2024-10-18 at 11.35.24 AM.png]]

##### Convnet Object Detection
Convnet based object detectors resemble sliding window template matching in feature space.
Architectures typically involve multiple scales and aspect ratios, and regress to a 2D offset in addition to category scores.

##### Local Feature Detection
Local information is more consistent among the image.
Consider people,
- Skin is different.
- Lighting is different.
	- These are going to create issues.

What if we factor out lighting and only focus on contours? Which are less lighting dependent. The contour of the object is pretty invariant.

![[Screenshot 2024-10-18 at 11.39.07 AM.png]]
We can represent objects by interest points, which describe what is important to that object.

![[Screenshot 2024-10-18 at 11.40.09 AM.png]]

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 8|Lecture 8]]
