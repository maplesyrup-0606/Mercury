#### Learning Algorithm
Learning algorithms are optimization algorithms and are about credit assignment.
→ By computing gradients and adjusting parameters based on loss, we are essentially assigning credits.

- **Gradient Based Learning** is a very successful learning algorithm.
	- Stochastic Gradient Descent (SGD).
- **Back-propagation (BP)** is an efficient SGD in the context of deep learning.

##### Feedforward Neural Networks
Consider the following MLP, and let’s look at forward pass,
![[Screenshot 2025-02-10 at 6.44.56 PM.png]]
$$\begin{aligned}
\mathbf{h}_{1}&=\sigma(W_{1}\mathbf{x})\\ \mathbf{h_{2}}&=\sigma(W_{2}\mathbf{h}_{1}) \\ &\vdots \\ 
\mathbf{h}_{M}&=\sigma(W_{M}\mathbf{h}_{M-1}) \\ \\
\mathbf{y}&=W_{M+1}\mathbf{h}_{M}
\end{aligned}$$
And the loss would be: $L=\ell(\mathbf{y},\bar{\mathbf{y}})$. For mini-batches: $L=\frac{1}{B}\sum_{i=1}^B \ell(\mathbf{y}_{i},\bar{\mathbf{y}}_{i})$.

##### Back Propagation
Let’s go through a bit of vector calculus,
**Gradient**: For a scalar-valued differentiable function: $f:\mathbb{R}^n\to \mathbb{R}$, the gradient 
$\nabla f:\mathbb{R}^n\to \mathbb{R}^n$. 

$$\begin{aligned}
&\mathbf{p}=\begin{bmatrix}
\mathbf{p}_{1} & \mathbf{p}_{2} & \cdots & \mathbf{p}_{n}
\end{bmatrix}^T \\ \\
& \nabla f(\mathbf{p})=\begin{bmatrix}
\frac{\partial f}{\partial x_{1}}(\mathbf{p}) \\
\vdots \\
\frac{\partial f}{\partial x_{n}}(\mathbf{p})
\end{bmatrix}
\end{aligned}$$

**Jacobian**: For a vector-valued differentiable function: $f:\mathbb{R}^n\to \mathbb{R}^m$ of multiple variables, the Jacobian matrix evaluated at $\mathbf{p}=\begin{bmatrix}\mathbf{p}_{1} & \mathbf{p}_{2} & \cdots & \mathbf{p}_{n} \end{bmatrix}^T$ is
$$\mathbf{J}_{f}(\mathbf{p})= \begin{bmatrix}
\nabla^Tf_{1}(\mathbf{p})  \\
\vdots \\
\nabla^Tf_{m}(\mathbf{p}) 
\end{bmatrix}=\begin{bmatrix}
\frac{\partial f_{1}}{\partial x_{1}}(\mathbf{p}) & \cdots & \frac{\partial f_{1}}{\partial x_{n}}(\mathbf{p}) \\
\vdots & \ddots & \vdots \\
\frac{\partial f_{m}}{\partial x_{1}}(\mathbf{p}) & \cdots & \frac{\partial f_{m}}{\partial x_{n}}(\mathbf{p})
\end{bmatrix}$$

- **Chain Rule**:
	- Scalar-valued & single variable:$$f:\mathbb{R}\to \mathbb{R}\quad g:\mathbb{R}\to \mathbb{R}$$$$ \frac{df(g(x))}{dx}= \frac{df(g(x))}{g(x)} \frac{dg(x)}{dx}  = \nabla f(g(x))\nabla g(x)$$
	- Scalar-valued & multiple variables:$$f:\mathbb{R}^m\to \mathbb{R} \quad g:\mathbb{R}^n\to \mathbb{R}^m$$$$\mathbf{J}_{g}(x)^T\nabla f(g(x))$$ Let’s look at one case, the gradient with respect to $x_{1}$, $$\frac{\partial f(g(x))}{\partial x_{1}} = \sum_{m=1}^M\frac{\partial f(g_{m}(x))}{\partial g_{m}(x)}\frac{\partial g_{m}(x)}{\partial x_{1}}$$$$\frac{\partial f(g(x))}{\partial x}=\begin{bmatrix}
