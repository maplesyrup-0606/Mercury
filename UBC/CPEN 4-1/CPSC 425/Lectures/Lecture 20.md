#### Pooling Layer
![[Screenshot 2024-12-09 at 8.32.41 PM.png]]
Assume the filter is an ‘eye’ detector. How can we make detection spatially invariant (insensitive to position of the eye in the image)?

e.g. → detecting an eye without wanting location would be a good case to use such.

By **pooling** (for instance, taking the max) the responses over spatial locations we gain robustness to position variations. 

As long as the neuron fires anywhere among the space of choice, the output is going to be large. → Feature volume is also decreased which helps us because high feature volumes take a lot of space, high computation.

What does the pooling layer do,
- Makes representation smaller, more manageable and spatially invariant.
- Operates over each activation map independently.
![[Screenshot 2024-12-09 at 8.36.33 PM.png]]
*how many parameters? (assuming doing max) → None. Max is just an operator.*

In pooling, **we choose one value on the way**, so when back-propagating we only propagate to one-convolution (not the others when pooling). 


###### Max Pooling 
![[Screenshot 2024-12-09 at 8.37.42 PM.png]]

###### Average Pooling
![[Screenshot 2024-12-09 at 8.38.02 PM.png]]

###### Summary
Accepts a volume of size: 
$$W_{i} \times H_{i} \times D_{i}$$

Requires hyper-parameters:
- Spatial extent of filters$$K$$
- Stride of application$$F$$

Produces a volume of size: $W_{o}\times H_{o}\times D_{o}$,
$$W_{o}=\frac{W_{i}}{F},H_{o}=\frac{H_{i}}{F},D_{o}=D_{i}$$

Number of total learnable parameters: 0


#### Deep Learning
###### Terminologies
- **Network Structure**: number and types of layers, forms of activation functions, dimensionality of each layer and connections (defines computational graph).
	- Generally kept fixed, requires some knowledge of the problem and NN to sensibly set.
	- deeper = better.
- **Loss Function**: objective function being optimized (`softmax, cross entropy, etc.`).
	- Requires knowledge of the nature of the problem.
- **Parameters**: trainable parameters of the network, including weights/biases of linear / FC layers, parameters of activation functions, etc.
	- Optimized using SGD (stochastic gradient descent) or variants.
- **Hyper-parameters**: parameters, including for optimization, that are not optimized directly as part of training (e.g., `learning rate, batch size, drop-out rate`)
	- Can’t differentiate with respect to → typically to grid search.

==Specification of neural architecture will define computational graph.==

###### Training

1. **Initialize** parameters of all layers
2. For a fixed number of iterations or until convergence
	- **form mini-batch** of examples 
		- (randomly chosen from training data set)
	- **compute forward pass** to make predictions for every example and compute the loss 
		- (recursively calling forward for each intermediate layer along computational graph)
	- **compute backward pass** to compute the gradient of the loss with respect to each parameter for each example 
		- (involves traversing through computational graph in reverse order calling backward on intermediate nodes and composing intermediate gradient - chain rule)
	- **update parameters** of all layers, by taking a step in the negative average **gradient** direction 
		- (computed over all examples of mini batch)


###### Inference / Prediction
Compute **forward pass** with **optimized** parameters on test examples.


###### Monitoring Learning: Visualizing Training Loss
![[Pasted image 20241209210254.png]]


![[Screenshot 2024-12-09 at 9.01.50 PM.png]]
- Big gap: **overfitting**
	- Doing really well in training set, doing poor in validation.
	- Solution: Increase regularization.
- Small (or no) gap: **underfitting**
	- Solution: Increase model capacity.

==Ideally, we want a small gap.==

###### Regularization: Data Augmentation
![[Screenshot 2024-12-09 at 9.06.12 PM.png]]
Often times there is some sort of photographer bias, some might take photos in facing direction, some from right direction etc.

We can apply a transformation to the data, to get more data and reduces biases in data.
![[Screenshot 2024-12-09 at 9.12.56 PM.png]]
And this is done before sent to the model.

