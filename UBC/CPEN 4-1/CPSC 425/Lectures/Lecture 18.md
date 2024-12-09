#### One-hot Regression
Why would we use one-hot? → It characterizes the probability (1 vs. 0) for every simple sample.

![[Screenshot 2024-12-01 at 12.44.57 AM.png]]
If we want to solve for $\mathbf{W}$,
$$\mathcal{L}=\lvert \mathbf{XW}-\mathbf{T} \rvert ^2$$
which is the least squares approximation.

But why is this sub-optimal?
→ Our predictions in general wouldn’t sum up to one. They are not going to be proper distributions.

And we learn $\mathbf{W}$ on the way on learning.

A linear classifier is a simple case of a fully connected neural network.

### Neural Networks
#### Neuron
A neuron,
- Is a basic unit of computation in a neural network.
- A neuron accepts some number of input signals, computes the weighted sum and applies an **activation function** (or **non-linearity**) to the sum.
- Common activation functions include RELU or sigmoid.

![[Screenshot 2024-12-01 at 12.49.59 AM.png]]
$$y=f\left( \sum_{i=1}^N x_{i}w_{i}  + b\right)$$

What do we learn?
- Weights.
- Bias.
- We might have to learn activation functions with parameters.

We can draw it another way,
![[Screenshot 2024-12-01 at 12.56.28 AM.png]]
We can simply add a new node with value 1 associated with the wait being the bias (add 1 dimension to input).
$$a=\sum_{i}w_{i}x_{i},\hspace{.2in}y=f(a)$$


###### A linear classifier
If we re-call what a linear classifier did,
$$f(\mathbf{x}_{i},\mathbf{W},\mathbf{b})=\mathbf{W}\mathbf{x}_{i}+\mathbf{b}$$
so basically a neuron is a linear classifier.

#### Activation Functions
##### Sigmoid
$$f(x)= \frac{1}{ 1+e^{-x}}$$
- Common in many neural networks.
- Maps the input to range [0, 1]
	- Useful when trying model probability distributions. (since we make it between 0 and 1)
##### ReLU
$$f(x)=\text{max}(x,0)$$
- We zero out anything that is negative.
- Otherwise, keep it.
- It is useful since it is non-linear + it is simple and gives nice gradients.

#### Neural Network
Connect a bunch of neurons together - a collection of connected neurons.
All neurons share the same connectivity → yet have different weights and bias associated.
![[Screenshot 2024-12-01 at 12.58.58 AM.png]]

![[Screenshot 2024-12-01 at 12.59.14 AM.png]]
This is called a ‘fully connected layer’ or a multi-layer perceptron (MLP).

We have,
- input layer: Actual inputs that go into layer.
- hidden layer: intermediate outputs.
- output layer: final layer, has class probabilities etc.

A neural network,
- Comprises neurons connected in an acyclic graph.
- The outputs of neurons can become inputs to other neurons.
- Neural networks typically contain multiple layers of neurons.

*Whether they are the same layer depends on where the inputs come from.*

==Each neuron will have its own vector of weights and a bias, it’s easier to think of all neurons in a layer as a single entity with a matrix of weights (size = number of inputs x number of neurons) and a vector of biases (size = number of neurons).==

![[Screenshot 2024-12-01 at 1.08.49 AM.png]]
So in this case, it makes a prediction of $\mathbf{y}\in \mathbb{R}^2$ with an input $\mathbf{x}\in \mathbb{R}^3$ thus we can simplify
$$\hat{\mathbf{y}}=f(\mathbf{x},\mathbf{W_{1}},\mathbf{W}_{2},\mathbf{b}_{1},\mathbf{b}_{2})=\sigma(\mathbf{W}_{2}^{(2\times 4)}\sigma(\mathbf{W}_{1}^{(4 \times 3)}\mathbf{x}+\mathbf{b}_{1}^{(4)})+\mathbf{b}_{2}^{(4)})$$

###### Why can’t we have linear activation functions?
In the example above, say that $\sigma$ is the identity. Then,
$$\sigma(\mathbf{W}_{2}^{(2\times 4)}\sigma(\mathbf{W}_{1}^{(4 \times 3)}\mathbf{x}+\mathbf{b}_{1}^{(4)})+\mathbf{b}_{2}^{(4)})=\mathbf{W}_{2}^{(2\times 4)}(\mathbf{W}_{1}^{(4 \times 
3)}\mathbf{x}+\mathbf{b}_{1}^{(4)})+\mathbf{b}_{2}^{(4)}$$
$$=\mathbf{W}_{2}^{(2\times 4)}\mathbf{W}_{1}^{(4 \times 3)}\mathbf{x}+\mathbf{W}_{2}^{(2\times 4)}\mathbf{b}_{1}^{(4)}+\mathbf{b}_{2}^{(4)}$$
$$=\mathbf{W}^*\mathbf{x}+\mathbf{b}^*$$
the only class of functions that we can represent becomes linear functions.
→ Lot of functions in the world wouldn’t be linear. → *We don’t want to be restricted to linear functions despite of depth of the neural network.*

