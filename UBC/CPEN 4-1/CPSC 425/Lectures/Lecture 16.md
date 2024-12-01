x#### Instance vs. Category
In classifications, we look for specific categories. We need the ability to find all possible “instances” under some “category”.

#### WordNet
We can use language to organize visual categories. It’s done in terms of synsets, which are groups of data elements considered semantically equivalent.

Visual categories have *complex relationships*.
- e.g. a “sail” is part of a “sailboat” which is a “watercraft”.

But, if we call a “sailboat” a “watercraft”, is that wrong? This is per application, each application will need different specifications.

#### Classification
**Problem**:
Assign new observations (in our case an image) into one of a fixed set of categories (classes).

**Key Idea**:
Build a model of data in a given category based on observations of instances in that category.

![[Screenshot 2024-11-30 at 5.35.08 PM.png]]
Typically, rather than giving an output of a particular label, we get a probabilistic representation of the input, for instance,
![[Screenshot 2024-11-30 at 5.35.55 PM.png]]

==It’s a procedure that accepts as input a set of features and outputs a class **label** (probability over class labels)==

Classifiers can be **binary** or **multi-class**,
$$\text{Binary :}[0] / [1] \hspace{.3in} \text{Multi-class}:[1,0,0,\cdots,0]$$
We build a classifier using a **training set** of labelled examples $\left\{ (\mathbf{x}_{i},y_{i}) \right\}$, where each $\mathbf{x}_{i}$ is a feature vector and each $y_{i}$ is a class label.

Given a previously unseen observation (new to training data set), we use the classifier to predict its class label.

[Set up]
- Collect DB of images with labels.
- Use ML to train an image classifier.
- Evaluate the classifier on test images.

![[Screenshot 2024-11-30 at 5.41.31 PM.png]]
This is simple for binary classification…

![[Screenshot 2024-11-30 at 5.42.23 PM.png]]
![[Screenshot 2024-11-30 at 5.42.32 PM.png]]
A large number of categories makes it hard to categorize.

###### Closed-world problem
The issue is that classification assumes that the incoming image belongs to one of the $k$ classes. However, in practice it is impossible to enumerate all relevant classes in the world, nor would doing so be useful. **We still need to deal with images that don’t belong to any category**.

**Solution**:
Create an ‘unknown’ or ‘irrelevant’ class.

![[Screenshot 2024-11-30 at 5.44.44 PM.png]]

#### Image Classification
##### Representation of Images
- Image pixels directly.
- Bag of Words.

###### Visual Words
Many algorithms for image classification accumulate evidence on the basis of *visual words*.
To classify a text document, we might find patterns in the occurrence of certain words.

For instance, if we have two documents,
![[Screenshot 2024-11-30 at 5.46.52 PM.png]]
We can build a dictionary and then measure how many times a word exists in the document.
By comparing the two, we can determine if they come from the same category or not.

A document (datapoint) is a vector of counts over each word (feature)
$$v_{d}=[n(w_{1},d),n(w_{2},d),\cdots,n(w_{T},d)] \hspace{.5in}n(\cdot)=\text{counts the number of occurences of word}$$

How can we measure the similarity between the two documents?
→Similarity between histograms (maybe cosine).

==But, what is the issue?==
→It is susceptible to the number of words in the document, we have to normalize by the total word count,
$$d(v_{i},v_{j})=\cos \theta= \frac{v_{i}\cdot v_{j} }{\lvert \lvert v_{i} \rvert  \rvert \lvert \lvert v_{j} \rvert  \rvert }$$

In images, the equivalent of a **word** is a **local image patch**. The local image is described using a descriptor such as SIFT.

We construct a **vocabulary** or **codebook** of local descriptors, containing representative local descriptors (with a histogram).

Some local features are very informative, 
- Deals well with occlusions.
- Scale invariant.
- Rotation invariant.

Spatial information of local features can be ignored for object recognition.

###### Standard bag of words pipeline (for image classification)
1. **Dictionary Learning**
	1. Learn Visual words using clustering.
