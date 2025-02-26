##### Data Interpolation
We are given a collection of **data samples** $\left\{ (x_{i},y_{i}) \right\}_{i=0}^n$.
- The $\left\{ x_{i} \right\}_{i=0}^n$ are called the **abscissae**, the $\left\{ y_{i} \right\}_{i=0}^n$ are called the **data values**.
- Want to find a function $v(x)$ which can be used to estimate sampled function for $x \neq x_{i}$. 
	- We construct $v(x)$ such that $v(x_{i})=y_{i}$ for $i = 0, \cdots,n$.

###### Wish List
- We want a reasonable looking interpolant.
- If possible, $v$ should be inexpensive to construct.
- If possible, $v(x)$ should be inexpensive to evaluate for a given $x$.

###### Interpolating Functions
A function $f(x)$ may be given on an interval, $a \leq x \leq b$, explicitly or implicitly. Want interpolant $v(x)$ such that 
$$v(x_{i})=f(x_{i}),\quad i = 0,1,\cdots,n$$
at points $x_{i} \in [a,b]$.

**Formulation**:.
We consider (for now at least) a **linear** combination of linearly independent **basis functions** $\left\{ \phi_{j}(x) \right\}$.

$$v(x) = \sum_{j=0}^nc_{j}\phi_{j}(x)$$
where $c_j$ are the *interpolation coefficients* or *interpolation weights*.

Given that, the conditions yield a linear system,
$$\begin{bmatrix}
\phi_{0}(x_{0}) & \phi_{1}(x_{0}) & \cdots & \phi _{n}(x_{0}) \\
\vdots & \vdots  & \ddots & \vdots \\
\phi_{0}(x_{n)}) & \phi_{1}(x_{n}) & \cdots & \phi_{n}(x_{n})
\end{bmatrix}\begin{bmatrix}
c_{0} \\
c_{1} \\
\vdots \\
c_{n}
\end{bmatrix}=\begin{bmatrix}
y_{0} \\
y_{1} \\
\vdots \\
y_{n}
\end{bmatrix}$$

#### Monomial Basis
$$v(x)=p(x)=p_{n}(x)=\sum_{j=0}^n c_{j}\phi_{j}(x) $$
we choose
$$\phi_{j}(x)=x^j$$
thus,
$$v(x)=p(x)=p_{n}(x)=\sum_{j=0}^n c_{j}x^j$$

e.g.
$$\left\{ (x_{i},y_{i}) \right\} = \left\{ (2,14),(6,24),(4,25),(7,15) \right\} $$

In particular, let $n=3$,
$$\left\{ \phi_{j}(x) \right\}=\left\{ 1,x,x^2,x^3 \right\}$$
$$\to p(x) = c_{0}+c_{1}x+c_{2}x^2+c_{3}x^3$$

If we construct the linear system,
$$A= \begin{bmatrix}
1 & 2 & 4 & 8 \\
1 & 6 & 36 & 216 \\
1 & 4 & 16 & 64 \\
1 & 7 & 49 & 343
\end{bmatrix}, \quad \mathbf{y} = \begin{bmatrix}
14 \\
24 \\
25 \\
15
\end{bmatrix} $$

$$\therefore \mathbf{c} \approx \begin{bmatrix}
3.8000 \\
2.7667 \\
1.7000 \\
-0.2667
\end{bmatrix} $$

*However*:
- This matrix is a **Vandermonde** matrix: non-singular. → Unique polynomial.
- Construction cost is $O(n^3)$ flops.
- Evaluation cost using Horner’s rule is $O(n)$.
- Coefficients $c_j$ are not indicative of $f(x)$, and (possibly) all change if one data value is modified.
- Potential stability difficulties if:
	- degree is large.
	- abscissae spread apart.

#### Lagrange Basis
We here choose coefficients such that $c_{j}=y_{j}$.

