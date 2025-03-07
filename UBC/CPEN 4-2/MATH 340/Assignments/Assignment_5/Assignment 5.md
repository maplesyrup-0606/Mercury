#### Question 1
Let’s consider the following dictionary for some LP problem,
$$\begin{aligned}
z &= 1+ x_{1}-x_{2} \\ 
x_{3} &= -2x_{1}-x_{2}\\ 
&x_{1},x_{2},x_{3} \geq 0
\end{aligned}$$

First, let’s look at the basic solution which is $(x_{1},x_{2},x_{3}) = (0,0,0)$. And $z=1$, in this situation.

Now, let’s pivot. We can choose the entering variable $x_1$, and the leaving variable would then be $x_3$.

$$\begin{aligned}
x_{3}=-2x_{1}-x_{2} &\to x_{1} = -\frac{1}{2}x_{2} -\frac{1}{2}x_{3} \\ 
z=1+x_{1}-x_{2} &\to z= 1 - \frac{3}{2}x_{2}-\frac{1}{2}x_{3}
\end{aligned}$$

Making the new dictionary,
$$\begin{aligned}
z&=1-\frac{3}{2}x_{2}-\frac{1}{2}x_{3} \\ 
x_{1}&=-\frac{1}{2}x_{2}-\frac{1}{2}x_{3}
\end{aligned}$$

Since all coefficients are negative in the objective function, we can conclude that the optimal solution is $(x_{1},x_{2},x_{3}) = (0,0,0)$ with the optimal value $z=1$. 

This is in fact the identical optimal solution and optimal value as we showed it above. And this happens because we have a degenerate dictionary at the optimal point, hence it cycles around the optimal point.

#### Question 2
##### (a)
We have six distinct ways to cut the rubber, 
$$\begin{aligned}
\left\{ 70,90 \right\} &\to \text{Waste: }40 \\ 
\left\{ 50,50,70 \right\} &\to \text{Waste: }30 \\
\left\{ 90,90 \right\} &\to \text{Waste: }20 \\ 
\left\{ 50,50,90 \right\} &\to \text{Waste: }10 \\ 
\left\{ 50,70,70 \right\} &\to \text{Waste: }10 \\ 
\left\{ 50,50,50,50 \right\} &\to \text{Waste: }0 
\end{aligned}$$

##### (b)
Starting from the method from the above, and excluding the last one, we can set them to variables $y_{1},y_{2},y_{3},y_{4},y_{5}$. 

Since we want to minimize waste while producing enough items, we can set the Lp Problem as the following,
$$\begin{aligned}
\text{Minimize } &40y_{1}+30y_{2}+20y_{3}+10y_{4}+10y_{5} \\ 
\text{subject to }&y_{1}+2y_{3}+y_{4} \geq 300 \\ 
&y_{1}+y_{2}+2y_{5} \geq 400 \\ 
& 2y_{2} + 2y_{4} + y_{5} \geq 1000 \\ 
& y_{1},y_{2},y_{3},y_{4},y_{5} \geq 0
\end{aligned}$$

##### (c) 
![[Pasted image 20250228151921.png]]
![[Pasted image 20250228151926.png]]
![[Pasted image 20250228151942.png]]
![[Pasted image 20250228151958.png]]
![[Pasted image 20250228152004.png]]
##### (d)
When the primal problem is in form,
$$\begin{aligned}
\text{minimize } & \vec{b}^T \vec{y}\\ 
\text{subject to } &A^T \vec{y} \geq \vec{c} \\ 
& \vec{y} \geq \vec{0}
\end{aligned}$$
the dual problem is in the form,
$$\begin{aligned}
\text{maximize } & \vec{c} \cdot  \vec{x} \\ 
\text{subject to } &A \vec{x}\leq \vec{b} \\
& \vec{x} \geq \vec{0}
\end{aligned}$$