2. **Encode**
	1. Build bag-of-words vectors for each image.
3. **Classify**
	1. Train and test data using bag-of-words.


**Dictionary Learning**
First, we *extract features* from images (using SIFT)
![[Screenshot 2024-11-30 at 5.58.57 PM.png]]
How should we extract features?
- Regular grid
- Interest point detector (SIFT!)
- etc..

Assume we’re using SIFT,
- We take all the interest points for a given image. → Compute SIFT descriptor.
	- We do this for many images across the web.
	- We compute SIFT descriptors for where matches would occur in different images.
![[Screenshot 2024-11-30 at 6.04.37 PM.png]]

Second, we learn the visual dictionary (K-means clustering)
![[Screenshot 2024-11-30 at 5.59.44 PM.png]]
And with the computed descriptors above, we can think of each vector as a point in some 128D space. Then, we can cluster those points to see what the typical clusters are in the space. The centers would be the ‘words of visual vocabulary’ (the SIFT interest points that occur most often).


[A bit of K-Means Clustering]
Assume we **know** how many clusters there are in the data - denoted by K. Each **cluster** is represented by a **cluster center**, or mean. 

Our objective is to **minimize the representation error (quantization error)** in letting each data point be represented by some cluster center.

Minimize,
$$\sum_{i \in \text{clusters}}\left\{ \sum_{j \in i^\text{th}\text{cluster}}\lvert \lvert x_{j}-\mu_{i} \rvert  \rvert ^2 \right\}$$

There are two steps:
1. Assume the cluster centers are known (fixed), assign each point to the closest cluster center.
2. Assume the assignment of the points to clusters is known (fixed). Compute the best center for each cluster, as the mean of the points assigned to the cluster.

- It converges to local minimum of the objective function.
	- Results are initialization dependent.

![[Screenshot 2024-11-30 at 6.16.55 PM.png]]

![[Screenshot 2024-11-30 at 6.17.10 PM.png]]
The bottom shows the keywords and the patches assigned to that keyword.

**Encoding**
The length of the histogram is K, how many keywords we extracted. 
The counts are vector quantization of SIFT descriptors. 
For a new image, we can extract SIFT descriptors and assign each SIFT descriptor to the closest cluster and augment the cluster by one.

![[Screenshot 2024-11-30 at 6.20.05 PM.png]]

**Classify**
For instance, bird vs. plane classifier linear classifier in space of histograms.
![[Screenshot 2024-11-30 at 6.21.14 PM.png]]
##### Classification Algorithms
- Bayes’ Classifier.
- Nearest Neighbour Classifier.
- SVM Classifier.

###### Bayes’ Rule
Let $c$ be the class label and let $x$ be the measurement (evidence)
$$P(c\vert x)= \frac{P(x\vert c)P(c)}{P(x)}$$
$P(x\vert c)$: class-conditional probability (likelihood), $P(c)$: prior probability, $P(x)$: unconditional probability.
The unconditional probability doesn’t really matter, what dictates are the likelihood and prior probability.

Simple Case:
- Binary classifier $c\in \left\{ 1,2 \right\}$
- Features are 1D $x \in \mathbb{R}$

We can classify $x$ as
$$1:P(1\vert x) > P(2\vert x) \hspace{.5in}2:P(1\vert x) < P(2\vert x)$$
in general we would have multiple classes and features being multi-dimensional.

Assume we have two classes: $c_{1}=\text{male},c_{2}=\text{female}$. We have a person who’s gender we don’t know and who’s name is ‘drew’.

Classifying drew as being male or female is equivalent to asking ‘is it more probable that drew is male or female’ → Checking with posterior probability is bigger.

![[Screenshot 2024-11-30 at 6.33.31 PM.png]]
$$P(\text{male}\vert \text{drew}) =  P(\text{drew}\vert\text{male})P(\text{male}) = \frac{1}{3} \times \frac{3}{8}=\frac{1}{8}$$
$$P(\text{female}\vert\text{drew})=\frac{2}{5} \times \frac{5}{8} = \frac{2}{8}$$
if we ignore the denominator. *It doesn’t matter since it appears in BOTH classifications*.