\sum_{m}\frac{\partial f(g_{m}(x))}{\partial g_{m}(x)}\frac{\partial g_{m}(x)}{\partial x_{1}} \\
\sum_{m}\frac{\partial f(g_{m}(x))}{\partial g_{m}(x)}\frac{\partial g_{m}(x)}{\partial x_{2}} \\
\vdots \\
\sum_{m}\frac{\partial f(g_{m}(x))}{\partial g_{m}(x)}\frac{\partial g_{m}(x)}{\partial x_{n}}
\end{bmatrix}$$$$=\begin{bmatrix}
\frac{\partial g_{1}}{\partial x_{1}} & \cdots & \frac{\partial g_{m}}{\partial x_{1}}  \\
\vdots & \ddots & \vdots \\
\frac{\partial g_{1}}{\partial x_{n}} & \cdots & \frac{\partial g_{m}}{\partial x_{n}}
\end{bmatrix}\begin{bmatrix}
\frac{\partial f}{\partial g_{1}} \\
\vdots \\
\frac{\partial f}{\partial g_{m}}
\end{bmatrix}=\mathbf{J}_{g}(x)^T\nabla f(g(x))$$If we consider all paths from each $x$ to the final, it’s easier.


During backward pass, let’s compute the gradient.
![[Screenshot 2025-02-10 at 7.52.36 PM.png]]
$$Loss:\quad L=\ell(\mathbf{y},\bar{\mathbf{y}})$$
Then the gradient loss w.r.t. $\mathbf{y}$ is
$$\mathbf{y}: \frac{\partial L}{\partial \mathbf{y}}$$
If we were to compute the gradient loss w.r.t to $\mathbf{h}_{M}$,
$$\frac{\partial L}{\partial \mathbf{h}_{M}}\leftarrow L=\ell(\mathbf{y},\bar{\mathbf{y}})\quad\mathbf{y}=W_{M+1}\mathbf{h}_{M}$$
$$\frac{\partial L}{\partial \mathbf{h}_{M}}=\left( \frac{\partial \mathbf{y}}{\partial \mathbf{h}_{M}} \right)^T\left( \frac{\partial L}{\partial \mathbf{y}} \right)$$
And we know that $\mathbf{y}=W_{M+1}\mathbf{h}_{M}$, therefore
$$\frac{\partial \mathbf{y}}{\partial \mathbf{h}_{M}}=W_{M+1}$$

What if we compute the gradient loss w.r.t. $W_{M+1}$? Ideally, we want something like,
$$\frac{\partial L}{\partial W_{M+1}}=\frac{\partial L}{\partial \mathbf{y}}\frac{\partial \mathbf{y}}{\partial W_{M+1}}$$
But there is a shape mismatch, the second term is a derivative of a vector w.r.t. a matrix. We cannot apply the chain rule like this! 

We know that $\mathbf{y}[i]$ is only dependent on $W_{M+1}[i,:]$,
$$\mathbf{y}[i]=\sum_{j}W_{M+1}[i,j]\mathbf{h}_{M}[j]$$
hence,
$$\frac{\partial \mathbf{y}[i]}{\partial W_{M+1}[i,j]}=\mathbf{h}_{M}[j]$$
letting us do,
$$\frac{\partial L}{\partial W_{M+1}[i,j]}=\frac{\partial L}{\partial \mathbf{y}[i]}\frac{\partial \mathbf{y}[i]}{\partial W_{M+1}[i,j]}=\frac{\partial L}{\partial \mathbf{y}[i]}\mathbf{h}_{M}[j]$$
since for $\mathbf{y}[j]$ where $i\neq j$, the partial derivative evaluates as 0 for the latter term.
$$\therefore \frac{\partial L}{\partial W_{M+1}}=\frac{\partial L}{\partial \mathbf{y}}\mathbf{h}_{M}^T$$
---
Let’s look at the loss w.r.t. $\mathbf{h}_{2}$, from the previous examples we know that,
$$\begin{aligned}
\frac{\partial L}{\partial \mathbf{h}_{M}}&=\left( \frac{\partial \mathbf{y}}{\partial \mathbf{h}_{M}} \right)^T\frac{\partial L}{\partial \mathbf{y}} \\
\frac{\partial L}{\partial \mathbf{h}_{M-1}}&=\left( \frac{\partial \mathbf{h}_M}{\partial \mathbf{h}_{M-1}} \right)^T\frac{\partial L}{\partial \mathbf{h}_{M}}
\end{aligned}$$
hence,
$$\begin{aligned}
\frac{\partial L}{\partial \mathbf{h}_{2}}&=\left( \frac{\partial \mathbf{h}_{3}}{\partial \mathbf{h}_{2}} \right)^T\cdots\left( \frac{\partial \mathbf{h}_{M}}{\partial \mathbf{h}_{M-1}} \right)^T\left( \frac{\partial \mathbf{y}}{\partial \mathbf{h}_{M}} \right)^T\frac{\partial L}{\partial \mathbf{y}} \\ 
&=\mathbf{J}_{3}^T\cdots\mathbf{J}_{M}^T\frac{\partial L}{\partial \mathbf{y}}\quad \mathbf{J}_{i+1}\equiv \frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{h}_{i}},\mathbf{h}_{M+1}\equiv \mathbf{y}
\end{aligned}$$