![[Screenshot 2024-12-09 at 9.13.32 PM.png]]
We wouldn’t do vertical flips since we want some natural photos.

![[Screenshot 2024-12-09 at 9.14.06 PM.png]]
We need the crops to be around the object of interest. Can be applied in testing as well, we can get a set of crops and do an inference on all crops and combine the results to get a better estimate.

![[Screenshot 2024-12-09 at 9.16.02 PM.png]]

==For difference types of data, we can have difference in these techniques. We make some transformations to data so that it doesn’t change the outcome the quantity we’re trying to predict.==

###### Activation Function: Sigmoid
![[Screenshot 2024-12-09 at 9.17.25 PM.png]]
What happens to the gradients too far to left or right → derivatives goes to zero → no learning actually happens. 

Learning happens most in the region near 0, gradient is largest.

- Famous in early neural networks.
- Maps input range to [0, 1]

###### Activation Function: ReLU
![[Screenshot 2024-12-09 at 9.18.52 PM.png]]
We have no way to ensure that the pre-activation values are in the ranges that are good for learning (since negative values just shoot down to 0).

So what can we do (for both ReLU and sigmoid)?

**Normalize each mini-batch** (using Batch Normalization layer before activation layer) by subtracting empirically computed mean and dividing by variance for every dimension → samples are approximately unit Gaussian (ensures data being between range of $\pm \sigma$).

$$\overline{x}^{(k)}= \frac{x^{(k)}-\mathbb{E}[x^{(k)}]}{\sqrt{ \text{Var}[x^{(k)}] }}$$
*Benefit*:
- improves learning (better gradients, higher learning rate, less reliance on initialization)

Since mean and variance are all continuous operations, differentiating with respect to these values is also possible.

*But at runtime this becomes hard, since we’re only passing one example we cannot get the average nor variance. → we can apply (keep track) average mean and average variance over all batches to apply in test time.*

###### Regularization: Drop Out
Randomly **set some neurons to zero** in the forward pass, with probability to `dropout rate (between 0 and 1)`.

![[Screenshot 2024-12-09 at 9.37.08 PM.png]]
```
1. Compute output of the linear/fc layer: o_i = W_i.T @ x_i + b_i
2. Compute a mask with probability proportional to dropout rate: m_i = rand(1,|o_i|) < dropout rate.
3. Apply the mask to zero out certain outputs.
```

==Why is this a good idea?==
- We’re training an **ensemble of models** that share parameters.
- Each binary mask is one model that is trained on (approximately) one data point.
- Basically, we ensuring that no neurons are super specialized. → Regularize overall learning among all neurons.

In inference,
- Integrate out all the models in the ensemble.
- **Monte Carlo Approximation**: many forward passes with different masks and average all predictions.

==Equivalent to forward pass with all connections on and scaling of the outputs by dropout rate.==

###### Regularization: Stochastic Depth
- This is effectively “dropout” but for layers. 
- Stochastically with some probability **turn off some layer** (for each batch).
- Effectively trains a collection of neural networks.

![[Screenshot 2024-12-09 at 9.48.04 PM.png]]

###### Model Ensemble
- **Training**: Train multiple independent models.
	- Same structure, training data but different initialization.
- **Test**: Average their results.

- **Alternative**: Multiple snapshots of the single model during training.
- **Improvement**: Instead of using the actual parameter vector, keep a moving average of the parameter vector and use that at test time (Polyak averaging)

### Computer Vision Problems
![[Screenshot 2024-12-09 at 9.52.14 PM.png]]

#### Categorization (Classification)
![[Screenshot 2024-12-09 at 9.52.53 PM.png]]
For each image, predict category it belongs to out of a fixed set (predict probability distribution).

![[Screenshot 2024-12-09 at 10.07.21 PM.png]]
Different structures, different hyper-parameter tuning leads to different results.

