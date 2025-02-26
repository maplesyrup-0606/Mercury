#### MLP (Multi-Layer Perceptron)
##### Linear Layer
Consider the following linear layer of a single output unit:
![[Screenshot 2025-02-10 at 4.56.41 PM.png]]
Which can be formulated as:
$$y=\sum_{n=1}^N w_{n}x_{n}$$
with,
$$\mathbf{w}=\begin{bmatrix}
w_{1} \\
w_{2} \\
\vdots \\
w_{N}
\end{bmatrix}\quad \mathbf{x}=\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{N}
\end{bmatrix}$$

if we had multiple output units,
![[Screenshot 2025-02-10 at 4.57.39 PM.png]]
each $y_m$, would be,
$$y_{m}=\sum_{n=1}^N w_{mn}x_{n}$$
hence for $\mathbf{y}=\begin{bmatrix}y_{1}\\y_{2}\\\vdots\\y_{M}\end{bmatrix}$,
$$W=\begin{bmatrix}
w_{11} & w_{12} & \cdots & w_{1N} \\
w_{21} & w_{22} & \cdots & w_{2N} \\
\vdots  & \vdots & \ddots & \vdots \\
w_{M{1}} & w_{M 2} & \cdots & w_{MN}
\end{bmatrix}$$
$$\to \mathbf{y}=W\mathbf{x}$$
but let’s not forget bias,
$$\mathbf{b}=\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{M}
\end{bmatrix}$$

Hence,
$$\mathbf{y}=W\mathbf{x}+\mathbf{b},\quad \mathbf{y}\in \mathbb{R}^{M\times 1},W\in \mathbb{R}^{M \times N},\mathbf{x}\in \mathbb{R}^{N \times 1}$$


To make things simple, we can write it instead in compact form,
$$\tilde{\mathbf{x}}=\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{N} \\
1
\end{bmatrix},\tilde{W}=\begin{bmatrix}
w_{11} & w_{12} & \cdots & w_{1N} & b_{1} \\
w_{21} & w_{22} & \cdots & w_{2N} & b_{2} \\
\vdots  & \vdots & \ddots & \vdots & \vdots \\
w_{M{1}} & w_{M 2} & \cdots & w_{MN} & b_{M}
\end{bmatrix}$$
$$\to \mathbf{y}=\tilde{W}\tilde{\mathbf{x}}$$

##### Nonlinear Activation
To make neural networks become non-linear models, we often apply *element-wise* non-linear activation functions.
$$\begin{aligned}
\bar{y}_{i}&=f(y_{i})\\ \bar{\mathbf{y}}&=f(\mathbf{y})
\end{aligned}$$

Types of non-linear activation functions,
- Sigmoid $$f(x)= \frac{1}{1+e^{-x}}$$
- Tanh - preferable than sigmoid due to stronger gradient. $$f(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}$$
- Softplus - useful to approximate ReLU.$$f(x)= \ln(1+e^x)$$
- ReLU (Rectified Linear Unit) $$f(x) = \text{max}(x,0)$$
- PReLU (Parametric) - can ensure neurons are active. $$f(x) = \begin{cases}
\alpha x\quad \text{if }x<0  \\
x \quad \text{otherwise}
\end{cases}$$
- ELU (Exponential) $$f(x)=\begin{cases}
\alpha(e^x-1)\quad \text{if }x<0 \\ x \quad \text{otherwise}
\end{cases}$$
###### Non-Element Wise
There is also **non-element-wise** non-linear activation functions.
- Softmax $$f(\mathbf{x})=\left[ \frac{\exp(\mathbf{x}_{1})}{\sum_{k=1}^K \exp(\mathbf{x}_{k})},\cdots,\frac{\exp(\mathbf{x}_{K})}{\sum_{k=1}^K \exp(\mathbf{x}_{k})} \right]$$
- Max-out $$f(\mathbf{x})=\text{max }_{i}\;\mathbf{x}_{i}$$
- Cummax $$f(\mathbf{x})=\left[ \frac{\exp(\mathbf{x}_{1})}{\sum_{k=1}^K \exp(\mathbf{x}_{k})},\cdots,\frac{\sum_{i=1}^j\exp(\mathbf{x}_{i})}{\sum_{k=1}^K \exp(\mathbf{x}_{k})},\cdots,1 \right]$$ This can be seen as a cumulative distribution function.