Let’s now compute for $\mathbf{J}_{i+1}=\frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{h}_{i}}$, recall that $\mathbf{h}_{i+1}=\sigma(W_{i+1}\mathbf{h}_{i})$, by letting $\mathbf{z}_{i+1}=W_{i+1}\mathbf{h}_{i}$,
$$\frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{h}_{i}}=\frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{z}_{i}}\frac{\partial \mathbf{z}_{i+1}}{\partial \mathbf{h}_{i}}$$

If we compute $\frac{\partial \mathbf{z}_{i+1}}{\partial \mathbf{h}_{i}}$,
$$\frac{\partial \mathbf{z}_{i+1}}{\partial \mathbf{h}_{i}}=W_{i+1}$$
and if we compute $\frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{z}_{i+1}}$,
$$\frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{z}_{i+1}}=\text{diag}(\sigma'(\mathbf{z}_{i+1}))$$

$$\therefore \frac{\partial \mathbf{h}_{i+1}}{\partial \mathbf{h}_{i}}=\text{diag}(\sigma'(\mathbf{z}_{i+1}))W_{i+1}$$
Which in summary makes,
$$\frac{\partial L}{\partial \mathbf{h}_{i}}=\mathbf{J}_{i+1}^T\cdots\mathbf{J}_{M}^T\frac{\partial L}{\partial \mathbf{y}}\quad\because \mathbf{J}_{i}=\text{diag}(\sigma'(\mathbf{z}_{i}))W_{i},\mathbf{z_{i}}=\sigma(W_{i}\mathbf{h}_{i-1})$$
--- 
Let’s compute $\frac{\partial L}{\partial W_{i}}$, we have to recall that $\mathbf{h}_{i}=\sigma(W_{i}\mathbf{h}_{i-1})=\sigma(\mathbf{z}_{i})$, 
$$\frac{\partial L}{\partial \mathbf{z}_{i}}=\left( \frac{\partial \mathbf{h}_{i}}{\partial \mathbf{z}_{i}} \right)^T\frac{\partial L}{\partial \mathbf{h}_{i}} =\sigma'(\mathbf{z}_{i}) \odot\frac{\partial L}{\partial \mathbf{h}_{i}}$$
using that the first term is a diagonal matrix and the second is a vector, we can simply make it a element-wise dot product.

Then,
$$\frac{\partial L}{\partial W_{i}[u,v]}=\frac{\partial L}{\partial \mathbf{z}_{i}[u]}\frac{\partial \mathbf{z}_{i}[u]}{\partial W_{i}[u,v]}=\frac{\partial L}{\partial \mathbf{z}_{i}[u]}\mathbf{h}_{i-1}[v]$$
$$\to \frac{\partial L}{\partial W_{i}}=\frac{\partial L}{\partial \mathbf{z}_{i}}\mathbf{h}_{i-1}^T$$

Therefore,
$$\therefore\frac{\partial L}{\partial W_{i}}=\left( \sigma'(\mathbf{z}_{i})\odot \frac{\partial L}{\partial \mathbf{h}_{i}} \right)\mathbf{h}_{i-1}^T$$
---
During backward pass, it is inefficient to compute $\mathbf{z}_{i}=W_{i}\mathbf{h}_{i-1},\mathbf{h}_{i-1}^T$ again since they are achievable in forward pass.
==Thus, we can cache these tensors in the forward pass and use them again!==
==Of course, backward pass is more inefficient..==

#### Initialization
Weight and bias initialization impacts gradients, of course because they carry some value (unless set to zero).

Let’s recall some probability stuff,

$$\mathbb{E}[x+y]=\mathbb{E}[x]+\mathbb{E}[y]$$
and for two independent random variables,
$$\begin{aligned}
\mathbb{E}[xy]&=\mathbb{E}[x]\mathbb{E}[y] \\
\mathbb{E}[x^2y^2]&=\mathbb{E}[x^2]\mathbb{E}[y^2]
\end{aligned}$$

$$\begin{aligned}
\mathbb{V}[x+y]&=\mathbb{E}[(x+y){^2}] -\mathbb{E}[x+y]^2\\
&=\mathbb{E}[x^2+y^2+2xy]-(\mathbb{E}[x]+\mathbb{E}[y])^2 \\ 
&= \mathbb{E}[x^2]+\mathbb{E}[y^2]+2\mathbb{E}[xy]-\mathbb{E}[x]^2-\mathbb{E}[y]^2-2\mathbb{E}[x]\mathbb{E}[y] \\
&= \mathbb{V}[x]+\mathbb{V}[y]
\end{aligned}$$
$$\begin{aligned}
\mathbb{V}[xy]&=\mathbb{E}[(xy)^2]-\mathbb{E}[xy]^2 \\
&=\mathbb{E}[x^2y^2]-\mathbb{E}[x]^2\mathbb{E}[y]^2 \\ 
&= \mathbb{E}[x^2]\mathbb{E}[y^2]-\mathbb{E}[x]^2\mathbb{E}[y^2]+\mathbb{E}[x]^2\mathbb{E}[y^2]-\mathbb{E}[x]^2\mathbb{E}[y]^2 \\
&= \mathbb{E}[y^2](\mathbb{E}[x^2]-\mathbb{E}[x]^2) + \mathbb{E}[x]^2(\mathbb{E}[y^2]-\mathbb{E}[y]^2) \\ 
&= \mathbb{E}[y^2]\mathbb{V}[x]+\mathbb{E}[x]^2\mathbb{V}[y] \\ 
&= \mathbb{V}[x](\mathbb{V}[y]+\mathbb{E}[y]^2)+\mathbb{E}[x]^2\mathbb{V}[y]\\ 
&= \mathbb{V}[x]\mathbb{V}[y] + \mathbb{V}[x]\mathbb{E}[y]^2+\mathbb{V}[y]\mathbb{E}[x]^2
\end{aligned}$$

If $\mathbb{E}[x]=\mathbb{E}[y]=0$, then $\mathbb{V}[xy]=\mathbb{V}[x]\mathbb{V}[y]$.

Now, let’s set the deep MLP with an activation function $\sigma(x)= \frac{e^x-e^{-x}}{e^x+e^{-x}}$ and assume we are in the linear regime. 
![[Screenshot 2025-02-10 at 9.23.01 PM.png]]

##### Forward Analysis
Then,
$$\mathbf{h}_{2}[i]=\sigma\left( \sum_{j}^{N_{1}}W_{2}[i,j]\mathbf{h}_{1}[j] \right) \approx \sum_{j}^{N_{1}}W_{2}[i,j]\mathbf{h}_{1}[j]$$
we further assume i.i.d and zero mean with same variance for all $\mathbf{h}_{i}[j]$ and all weights $W_{2}[i,j]$ at all layers, then
$$\begin{aligned}
\mathbb{V}[\mathbf{h}_{2}[i]]&=\mathbb{V}\left[\sum_{j=1}^{N_{1}}W_{2}[i,j]\mathbf{h}_{1}[j]\right]\\
&=\sum_{j=1}^{N_{1}}\mathbb{V}\left[W_{2}[i,j]\mathbf{h}_{1}[j]\right] \\
&= \sum_{j=1}^{N_{1}}\mathbb{V}[W_{2}[i,j]]\mathbb{V}[\mathbf{h}_{1}[j]] \\ 
&= N_{1}\mathbb{V}[W_{2}[i,j]]\mathbb{V}[\mathbf{h}_{1}[j]]
\end{aligned}$$
==This relation holds for all layers with the given assumptions.==

Then,
$$\mathbb{V}[\mathbf{h}_{l}[i]]\approx \mathbb{V}[\mathbf{x}[j]]\prod_{k=1}^lN_{k-1}\mathbb{V}[W_{k}[i,j]]$$
$i,j$ here are arbitrary due to the assumptions.

To preserve variance of activations through forward pass, we ideally want
$$\mathbb{V}[\mathbf{h}_{l}[i]]\approx \mathbb{V}[\mathbf{x}[j]]$$
then we can simply set,
$$\mathbb{V}[W_{k}[i,j]]N_{k-1}=1\to \mathbb{V}[W_{k}[i,j]]=\frac{1}{N_{k-1}}$$

##### Backward Analysis
With the same assumptions, we want to analyze backwards, why?
→In forward propagation, we need some variance maintained from activations so that things don’t blow up or diminish. Same for backwards, we don’t want the gradient to cause a vanish or blow up as well!

With,
$$\mathbf{h}_{2}[i]=\sigma\left( \sum_{j}^{N_{1}}W_{2}[i,j]\mathbf{h}_{1}[j] \right) \approx \sum_{j}^{N_{1}}W_{2}[i,j]\mathbf{h}_{1}[j]$$
Let’s look at the gradient w.r.t. activations,
$$\frac{\partial L}{\partial \mathbf{h}_{1}[j]}= \sum_{i=1}^{N_{2}}\frac{\partial L}{\partial \mathbf{h}_{2}[i]}\frac{\partial \mathbf{h}_{2}[i]}{\partial \mathbf{h}_{1}[j] }\approx \sum_{i=1}^{N_{2}}\frac{\partial L}{\partial \mathbf{h}_{2}[i]}W_{2}[i,j]$$

By again assuming i.i.d and zero mean with same variance for $\frac{\partial L}{\partial \mathbf{h}_{2}[i]},W_{2}[i,j],\mathbf{h}_{2}[i]$ for all layers, then
$$\begin{aligned}
\mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{h}_{1}[j]} \right]&\approx \sum_{i=1}^{N_{2}}\mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{h}_{2}[i]} \right]\mathbb{V}[W_{2}[i,j]] \\
&=N_{2}\mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{h}_{2}[i]} \right]\mathbb{V}[W_{2}[i,j]] \\ 
&= \mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{y}[i]} \right]\prod_{k=2}^{M+1}N_{k}\mathbb{V}[W_{k}[i,j]]
\end{aligned}$$
setting $$\mathbb{V}[W_{k}[i,j]]=\frac{1}{N_{k}}$$
preserves the variance of gradients w.r.t. to activations.