###### ResNet
Even deeper, **using residual connections**.
![[Screenshot 2024-12-09 at 10.08.20 PM.png]]
Where we have a set of blocks (which very small convolutions, maybe 3 x 3), what we output is the residual (refinement) to the input. 
$$X \to F(X)+ X$$

Why is this useful?
Let’s see what happens when we continue to stacking deeper layers on a plain CNN,
![[Screenshot 2024-12-09 at 10.10.15 PM.png]]
We can see that the 20-layer CNN has a much less test-error when compared to the deeper 56-layer. That’s not good, more expression less performance.
→ Maybe it’s over fitting?

But this was the same for training,
![[Screenshot 2024-12-09 at 10.11.33 PM.png]]

Then it’s not overfitting, the optimizer can’t figure out what parameters are good for deeper layers.

**Optimizing Deep Neural Networks → Vanishing Gradient Problem**
![[Screenshot 2024-12-09 at 10.12.20 PM.png]]
If we have a chain of neurons and want to compute the derivative with respect to one neuron, then we get an expression, for instance on $b_1$,
$$\frac{\partial C}{\partial b_{1}}=\sigma'(z_{1})w_{2}\sigma'(z_{2})w_{3}\sigma'(z_{3})w_{4}\sigma'(z_{3})\frac{\partial C}{\partial a_{4}}$$
$$\frac{\partial C}{\partial b_{3}}=\sigma'(z_{3})w_{4}\sigma'(z_{4})\frac{\partial C}{\partial a_{4}}$$
we have some common terms. But we can see that it is a product of many weights times the gradients of activation functions.

The highest gradient for a sigmoid is 1/4, when taking large products of gradients less than 1, it approaches 0. On the other hand, when gradients are bigger than 1, it approaches $\infty$. So, for stable learning we want gradient close to 1.

**Hypothesis**:
Deeper models are harder to optimize.

**Observation**: 
The deeper model should perform just as well.

**Solution**: 
Use network to fit residual mapping instead of directly trying to fit a desired underlying mapping.

We get skip connections, 
![[Screenshot 2024-12-09 at 10.18.19 PM.png]]
When computing gradient, instead of going through all layers. We can skip through blocks and still get a gradient. 

We can a lot of paths where some gradients go through many/few layers → but we get gradient flow. 
###### Comparing Complexity
![[Screenshot 2024-12-09 at 10.31.35 PM.png]]
Not necessarily the case that larger networks perform better. Not all about size.
#### Object Detection
![[Screenshot 2024-12-09 at 10.43.10 PM.png]]
Problem: Number of outputs is variable now!

![[Screenshot 2024-12-09 at 10.43.40 PM.png]]
We can apply CNN to many different crops in the image and CNN classifies each patch as an object or background.

Issue? → If we’re doing this in a sliding window fashion, we need to apply CNN to many many patches in each image.

###### Region Proposals
Find image regions that are likely to contain objects (any object).
- Looking at histograms distributions, region aspect ratio, closed contours etc.

Relatively **fast to run**,
![[Screenshot 2024-12-09 at 10.46.03 PM.png]]
Goal is to get “true” object regions to be in as few top K proposals.

###### R-CNN Architecture
![[Screenshot 2024-12-09 at 10.46.50 PM.png]]
To make the bound box appropriately fit the object, we can regress on the bound box to get a good coordinate to fit on. Also, we have a loss for classification.

Algorithm:
```
— Extract promising candidate regions using an object proposals algorithm
— Resize each proposal window to the size of the input layer of a trained
convolutional neural network
— Input each resized image patch to the convolutional neural network
```


The issue is that it is still quite computationally heavy, we’re recomputing a lot of things on the work boxes → Why can’t we not pull out the features after running a CNN once?

###### Fast R-CNN
We can forward pass the *whole image* through a CNN. We extract our features out of some layer of convolution (say layer 5, conv 5).

The region proposals can be mapped to the resolution of convolution features. And extract these regions.

