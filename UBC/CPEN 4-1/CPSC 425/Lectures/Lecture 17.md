#### Inference of Bag-of-Words Representation
**Algorithm**:
```
Initialize an empty K-bin histogram, where K is the number of codewords.
Extract local descriptors (SIFT) from the image.

For each local descriptor x :
	Map (Quantize) x to its closest codeword -> c(x)
	increment histogram bin for c(x)

Return Histogram
```
We can then classify the histogram using a trained classifier, e.g. a support vector machine or k-Nearest Neighbour classifier.

#### Spatial Pyramid
The bag-of-words representation doesn’t preserve any spatial information (we’re only counting). 

The **spatial pyramid** is one way to incorporate spatial information into the image descriptor.

A spatial pyramid partitions the image and counts codewords within each grid box; this is performed at multiple levels.

![[Screenshot 2024-11-30 at 7.38.58 PM.png]]
Compute BOW histograms for each quadrant and then concatenate them.
Original bag of word is 1000 dimensions, we have 4000 thousand the next and the last one is 16000 dimensions. → 21000 dimensions. (Dimensionality increases by incorporating spatial information!!)

#### VLAD (Vector of Locally Aggregated Descriptors)
Other than incrementing the histogram bin. For example, it might be useful to describe how local descriptors are quantized to their visual words. Instead of incrementing the histogram bin, which doesn’t give the idea of how the words are distributed respect to code words.

In the VLAD representation, instead of incrementing the histogram bin by one, we increment it by the residual vector $\mathbf{x-c(\mathbf{x})}$.

This stores how close the descriptor is to some keyword, thus including more information. Instead of storing the count in each position, we store the average residual (128 dimensions).

Helps distinguish objects based on fine grained details, for instance if we want to distinguish between a tiger and a cat.
![[Screenshot 2024-11-30 at 7.45.54 PM.png]]

The dimensionality of a VLAD descriptor is $Kd$:
- $K$ is the number of codewords.
- $d$ is the dimensionality of the local descriptor.

VLAD characterizes the distribution of local descriptors with respect to the codewords.

#### Decision Tree
A decision tree is a simple non-linear parametric classifier. Consists of a tree in which each internal node is associated with a feature test.

A data point starts at the root and recursively proceeds to the child node determined by the feature test, until it reaches a leaf node.

The leaf node stores a class label or a probability distribution over class labels.
![[Screenshot 2024-11-30 at 8.09.59 PM.png]]

Considering the features, what kind of test can we do to informatively choose which test to apply first to create a classifier that would accordingly classify data.

![[Screenshot 2024-11-30 at 8.12.41 PM.png]]
We have two tests, we need to evaluate which test is better → we need to measure information gain, how much information would we gain by doing either of these tests (which is measured in terms of entropy)

###### Entropy 
The **entropy** of a set $S$ of data samples is defined as 
$$H(S) =-\sum_{c \in C}p(c) \log(p(c))$$
where $C$ is the set of classes represented in $S$, and $p(c)$ is the empirical distribution of class $c$ in $S$.

Entropy is highest when data samples are spread equally across all classes, and zero when all data samples are from the same class.

![[Screenshot 2024-11-30 at 8.15.08 PM.png]]
The information gain is the entropy of the root minus the sum of the entropy of its child nodes.

$$I = H(S) - \sum_{i \in \left\{ \text{children} \right\}} \frac{\lvert S^i \rvert }{\lvert S \rvert }H(S^i)$$
We would prefer the test which has a higher information gain.
This is building a tree in a greedy recursive manner by maximizing information gain at each node.

![[Screenshot 2024-11-30 at 8.18.53 PM.png]]

###### Random Forest
A random forest is an ensemble of decision trees. Because decision trees tend to have high variance in terms of results. If we want to reduce variance, we create many variants of decision trees and vote among the decisions between different decision trees.

→ How do we get different decision trees?
Randomness is incorporated via training set sampling and / or generation of the candidate binary tests.

The prediction of the random forest is obtained by averaging over all decision trees.
![[Screenshot 2024-11-30 at 8.21.25 PM.png]]

[Kinect]
We classify the pixel to which body part it belongs to → identify joints. And this is done by random forests.