$$\phi_{j}(x) = \frac{(x-x_{0})\cdots(x-x_{j-1})(x-x_{{j+1}})\cdots(x-x_{n})}{(x_{j}-x_{0})\cdots(x_{j}-x_{j-1})(x_{j}-x_{j+1})\cdots(x_{j}-x_{n})}= \prod_{i = 0, i\neq j}^n \frac{(x-x_{i})}{(x_{j}-x_{i})}$$
Then we have,
$$\phi_{j}(x_{i}) = \begin{cases}0 , i\neq j \\ 1, i=j\end{cases}
$$
so
$$p(x) = \sum_{j=0}^n y_{j} \phi_{j}(x)$$

e.g. 
Considering the data points,
$$\left\{ (2,14),(6,24),(4,25),(7,15) \right\}$$

We can compute the basis functions,
$$\phi_{0}(x) = 14\frac{(x-6)(x-4)(x-7)}{(2-6)(2-4)(2-7)} = 14 \frac{(x-6)(x-4)(x-7)}{(-4)(-2)(-5)} $$
$$\phi_{1}(x) = 24\frac{(x-2)(x-4)(x-7)}{(6-2)(6-4)(6-7)} = 24 \frac{(x-2)(x-4)(x-7)}{(+4)(+2)(-1)}$$
$$\phi_{2}(x) = 25 \frac{(x-2)(x-6)(x-7)}{(4-2)(4-6)(4-7)} = 25 \frac{ (x-2)(x-6)(x-7)}{(+2)(-2)(-3)}$$
$$\phi_{3}(x) = 15 \frac{ (x-2)(x-6)(x-4)}{(7-2)(7-6)(7-4)}=15 \frac{(x-2)(x-6)(x-4)}{(+5)(+1)(+3)}$$
By defining the denominators as $w_{i}$ and letting $\psi(x) =(x-2)(x-6)(x-4)(x-7)$,
$$p(x) = \psi(x) \left[ \frac{14w_{0}}{x-2} + \frac{24w_{1}}{x-6} + \frac{25w_{2}}{x-4} + \frac{15w_{3}}{x-7} \right]$$
$$ =\psi(x) \sum_{i=0}^3 \frac{y_{i}w_{i}}{(x-x_{i})}$$

[Assessment]
- Not as simple as monomial basis.
- Matrix is identity $I$.
- Construction costs is $O(n^2)$ flops (OK even if $n$ large).
- Evaluation cost is $O(n)$ flops (sort of low).
- Coefficients $c_j$ indicative of data and useful for function manipulation such as integration / differentiation.
- Stable even if degree is large or abscissae spread apart.

#### Newton basis and divided differences
From previous methods, if we added a new data points, we would have to change the whole interpolant. We don’t want that 😥,
- Need $n \to n+ 1$, easy construction / evaluation.
- To this end require,
	- New basis function can’t disturb prior interpolation. $$\phi_{j}(x_{i})=0, i<j$$
	- Old basis function does not need information about new data values:$$\phi_{j}(x) \text{ is independent of } (x_{i},y_{i})\text{ for } i>j.$$
- Newton basis functions,$$\phi_{j}(x) = \prod_{i=0}^{j-1}(x-x_{i}), \quad j=0,1,\cdots,n$$
- The matrix tends to be a lower triangular matrix.

Again for the dataset,
$$\left\{ (x_{i},y_{i}) \right\} = \left\{ (2,14),(6,24),(4,25),(7,15) \right\} $$
- Basis functions
$$\phi_{0}(x) = 1, \phi_{1}(x)=(x-2)$$
$$\phi_{2}(x)=(x-2)(x-6),\phi_{3}(x)=(x-2)(x-6)(x-4)$$

- Linear System
$$\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 4 & 0 & 0 \\
1 & 2 & -4 & 0 \\
1 & 5 & 5 & -15
\end{bmatrix}$$

And we can solve for the linear system $A\mathbf{c}=\mathbf{y}$.

