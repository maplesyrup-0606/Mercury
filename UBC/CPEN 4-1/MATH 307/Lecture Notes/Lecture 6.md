### Example of condition numbers
Consider a parallel circuit with $N$ loops,
![[Pasted image 20240928180535.png]]

We have the following relationship between voltages, currents and resistors in the circuit giving the linear system of equations,
$$V = 2Ri_{1}-Ri_{2}$$
$$V = -Ri_{1}+2Ri_{2}-Ri_{3}$$
$$V=-Ri_{2}+2Ri_{3}-Ri_{4}$$
$$\vdots$$
$$V = -Ri_{N-1}+2Ri_{N}$$

We can write this system of equations as,
$$\begin{bmatrix}
2R  & -R &  &  &  &  \\
-R & 2R & -R &  &  &  \\
 & -R & 2R & -R &  &  \\
 &  &  & \ddots &  &  \\
 &  &  &  & -R & 2R & -R \\
 &  &  &  &  &  -R & 2R
\end{bmatrix}\begin{bmatrix}
i_{1}  \\
i_{2} \\
\vdots  \\
i_{N} 
\end{bmatrix}=\begin{bmatrix}
V \\
V \\
\vdots \\
V
\end{bmatrix}$$

$$\leftrightarrow A\mathbf{i}=\mathbf{b}$$

we are guaranteed that $V=12$ with an error margin of $\pm 0.1$. What is the relative error in the currents in terms of $\text{cond}(A_{0}),N$ where $A_{0}=\frac{1}{R}A$?

Let’s recall $A_{0}=\frac{1}{R}A$ and $\text{cond}(A_{0})=\text{cond}(A)$,
$$\text{cond}(A)=\lvert \lvert A \rvert  \rvert \lvert A^{-1} \rvert  \rvert $$
$$=\lvert \lvert RA_{0} \rvert  \rvert \left\lvert  \left\lvert  \frac{1}{R}(A_{0})^{-1}  \right\rvert   \right\rvert $$
$$=R \lvert \lvert A_{0} \rvert  \rvert \frac{1}{R}\lvert \lvert (A_{0})^{-1}\rvert  \rvert $$
$$= \lvert \lvert A_{0} \rvert  \rvert \lvert \lvert (A_{0})^{-1} \rvert  \rvert $$
$$=\text{cond}(A_{0})$$
Now,
$$\frac{\lvert \lvert \Delta \mathbf{i} \rvert  \rvert }{\lvert \lvert \mathbf{i} \rvert  \rvert } \leq \text{cond}(A) \frac{\lvert \lvert \Delta \mathbf{b} \rvert  \rvert }{\lvert \lvert \mathbf{b} \rvert  \rvert }$$

Now, let’s determine $\lvert \lvert \Delta \mathbf{b} \rvert \rvert$ and $\lvert \lvert \mathbf{b} \rvert \rvert$,
Since we are given that $V=12$, we have 
$$\mathbf{b}=\sqrt{ V^2 \cdot N}=V\sqrt{ N }=12\sqrt{ N }$$


$$\lvert \lvert \Delta \mathbf{b} \rvert  \rvert =\lvert \lvert \begin{bmatrix}
0.1 \\
0.1 \\
\vdots \\
0.1
\end{bmatrix} \rvert  \rvert =\sqrt{ N(0.1)^2 }=0.1\sqrt{ N }$$

As a result,
$$\frac{\lvert \lvert \Delta \mathbf{i} \rvert  \rvert }{\lvert \lvert \mathbf{i} \rvert  \rvert } \leq \text{cond}(A_{0}) \frac{0.1\sqrt{ N }}{12\sqrt{ N }}=\frac{1}{120}\text{cond}(A_{0})$$


#### Alternatives
If only the first battery had an error of $\pm 0.1$ and all the others are perfect, then we would have
$$\lvert \lvert \Delta \mathbf{b} \rvert  \rvert =\lvert \lvert \begin{bmatrix}
0.1 \\
0 \\
\vdots \\
0
\end{bmatrix} \rvert  \rvert =\sqrt{ 0.1^2 } = 0.1$$

Hence, making the upper bound
$$\frac{\lvert \lvert \Delta \mathbf{i} \rvert  \rvert }{\lvert \lvert \mathbf{i} \rvert  \rvert } \leq \text{cond}(A_{0}) \frac{0.1}{12\sqrt{ N }}=\frac{1}{120\sqrt{ N }}\text{cond}(A_{0})$$


### Examples of interpolation
Find a function $p(t)=c_{0}+c_{1}t+c_{2}t^2$ that interpolates $(-1,1),(0,1),(1,3)$. 

$$p(-1)=1 \leftrightarrow c_{0}-c_{1}+c_{2}=1$$
$$p(0)=1 \leftrightarrow c_{0}=1$$
$$p(1)=3 \leftrightarrow c_{0}+c_{1}+c_{2}=3$$

$$\begin{bmatrix}
1 & -1 & 1 \\
1 & 0 & 0 \\
1 & 1 & 1
\end{bmatrix}\begin{bmatrix}
c_{0} \\
c_{1} \\
c_{2}
\end{bmatrix}=\begin{bmatrix}
1 \\
1 \\
3 
\end{bmatrix}$$