#### Light Theory: Neural Networks as Universal Approximator
Neural Networks can arbitrarily approximate any ***continuous*** function for every value  of possible inputs.

We can guarantee that by using enough hidden neurons we can always find a neural network whose output $g(x)$ satisfies $\lvert g(x)-f(x) \rvert < \epsilon$ for an arbitrarily small $\epsilon$.

Let’s consider a really small neural network: one hidden layer with two hidden neurons + single output layer with one neuron (with sigmoid activations)

![[Screenshot 2024-12-01 at 1.21.23 AM.png]]
![[Screenshot 2024-12-01 at 1.21.33 AM.png]]
As $w$ increases the step gets steeper and as $b$ increases the function shifts to the right.
With a really high $w$ we can create a step function, and the value of $b$ determines where the step happens.

Since we have two combinations, we can have two step functions aggregated.
Let $s$ the step, $s=- \frac{b}{w}$
![[Screenshot 2024-12-01 at 1.22.51 AM.png]]
with negative weights,
![[Screenshot 2024-12-01 at 1.23.27 AM.png]]

The more neurons → the more steps we can create. And with **Riemann sum approximation** we can approximate any function.
![[Screenshot 2024-12-01 at 1.24.58 AM.png]]

They are however some conditions that need to be true for the proof to hold,
- Activation functions need to be well-defined. $$\lim_{ x \to \infty } a(x)=A$$$$\lim_{ x \to -\infty }a(x)=B $$$$A \neq B$$

And since for linear functions, which are not bounded, this condition would not hold. → Can’t use them!!!

##### In the case of ReLU
- With ReLU activation, we effectively get a linear spline approximation to any function. 
- Optimization of neural network parameters = finding slops and transitions of linear pieces.
- The quality of approximation on the number of linear segments.

We model functions to be piece-wise linear (the positive component) → which approximates the non-linear function.

![[Screenshot 2024-12-01 at 1.30.55 AM.png]]


##### Some Theorems
###### Universal Approximation Theorem
Single hidden layer can approximate any continuous function with compact support to arbitrary accuracy, when the width goes to infinity.

###### Revised
A network of infinite depth with a hidden layer of size $d+1$ neurons where $d$ is the dimension of the input space, can approximate any continuous function.

###### Further Revised
ResNet with a single hidden unit and infinite depth can approximate any continuous function.

==We can trade off depth for width of neural network.==

##### Practice
![[Screenshot 2024-12-01 at 1.41.16 AM.png]]
How many neurons do we have? → 6 (don’t count input)
How many layers? → 2 (same)
How many weights do we have? → 3x4 + 4x2 = 20
How many (learnable parameters) do we have? → # weights + # bias = 20 + 6 = 26
–> One bias per neuron.

Modern CNNs contain 10-20 layers and on the order of 100 million parameters.
Training a neural network requires estimating a large number of parameters.

#### Training a Neural Network
Consider the following simple neural network,
![[Screenshot 2024-12-01 at 1.44.31 AM.png]]

With a given output, we want to change it to a probability distribution,
![[Screenshot 2024-12-01 at 1.44.53 AM.png]]

- **Input and Output** layers (size and form) are dictated by the problem, intermediate layers have few constraints and can be *anything*.
	- Intermediate is the hyper parameter!

![[Screenshot 2024-12-01 at 1.47.33 AM.png]]
Inference (output is made to proper distribution):
$$o(f(\mathbf{x},\cdots))$$

Learning:
$$\mathcal{L}(\mathbf{y},o(f(\mathbf{x},\cdots)))$$


What we eventually want to do is learn our weights and biases, we want to learn it in such a way that the inference matches our one-hot probability distribution.

We want to measure the similarity between the distributions and make sure they are as similar as possible.

num neurons = complexity
##### Back Propagation
When training a neural network, the final output will be some loss (error) function
e.g. cross-entropy
$$\mathcal{L}=-\sum_{i}y_{i}\log(\hat{y_{i}}) \hspace{.5in}\hat{y_{i}}= \frac{e^{f_{y_{i}}}}{\sum_{j}e^{f_{y_{j}}}} \hspace{.1in} \leftarrow \text{soft max}$$
which defines loss for the $i$-th training example with true class index $y_{i}$; and $f_{j}$ is the $j$-th element of the vector of class scores coming from the neural network. ($\hat{y_{i}}$ is our prediction)