##### Divided Differences
This powerful method is an alternative of finding the coefficients.
- Easier to add and delete data points.
- Provides a tool for analyzing interpolation error.
- Defined recursively,$$f[x_{i}]=y_{i},\quad f[x_{i}, \cdots, x_{j}] = \frac{f[x_{i+1},\cdots,x_{j}] - f[x_{i}, \cdots, x_{j-1}]}{x_{j} - x_{i}}$$
- Coefficients are just the diagonal  $c_{j} = f[x_{0},\cdots,x_{j}]$.
- To add another data point ($n\to n+1$), add another row.

![[Screenshot 2025-01-30 at 9.36.38 PM.png]]
And $c_{j} = f[x_{0},\cdots ,x_{j}], j=0,1,\cdots,n$.

Hence, the interpolating polynomial is
$$p_{n}(x) = \sum_{j=0}^n f[x_{0},x_{1},\cdots,x_{j}] (x-x_{0})(x-x_{1}) \cdots (x-x_{j-1})$$

#### Interpolation Error
Assume that $f$ is the function to be interpolated and $y_{i}= f(x_{i}), i =0,1,2,\cdots,n$. Denote the interpolant by $p_n(x)$. For any $x$ we want to estimate the error
$$e_{n}(x) = f(x)-p_{n}(x)$$

Let’s fix $x \notin \left\{ x_{i} \right\}_{i=0}^n$ and assume were adding a new point $(x,f(x))$. Using the properties of the newtonian basis,
$$e_{n}(x) = f(x) - p_{n}(x)=p_{n+1}(x) - p_{n}(x)$$
where
$$p_{n+1}(x) = p_{n}(x) + f[x_{0},\cdots,x]\prod_{j=0}^n (x-x_{j})$$
thus,
$$\therefore e_{n}(x) = f[x_{0},x_{1},\cdots,x]\psi(x)$$

###### Error estimations / bounds
Let $a= \text{min}_{i}x_{i},b=\text{max}_{i}x_{i}$ and assume $x \in [a,b]$ ←> otherwise we’d be extrapolating.

For $e_n(x)$, it has $n+1$ roots. 
$$e_{n}(x_{0}) =e_{n}(x_{1})=\cdots=e_{n}(x_{n})=0$$
According to Role’s theorem, for $\xi_{i} \in (x_{i},x_{i+1}) \quad i=0,\cdots,n-1$, we have that
$$e_{n}'(\xi_{i}) = 0$$
and we have $n$ roots now.

Recursively following the process,
$$e_{n}^{(n)}(x) \to 1 \text{ root}$$
$$e_{n}^{(n+1)}(\xi) = f^{(n+1)}(\xi) - p_{n}^{(n+1)}(\xi) =f^{(n+1)}(\xi) = f[x_{0},x_{1},\cdots,x_{n},x](n+1)!$$
$$\therefore f[x_{0},x_{1},\cdots,x,x_{n}] = \frac{f^{(n+1)}(\xi)}{(n+1)!}$$
and such $\exists \xi \in [a,b]$.

If we were to find the upper bounds,
$$\lvert e_{n}(x) \rvert \leq \text{max}_{{t \in [a,b]}} \frac{\lvert f^{(n+1)}(t) \rvert }{(n+1)!} \text{max}_{s \in[a,b]}\left\lvert  \prod_{j=0}^n (s-x_{j})  \right\rvert = \frac{\lvert \lvert f^{(n+1)} \rvert  \rvert_{\infty} }{(n+1)!}\lvert \lvert \psi \rvert  \rvert _{\infty}  $$
$$\lvert \lvert e_{n} \rvert  \rvert_{\infty} \leq \frac{\lvert \lvert f^{(n+1)} \rvert  \rvert_{\infty} }{(n+1)!}(b-a)^{n+1} $$