Elimination on the augmented matrix gives,
$$\begin{bmatrix}
1 & -1 & 1 & \vert &  1  \\
0 & 1 & -1 & \vert & 0 \\
0 & 0 & 2 & \vert & 2
\end{bmatrix}$$

from which we get by elimination that $c_{2}=1,c_{1}=1,c_{0}=1$.
$$\therefore p(t) =1+t+t^2$$

## Cubic Spline Interpolation
Mathematically, we will define a cubic spline function $p(t)$ piecewise as
$$p(t) = 
\begin{array}{cc}
  \{ & 
    \begin{array}{cc}
      p_{1}(t) & t \in [t_{0},t_{1}]  \\
      p_{2}(t) & t \in [t_{1},t_{2}]  \\
\vdots \\
p_{N}(t) & t \in [t_{N-1},t_{N}]
    \end{array}
\end{array}
$$

Each piece is defined as
$$p_{k}(t)=a_{k}(t-t_{k-1})^3+b_{k}(t-t_{k-1})^2+c_{k}(t-t_{k-1})+ d_{k}$$
for $t \in [t_{k-1},t_{k}]$ where $k=1,\cdots,N$ such that $p(t),p’(t),p’’(t)$ are continuous and $p(t_i)=y_{i}$ for $i=0,\cdots,N$. 

The coefficient matrix of a cubic spline is,
$$C=\begin{bmatrix}
a_{1} & a_{2} & \cdots & a_{N} \\
b_{1} & b_{2} & \cdots & b_{N} \\
c_{1} & c_{2} & \cdots  & c_{N} \\
d_{1} & d_{2} & \cdots & d_{N}
\end{bmatrix}$$

The cubic spline as $4N$ unknowns and now we will find the equations which will determine the coefficients.

Given a set of data points $(t_{0},y_{0}),(t_{1},y_{1}),\cdots,(t_{N},y_{N})$, we want the cubic spline to fit the data points, which gives the requirement
$$p(t_{i}) = y_{i},\hspace{.1in}\forall i =0,1,\cdots,N$$

Let us find the equations to determine the coefficients,
![[Screenshot 2024-09-28 at 6.45.37 PM.png]]

**Left endpoints:**
We want $p_{k}(t_{k-1}) = y_{k-1}$ for $k=1,2,\cdots,N$.
When we plug in the definition of $p_{k}$, we get
$$d_{k}= y_{k-1}$$
for $k =1,2,\cdots,N$, which gives us $N$ equations.

**Right endpoints:**
We want $p_{k}(t_{k})=y_{k}$ for $k=1,2,\cdots,N$.
When we plug in the definition of $p_k$, we get
$$p_{k}(t_{k})=a_{k}(t_{k}-t_{k-1})^3+b_{k}(t_{k}-t_{k-1})^2+c_{k}(t_{k}-t_{k-1})+ d_{k} =y_{k}$$
for $k=1,2,\cdots,N$, which gives us $N$ equations.

**First derivatives at interior points $t_{1},t_{2},\cdots,t_{N-1}$:**
We need to satisfy $p'_{k}(t_{k})=p'_{k+1}(t_{k})$ for $k=1,2,\cdots,N-1$.

$$p'_{k}(t)=3a_{k}(t-t_{k-1})^2+2b_k(t-t_{k-1})+c_{k}$$
$$p'_{k+1}(t)=3a_{k+1}(t-t_{k})^2+2b_{k+1}(t-t_{k})+c_{k+1}$$

$$p'_{k}(t_{k})=3a_{k}(t_{k}-t_{k-1})^2+2b_{k}(t_{k}-t_{k-1})+c_{k}=3a_{k+1}(t_{k}-t_{k})^2+2b_{k+1}(t_{k}-t_{k})+c_{k+1}=p'_{k+1}(t_{k})$$

$$3a_{k}(t_{k}-t_{k-1})^2+2b_{k}(t_{k}-t_{k-1})+c_{k} = c_{k+1}$$

This is another $N-1$ equations.

**Second derivatives at interior points $t_{1},t_{2},\cdots,t_{N-1}$:**
We need to satisfy $p''_{k}(t_{k})=p''_{k+1}(t_{k})$ for $k=1,2,\cdots,N-1$.
$$p''_{k}(t)=6a_{k}(t-t_{k-1})+2b_k$$
$$p''_{k+1}(t)=6a_{k+1}(t-t_{k})+2b_{k+1}$$

$$p''_{k}(t_{k})=6a_{k}(t_{k}-t_{k-1})+2b_k = 6a_{k+1}(t_{k}-t_{k})+2b_{k+1}=p''_{k+1}(t_{k})$$

$$6a_{k}(t_{k}-t_{k-1})+2b_k = 2b_{k+1}$$

This is another $N-1$ equations.

Since we have so far $4N-2$ equations and $4N$ unknowns, we have different options to put more requirements on the cubic spline.

One such requirement is for obtaining *natural* cubic spline, which sets
$$p''_{1}(t_{0})=0 \text{ and }p''_{N}(t_N)=0,$$

which after plugging into the definitions of $p''_{k}$ gives,
$$b_{1}=0 \text{ and } 6a_{N}(t_{N}-t_{N-1})+2b_{N}=0$$

#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 7|Lecture 7]]