Consider a neural network which takes input vector $\mathbf{x}_{i}$ and predicts scores for 3 classes, with true class being class 3:
![[Screenshot 2024-12-01 at 1.53.08 AM.png]]
==soft max ensures the transformation to a proper distribution.==

Since our true labels are 0 and 1, the ground truth label $y_i$ is 0 or 1. So the sum collapses to
$$\mathcal{L}=-\log(0.353)$$

We want the probability go to 1, so the loss would go to 0 for a good approximation.


Now we need to minimize the loss → via the gradient of loss with respect to the network parameters (weights, biases)
#### Gradient Descent
![[Screenshot 2024-12-01 at 1.57.28 AM.png]]

For $k=0$ to max number of iterations,
1. Start from random value of $\mathbf{W}_{0},\mathbf{b}_{0}$
2. Compute the gradient of the loss with respect to previous parameters: $$\nabla \mathcal{L}(\mathbf{W},\mathbf{b})|_{\mathbf{W}=\mathbf{W}_{k},\mathbf{b}=\mathbf{b}_{k}}$$
3. Re-estimate the parameters $$\mathbf{W}_{k+1}=\mathbf{W}_{k}-\lambda \frac{\partial \mathcal{L}(\mathbf{W},\mathbf{b})}{\mathbf{\partial W}}|_{\mathbf{W}=\mathbf{W}_{k},\mathbf{b}=\mathbf{b}_{k}}$$$$\mathbf{b}_{k+1}=\mathbf{b}_{k}-\lambda \frac{\partial \mathcal{L}(\mathbf{W},\mathbf{b})}{\partial \mathbf{b}}|_{\mathbf{W}=\mathbf{W}_{k},\mathbf{b}=\mathbf{b}_{k}}$$
$\lambda$ is the learning-rate,
- Too big: might not converge.
- Too small: takes a long time.
	- Need adequate steps. (Also a hyper parameter)

==We can’t guarantee to converge to global minima, but we can converge to local minima.==

Would look like something like this (For L2 Norm),
$$\mathcal{L}=\sum_{i=1}^{\lvert \mathcal{D}_{\text{train}} \rvert }\lvert \lvert \mathbf{y}_{i}-\hat{\mathbf{y}}_{i} \rvert  \rvert= \sum_{i=1}^{\lvert \mathcal{D}_{\text{train}} \rvert }\lvert \lvert \mathbf{y}_{i}-f(\mathbf{x}_{i},\mathbf{W}_{1},\mathbf{W}_{2},\mathbf{b}_{1},\mathbf{b}_{2}) \rvert  \rvert $$
What’s the issue?
→ It takes way too long, for each step we have to compute it over all inputs that were fed to the neural network!!


*Stochastic Gradient Descent*
Instead of computing gradient to the whole set, we can compute the gradient (approximate it) with mini-batches of a much smaller size. (With small steps, we’re still guaranteed a local optima)

Either way we still need to compute gradients of fairly complex functions
###### Numerical Differentiation
We can approximate via numerical methods,
- forward differencing.
- central differencing.

==Not very accurate..==
#### Auto Differentiation
###### Symbolic Differentiation
We can represent the input function as a **computational graph** (a symbolic tree) with incorporating various rules, namely,
- Sum rule
- Product rule
- Chain rule

![[Screenshot 2024-12-01 at 2.08.22 AM.png]]

For complex functions, expressions can grow exponentially and it’s difficult to deal with piece-wise functions (Many symbolic cases are created).

**Intuition**:
Interleave symbolic differentiation and simplification.

**Key Idea**:
Apply symbolic differentiation at the elementary operation level, evaluate and keep intermediate results.

For instance, consider the function,
$$y=f(x_{1},x_{2})=\ln(x_{1})+x_{1}x_{2}-\sin(x_{2})$$

![[Screenshot 2024-12-01 at 2.10.39 AM.png]]
- Each **node** is an input, intermediate, or output variable.
- **Edges** represent the mathematical operations.
- **Computational graph** with variable ordering from topological sort.

We then have the following equations,
$$v_{0}=x_{1},v_{1}=x_{2},v_{2}=\ln(v_{0}),v_{3}=v_{0} \cdot v_{1}$$
$$v_{4}=\sin(v_{1}),v_{5}=v_{2}+v_{3},v_{6}=v_{5}-v_{4},y=v_{6}$$


