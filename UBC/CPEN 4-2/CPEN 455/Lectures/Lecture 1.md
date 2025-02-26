#### Statistical Learning Setup

##### Assumptions of IID sampling and unknown data distribution
Training data are sampled from an **unknown** data distribution in an i.i.d. fashion.
$$(x_{n},y_{n}) \sim^{\text{iid}} \mathbb{P}_{\text{data}}(x,y)\quad n=1,\cdots,N$$

therefore the training data set is,
$$D=\left\{ (x_{n},y_{n}) \vert n=1,\cdots,N\right\}\sim \mathbb{P}_{\text{data}}(x,y)^N$$

Either input or output could be continuous or discrete scalar, vectors, tensors, sets,..etc.
$$\begin{aligned}
\text{E.g. regression}\quad &x_{n}\in \mathbb{R}^2\quad y_{n}\in \mathbb{R} \\
\text{classification}\quad &x_{n}\in \mathbb{R}^2\quad y_{n} \in \left\{ 1,2,\cdots,K \right\}
\end{aligned}$$

##### Model and Loss
[Model]
We introduce a model with learnable parameter $w$ as 
$$f(x,w)$$
- *Hyperparameters* are **not** learnable.
- It belongs to a hypothesis class, $f(x,w)\in \mathcal{H}$.
	- e.g. All linear models with weight norm no larger than 1 $$\mathcal{H}=\left\{ f(x,w)\vert f(x,w) = w^Tx,\lvert \lvert w \rvert  \rvert \leq{1} \right\}$$

[Loss]
Loss is denoted as $$\ell(y,f(x,w))$$
- Generalization error (a.k.a risk error, or expected loss) $$\mathbb{E}_{\mathbb{P}_{\text{data}}(x,y)}\left[\ell(y,f(x,w))\right]$$
	- Error observed when model is applied **to unseen data.**
- Training error (empirical risk or training loss)$$\frac{1}{N}\sum_{i=1}^N\ell(y_{n},f(x_{n},w))$$
	- Error (loss) computed **on training set**. Indicates how well model fits on training data.

[Learning]
Ideally, we want to find a model in the hypothesis class that minimizes the risk:
$$\text{min}_{f \in \mathbb{H}} \mathbb{E}_{\mathbb{P}_{\text{data}}(x,y)}\left[\ell(y,f(x,w))\right]$$
but the risk is incomputable (because of unknown data distribution), we can approximate it via
$$\text{min}_{f \in \mathbb{H}} \frac{1}{N}\sum_{n=1}^N \ell(y_{n},f(x_{n},w))$$
which is so called the “empirical risk minimization (ERM)”.

#### Linear Regression

##### Problem Specification (1D-Regression) 
$$\begin{aligned}
&(x_{n},y_{n}) \sim^{\text{iid}}\mathbb{P}_{\text{data}}(x,y)\quad n=1,\cdots,N \\
&x_{n}\in \mathbb{R}\quad y_{n}\in \mathbb{R}
\end{aligned}$$
###### Model Design
$$\text{Linear model (or linear layer)}\quad \hat{y}=w^Tx+b$$
##### Loss Design
$$L(\left\{ \hat{y}_{n},y_{n} \right\}) = \frac{1}{N}\sum_{n=1}^N\ell(\hat{y}_{n},y_{n})$$
- Mean squared error (MES), L2 Loss $$\ell(\hat{y}_{n},y_{n})=\lvert \lvert \hat{y}_{n}-y_{n} \rvert  \rvert^2_{2} $$
- L1 Loss $$\ell(\hat{y}_{n},y_{n})=\lvert \lvert \hat{y}_{n}-y_{n} \rvert  \rvert _{1}$$
- Smooth L1 loss (similar to Huber loss)$$\begin{cases}
\frac{1}{2\beta}\lvert \lvert \hat{y}_{n}-y_{n} \rvert  \rvert ^2_{2}\quad \text{if }\lvert \lvert \hat{y}_{n}-y_{n} \rvert  \rvert _{1}<\beta  \\
\lvert \lvert \hat{y}_{n}-y_{n} \rvert  \rvert _{1}- \frac{1}{2\beta}\quad \text{otherwise}
\end{cases}$$
	- Is used to combine the benefits of each. At lower ranges, L2 loss is used for gradient. And at large error, prevents exploding by incorporating L1 loss.
![[Pasted image 20250208214018.png]]


##### Inference Algorithm
We typically interpret “inference” as the computational process from input to output.
→ e.g. the forward pass of a feedforward neural network.
a.k.a
$$\hat{y}=wx^T+b$$

