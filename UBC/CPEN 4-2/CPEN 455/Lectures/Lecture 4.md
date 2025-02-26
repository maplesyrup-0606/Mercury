#### Learning Rate / Momentum / Adam
We know to compute gradients, let’s take a look on how to preform gradient-based learning. (e.g. SGD)

**Algorithm SGD**
$$\begin{aligned}
&\text{Input: step $T$, learning Rate $\eta$, initial $W^0$, batch size $B$}\\
&\text{For $t=1,\cdots,T$} \\ 
&\quad \text{Get mini-batch data ($X^t,Y^t$)} \\
&\quad L(W^{t-1},X^t,Y^t)= \frac{1}{B}\sum_{i=1}^B \ell(f(W^{t-1},X^t[i]),Y^t[i])) \\
&\quad W^t=W^{t-1} -\eta \frac{\partial L(W^{t-1},X^t,Y^t)}{\partial W} \\ 
&\text{Return $W^T$}
\end{aligned}$$


- $f(W^{t-1},X^t[i])$: forward pass.
- $\frac{\partial L(W^{t-1},X^t,Y^t)}{\partial W}$: backward pass.

SGD has trouble navigating ravines, i.e. areas where the surface curves much more steeply in one dimension than in another.
- In directions with steep curvature, SGD makes large updates.
- In flat directions, update steps are smaller.
→ zigzag, slower convergence towards minimum.

**SGD with Momentum**
$$\begin{aligned}
&\text{Input: step $T$, learning Rate $\eta$, initial $W^0$, batch size $B$}\\ &\quad \text{momentum $\beta$, initial $M^0$}\\
&\text{For $t=1,\cdots,T$} \\ 
&\quad \text{Get mini-batch data ($X^t,Y^t$)} \\
&\quad L(W^{t-1},X^t,Y^t)= \frac{1}{B}\sum_{i=1}^B \ell(f(W^{t-1},X^t[i]),Y^t[i])) \\
&\quad M^t = \beta M^{t-1} + \frac{\partial L(W^{t-1},X^t,Y^t)}{\partial W}  \\
&\quad W^t=W^{t-1} -\eta M^t\\ 
&\text{Return $W^T$}
\end{aligned}$$
- $M^t$ represents the momentum with the momentum coefficient $\beta$. It provides more weight to directions where the gradient points the same way.

**Adaptive Learning Rate**
Let $g^t = \frac{\partial L(W^{t-1},X^t,Y^t)}{\partial W}$, then
$$W^t=W^{t-1}-\eta g^t$$
from GD/SGD. How can we tune the learning rate?
==This is crucial since without adaptive learning rate, the learning rate is applied equally to all parameters.==

AdaGrad (Adaptive Gradient) proposes to assign larger learning rates to infrequently updated weights and smaller ones to frequently updated weights.

---

$$\begin{aligned}
G^t&=\sum_{\tau =1}^tg^\tau g^{\tau^T}=\begin{bmatrix}
g_{1}^2 & g_{1}g_{2} & \cdots & g_{1}g_{t} \\
g_{2}g_{1} & g_{2}^2 & \cdots & g_{2}g_{t} \\
\vdots & \vdots & \ddots & \vdots \\
g_{t}g_{1} & g_{t}g_{2} & \cdots & g_{t}^2
\end{bmatrix} \\ \\
W^t&=W^{t-1} -\eta \text{diag}(\epsilon I+G^t)^{-1/2}g^t
\end{aligned}$$

The diagonal for $G^t$ will be larger for frequently updated since less updates mean near 0 gradient and the sum of those diagonals would essentially be small. And using the relation $\text{diag}(\epsilon I+G^t)^{-1/2}$, this would put more learning rate an infrequent updates.

However → Since we accumulate (squared) gradients from the beginning, our learning rate is always decaying, **and can vanish before we converge**.

Why? → Due to unbounded $G^t$, our effective learning rate $\text{diag}(\epsilon I+G^t)^{-1/2}g^t$ is decreasing unboundedly and hence may vanish.

RMSProp proposes to use exponential moving average (EMA) of past squared gradients.
$$\begin{aligned}
G^t=\rho G^{t-1}+(1-\rho)g^tg^{t^T}
\end{aligned}$$

Adadelta leverages the same denominator trick (EMA) and additional weighting (numerator) based on parameter updates.

**Adam (BP + Adaptive Learning + Momentum)**
Based on RMSProp, Adam proposes to keep another EMA of past gradients.
$$\begin{aligned}
\tilde{g}^t &= \beta_{1}\tilde{g}^{t-1}+(1-\beta_{1})g^t \\ \\
G^t&=\beta_{2}G^{t-1} + (1-\beta_{2})g^tg^{t^T} \\ \\
W^t &= W^{t-1} -\eta_{t}\text{diag}(\epsilon I+G^t)^{-1/2}\tilde{g}^t \\ \\
\eta_{t} &= \eta \frac{\sqrt{ 1-\beta^t_{2} }}{1-\beta_{1}^t}
\end{aligned}$$

When $\beta_{1}=0$, Adam is almost the same as RMSProp besides the $\eta_{t}$ from above.