**Simple Test**:
Threshold on difference of two depth values at an offset from a target pixel
$$f_{\theta}(I,\mathbf{x})= d_{I}\left( \mathbf{x}+ \frac{\mathbf{u}}{d_{I}(\mathbf{x})} \right) - d_{I}\left( \mathbf{x}+ \frac{\mathbf{v}}{d_{I}(\mathbf{x})} \right)$$
$$f_{\theta}(I,\mathbf{x}) > \Theta_{j}$$
![[Screenshot 2024-11-30 at 8.23.55 PM.png]]
Comparing two depth values at a particular $\mathbf{u},\mathbf{v}$. Depending on difference, we choose the child node. → We have parameters $\mathbf{u},\mathbf{v}$ (offsets), $\Theta_{j}$ (threshold).

We can have $\# \text{pix} \times \# \text{pix} \times \# \text{threshold}$ tests (A LOT). And we have to figure which one is more informative at each node (very slow).

- Learning is slow (Training).
- Inference is fast (Real-time).

#### Combining Classifiers
One common strategy to obtain a better classifier is to combine multiple classifiers. A simple approach is to train an ensemble of independent classifiers, and average their predictions.

By combining classifiers, we can get more expressive classifiers.

**Boosting** is another approach:
- Train an ensemble of classifiers sequentially.
- Bias subsequent classifiers to correctly predict training examples that previous classifiers got wrong.
- The final boosted classifier is a weighted combination of the individual classifiers.

#### Object Detection: Introduction
We have been talking about image classification, where we pass a whole image into a classifier and obtain a class label as output.

We assumed the image contained a single, central object. 

The task of **object detection** is to detect and localize all instances of a target object class in an image. 
- Localization typically means putting a tight bounding box around the object.

##### Sliding Window
Train an image classifier as described previously. ‘Slide’ a fixed-sized detection window across the image and evaluate the classifier on each window.

![[Screenshot 2024-11-30 at 8.34.41 PM.png]]
We can change size, resolution of window. (Not the most efficient since we look over location in very different scales and classify)

How we train these classifiers?
Image classifiers can be applied to regions/windows (image level classifiers) → since images contain other things, it would not be a very accurate object detector.
![[Screenshot 2024-11-30 at 8.37.15 PM.png]]

What we can do instead is label bound boxes and extract all patches that contain cats and train the classifier based on cropped cat images.

But now these are in different sizes → Need something to ensure classify a fixed size → We can warp images to some canonical size and then train!

![[Screenshot 2024-11-30 at 8.40.23 PM.png]]

The **Viola-Jones** face detector is a classic sliding window detector that learns both efficient features and a classifier. The key strategy is to use features that are fast to evaluate to reject most windows early (this one computes rectangular features within each window).

###### Efficiency
The main issue of sliding window is efficiency. We evaluate many different boxes. A lot of boxes have no chance to detect what we want → wasting resources.

**Observation**:
- On average, only 0.01% of all sub-windows are positive.
- Equal computation time is spent on all sub-windows.
- We should only spend most time only on potentially positive sub-windows.

==Need to disregard those with no chance! We should disregard earlier!!!!==

**Solution**:
- A simple 2-feature classifier can act as a 1st layer of a series to filter out most negative windows.
- 2nd layer with 10 features can tackle “harder”-negative windows which survived the first layer → and so on..

#### Cascading Classifiers
 ![[Screenshot 2024-11-30 at 8.47.53 PM.png]]
To make detection faster, features can be reordered by increasing complexity of evaluation and the thresholds adjusted so that the early simpler tests have few or no false negatives.

Any window that is rejected by early tests can be discarded quickly without computing the other features.

#### Hard Negative Mining
The fact that if we are going to randomly select data for a classification task, a lot of data samples (particularly for negatives) would be very easy examples. In the world, there can be patterns that can be confused with the task, but generally not the task we want to classify.

Having those in the training set would boost (hard to find though). 
Train a classifier in the standard way, we have a set of images that are for sure not faces (large) → we run the classifier on these → find the places where the classifier detects a face → we know that this is a false positive → collect those regions classifier fired on (strongly) → add to negative set → re-train → repeat.

![[Screenshot 2024-11-30 at 8.56.41 PM.png]]

#### Object Proposal
Instead of lots of possible regions where we evaluate classifier → we have an algorithm that very quickly generate a set of regions that may contain ANY object.

![[Screenshot 2024-11-30 at 8.58.05 PM.png]]
We can compute the classifier on these regions to reduce computation time.

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 18|Lecture 18]]