---
What about the gradients w.r.t. the weights?
$$\frac{\partial L}{\partial W_{2}[i,j]}=\frac{\partial L}{\partial \mathbf{h}_{2}[i]}\frac{\partial \mathbf{h}_{2}[i]}{\partial W_{2}[i,j]} \approx \frac{\partial L}{\partial \mathbf{h}_{2}[i]}\mathbf{h}_{1}[j]$$

then,
$$\begin{aligned}
\mathbb{V}\left[ \frac{\partial L}{\partial W_{2}[i,j]} \right]&\approx \mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{h}_{2}[i]} \right]\mathbb{V}[\mathbf{h}_{1}[j]] \\
&= \left( \mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{y}[i]} \right]\prod_{k=3}^{M+1}N_{k}\mathbb{V}[W_{k}[i,j]] \right)\left(\mathbb{V}[\mathbf{x}[j]]\prod_{k=1}^1 N_{k-1}\mathbb{V}[W_{k}[i,j]]\right) \\ 
&= \frac{N_{0}}{N_{1}} \left(\mathbb{V}[\mathbf{x}[j]]\prod_{k=1}^1 N_{k}\mathbb{V}[W_{k}[i,j]]\right)\left(\prod_{k=3}^{M+1}N_{k}\mathbb{V}[W_{k}[i,j]] \right)\mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{y}[i]} \right]\mathbb{V[\mathbf{x}]}[j] \\ 
&= \frac{N_{0}}{N_{1}}\mathbb{V}\left[ \frac{\partial L}{\partial \mathbf{y}[i]} \right]\mathbb{V}[\mathbf{x}[j]]
\end{aligned}$$
with the setting of the weight variances as $\mathbb{V}[W_{k}[i,j]]=\frac{1}{N_{k}}$, it makes the variance with respect to the gradients of the weights behave reasonably! (no explode, vanishing)

--- 
But to compromise between the two goals (preserve variance of activations + gradients), we can take the denominators,
$$\mathbb{V}[W_{k}[i,j]]= \frac{1}{\frac{N_{k}+N_{k-1}}{2}}=\frac{2}{N_{k}+N_{k-1}}$$

#### Next Lecture [[UBC/CPEN 4-2/CPEN 455/Lectures/Lecture 4|Lecture 4]]