e.g.
Let’s consider
$$\left\{ (x_{0},y_{0}),(x_{1},y_{1}) \right\}$$
We have $n=1 \to n+1 = 2$,
$$\lvert \lvert e_{n} \rvert  \rvert  \leq \frac{1}{2}\lvert \lvert f'' \rvert  \rvert \cdot \text{max}_{s} \lvert (s-x_{0})(s-x_{1}) \rvert  $$
$$\lvert \lvert (s-x_{0})(s-x_{1}) \rvert  \rvert = \lvert \lvert s^2-(x_{0}+x_{1})s +x_{0}x_{1} \rvert  \rvert  $$
$$\text{max: } x= \frac{x_{0}+x_{1}}{2}$$
$$ \implies \text{max}_{s} \lvert (s-x_{0})(s-x_{1}) \rvert  = \frac{1}{4}(x_{1}-x_{0})^2 $$
$$\therefore \lvert \lvert e_{n} \rvert  \rvert \leq \frac{1}{8} (x_{1}-x_{0})^2\lvert \lvert f'' \rvert  \rvert $$

**How can we possibly bound the error potentially smaller?**
1. Can we change the order of $x_{0},x_{1},\cdots,x_{n}$?
No, changing the permutation does not cause any difference.

2. Not use $\lvert \lvert f^{(n+1)} \rvert \rvert_{\infty}$ to bound $f^{(n+1)}(x)$ over $[a,b]$?
No, my opinion is that we need to use the maximum of $f^{(n+1)}$ and bound the maximum error.
What other things do we know? Do we know lower degree derivatives that perhaps help represent the error bound?

3. Choose different $\left\{ x_{i} \right\}$ so $\text{max}_{s \in [a,b]} \left\lvert  \prod_{j=0}^n (s -x_{j}) \right\rvert$ is smaller.
Yes, this is realistically possible. If we properly choose $x_{i}$ we can reduce the maximum.

4. Make $f(x)$ smoother and with more continuous derivatives.
No, more derivatives does not help necessarily. We can have smooth yet very high bounded derivatives.

#### Chebyshev Interpolation
Can we minimize the error bound?

$$\text{max}_{{t \in [a,b]}} \frac{\lvert f^{(n+1)}(t) \rvert }{(n+1)!} \text{max}_{s \in[a,b]}\left\lvert  \prod_{j=0}^n (s-x_{j})  \right\rvert$$

Let’s assume that we can evaluate $f(x)$ at *any* $n+1$ points $x_{i}$. 
Knowing **nothing more** about the interpolated function $f(x)$, choose the abscissae $x_i$ attempting to minimize,
$$\text{max}_{s \in[a,b]}\left\lvert  \prod_{j=0}^n (s-x_{j})  \right\rvert$$
→ This leads to **chebyshev points**: for instance, over $a=-1,b=1$ they are
$$x_{i} = \cos\left(  \frac{2i+1}{2(n+1)}\pi \right),\quad i=0,\cdots,n$$

###### Chebyshev Points
These points solve the **min-max** problem
$$\beta = \text{min}_{x_{0},x_{1},\cdots,x_{n}} \text{max}_{-1\leq x\leq 1} \lvert (x-x_{0})(x-x_{1})\cdots(x-x_{n}) \rvert $$
yielding the value
$$\beta = 2^{-n}$$

Hence,
$$\text{max}_{-1 \leq x \leq 1}\lvert f(x) - p_{n}(x) \rvert \leq \frac{1}{2^n(n+1)!}\text{max}_{-1 \leq t\leq 1} \lvert f^{(n+1)}(t) \rvert  $$
For a general interval $[a,b]$, scale and translate $[-1,1]$ onto $[a,b]$
$$x = a + \frac{b-a}{2}(t+1), \quad t \in [-1,1]$$
$$x_{i} \leftarrow a + \frac{b-a}{2}(x_{i} + 1),\quad i=0,\cdots,n$$

For instance, for $f(x) = \frac{1}{1+25x^2}$,
```functionplot
---
title: n=4.9
xLabel: x
yLabel: y
bounds: [-1,1,-0.5,0.5]
disableZoom: false
grid: true
---
f(x) = 1/(1+25x^2)

```
![[Screenshot 2025-01-31 at 11.29.29 AM.png]]

As $n$ increases,
![[Screenshot 2025-01-31 at 11.29.38 AM.png]]