We need a new layer to do so…
###### RoI Pooling Layer (RoI Align)
![[Screenshot 2024-12-09 at 10.53.37 PM.png]]
![[Screenshot 2024-12-09 at 10.54.18 PM.png]]
If we have a particular box, we can sample that box to some spatial locations(e.g. 7 x 7 = 49) that are defined with respect to the coordinates of the box and we can estimate where the sampling locations are.

They are not on pixel grid or feature grid → we interpolate what that feature would look like at that position by taking nearest four corners. (Since it is a weighted combination → we can back propagate - differentiable)

Now if we have an image, feature map (256 x 256 x 500), we can interpolate to get a 500 dimensional vector that is a feature that doesn’t live on the feature grid.

![[Screenshot 2024-12-11 at 1.24.28 AM.png]]
==Region proposals dominate performance.==
###### Faster R-CNN
![[Screenshot 2024-12-11 at 1.26.55 AM.png]]
The proposal bounding-box regression just checks if there is an object or not inside. Unlike having a region proposal that came externally we’re training them at the same time.

###### YOLO
Instead of having region proposals, we output the boxes all at the same time. For each one of the feature elements (vectors) we try to predict a box of an object that sits on top of that location (for each location, predict a bounding box a potential object that sits there and a label that would say if there is an object there or not).

Can predict multiple boxes,
![[Screenshot 2024-12-11 at 1.30.45 AM.png]]
![[Screenshot 2024-12-11 at 1.32.49 AM.png]]
#Boxes can change.

#### Segmentation
![[Screenshot 2024-12-11 at 1.37.37 AM.png]]
Our task is to label **every pixel** to which class it belongs to.
We can extract patches and pass to CNN and get a label for the center of that patch. 
→ This is very inefficient, has to be done for every pixel. We are applying a CNN to many overlapping patches.

We can instead design a network of convolutional layers to make predictions for all pixels at once. Ultimately a convolutional layer that outputs feature volume of C x H x W where it chooses the number of classes.

We get a probability of every single class at each pixel. (We need to do enough padding to retain size → so that output aligns with the size of the image.)

For training, we put a soft-max across the depth (classes) so that we create a probability distribution. In inference, we just do an arg-max.
![[Screenshot 2024-12-11 at 1.39.52 AM.png]]

Issues? → We do a lot of convolutions. If we want receptive fields to be large, we need a lot of convolutional layers.
###### Semantic Segmentation
![[Screenshot 2024-12-11 at 1.43.21 AM.png]]
We also incorporate down/up sampling, downsampling would allow us to get larger receptive fields (contain more context). Then we can upsample to get original resolution.

Downsampling is just pooling, but how do we undo the pooling (upsampling)?

###### In-network Up Sampling: Max unpooling
We can do easily with nearest neighbour by replicating,
![[Screenshot 2024-12-11 at 1.45.02 AM.png]]

Or, bed of nails, we can remember from downsampling which element contributed to arg-max and upsample to that same location (so we go the other way).

![[Screenshot 2024-12-11 at 1.46.41 AM.png]]

###### In-network Up Sampling: Transpose Convolution
We can get the convolution (dot product between filter and input), with a stride and some padding,

![[Screenshot 2024-12-11 at 1.48.33 AM.png]]
The stride gives a ratio in movement in input vs. output (in the case above we see that it’s a 2:1 ratio).

When upsampling, the input gives weight for the filter,
![[Screenshot 2024-12-11 at 1.55.56 AM.png]]
for the next input, we sum where the output overlaps,
![[Screenshot 2024-12-11 at 1.56.15 AM.png]]

The output contains copies of the filter weighted multiplied by the input, summing at overlaps in the output.

#### Instance Segmentation
###### Mask R-CNN
Now for each pixel, we also want to label them. Hence, giving an instance.
![[Screenshot 2024-12-11 at 1.59.50 AM.png]]
![[Screenshot 2024-12-11 at 2.00.05 AM.png]]
Basically, on top of a R-CNN we run a similar layer in parallel to label as well. Also includes a regressor to match the location of the bounding box.