We know that,
$$\begin{aligned}
\vec{b} &= \begin{bmatrix}
40 \\
30 \\
20 \\
10 \\
10 
\end{bmatrix} \\ 
\vec{c} &= \begin{bmatrix}
300 \\
400 \\
1000
\end{bmatrix} \\
A &= \begin{bmatrix}
1 & 1 & 0  \\
0 & 1 & 2 \\
2 & 0 & 0 \\
1 & 0 &2  \\
0 & 2 & 1
\end{bmatrix} \\
\vec{x}&= \begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix}
\end{aligned}$$
Thus, the dual problem is
$$\begin{aligned}
\text{maximize } &300x_{1}+400x_{2}+1000x_{3} \\ 
\text{subject to }&x_{1}+x_{2} \leq 40 \\
&x_{2}+2x_{3} \leq 30 \\
&2x_{1} \leq 20 \\ 
&x_{1}+2x_{3} \leq 10 \\ 
& 2x_{2}+x_{3} \leq 10 \\
&x_{1},x_{2},x_{3} \geq 0
\end{aligned}$$



And we can see that the primal and the dual Lp problems have the same optimal objective value of 5000.

![[Pasted image 20250228152213.png]]![[Pasted image 20250228152239.png]]
![[Pasted image 20250228152252.png]]
![[Pasted image 20250228152304.png]]
![[Pasted image 20250228152311.png]]

#### Question 3
Let’s consider the linear programming problem,
$$\begin{aligned}
\text{maximize } &x_{1} \\
\text{subject to } & -x_{1}+x_{2} \geq 1\\
& -x_{1}+x_{2} \leq -1 \\ 
&x_{1},x_{2} \geq 0
\end{aligned}$$

Let’s find the feasibility of the linear programming problem by drawing out the feasibility regions,
![[Pasted image 20250227162928.png]]

We can see that there is no overlap, hence it is infeasible.

Now, let’s construct the dual problem, let’s start out with writing $\vec{c}, \vec{b}, A$,
$$\begin{aligned}
&\vec{c} = \begin{bmatrix}
1 \\
0
\end{bmatrix}\\
& \vec{b} = \begin{bmatrix}
-1 \\
-1
\end{bmatrix} \\ 
A &= \begin{bmatrix}
1 & -1 \\
-1 & 1
\end{bmatrix}
\end{aligned}$$

And this is because in standard form the first condition is $x_{1}-x_{2} \leq -1$.

Then the dual problem which has the following form, where $\vec{y} = \begin{bmatrix}y_{1} \\ y_{2} \end{bmatrix}$,
$$\begin{aligned}
\text{minimize } & \vec{b}^T \vec{y}\\ 
\text{subject to } &A^T \vec{y} \geq \vec{c} \\ 
& \vec{y} \geq \vec{0}
\end{aligned}$$
will be the following,
$$\begin{aligned}
\text{minimize } & -y_{1}-y_{2} \\ 
\text{subject to } &y_{1} -y_{2} \geq 1 \\
& -y_{1} + y_{2} \geq 0 \\ 
&y_{1},y_{2} \geq 0
\end{aligned}$$

If we were to draw the feasibility region out again for the dual problem, we get
,![[Pasted image 20250227163820.png]]
Once again, we can see no overlap hence it’s also infeasible.

Therefore, this example shows both the Primal and Dual LP’s are infeasible.