For higher dimensional data,
![[Screenshot 2024-11-30 at 6.37.47 PM.png]]
We can extract two channels (green, blue) and extract patches some sky and grass. We can measure a prior distribution or fit a gaussian distribution to the data (likelihood). 
With the Gaussian likelihood we can evaluate the likelihood and compute the probability.

###### Bayes’ Risk
Some errors may be inevitable: the minimum risk (shaded area) is called the Bayes’ Risk.
![[Screenshot 2024-11-30 at 6.40.57 PM.png]]
We have a decision boundary where it sets the classification of the data. The value where the posterior’s are the same is called the “decision boundary”.

The shaded region is the misclassification region.

###### Loss Functions and Classifier
In general, misclassifications would not be equally bad either way. We may want to be sensitive to a specific direction.

The total risk of using classifier $s$ is,
$$R(s)=P(1\to 2 \vert s)L(1\to{2}) + P(2\to 1\vert s)L(2\to 1)$$
where the cost of miss-classification is denoted by $L$.

###### Classifier Strategies
We normally have two broad types: **parametric** and **non-parametric**.

**Parametric Classifiers**
They are *model driven*. The parameters of the model are learned from the training examples. New data points are classified by the learned model.
- Fast, compact (num parameters < num data samples).
- Flexibility and accuracy depend on model assumptions.

Ex. Bayes’

**Non-parametric Classifiers**
They are *data driven*. New data points are classified by comparing to the training examples directly. “The data is the model”.
- Slow.
- Highly flexible decision boundaries.

Ex. Nearest Neighbours
Given a new data point, assign the label of nearest training example in feature space.
![[Screenshot 2024-11-30 at 6.50.13 PM.png]]

For images,
$$i_{N N}=\text{arg }\text{min}_{i}\lvert x_{q}-x_{i} \rvert $$
![[Screenshot 2024-11-30 at 6.50.53 PM.png]]
We take a query image, extract the high dimensional histogram. And compute the distance between the test sample hence output a label for the query image.
$$\hat{y}(x_{q})=y(x_{i N N})$$
![[Screenshot 2024-11-30 at 6.52.03 PM.png]]
We can view each image as a point in the high dimensional space.

There’s also k-Nearest Neighbours,
- Given a new data point, find the k nearest training examples. Assign the label by majority vote.
- Simple method that works well if the distance measured correctly weights the various dimensions.
- For large data sets, as k increases kNN approaches optimality in terms of minimizing probability of error.

![[Screenshot 2024-11-30 at 6.59.29 PM.png]]

###### Linear SVM (parametric)
**Idea**:
Try to obtain decision boundary directly.

The decision boundary is parameterized as a *separating hyperplane* in feature space.
- e.g. separating a line in 2D

We choose the hyperplane that is as far as possible from each class - that maximizes the distance to the closest point from either class.

###### Linear Classifier
Defines a score function:
$$f(\mathbf{x}_{i},\mathbf{W},\mathbf{b})=\mathbf{W}\mathbf{x}_{i}+\mathbf{b}$$
$\mathbf{W}$: weights (parameters), $\mathbf{b}$: bias vector (parameters), $\mathbf{x}_{i}$: image features

![[Screenshot 2024-11-30 at 7.03.17 PM.png]]
We would have a bias and weight for each class. (need to learn weights and bias for correct classes) → weights are related to hyperplane.

![[Screenshot 2024-11-30 at 7.04.08 PM.png]]

What is the best $\mathbf{W}$?
→ Intuitively, the line that is the furthest from all interior points.

We can write the decision boundary in terms of support vectors, which are the data points closest to the decision boundary.
![[Screenshot 2024-11-30 at 7.06.42 PM.png]]

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 17|Lecture 17]]
