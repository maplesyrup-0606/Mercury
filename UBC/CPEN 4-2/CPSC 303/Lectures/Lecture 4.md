What may go wrong with polynomial interpolation? We are still given a collection of **data samples** $\left\{ (x_{i},y_{i}) \right\}_{i=0}^n$.
- The error bound may not be small if $\frac{\lvert \lvert f^{(n+1)} \rvert \rvert}{(n+1)!}$ isn’t.
- High order polynomials tend to oscillate **a lot!**
- Data often suggest piecewise smoothness, whereas polynomials are infinitely differentiable everywhere.
- **No Locality:** changing any one data value may *drastically* alter the entire polynomial interpolant.

#### Piecewise Polynomial Interpolation
Divide given interval $[a,b]$ into subintervals
$$a=t_{0} <t_{1}<t_{2} < \cdots<t_{r }= b$$
where $t_{i}$ are “breakpoints” / “knots”.

We construct the interpolant,
$$v(x)=s_{i}(x), \quad t_{i} \leq x \leq t_{i+1}, \quad i= 0,\cdots,r-1$$
where each $s_i(x)$ is a polynomial of low degree.

We need $v(x)$ to satisfy the *global smoothness in addition to interpolation conditions*.

![[Screenshot 2025-01-31 at 12.15.01 PM.png]]

###### $t_{i}$ and $x_{k}$
We need to distinguish the abscissae $x_k$ and knots (break points),
$$a \leq x_{0} \leq x_{1} \leq \cdots \leq x_{n-1} \leq x_{n} \leq b$$
$$a = t_{0} < t_{1} < \cdots < t_{r-1} < t_{r} = b$$
and let’s set,
$$h= \text{max}_{1 \leq i \leq r}(t_{i} - t_{i-1})$$
We rely on $h$ being small, while $b-a$ doesn’t need to be.

#### Local Interpolants
- Local piecewise polynomial interpolants are simply constructed from local polynomial interpolation on each subinterval $[t_{i-1},t_{i}]$.
- *Some* global smoothness conditions are automatically satisfied.
	- **Though, we don’t really have control over how much global smoothness is easily achieved.**
- Interpolation error bounds are easily derived from polynomial interpolation.
- Interpolant is **only dependent on local data**.

###### Piecewise Linear Interpolation
Assuming $\left\{ x_{i} \right\}_{i=0}^n$ are distinct and ordered, identify $t_{i}=x_{i},y_{i}=f(x_{i})$.
Determine $s_{i}(x)$ as the straight line interpolant at $x_{i}$ and $x_{i+1}$,
$$v(x)= s_{i}(x)= f(x_{i} ) + f[x_{i},x_{i+1}](x-x_{i)})$$
$$=y_{i} + \frac{y_{i+1}-y_{i}}{x_{i+1}-x_{i}}(x-x_{i}),\quad x_{i}\leq x\leq x_{i+1},0\leq i \leq n-1 $$

Inherently, we have that $v(x)$ is continuous but not smoother than that.
- No new minima, and maxima are invented by $v(x)$ not shown in the data points $f(x)$.

[Error Analysis]
For linear polynomials: $m=1,t_{i}=x_{i}$, so for $x_{i-1}\leq x\leq x_{i}$,
$$\lvert f(x) - v(x) \rvert \leq \text{max}_{\xi \in [x_{i-1},x_{i}]} \frac{\lvert f''(\xi) \rvert }{2}\text{max}_{\zeta \in [x_{i-1},x_{i}] } \lvert (\zeta-x_{i-1})(\zeta-x_{i}) \rvert  $$
$$=\text{max}_{\xi \in [x_{i-1},x_{i}]} \frac{\lvert f''(\xi) \rvert }{2}\left\lvert  \frac{x_{i}-x_{i-1}}{2}  \right\rvert^2  $$

- Recall that $h= \text{max}_{1 \leq i \leq r}(t_{i} - t_{i-1})$. Then on the entire interval $[a,b]$,
$$\lvert \lvert f-v \rvert  \rvert _{\infty} \leq \frac{h^2}{8}\lvert \lvert f'' \rvert  \rvert _{\infty}$$

- The error is $O(h^2)$, if we have $n+1$ equi-distant data points, then $h= \frac{b-a}{n}$ and the error is $O\left( \frac{1}{n^2} \right)$.

