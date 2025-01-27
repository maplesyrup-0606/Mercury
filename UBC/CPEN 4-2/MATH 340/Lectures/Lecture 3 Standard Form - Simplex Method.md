ex) A line is convex
$$L= \left\{ \vec{x} \in \mathbb{R}^n \hspace{.05in} \vert \hspace{.05in} \vec{a} \cdot  \vec{x} = b \right\}$$
[Proof]
Pick any $\vec{x}_{1}, \vec{y}_{1}$ from $L$, namely, $\vec{a} \cdot  \vec{x}_{1} =b$ and $\vec{a} \cdot  \vec{y}_{1} =b$. Pick any point from the line segment between $\vec{x}_{1}, \vec{y}_{1}$, namely 
$$(1-t) \vec{x}_{1} + t\vec{y}_{1} = \vec{x}_{1} + t(\vec{y}_{1} -\vec{x}_{1}), t\in[0,1]$$

Now let’s plug it in,
$$\vec{a} \cdot ((1-t) \vec{x}_{1} + t \vec{y}_{1}) = \vec{a} \cdot ((1-t)\vec{x}_{1}) + \vec{a} \cdot  \vec{y}_{1} = (1-t) (\vec{a} \cdot  \vec{x}_{1}) + t(\vec{a} \cdot  \vec{y}_{1}) = (1-t)(b) + t(b) = b $$
$$\therefore (1-t) \vec{x}_{1} + t  \vec{y}_{1} \in L$$
Yay Convex!

#### Standard form of LP
==Inequality Form==
We have the objective function,
$$\text{maximize } c_{1}x_{1} + c_{2}x_{2}+ \cdots + c_{n}x_{n}$$
And $n + m$ constraints along with $n$ decision variables $x_{1},\cdots,x_{n}$,
$$\text{subject to } a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} \leq b_{1}$$
$$a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} \leq b_{2}$$
$$\vdots$$
$$a_{m1}x_{1} + a_{m2}x_{2} + \cdots + a_{mn}x_{n} \leq b_{m}$$
$$x_{1},x_{2},\cdots,x_{n} \geq 0$$

the bottom constraint is consisted of $n$ constraints.

###### Matrix Form
$$\vec{c} = \left( c_{1},c_{2},\cdots,c_{n} \right)  \in \mathbb{R}^n$$
$$\vec{x} = \left( x_{1},\cdots,x_{n} \right) \in \mathbb{R}^n$$
$$\vec{b} = \left( b_{1},\cdots,b_{m} \right) \in \mathbb{R}^m$$
$$A = \begin{bmatrix}
a_{11}  & a_{12} & \cdots & a_{1n}  \\
\vdots &  &  & \vdots \\
a_{m1} & \cdots &   & a_{mn}
\end{bmatrix}$$

If we try out $A \vec{x}$,
$$A \vec{x} = \begin{bmatrix}
a_{11}  & a_{12} & \cdots & a_{1n}  \\
\vdots &  &  & \vdots \\
a_{m1} & \cdots &   & a_{mn}
\end{bmatrix} \begin{bmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{bmatrix} = \begin{bmatrix}
a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} \\
\vdots \\
a_{m1}x_{1} + a_{m 2}x_{2} + \cdots + a_{mn}x_{n}
\end{bmatrix} \in \mathbb{R}^m$$
$$\vec{c} \cdot \vec{x} = \vec{c}^T \vec{x} = c_{1}x_{1}+\cdots+c_{n}x_{n}$$
If we represent this as a linear programming problem,
$$\text{maximize } \vec{c} \cdot \vec{x}$$
$$\text{subject to } A \vec{x} \leq \vec{b}$$
$$\vec{x} \geq \vec{0}$$
Here, $\vec{\alpha} \geq \vec{\beta}$ denotes $\alpha_{i} \geq \beta_{i}$ for $1 \leq i \leq n$.

###### Equality Form
==But how do we handle standard form LP?== → We need to modify it into equality form!
And this can be done by introducing slack variables.

$$x_{n+1} = b_{1} - (a_{11}x_{1} + a_{12}x_{2}  + \cdots + a_{1n}x_{n})$$
$$x_{n+2} = b_{2} - (a_{21}x_{1} + a_{22}x_{2}  + \cdots + a_{2n}x_{n})$$
$$\vdots$$
$$x_{n+m} = b_{m} - (a_{m1}x_{1} + a_{m2}x_{2}  + \cdots + a_{mn}x_{n})$$

For each $b_{k}$, associate the slack variable $x_{n+k}$,
$$x_{n+k}= b_{k} - (a_{k1}x_{1} + a_{k 2}x_{2} + \cdots + a_{kn}x_{n})$$
where $x_{n+k} \geq 0$.

Hence,
$$\text{maximize } c_{1}x_{1} + c_{2}x_{2} + \cdots+ c_{n}x_{n}$$
$$\text{subject to } a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1 n}x_{n} + x_{n+1} = b_{1}$$
$$a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2 n}x_{n} + x_{n+2} = b_{2}$$
$$\vdots$$
$$a_{m1}x_{1} + a_{m2}x_{2} + \cdots + a_{m n}x_{n} + x_{n+m} = b_{m}$$
$$x_{1},x_{2},\cdots, x_{n}, x_{n+1},x_{n+2},\cdots, x_{n+m} \geq 0$$


What is the benefit of the standard equality form?
- Inequality constraints are **only** in a very simple form! $$x_{i} \geq 0$$
- Inequality constraints are those that are hard to handle “algebraically”.

###### Standard Equality Form in Matrix Notation
$$\text{maximize } \vec{c'} \cdot  \vec{x'}$$
$$\text{subject to } A'\vec{x'} = \vec{b}$$
$$\vec{x'} \geq \vec{0}$$

where,
$$\vec{c'}= \begin{bmatrix}
c_{1} \\
c_{2} \\
\vdots \\
c_{n} \\
0 \\
\vdots \\
0
\end{bmatrix} \in \mathbb{R}^{n+m}, \vec{x'} = \begin{bmatrix}
x_{1}  \\
\vdots \\
x_{n} \\
x_{n+1} \\
\vdots \\
x_{n+m}
\end{bmatrix} \in \mathbb{R}^{n+m}, \vec{b}=\begin{bmatrix}
b_{1} \\
\vdots \\
b_{m}
\end{bmatrix} \in \mathbb{R}^m$$
$$A'=\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} & 1 &  &  \\
\vdots &  & \ddots &  &  & \ddots \\
a_{m1} & a_{m2} & \cdots & a_{mn} &  &  & 1
\end{bmatrix} \in \mathbb{R}^{m \times (n+m)}$$
[Fact]
For this matrix, we have
$$\text{dim} \left\{ \vec{x'} \in \mathbb{R}^{m +{n}} \hspace{.05in} \vert \hspace{.05in} A'\vec{x'} = \vec{b'} \right\} = (m + n) - m = n$$
It is $(m+n) - m$ since the dimension of $\mathbb{R}^{m+n}$ is $m+n$ and we have $m$ as the rank of $A’$ since $A'$ has $m$ linearly independent vectors.

- How do we visualize the feasible region? (In equality form?)
	- View inside the set $\left\{ \vec{x'} \hspace{.05in} \vert \hspace{.05in}  A'\vec{x'}=\vec{b} \right\}$
![[Screenshot 2025-01-26 at 1.43.03 AM.png]]

At a vertex, there meets $n$ linearly independent hyperplanes out of the $m+n$ hyper planes.
$$x_{1}=0,x_{2}=0,\cdots,x_{m+n}=0$$