##### Forward Mode
Let’s use the example $f(2,5)$
$$v_{0}=x_{1}=2,v_{1}=x_{2}=5$$
$$v_{2}=\ln(v_{0})=\ln(2),v_{3}=v_{0}\cdot v_{1}=10$$
$$v_{4}=\sin(v_{1})=\sin(5),v_{5}=v_{2}+v_{3}=10+\ln(2)$$
$$v_{6}=v_{5}-v_{4}=10+\ln(2)-\sin(5)$$
$$y=v_{6}=10+\ln(2)-\sin(5)$$

Which gives us the final value!

Now we want to compute the derivative with respect to all variables,
$$\frac{\partial v_{0}}{\partial x_{1}}=1,\frac{\partial v_{1}}{\partial x_{1}}=0,\frac{\partial v_{2}}{\partial x_{1}}=\frac{1}{v_{0}}\frac{\partial v_{0}}{\partial x_{1}}=0.5$$
$$\frac{\partial v_{3}}{\partial x_{1}}=\frac{\partial v_{0}}{\partial x_{1}}\cdot v_{1}+\frac{\partial v_{1}}{\partial x_{1}}v_{0}=5$$
and so on..

![[Screenshot 2024-12-01 at 2.20.58 AM.png]]

We have many weights, we have to go through this process many times, in the case above $x_{2}$ is not done yet…

Given,
$$\mathbf{y}=f(\mathbf{x}):\mathbb{R}^m\to \mathbb{R}^n$$
We need $m$ forward passes to get the full Jacobian (all gradients of output w.r.t. each input), where $m$ is the number of inputs.

==Knowing that we have a large number of inputs where as we have **one output**. We should rather do it in **reverse mode** that computes all gradients in **one pass**!!!!!!==

##### Reverse Mode
The number of outputs is exceptionally small for a neural network → it’s just 1. why? ultimately we’re optimizing a Loss, which is one value. ==similarity is just one number.==

![[Screenshot 2024-12-01 at 2.54.39 PM.png]]
Traverse the original graph in the reverse topological order and for each node in the original graph, introduce an **adjoint node**, which computes derivative of the output with respect to the local node.

$$\overline{v}_{i}=\frac{\partial y_{j}}{\partial v_{i}}=\sum_{k \in \text{pa}(i)}\frac{\partial v_{k}}{\partial v_{i}}\frac{\partial y_{j}}{\partial v_{k}}= \sum_{k \in \text{pa}(i)}\frac{\partial v_{k}}{\partial v_{i}}\overline{v}_{k}$$

Let’s try it out with the same example,
$$f(x_{1},x_{2}) =\ln(x_{1})+x_{1}x_{2} - \sin(x_{2})$$

$$\overline{v}_{6}=\frac{\partial y}{\partial v_{6}} = 1$$
$$\overline{v}_{5}=\overline{v}_{6} \frac{\partial v_{6}}{\partial v_{5}}=\overline{v}_{6}\cdot 1= \overline{v}_{6} = 1$$
$$\overline{v}_{4}=\overline{v}_{6}\frac{\partial v_{6}}{\partial v_{4}}=-\overline{v}_{6}=-1$$
$$\overline{v}_{3}=\overline{v}_{5}\frac{\partial v_{5}}{\partial v_{3}}=\overline{v}_{5}=1$$
$$\overline{v}_{2}=\overline{v}_{5}\frac{\partial v_{5}}{\partial v_{2}}=1\cdot 1= 1$$
$$\overline{v}_{1}=\overline{v}_{3}\frac{\partial v_{3}}{\partial v_{1}}+\overline{v}_{4}\frac{\partial v_{4}}{\partial v_{1}}=\overline{v}_{3}v_{0} + \overline{v}_{4}\cos(v_{1})$$
$$\overline{v}_{0}=\overline{v}_{2}\frac{\partial v_{2}}{\partial v_{0}}+\overline{v}_{3}\frac{\partial v_{3}}{\partial v_{0}}=\frac{\overline{v}_{2}}{v_{0}}+\overline{v}_{3}v_{1}$$

*We already have each $v_{i}$ computed.*

We’ve done a fairly simple example, but it would work the same if we had a more shallow graph with bigger and complex functions.
![[Screenshot 2024-12-01 at 3.13.17 PM.png]]

In NNs, it might be more convenient to think of layers,
![[Screenshot 2024-12-01 at 3.13.55 PM.png]]
We can have the one fully connected layer abstracted with an activation function, we can do the same gradient operation for this entire layer in matrix form.

![[Screenshot 2024-12-01 at 3.14.32 PM.png]]
The adjoint for $\mathbf{x}$ would be,
$$\overline{\mathbf{x}}=\overline{\mathbf{y}}\frac{\partial \mathbf{y}}{\partial \mathbf{x}}$$

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 19|Lecture 19]]