###### Side Notes
In order to realize the insane accuracy of chebyshev polynomial interpolation, we require that $f$,
- is very smooth → many bounded derivatives.
- can be evaluated practically everywhere.

Because of the high polynomial degree, use the **Lagrange** basis.
Chebyshev is mostly used for function manipulation (solving differential equations with smooth coefficients).
Not every application requires an extremely accurate interpolant.

#### Interpolating Derivative Values
E.g. The quadratic interpolant for  
$$f(0)=1.5,f'(0)=1,f(20)=0$$
Hence,
$$\left\{ (x_{i},y_{i}) \right\} = \left\{ (0,1.5)(0,1)(20,0) \right\}$$

If we use a monomial basis,
$$p(x)=c_{0}+c_{1}x+c_{2}x^2$$
$$p(0) = c_{0}=1.5$$
$$p'(0) = c_{1}=1$$
$$p(20)=c_{0}+20c_{1}+400c_{2} = 0 \to c_{2}=-\frac{21.5}{400}$$

##### Hermite Cubic
Consider,
$$\left\{ (x_{i},y_{i}) \right\}= \left\{ (t_{0},f(t_{0})),(t_{0},f'(t_{0})),(t_{1},f(t_{1})),(t_{1},f'(t_{1})) \right\}$$

If we use the simplest basis, the monomial basis $p(x)=c_{0}+c_{1}x+c_{2}x^2+c_{3}x^3$, we can form the linear system,
$$\begin{bmatrix}
1 & t_{0} & t_{0}^2 & t_{0}^3 \\
1 & t_{1} & t_{1}^2 & t_{1}^3 \\
0 & 1 &  2t_{0} & 3t_{0}^2 \\
0 & 1 & 2t_{1} & 3t_{1}^2
\end{bmatrix}\begin{bmatrix}
c_{0} \\
c_{1} \\
c_{2} \\
c_{3}
\end{bmatrix} =\begin{bmatrix}
f(t_{0}) \\
f(t_{1}) \\
f'(t_{0}) \\
f'(t_{1})
\end{bmatrix}$$

##### General Algorithm: Newton form with divided differences
First, note the following,
$$\gamma_{j,l}= f[x_{j-l},x_{j-l+1},\cdots,x_{j}] \quad 0\leq l\leq j\leq n$$
Hence, each diagonal entrance $c_{j}$ will be in the form $\gamma_{j,j} = f[x_{0},\cdots,x_{j}]$.

1. **Construction**
Given data $\left\{ (x_{i},y_{i}) \right\}_{i=0}^n$, where the abscissae are not necessarily distinct (for instance, derivatives).

```
for j = 0,1,...,n
	for l = 0,1,...j
		compute gamma[j,l]
```
Where $\gamma_{j,l}$ is
$$\gamma_{j,l} = \begin{cases}
\frac{\gamma_{j,l-1} -\gamma_{j-1,l-1}}{x_{j} - x_{j-l}} \quad \text{ if }x_{j} \neq x_{j-l} \\ \frac{f^{(l)}(x_{j})}{l!} \quad \text{otherwise}
\end{cases}$$

2. **Evaluation**
Given an evaluation point $x$,
$$p =\gamma_{n,n}$$
$$\text{for }j = n-1,n-2,\cdots,0: p = p(x-x_{j}) +\gamma_{j,j}$$


E.g.

| $t_i$ | $f(t_i)$  | $f’(t_i)$ | $f''(t_{i})$ |
| ----- | --------- | --------- | ------------ |
| 8.3   | 17.564921 | 3.116256  | 0.120482     |
| 8.6   | 18.505155 | 3.151762  |              |
$$(x_{0},x_{1},x_{2},x_{3},x_{4}) = (\underbrace{ 8.3,8.3,8.3 }_{ m_{0}=2 },\underbrace{ 8.6,8.6 }_{ m_{1}=1 })$$
![[Screenshot 2025-01-31 at 12.02.17 PM.png]]

#### Next Lecture [[UBC/CPEN 4-2/CPSC 303/Lectures/Lecture 4|Lecture 4]]