##### Learning Algorithm
Learning is an optimization problem → A learning algorithm is just an optimization algorithm.

1. Gradient Based
	1. 1st order gradient method (stochastic gradient descent (SGD)).
	2. 2nd order gradient method (Newton’s method).
2. Gradient Free
	1. Genetic algorithms
	2. Random search

In linear regression, we have
$$f(x,w,b)=\hat{y}=w^Tx+b$$
with MSE loss, the learning problem is
$$\text{min}_{w,b}L(w,b)= \frac{1}{N}\sum_{n=1}^N\ell(f(x_{n},w,b),y_{n})= \frac{1}{N}\sum_{n=1}^N \lvert \lvert w^Tx_{n}+b-y_{n} \rvert  \rvert _{2}^2$$

to just remove the scaling of 2 when getting the gradient, we can write it equivalently as,
$$\text{min}_{w,b}L(w,b)= \frac{1}{N}\sum_{n=1}^N\ell(f(x_{n},w,b),y_{n})= \frac{1}{2N}\sum_{n=1}^N \lvert \lvert w^Tx_{n}+b-y_{n} \rvert  \rvert _{2}^2$$

but to use either gradient descent or stochastic gradient descent, we need to get the gradient.

###### Gradient
Loss is typically a scalar, parameters can be viewed as a vector,
$$\frac{\partial L}{\partial w[i]}= \lim_{ \epsilon \to 0 } \frac{L(w+\epsilon e_{i},b)-L(w,b)}{\epsilon}$$
where $w[i]$ is the $i$-th element (scalar) of weight and $e_{i}$ is a zero vector except that the $i$-th element is 1.

$$\begin{aligned}
L(w,b)&= \frac{1}{2N}\sum_{n=1}^N \lvert \lvert w^Tx_{n}+b-y_{n} \rvert  \rvert _{2}^2 \\ 
&= \frac{1}{2N} \sum_{n=1}^N \left(\sum_{d=1}^D w[d]x_{n}[d]+b-y_{n}\right)^2
\end{aligned}$$

Then,
$$\begin{aligned}
\frac{\partial L(w,b)}{\partial w[i]} &=\sum_{n=1}^N \frac{\partial L(w,b)}{\partial l_{n}}\frac{\partial l_{n}}{\partial w[i]}\\
&=\sum _{n=1}^N\frac{\partial \frac{1}{2N}\sum_{n=1}^Nl_{n}^2}{\partial l_{n}}\frac{\partial l_{n}}{\partial w[i]} \\
&= \frac{1}{2N}\sum_{n=1}^N 2l_{n} \frac{\partial l_{n}}{\partial w[i]} \\ 
&= \frac{1}{N}\sum_{n=1}^N l_{n}\frac{\partial \left(\sum_{d=1}^D w[d]x_{n}[d]+b-y_{n} \right)}{\partial w[i]} \\ 
&= \frac{1}{N}\sum_{n=1}^N l_{n}x_{n}[i] 
\end{aligned}$$

In a compact vector form:
$$\begin{aligned}
\frac{\partial L(w,b)}{\partial w} &= \begin{bmatrix}
\frac{\partial L(w,b)}{\partial w[1]}  \\
\vdots \\
\frac{\partial L(w,b)}{\partial w[D]}
\end{bmatrix} \\ &= \frac{1}{N}\sum_{n=1}^Nl_{n}x_{n}
\end{aligned}$$

==The problem is that if $N$ is too large, then we won’t have a meaningful gradient, therefore we can randomly sample smaller batches (a.k.a mini-batches) to compute the gradient.==

Let’s try computing $\frac{\partial L(w,b)}{\partial  b}$,
$$\begin{aligned}
\frac{\partial L(w,b)}{\partial b} &=\sum_{n=1}^N\frac{\partial L(w,b)}{\partial l_{n}}\frac{\partial l_{n}}{\partial b} \\
&= \frac{1}{2N}\sum_{n=1}^N 2l_{n} \frac{\partial \left(\sum_{d=1}^D w[d]x_{n}[d]+b-y_{n} \right)}{\partial b} \\ 
&= \frac{1}{N}\sum_{n=1}^Nl_{n}D
\end{aligned}$$

Then we can perform the gradient descent algorithm,
```
Input: GD step T, learning Rate s, initial (w0,b0)

For t = 1,...,T
	w^t = w^{t-1} - s * pdiv(L(w^{t-1},b^{t-1}))_w
	b^t = b^{t-1} - s * pdiv(L(w^{t-1},b^{t-1}))_b

return (w^T,b^T)
```
- Learning rate = step size. 
- If we use the full training dataset to compute the gradient descent per step, then it is called (batch) gradient descent.
- If we use random mini-batch data to compute the gradient per step, then it is called *stochastic gradient descent*.