#### Question 4
Let’s start by annotating the given variables in vector / matrix form.
$$\begin{aligned}
A &=\begin{bmatrix}
a_{11} & a_{12}  & \cdots & a_{1n} \\
a_{21} & a_{21} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots  \\
a_{m 1} & a_{m 2} & \cdots & a_{mn}
\end{bmatrix} \in \mathbb{R}^{m \times n} \\ 
\vec{c} &= \begin{bmatrix}
c_{1} \\
c_{2} \\
\vdots \\
c_{m}
\end{bmatrix} \in \mathbb{R}^m \\
\vec{w} &= \begin{bmatrix}
w_{1} \\
w_{2} \\
\vdots \\
w_{n}
\end{bmatrix} \in \mathbb{R}^n \\ 
\vec{x}&= \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix} \in \mathbb{R}^n \\ 
\vec{y} &= \begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots \\
y_{m}
\end{bmatrix} \in \mathbb{R}^m
\end{aligned}$$
Then we can represent the sum,
$$\text{max}_{x_{1},\cdots,x_{n} \in \mathbb{R}}\left[ \sum_{i=1}^m y_{i} \left[ \sum_{k=1}^n a_{ik}x_{k} +c_{i} \right] + \sum_{j=1}^n w_{j}x_{j} \right]$$
into
$$\begin{aligned}
\text{max }_{x_{1},\cdots,x_{n}\in \mathbb{R}}\left[\vec{y}^T (A \vec{x} +\vec{c}) + \vec{w}^T \vec{x} \right] &= \text{max }_{x_{1},\cdots,x_{n}\in \mathbb{R}}\left[\vec{y}^T \vec{c} + \vec{y}^TA \vec{x} + \vec{w}^T \vec{x} \right] \\ 
&= \text{max }_{x_{1},\cdots,x_{n}\in \mathbb{R}} \left[ \vec{y}^T \vec{c} + (A^T \vec{y} + \vec{w})^T \vec{x} \right] \\ 
&= \vec{y}^T \vec{c} + \text{max }_{x_{1},\cdots,x_{n}\in \mathbb{R}} \left[ (A^T \vec{y} + \vec{w})^T \vec{x} \right]
\end{aligned} $$

we only then have to consider when $(A^T \vec{y} +  \vec{w}) = \vec{0}$ since that would be the only case where the sum doesn’t diverge to $\infty$.

Thus,
$$\text{max }_{x_{1},\cdots,x_{n}\in \mathbb{R}}\left[\vec{y}^T (A \vec{x} +\vec{c}) + \vec{w}^T \vec{x} \right] = \begin{cases}
\vec{y}^T \vec{c} \quad &\text{if }A^T \vec{y}+ \vec{w} = \vec{0} \\
+\infty &\text{otherwise} 
\end{cases}$$

#### Question 5
##### (a)
$$\begin{aligned}
F(\vec{y}) &= \text{max}_{\vec{x} \in \mathbb{R}^n, \vec{x} \geq \vec{0}} \left[ \vec{y}\cdot  \vec{x} + \vec{c} \cdot  \vec{x} \right] \\ 
&= \text{max}_{\vec{x} \in \mathbb{R}^n, \vec{x} \geq \vec{0}} \left[ (\vec{y} + \vec{c}) \cdot  \vec{x} \right] 
\end{aligned}$$
In general, if $\vec{x} \in \mathbb{R}^n$ without $\vec{x} \geq \vec{0}$, we would only seek the case where $\vec{y} + \vec{c} = \vec{0}$ to have a maximum of $0$, however since $\vec{x} \geq \vec{0}$ we can let $\vec{y} + \vec{c} \leq \vec{0}$. This is because when $\vec{y} + \vec{c} < \vec{0}$, the maximum is limited to $\vec{0}$ if we have the constraint $\vec{x} \geq \vec{0}$. 

Thus,
$$F(\vec{y}) = \text{max}_{\vec{x} \in \mathbb{R}^n, \vec{x} \geq \vec{0}} \left[ \vec{y}\cdot  \vec{x} + \vec{c} \cdot  \vec{x} \right] = \begin{cases}
0 \quad &\text{if } \vec{y}+\vec{c} \leq \vec{0} \\
\infty &\text{otherwise}
\end{cases}$$
##### (b)
From (a), we showed that $F(\vec{y})$ is 0 when $\vec{y} +\vec{c} \leq \vec{0}$, otherwise $\infty$. Then, for the LP problem 
$$\text{Minimize } F(\vec{y})$$
we can see that the optimal value we need to find is ${0}$. 

In order to for this to happen, we need to make $\vec{y}+ \vec{c} \leq \vec{0}$. Given that the constraint we have is $\vec{y} \geq \vec{0}$, 
$$\vec{y}+\vec{c} \leq \vec{0} \to \vec{c} \leq -\vec{y} \leq \vec{0}$$
Then, we can conclude that if $\vec{c} \leq \vec{0}$, we can have $F(\vec{y}) = 0$ which is the optimal value.