#### Batch Normalization
Let’s first define a term, **Internal Covariate Shift**
→ *The change in the distribution of network activations due to the change in network parameters during training.*

We want to reduce Internal Covariate Shift → Which can improve training (e.g. converge faster, better generalization).

That’s why we want batch normalization!

1. If the internal activations are properly normalized, the neural network is more stable.
	1. If layers can easily blow up or vanish → this could help.
2. Normalizing activations tends to better leverage non-linearity.
	1. Normalizing pre-activations helps avoid saturation region of non-linear activation function.

Suppose we have a batch of activations $X \in \mathbb{R}^{B \times D}$,
![[Screenshot 2025-02-10 at 5.32.57 PM.png]]

Then,
$$\mathbf{m}[j]= \frac{1}{B}\sum_{i=1}^B X[i,j]$$
we are computing the mean of each column,
$$\mathbf{m}= \frac{1}{B}\sum_{i=1}^B X[i,:]$$

For variance,
$$\mathbf{v}[j]= \frac{1}{B}\sum_{i=1}^B (X[i,j]-\mathbf{m}[j])^2$$
Thus, the normalized activations will be:
$$\hat{X}[i,j]=\gamma[j] \frac{ X[i,j]-\mathbf{m}[j]}{\sqrt{  \mathbf{v}[j]+\epsilon}}+ \beta[j]$$
where $\gamma,\beta$ are learnable parameters. If $\gamma=1,\beta=0$, then $\hat{X}[i,j] \sim \mathcal{N}(0,1)$.
But in general, $\hat{X}[i,j] \sim \mathcal{N}(\beta,\gamma^2)$.

- We want to have $\epsilon$ to avoid dividing by zero during training.

In practice, to account for dynamically changing weights and stochastic data, we use running mean and variance:
$$\begin{aligned}
\mathbf{m}^t[j]&=(1-\alpha)\mathbf{m}^{t-1}[j]+\alpha \mathbf{m}[j] \\ 
\mathbf{v}^t[j]&=(1-\alpha)\mathbf{v}^{t-1}[j]+\alpha \mathbf{v}[j]
\end{aligned}$$

#### Dropout
Suppose we have a batch of activation $X \in \mathbb{R}^{B \times D}$, we can make them stochastic by randomly turning some units off,
![[Screenshot 2025-02-10 at 6.18.40 PM.png]]
Mathematically speaking, we create a matrix mask $M \in \mathbb{R}^{B \times D}$,
$$\begin{aligned}
M[i,j]\sim &\text{ Bernoulli}(1-p) \\ 
\mathbb{P}(M[i,j]=1)&=1-p \\ 
\mathbb{P}(M[i,j]=0)&=p
\end{aligned}$$
then we can perform an element-wise product,
$$\begin{aligned}
\hat{X}&=M \odot X \\ 
\hat{X}[i,j]&=M[i,j]X[i,j]
\end{aligned}$$
![[Screenshot 2025-02-10 at 6.24.36 PM.png]]

- It turns off a random subset of units, thus blocking a random subset of paths.
- Every sample gets its own sub-network, thus being less likely to overfit.

How do we perform testing? → We compute the expected output for each unit!
$$\begin{aligned}
\mathbb{E}\left[\hat{X}[i,j]\right]&= \mathbb{E}\left[M[i,j]X[i,j]\right] \\ &= \mathbb{E}[M[i,j]]X[i,j] \\ 
&= (1-p)X[i,j]
\end{aligned}$$

#### Building a Deep MLP
We basically construct a deep MLP by building blocks and one block is,
$$\text{Linear}\to \text{BN}\to \text{Non-linear Activation}\to \text{Dropout (optional)}$$![[Screenshot 2025-02-10 at 6.39.14 PM.png]]

And with these blocks, the deep MLP is built.
![[Screenshot 2025-02-10 at 6.39.31 PM.png]]

#### Next Lecture [[UBC/CPEN 4-2/CPEN 455/Lectures/Lecture 3|Lecture 3]]