==The last return is not necessarily the best result, we might have not converged or we might have overfitted etc.==

##### Validation and Testing
Our ultimate goal is to **learn a model on observed data so that it can generalize well to unseen data!**

To facilitate this goal, we typically split a dataset into **train/validation/test** subsets.

1. During training, we use the training set to train the model, e.g. *GD to train linear regression*.
2. We can tune hyperparameters and select the best model based on *validation performance*, e.g. we can evaluate models on the validation set every 100 steps and return model with best validation metric.
3. Never use test set to select model.

For small datasets, we can use k-fold cross-validation so that we rotate training and validation.

###### Overfitting vs. Underfitting
![[Screenshot 2025-02-08 at 10.59.38 PM.png]]

- **Underfitting**:
	- Model is too simple to fit the data.
- **Overfitting**:
	- Model is too complicate, perfectly fits data but no generalization.

When we have both perfectly fitting + well generalization → we call it **benign overfitting**.

###### Bias vs. Variance Tradeoff
As the degree (a.k.a complexity) increases, the variance of the model tends to increase, and the bias tends to decrease.
- bias: Error caused by a model solving complex problems when it is over simplified (hence underfitting).
- variance: Error caused by model being highly sensitive to data, creating more complex models (hence overfitting).

Recall that,
$$\begin{aligned}
&1.(x_{n},y_{n})\sim^{\text{iid}}\mathbb{P}_{\text{data}}(x,y) \quad n=1,\cdots,N \\
&2.\text{training data set }D= \left\{ (x_{n},y_{n})\vert n=1,\cdots,N \right\}\sim \mathbb{P}_{\text{data}}(x,y)^N \\
&3.\text{expected label/ouput }\bar{y}(x) =\mathbb{E}_{\mathbb{P}_{\text{data}}(y|x)}[y] = \int_{y}y\mathbb{P}_{\text{data}}(y\vert x)dy \\
&4.\text{our learned model }f(x,w^*) = f(x,\mathcal{A}(D,w^0)) \equiv f_{D}(x) \\ 
&5.\text{expected learned model } \bar{f}(x) = \mathbb{E}_{D\sim \mathbb{P}_{\text{data}}(x,y)^N}[f_{D}(x)]
\end{aligned}$$
where basically $\mathcal{A}$ is the mapping between the training data set, initial weight and the learned weight.


And,
$$\begin{aligned}
&1.\text{generalization error }\mathbb{E}_{\mathbb{P}_{\text{data}}(x,y)}[(y-f_{D}(x))^2] \\ 
&2.\text{expected generalization error }\mathbb{E}_{D\sim \mathbb{P}_{\text{data}}(x,y)^N,(x,y)\sim \mathbb{P}_{\text{data}}(x,y)}[(y-f_{D}(x))^2]
\end{aligned}$$
Since the second one considers all possible training sets, this is what we actually care about.

Let’s do some math,
$$\begin{aligned}
\mathbb{E}_{D,x,y}\left[(y-f_{D}(x))^2\right]&\equiv \mathbb{E}_{D\sim \mathbb{P}_{\text{data}}(x,y)^N,(x,y)\sim \mathbb{P}_{\text{data}}(x,y)}[(y-f_{D}(x))^2] \\
&=\mathbb{E}_{D,x,y}[(f_{D}(x)-\bar{f}(x)+\bar{f}(x)-y)^2] \\ 
&= \mathbb{E}_{D,x,y}[(f_{D}(x)-\bar{f}(x))^2]+2\mathbb{E}_{D,x,y}[(f_{D}(x)-\bar{f}(x))(\bar{f}(x)-y)]\\
&+ \mathbb{E}_{D,x,y}[(\bar{f}(x)-y)^2] \\ 
&= \mathbb{E}_{D,x}[(f_{D}(x)-\bar{f}(x))^2]+2\mathbb{E}_{D,x,y}[(f_{D}(x)-\bar{f}(x))(\bar{f}(x)-y)]\\
&+ \mathbb{E}_{D,x}[(\bar{f}(x)-y)^2] \quad \text{remove those with no } y \text{ dependencies} 

\end{aligned}$$


