
#### Definition of least squares approximation
Suppose $A \in \mathbb{R}^{m\times n}$ and $\text{rank}(A)=n$. Let $b \in \mathbb{R}^m$ has either a unique solution or no solution. What do we do?

The least squares approximation of $Ax=b$ is $x \in \mathbb{R}^n$ which minimizes $\lvert \lvert Ax-b \rvert \rvert$ or equivalently, one that minimizes $\lvert \lvert Ax-b \rvert \rvert^2$.

#### Theorem
The least squares approximation is the solution to
$$A^TAx=A^Tb$$

[Proof]
For any $x \in \mathbb{R}^n$, we have that $Ax \in R(A)$ by definition of range. So we want $b$ to be as close as possible to $R(A)$. 
We know that $\lvert \lvert Ax-b \rvert \rvert=0$, that is minimum if $b \in R(A)$. If this is not possible, it is minimum when $Ax=\text{proj}_{R(A)}(b)$:
$$b-Ax = b - \text{proj}_{R(A)}(b) \in R(A)^\perp = N(A^T) \iff A^T(b-Ax)=0 \iff A^TAx=A^Tb$$
Since $\text{cond}(A^TA)=\text{cond}(A)^2$, bad condition numbers are amplified.

#### Theorem
Let $A=QR=Q_{1}R_{1}$. The least squares approximation is the solution of 
$$R_{1}x=Q_{1}^Tb$$

[Proof]
Note how
$$\lvert \lvert Ax-b \rvert  \rvert =\lvert \lvert QRx-b \rvert  \rvert =\lvert \lvert Q(Rx-Q^Tb) \rvert  \rvert=\lvert \lvert Rx-Q^Tb \rvert  \rvert  $$
by $QQ^T=I$ and $\lvert \lvert Qv \rvert \rvert=v$ for ant $v$.

Consequently, we have
$$\lvert \lvert Rx-Q^Tb \rvert  \rvert =\lvert \lvert \begin{bmatrix}
R_{1}x-Q_{1}^Tb \\
-Q_{2}^Tb
\end{bmatrix} \rvert  \rvert $$
Hence, this shows us that $\lvert \lvert Ax-b \rvert \rvert$ is minimum when $R_{1}x=Q_{1}^Tb$ because the other term in the norm is independent of $x$. As a result, we need to solve this system. 

Recall that $R_{1}\in \mathbb{R}^{n\times n}$ and upper triangle with rank $n$, giving us a unique solution for $x$.

#### Fitting models to data
Consider $N+1$ data points $(t_{0},y_{0}),(t_{1},y_{1}),\cdots,(t_{N},y_{N})$. Choose a model
$$f(t)=c_{0}f_{0}(t)+c_{1}f_{1}(t)+\cdots+c_{d}f_{d}(t)$$

We have that $f_{0},f_{1},\cdots,f_{d}$ are known functions and $c_{0},c_{1},\cdots,c_{d}$ are unknown coefficients. We wish to find $c_{0},c_{1},\cdots,c_{d}$ that best fits the data in terms of smallest “sum of squared errors (SSE)”.

$$SSE=\sum_{k=0}^N (y_{k}-f(t_{k}))^2$$
$$=\left\lvert \left\lvert \begin{bmatrix}
y_{0}-f(t_{0}) \\
y_{1}-f(t_{1}) \\
\vdots \\
y_{N}-f(t_{N})
\end{bmatrix} \right\rvert  \right\rvert^2 $$
$$=\left\lvert \left\lvert \begin{bmatrix}
y_{0} - [c_{0}f_{0}(t_{0})+c_{1}f_{1}(t_{0}) + \cdots+c_{d}f_{d}(t_{0})] \\
y_{1} - [c_{0}f_{0}(t_{1})+c_{1}f_{1}(t_{1}) + \cdots+c_{d}f_{d}(t_{1})] \\
\vdots \\
y_{N} - [c_{0}f_{0}(t_{N})+c_{1}f_{1}(t_{N}) + \cdots+c_{d}f_{d}(t_{N})] 
\end{bmatrix} \right\rvert  \right\rvert^2$$
$$=\left\lvert \left\lvert \begin{bmatrix}
y_{0} \\
y_{1} \\
\vdots \\
y_{N}
\end{bmatrix} - \begin{bmatrix}
f_{0}(t_{0}) & f_{1}(t_{0}) & \cdots & f_{d}(t_{0}) \\
f_{0}(t_{1}) & f_{1}(t_{1}) & \cdots & f_{d}(t_{1}) \\
\vdots \\
f_{0}(t_{N}) & f_{1}(t_{N}) & \cdots & f_{d}(t_{N)})
\end{bmatrix}\begin{bmatrix}
c_{0} \\
c_{1} \\
\vdots \\
c_{d}
\end{bmatrix} \right\rvert  \right\rvert^2 $$

###### Example
Find the function of the form $f(t)=c_{0}+c_{1}t$ which best fits the data points 
$$(-1,1),\hspace{.2in} (0,2),\hspace{.2in}(1,4)$$
using the least squares approximation.

$$f_{0}=1,\hspace{.2in}f_{1}=t$$
$$SSE=\left\lvert \left\lvert \begin{bmatrix}
1 \\
2 \\
4
\end{bmatrix} - \begin{bmatrix}
1 & -1 \\
1 & 0 \\
1 & 1
\end{bmatrix}\begin{bmatrix}
c_{0} \\
c_{1}
\end{bmatrix} \right\rvert  \right\rvert^2 $$
$$=\left\lvert \left\lvert \begin{bmatrix}
1-c_{0}+c_{1} \\
2-c_{0} \\
4-c_{0}-c_{1}
\end{bmatrix}\right\rvert  \right\rvert^2$$

Let’s try using QR decomposition, in this case we have $A,b$ being
$$A=\begin{bmatrix}
1 & -1 \\
1 & 0 \\
1 & 1
\end{bmatrix}, \hspace{.1in}b=\begin{bmatrix}
1 \\
2 \\
4
\end{bmatrix}$$

Then we can use the solution to $A^TAx=A^Tb$,
$$\begin{bmatrix}
1 & 1 & 1 \\
-1 & 0 & 1
\end{bmatrix}\begin{bmatrix}
1 & -1 \\
1 & 0 \\
1 & 1
\end{bmatrix}x=\begin{bmatrix}
1 & 1 & 1 \\
-1 & 0 & 1
\end{bmatrix}\begin{bmatrix}
1 \\
2 \\
4 \\
\end{bmatrix}$$
$$\to \begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}x=\begin{bmatrix}
7 \\
3
\end{bmatrix}$$
$$\therefore x=\begin{bmatrix}
\frac{7}{3} \\
\frac{3}{2}
\end{bmatrix} \to f(t)=\frac{7}{3}+\frac{3}{2}t$$
==Of course, this is quite off.==

#### Next Lecture [[Lecture 19]]