###### Piecewise Cubic Interpolation
Let,
$$v(x) = s_{i}(x) = a_{i} + b_{i}(x-t_{i})+c_{i}(x-t_{i})^2 + d_{i}(x-t_{i})^3$$
$$t_{i} \leq x\leq t_{i+1},\quad i = 0,\cdots,r-1$$
- We have $4r$ coefficients in total : $4 \text{ (per polynomial)} \times r\text{ (total intervals)}$.
Out of the $4r$ coefficients, we have $2r$ used to satisfy interpolation of $f$ values.
- The other $2r$ are used either to interpolate more data or to require higher degrees of smoothness (even both).
- Interpolating also $f'(t_{i}), i=0,1,\cdots,r$ leads to a $C^1$-cubic, which is a local piecewise polynomial interpolant. We can also increase smoothness further to obtain a $C^2$-cubic.

###### Piecewise cubic Hermite Interpolation
It’s the cleanest piecewise cubic, assume that the values of $f'(t_{i})$ are also provided. Hence, $r = \frac{(n-1)}{2}$.
$$(x_{0},x_{1},\cdots,x_{n-1},x_{n}) = (t_{0},t_{0},t_{1},t_{1},\cdots,t_{r},t_{r})$$

And each cubic satisfies $s_i(x), \quad 0\le i \le r-1$, 
$$s_{i}(t_{i})=f(t_{i}), s_{i}(t_{i+1})=f(t_{i+1})$$
$$s_{i}'(t_{i})=f'(t_{i}), s_{i}'(t_{i+1})=f'(t_{i+1})$$

Since $n=3$ (it’s cubic duh),
$$\lvert f(x) - v(x) \rvert \leq \frac{h^4}{384}\text{max}_{a \leq \xi \leq b}\lvert f''''(\xi) \rvert  $$

$$\begin{aligned}
 g(x) &= (x-t_{i})^2(x-t_{i+1})^2  \\ 
 g'(x) &= 2(x-t_{i})(x - t_{i+1})^2 + 2(x-t_{i})^2(x-t_{i+1}) \\ 
 &= 2(x-t_{i})(x-t_{i+1})(2x - t_{i}-t_{i+1}) \\ 
 g\left(  \frac{t_{i} + t_{i+1}}{2}  \right)&=  \left(  \frac{t_{i}-t_{i+1}}{2}  \right)^4 \\ 
\left\lvert  \prod_{i} (s-t_{i}) \right\rvert  & \leq \frac{h^4}{16} \\
\lvert f(x)-v(x) \rvert &\leq \frac{h^4}{16} \cdot \frac{1}{4!} =  \frac{h^4}{384}
\end{aligned} $$
###### Cubic Spline Interpolation
We are now only given function values,
- $\left\{ x_{i},f(x_{i}) \right\}, x_{0}<x_{1}<\cdots<x_{n}$.
- Set $t_{i}=x_{i},r=n$ and use $2r$ conditions for $C^0$ interpolation.
- Use $2(r-1)$ additional coefficients to impose a global $C^2$ smoothness.
	- $r-1$ for each $f',f''$.
- We still have 2 left! → this is our choice to decide where to use.

**The two additional conditions**:
- Free boundary, natural spline $$v''(x_{0})=v''(x_{n})=0$$ has low accuracy of $O(h^2)$.
- Clamped boundary, complete spline$$v'(x_{0})=f'(x_{0}),\quad v'(x_{n})=f'(x_{n})$$
- *Not-a-knot*: Ensures continuity of 3rd derivative at $x_{1},x_{n-1}$.

###### Obtaining the Cubic Spline
- Form / solve tridiagonal system of size $n(\pm {1})$,
- Construction cost is still linear in $n$, but approximation is not entirely local. Still, much better than polynomial interpolation.


| Interpolant             | Local?    | Order | Smooth? | Selling features                         |
| ----------------------- | --------- | ----- | ------- | ---------------------------------------- |
| Piecewise consant       | Yes       | 1     | bounded | Accommodates discontinuous $f$           |
| Broken Line             | Yes       | 2     | $C^0$   | simple, max - min at data values         |
| Piecewise Cubic Hermite | Yes       | 4     | $C^1$   | Elegant / accurate                       |
| Spline (not-a-knot)     | not quite | 4     | $C^2$   | Accurate, smooth, requires only $f$ data |

Why is cubic spline not quite local? → It requires dependencies on each data point for left and right.