$$\begin{aligned}
\mathbb{E}_{D,x,y}[(f_{D}(x)-\bar{f}(x))(\bar{f}(x)-y)] &= \mathbb{E}_{x,y}[\mathbb{E}_{D}[(f_{D}(x)-\bar{f}(x))(\bar{f}(x)-y)]] \\
&= \mathbb{E}_{x,y}[(\mathbb{E}_{D}[f_{D}(x)]-\bar{f}(x))(\bar{f}(x))-y]\\
&= \mathbb{E}_{x,y}[(\bar{f}(x)-\bar{f}(x))(\bar{f}(x)-y)] \\
&=0
\end{aligned}$$

$$\begin{aligned}
\mathbb{E}_{D,x}[(\bar{f}(x)-y)^2] &= \mathbb{E}_{D,x}[(\bar{f}(x)-\bar{y}(x)+\bar{y}(x)-y)^2] \\
&= \mathbb{E}_{x,y}[(\bar{f}(x)-\bar{y}(x))^2]+2\mathbb{E}_{x,y}[(\bar{f}(x)-\bar{y}(x))(\bar{y}(x)-y)] \\
&+ \mathbb{E}_{x,y}[(\bar{y}(x)-y)^2] 
\end{aligned}$$
$$\begin{aligned}
\mathbb{E}_{x,y}[(\bar{f}(x)-\bar{y}(x))(\bar{y}(x)-y)] &= \mathbb{E}_{x}[(\bar{f}(x)-\bar{y}(x))\mathbb{E}_{y\vert x}[(\bar{y}(x)-y)]] \\ 
&= \mathbb{E}_{x}[(\bar{f}(x)-\bar{y}(x))(\bar{y}(x)-\mathbb{E}_{y\vert x}[y])] \\ 
&= \mathbb{E}_{x}[(\bar{f}(x)-\bar{y}(x))(\bar{y}(x)-\bar{y}(x))] \\&=0
\end{aligned}$$

Thus, we end up with
$$\begin{aligned}
\mathbb{E}_{D,x,y}\left[(y-f_{D}(x))^2\right]&= \underbrace{ \mathbb{E}_{D,x}[(f_{D}(x)-\bar{f}(x))^2] }_{ \text{Variance} }+ \underbrace{ \mathbb{E}_{x,y}[(\bar{f}(x)-\bar{y}(x))^2] }_{ \text{Bias}^2 }\\& + \underbrace{ \mathbb{E}_{x,y}[(\bar{y}(x)-y)^2]  }_{ \text{Noise} }
\end{aligned}$$
- **Variance**: Captures how much your classifier changes if you train on a different training set. How “over-specialized” is your classifier to a particular training data set?
- **Bias**: What is the inherent error that you obtain from your classifier even with infinite training data? Inherent to model.
- **Noise**: How big is the data-intrinsic noise? This error measures ambiguity due to your data distribution and future representation. *YOU CAN NEVER BEAT THIS, ITS AN ASPECT OF DATA*.

==Classic Bias-Variance tradeoff cannot explain deep leaning as the model complexity measure is hard to find, e.g., #paramters cannot be a reliable factor.==

#### Linear Models for Classification
Suppose we’d like to do a binary classification with a linear model,
$$\begin{aligned}
&\left\{ (x_{n},y_{n})\vert n=1,\cdots,N \right\}\sim^{\text{iid}}\mathbb{P}_{\text{data}}(x,y) \\ 
&x_{n} \in \mathbb{R}^D\quad y_{n}\in \left\{ 0,1 \right\}\\
&f(x,w,b)=w^Tx+b
\end{aligned}$$

We can construct the threshold classifier (discontinuous heaviside) as,
$$\hat{y}=\begin{cases}
1\quad \text{if }f(x,w,b) >0  \\
0\quad \text{otherwise}
\end{cases}$$

The classification accuracy can be written as,
$$\bar{\ell}=\frac{1}{N}\sum_{n=1}^N \mathbf{1}[\hat{y}_{n}\neq y_{n}]$$
But this is discontinuous, how can we perform gradient descent to learn the model?

**Continuous Approximation!**
```functionplot
---
title: sigmoid
xLabel: x
yLabel: y
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
f(x)=1/(1+exp(-x))
```
The sigmoid function,
$$\sigma(x)=\frac{1}{1+e^{-x}}$$
can approximate the threshold classifier.
$$\hat{y}=\sigma(w^Tx+b)$$
will then output a probability.

==The problem with sigmoid is that the gradient becomes very near to 0 for ranges further from 0, hence making its gradient not-useful enough.==


The non-differentiable 0-1 loss for classification is,
$$L(\left\{ \hat{y}_{n} \right\},\left\{ y_{n} \right\})=\frac{1}{N}\sum_{n=1}^N \mathbf{1}[\hat{y}_{n}\neq y_{n}] $$
Since sigmoid *outputs a probability*, we can use cross-entropy (CE) to approximate 0-1 loss. 