Let’s investigate the term,
$$\frac{\sqrt{ 1-\beta^t_{2} }}{1-\beta_{1}^t}$$

$$\begin{aligned}
\mathbb{E}[\tilde{g}^t] &= \mathbb{E}[\beta_{1}\tilde{g}^{t-1}+(1-\beta_{1})g^t] \\
&= \mathbb{E}[\beta_{1}(\beta_{1}\tilde{g}^{t-2} + (1-\beta_{1})g^{t-1})+(1-\beta_{1}){g}^t] \\ 
&= \mathbb{E}[\beta_{1}^2\tilde{g}^{t-2} + \beta_{1}(1-\beta_{1})g^{t-1}+(1-\beta_{1})g^t] \\ 
&= \mathbb{E}\left[ \sum_{i=1}^t \beta_{1}^{t-i}(1-\beta_{1})g^i+\beta_{1}^t \tilde{g}^0 \right]
\end{aligned}$$

Since $\tilde{g}_0$ is an initial term, we can ignore this term with zero initialization and assume the gradients each time step are stationary, then,
$$\begin{aligned}
&\approx \sum_{i=1}^t\beta_{1}^{t-i}(1-\beta_{1})\mathbb{E}[g^{i}] \\ 
&= \left( \sum_{i=0}^{t-1}\beta_{1}^i \right)(1-\beta_{1})\mathbb{E}[g^{i}] \\
&= (1-\beta_{1}^t)\mathbb{E}[g^{i}]
\end{aligned}$$

Similarly, we have that
$$\begin{aligned}
\mathbb{E}[G^t]&\approx (1-\beta_{2}^t)\mathbb{E}[g^ig^{i^T}] \\
\mathbb{E}[G^t[j,j]]&\approx (1-\beta_{2}^t)\mathbb{E}[(g^i[j])^2]
\end{aligned}$$

By letting $\Delta W^t = \eta_{t}\text{diag}(\epsilon I+G^t)^{-1/2}\tilde{g}^t$,
$$\begin{aligned}
\mathbb{E}[\Delta W^t[j]]&=\mathbb{E}\left[ \eta _{t} \frac{1}{\sqrt{ \epsilon+G^t[j,j] }}\tilde{g}^t[j] \right]\approx\mathbb{E}\left[ \eta _{t} \frac{1}{\sqrt{ G^t[j,j] }}\tilde{g}^t[j] \right] \\ 
&=\eta_{t} \frac{\mathbb{E}[\tilde{g}^t[j]]}{\mathbb{E}[\sqrt{ G^t[j,j] }]} \approx \eta_{t} \frac{\mathbb{E}[\tilde{g}^t[j]]}{\sqrt{ \mathbb{E}[G^t[j,j]] }} \\ 
&\approx \eta_{t} \frac{(1-\beta_{1}^t)\mathbb{E}[g^i[j]]}{\sqrt{ (1-\beta_{2}^t)\mathbb{E}[(g^i[j])^2] }} \leq \eta_{t} \frac{(1-\beta_{1}^t)}{\sqrt{ (1-\beta_{2}^t) }}=\eta
\end{aligned}$$

[Jensen’s Inequality]
$$\mathbb{E}[g^i[j]] \leq \sqrt{ \mathbb{E}[(g^i[j])^2]}$$
![[Screenshot 2025-02-11 at 4.54.17 PM.png]]

#### Weight Decay
Suppose we are *overfitting* and want to regularize the complexity of our neural networks to reduce it. We can penalize weights so that they are not far from 0, thus restricting the set of models we are considering.

==Large weights → Sharp, complex decision boundaries. Which means that the model is trying to fit every point perfectly creating a squiggly overfitting vibe.==

$$\begin{aligned}
L(W,X,Y) &= \frac{1}{B}\sum_{i=1}^B \ell(f(W,X[i]),Y[i]) \\ 
\tilde{L}(W,X,Y) &= L(W,X,Y) + \frac{\lambda}{2}\lvert \lvert \text{Vec}(W) \rvert  \rvert _{2}^2
\end{aligned}$$

we can control the lambda to trade-off model complexity and overfitting.

If we look at the gradient,
$$\frac{\partial \tilde{L}}{\partial W} = \frac{\partial L}{\partial W}+\lambda W$$

For SGD, SGD + Momentum, we directly add. But for Adam, we have two possibilities,
1. add it to gradient.
2. add it to gradient update.

These are different since the order changes and how Adam is constructed, #2 is called AdamW!

[Adam]
![[Screenshot 2025-02-11 at 5.13.37 PM.png]]

[AdamW]
![[Screenshot 2025-02-11 at 5.13.56 PM.png]]
==For some cases, the latter works much better.==

#### Early Stopping
We are not forced to run the optimization until the maximum number of iterations, or until its convergence.

We can check the validation error and if it is still increasing within a time window, then we stop training.

If we are worried that it will go down, run till the maximum number of iterations and pick the one with the least validation error.
![[Screenshot 2025-02-11 at 5.18.06 PM.png]]

#### Next Lecture [[UBC/CPEN 4-2/CPEN 455/Lectures/Lecture 5|Lecture 5]]
