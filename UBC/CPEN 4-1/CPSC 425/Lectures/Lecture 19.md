In reality, we wouldn’t have a limited size of inputs. Let’s see what the situation is when varying size of inputs.

![[Screenshot 2024-12-01 at 3.48.51 PM.png]]
Consider this fully connected layer with 200 x 200 greyscale images (not huge) along with 40K hidden units. → We have ~ 2 billion parameters *for one layer*.

That’s why we want **Convolution Neural Networks**, we need some assumptions to implement one,
- Spatial correlations are generally local.
	- Local information is sufficient.
- Waste of resources and we generally don’t have enough data to train networks this large.

Instead of having one of the neurons looking at all pixels, we have each neuron looking at a specific region, we can have a locally connected layer,
![[Screenshot 2024-12-01 at 3.51.37 PM.png]]
We can see that the number of parameters reduce greatly.

But we still have the question “why specialize a neuron, if we have a neuron looking for a specific pattern why would we limit it to looking only at a specific region?”
→ Stationarity: statistics is similar at different locations.

We look for a specific pattern over every patch of an image.

==We share the same parameters across locations (assuming input is stationary)==
![[Screenshot 2024-12-01 at 3.55.01 PM.png]]

In a fully connected layer,
![[Screenshot 2024-12-01 at 3.55.28 PM.png]]
We would have an associated weight for each neuron and each location along with a specific bias.

In a locally connected layer,
![[Screenshot 2024-12-01 at 3.56.06 PM.png]]
We would have weights and bias for only a specific region per neuron.

For a convolutional layer,
![[Screenshot 2024-12-01 at 3.56.48 PM.png]]
It will have locally responsible neurons, but the weights / bias would be shared across all positions.

A simple representation if having a single neuron being shifted around each region,
![[Screenshot 2024-12-01 at 3.58.53 PM.png]]

The benefit of the single neuron approach is that we don’t need to know the size of the input → we just need to shift the neuron more → which defines the size of the output.

The weights is similar to a filter → which we’ve done before.
![[Screenshot 2024-12-01 at 4.00.47 PM.png]]
we can learn these filters.

But we can learn more than one filter, we can learn a whole series of filters,
![[Screenshot 2024-12-01 at 4.01.44 PM.png]]
where each filter has a different pattern it is looking for.

A bit more formally,
![[Screenshot 2024-12-01 at 4.02.21 PM.png]]
Filters always extend the full depth of the input volume. How many outputs would we have? → for a given placement we would have one output, the number of parameters is going to be 75 and a single bias.
![[Screenshot 2024-12-01 at 4.03.53 PM.png]]
And the output depth would depend on the number of filters. If we have 5 filters, depth would be 5 and so on..

###### 1 x 1 Convolutions
![[Screenshot 2024-12-01 at 4.05.49 PM.png]]
We can do compression in terms of the number of channels, we can learn a reduction. And this is totally fine.

***Convolutional neural networks*** can be seen as a learning a hierarchy of filters.
- As we go deeper in the network, filters learn and respond to increasingly specialized structures.
- The first layers may contain simple orientation filters, middle layers may respond to common substructures, and final layers may respond to entire objects.


###### Summary
Accepts a volume of size:
$$W_{i}\times H_{i}\times D_{i}$$
Requires hyper-parameters:
- Number of filters: $K$ (typically $K \in \left\{ 32,64,128,\cdots \right\}$).
- Spatial extent of filters: $F$ (typically $F \in \left\{ 1,3,5,\cdots \right\}$).
- Stride of application: $S$ (typically $S \in \left\{ 1,2 \right\}$).
- Zero padding: $P$ (typically $P\in \left\{ 0,1,2 \right\}$).

Produces a volume of size:
$$W_{o}\times H_{o}\times D_{o}$$
$$W_{o}=\frac{W_{i}-F+2P}{S}+ 1 \hspace{.2in}H_{o}=\frac{H_{i}-F+2P}{S}+1$$

Number of total learnable parameters:
$$(F\times F\times D_{i}) \times K+K$$

==Visualizing only works for the first layer.==

###### Intermediate features through back propagation
If we have the gradient computed for every pixel, why don’t we rather take an image and optimize the image so that the neuron output is a high as possible.

Maximize an output of the neuron, fix the parameters and tweak the image.

We just do
1. back propagation: find the part of an image that a neuron responds to.
2. gradient ascent: generate a synthetic image that maximally activates a neuron.

$$\mathbf{I}^*=\text{arg}\text{max}_{\mathbf{I}}f(\mathbf{I})+R(\mathbf{I})$$
where $f(\mathbf{I})$ is the score for class before soft-maxing (neuron value) and $R(\mathbf{I})$ is the image regularizer.


1. Initialize image with all zeros (also can start from existing image).
2. Forward image to compute the current scores.
3. BackProp to get gradient of the neuron with respect to image pixels.
4. Make a small update to an image.
5. Go back to step 2 and repeat.