Particularly, for two distributions $(p,q)$ of a discrete random variable with $K$ states, CE is defined as 
$$CE(p,q)=- \sum_{i=1}^K p[i]\log q[i]$$
Compared to 0-1 loss, it provides a finer measure. We would rather like to have a confidence in measure of output rather than treating equal penalties for different results.

Since we have binary states, we can reduce the CE loss to,
$$L(\left\{ \hat{y}_{n} \right\},\left\{ y_{n} \right\})= -\frac{1}{N}\sum_{n=1}^N (\mathbf{1}[y_{n}=1]\log \hat{y}_{n}+\mathbf{1}[y_{n}=0]\log(1-\hat{y}_{n}))$$

[Summary]
Since we can’t compute the gradient of 1-0 classification, we approximate it by the sigmoid which outputs a probability. Then we also need to approximate the original loss function (since it also gives values between 0~1) and this is where cross-entropy jumps in.

###### Multi-class Classification
Consider the following,
$$\begin{aligned}
&\left\{ (x_{n},y_{n})\vert n=1,\cdots,N \right\}\sim^{\text{iid}}\mathbb{P}_{\text{data}}(x,y) \\ \\
&x_{n} \in \mathbb{R}^D\quad y_{n}\in \left\{ 1,\cdots,K \right\}\\ \\
&f(x,W,b)=Wx+b \quad W \in \mathbb{R}^{K \times D}\; b\in \mathbb{R}^{K\times{1}}
\end{aligned}$$

We typically use 1-of-K encoding for the output:
$$y_{n}=k\quad \iff y_{n }= \underbrace{ [0,\cdots,0,1,0,\cdots,0] }_{ k-\text{th entry is 1} }$$
This allows use to use C-E, but not sigmoid (need to normalize + gets independent probability). Thus, we use the softmax function, which outputs a valid probability distribution of a discrete RV with $K$ states.
$$\text{softmax}(x)[i]= \frac{\exp(x[i])}{\sum_{k=1}^K\exp(x[k])}$$

Then we CE can be written as,
$$\begin{aligned}
L(\left\{ \hat{y}_{n} \right\},\left\{ y_{n} \right\})&= -\frac{1}{N}\sum_{n=1}^N\sum_{k=1}^K \mathbf{1}[y_{n}=k]\log \hat{y}_{n}[k] \\
&=  -\frac{1}{N}\sum_{n=1}^N\sum_{k=1}^K \mathbf{1}[y_{n}=k]\log \text{softmax}(f(x_{n},w,b))[k] \\
&=   -\frac{1}{N}\sum_{n=1}^N\sum_{k=1}^K \mathbf{1}[y_{n}=k]\left( f(x_{n},w,b)[k]-\log \sum_{j=1}^K \exp(f(x_{n},w,b))[j] \right)
\end{aligned}$$

But before we dig in, let’s look at the following operator,
$$\log \sum_{j=1}^K \exp$$
this is the log-sum-exp operator, it approximates the maximum operator.
$$\begin{aligned}
\log \sum_{k=1}^K \exp(x_{i})&=x^*-\log \exp(x^*)+ \log \sum_{i=1}^K\exp(x_{i})\\ &
=x^* + \log \sum_{i=1}^K\exp(x_{i}-x^*) \\
&x^* = \text{max}[x_{1},\cdots,x_{K}]
\end{aligned}$$
Without the log-sum-exp trick from above, we are prone to overflowing/underflowing. Thus, we use the Log-sum-exp trick to make it more numerically efficient.

###### Softmax
Softmax is an approximation of argmax, to see this we can change the base of the power,
$$e \to e^{ \frac{1}{\beta} }$$
then softmax becomes,
$$\text{softmax}(x)[i]= \frac{\exp\left( \frac{1}{\beta}x[i] \right)}{\sum_{k=1}^K\exp\left( \frac{1}{\beta}x[k] \right)}$$
$$\lim_{ \beta \to 0 } \text{softmax}(x)=\underbrace{ [0,\cdots,0,1,0,\cdots,0] }_{ \text{k-th entry is 1}  \to k=\text{argmax}_{i}x[i]}$$
$$\lim_{ \beta \to \infty }\text{softmax}(x) =\left[ \frac{1}{K},\cdots, \frac{1}{K} \right] $$
and $\beta$ is often called *temperature*.

#### Next Lecture [[UBC/CPEN 4-2/CPEN 455/Lectures/Lecture 2|Lecture 2]]
