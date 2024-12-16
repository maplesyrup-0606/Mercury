#### Question 1
Which of the following statements about max-pooling are true? Which are false?

- It allows a neuron in a network to have information about features in a larger part of the image, compared to a neuron at the same depth in a network without max-pooling.
**True**, unlike a general neuron, a max-pooling layer would take more information of a specific region.

- It increases the number of parameters when compared to a similar network without max-pooling.
**False**, no parameters are needed for max-pooling.

- It increases sensitivity of the network towards position of features within an image.
**False**, it is spatially invariant.

#### Question 2
Consider a simple convolutional neural network with one convolutional layer. Which of the statements are true? which are false?

- It is scale invariant.
**False**

- It is scale equivariant.
**False**

- It is rotation invariant.
**False**

- It is rotation equivariant.
**False**, pattern changing would lead to different filters.

- It is translation invariant.
**False**, as mentioned above filters would change with translation.

- It is translation equivariant.
**True**, the filters would shift accordingly.

#### Question 3
What are the two passes of Back-propagation and their roles?

1. Forward pass: getting a prediction by evaluating function described by neural network.
2. Backward pass: computing the gradients per input of the loss with respect to parameters of the network.

#### Question 4
What is $\lambda$, what happens if it is small or big?

It is learning rate. If it is small it would take a long time to converge. On the other hand, if it is large we might not converge at all.

#### Question 5 
You want to map every possible image of size 64 x 64 to a binary category. Each image has 3 channels and each pixel in each channel can take an integer value between 0 and 255. How many bits do you need to represent this mapping?

We have $256$ values and $3 \times 64 \times 64$ permutations. $256^{3 \times 64 \times 64}$.

#### Question 6
The mapping from previous question clearly can not be stored in memory. Instead, it is typically encoded using a neural network classifier. Recall the simple single hidden layer classifier that was illustrated in class, containing an input layer, a hidden layer and an output layer. Assuming we use a single hidden layer of size 100 for this task.  

-  What is the size of the weight matrices W1 and W2?  
$$W_{1}= (64\times \ 64 \times 3)\times 100$$
$$W_{2} = 1 \times 100$$
-  What about the bias vectors b1 and b2?  
$$b_{1} = 100 $$
$$b_{2} = 1$$
- How many learnable parameters are there?  
$$(64 \times 64 \times 3) \times 100 + 100 + 100 + 1$$
-  How many bits do you need to store your two layer neural network (you may ignore the biases b1 and b2)?
idk

#### Question 7 - a
Consider a problem of detecting whether there is a car is in any given grayscale satellite image of size 1024 × 1024 pixels. Considering that the largest instance of the car that can appear in such an image is 11 × 11 pixels, design the simplest two-layer neural network consisting of one Convolutional and one Max Pooling layer. What would be a reasonable design? How many learnable parameters would such a network have?

We can use a convolutional layer with a size of 11 x 11, following right after a pooling layer. We will do no padding and the max pooling layer would be size (1024 - 10) x (1024 - 10)

Then we would have $$(11\times 11) + 1 = 122$$ parameters for the convolutional layer and 0 parameters for the max pooling layer.

After convolving we use the max pooling to decide if the car exists.

#### Question 7 - b
Now consider that you have access to a library that ONLY supports 3 × 3 × 1 convolutional filters. How could you implement the architecture that could conceptually have the same behaviour? How many parameters would such an architecture have?

We can imitate a 11 x 11 x 1 filter if we convolve five 3 x 3 x 1 convolutional filters. So we would have a design that will have five layers of 3 x 3 convolutional filters.

We would then have the size,
$$(1024 \times 1024) \to (1022 \times 1022) \to (1020 \times 1020) $$
$$\to (1018 \times 1018) \to (1016 \times 1016) \to (1014 \times 1014)$$
so we can keep the same max pooling layer.

The number of parameters will be 
$$5 \times (3 \times 3 + 1) = 50$$

#### Question 8
Consider an intermediate convolutional neural network layer within a CNN which receives as an input the output from the previous layer of size 512 × 512 × 128 Assuming that the convolutional layer we are considering applies 48 7 × 7 filters at stride 2 with no padding. What is the number of parameters that need to be learned in this layer? What is the size of the resulting activation map?

The number of parameters will be 
$$48 \times (7 \times 7 \times 128 + 1)$$

The size will be 
$$\left( \frac{512 - 6}{2} \times \frac{512 -6}{2} \right) \times 48$$
since the depth would be the number of filters applied.

#### Question 9
Lets say you want to re-implement the template matching assignment on face detection using a neural network. What architectural design choices would you make and how would you setup the parameters? What would be the key difference between your original filtering implementation and the neural network implementation?  

We can implement a normalized correlation with one single neural network. With a single filter ==with the size of a template.== The activation function can be $\sigma(x) = \frac{x}{\lvert x \rvert}$ so that it normalizes. The initial setup of weights and bias can be set to 0.
#### Question 10
Consider a convolution layer. The input consists of 6 feature maps of size 20 × 20. The output consists of 8 feature maps, and the filters are of size 5 × 5. The convolution is done with a stride of 2 and with zero padding, so the output feature maps are of size 10 × 10. 

input dimension: 6 x 20 x 20
filter dimensions: 6 x 5 x 5 and 8 of them
output dimensions: 8 x 10 x 10

- Determine the number of weights in this convolution layer.
$$8 \times (5 \times 5  \times 6)$$

- Now suppose we made this a fully connected layer, but where the number of input and output units are kept the same as in the network described above. Determine the number of weights in this layer.  

$$(6 \times 20 \times 20) \times (8 \times 10 \times 10)$$