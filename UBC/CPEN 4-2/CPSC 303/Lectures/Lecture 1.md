#### Algorithm Properties
- Accuracy
- Efficiency
- Robustness

###### Problem conditioning and algorithm stability
- A problem is **ill-conditioned** if a small perturbation in the data may produce a large difference in the result. ←> Otherwise **well-conditioned**.
- An algorithm is **stable** if its output is the exact result of slightly perturbed input.

![[Pasted image 20250130191758.png]]

###### Computational error and data propagation error
When we approximate $f(x)$ by $\bar{f}(\bar{x})$, the difference in the result can be presented as follows:
$$\bar{f} (\bar{x}) - f(x) = \underbrace{ \bar{f} ( \bar{x}) - f(\bar{x}) }_{e_{a}} + \underbrace{ f(\bar{x}) - f(x) }_{ e_{p} }  $$
- $e_a$ is related to the stability of the algorithm.
- $e_p$ is related to the conditioning of the problem.

###### Forward / Backward error
- Forward Error: When we compute an approximation $\bar{y}$ to $y=f(x)$.
$$\lvert \bar{y}-y \rvert \text{: absolute error} \quad \frac{\lvert \bar{y}-y \rvert }{\lvert y \rvert } \text{: relative error}  $$

- Backward Error: Given an approximation $\bar{y}$ of $y=f(x)$, what is $\bar{x}$ for which $\bar{y} = f(\bar{x})$?
$$\lvert \bar{x}-x \rvert \text{: absolute error} \quad \frac{\lvert \bar{x}-x \rvert }{\lvert x \rvert } \text{: relative error}  $$


*Ideally, we want both forward and backward errors small.*

e.g.
Suppose that a certain algorithm for computing the square root function $f(x) =\sqrt{ x }$ gives us the approximate value $\bar{y}=1.7$ for $y=f(3) =\sqrt{ 3 }=1.73205\dots$

The absolute and relative forward errors are,
$$\lvert y-\bar{y} \rvert = 1.73205.. 0 - 1.7  = 0.03205\dots$$
$$ \frac{\lvert y-\bar{y} \rvert }{\lvert y \rvert } = \frac{0.03205\dots}{1.73205\dots} $$

To compute the backward error, we look for $\bar{x}$ such that $\bar{y}=1.7=f(\bar{x})=\sqrt{ \bar{x} }$.
Here, we get
$$\bar{x} = \bar{y}^2 = 1.7^2 = 2.89$$
$$\lvert \bar{x}-x \rvert =\lvert 2.89 - 3 \rvert=0.11 $$
$$ \frac{\lvert \bar{x}-x \rvert }{x}= \frac{0.11}{3} =0.036666666\dots$$



###### Condition Number
The condition number of a problem measures approximately 
1. the ratio between the relative change in the solution and the relative change in the input for a small change $\lvert \bar{x}-x \rvert$ 
, or 
2. the ratio between the relative forward error and the relative backward error: $$\frac{ \frac{\lvert y-\bar{y} \rvert}{\lvert y \rvert} }{ \frac{\lvert \bar{x}-x \rvert}{\lvert x \rvert } }$$
Using Taylor Expansions,
$$f(\bar{x}) = f(x) + (\bar{x}-x)f'(x) + \mathcal{O}((\bar{x}-x)^2)$$

- If condition number is large → ill conditioned.
- If condition number is small → well conditioned.

*For a problem $y=f(x)$, an algorithm is stable if its output $\bar{y} = \bar{f}(x)$ is the exact result of the problem for a slightly perturbed input parameter, $\bar{x}$.*

#### Next Lecture [[UBC/CPEN 4-2/CPSC 303/Lectures/Lecture 2|Lecture 2]]

