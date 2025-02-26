### Q1 
#### (a)
Let’s consider the two conditions among the three given,
$$-x+2y \leq -2 \quad -3x+y \geq -4$$
and let’s re-arrange to,
$$2y+2 \leq x \quad \frac{1}{3} y + \frac{4}{3} \geq x$$
in order for both to be satisfied,
$$2y +2 \leq x \leq \frac{1}{3}y + \frac{4}{3}$$
we also need to satisfy,
$$\begin{aligned}
2y+2 \leq \frac{1}{3}y + \frac{4}{3} &\to \frac{5}{3}y \leq -\frac{2}{3} \\
&\to y\leq -\frac{2}{5}
\end{aligned}$$
But we have to satisfy $x,y \geq{0}$, hence there is no pair $(x,y)$ that can satisfy these conditions.

#### (b)
Let’s start with the auxiliary LP problem to see investigate feasibility.

$$\begin{aligned}
\text{maximize}\;&-x_{0} \\
&x_{1}+x_{2}-x_{0}\leq{1}\\
&2x_{1}-x_{2}-x_{0} \leq -1 \\
 -&3x_{1}-2x_{2}-x_{0} \leq -4
\end{aligned}$$
$$\begin{aligned}
&w=-x_{0} \\ 
&x_{3}=1+x_{0}-x_{1}-x_{2}\\
&x_{4}=-1+x_{0}-2x_{1}+x_{2}\\
&x_{5}=-4+x_{0}+3x_{1}+2x_{2}
\end{aligned}$$
Our entering variable is $x_0$, we know have to find the leaving variable by finding the one that becomes 0 the last.

$$\begin{aligned}
&x_{3}=1+x_{0} \to x_{3}\neq{0}\\
&x_{4}=-1+x_{0} \to x_{0} = 1 \\
&x_{5}=-4+x_{0} \to x_{0}=4
\end{aligned}$$
we can see that $x_{5}$ is the leaving variable.

$$\begin{aligned}
x_{0}&=4-3x_{1}-2x_{2}+x_{5} \\
x_{3}&=1+(4-3x_{1}-2x_{2}+x_{5})-x_{1}-x_{2} \\ 
&=5-4x_{1}-3x_{2}+x_{5} \\
x_{4}&=-1+(4-3x_{1}-2x_{2}+x_{5})-2x_{1}+x_{2} \\
&= 3-5x_{1}-x_{2}+x_{5} \\ 
w&=-(4-3x_{1}-2x_{2}+x_{5}) = -4+3x_{1}+2x_{2}-x_{5}
\end{aligned}$$

Our next dictionary is then,
$$\begin{aligned}
w&= -4+3x_{1}+2x_{2}-x_{5}\\
x_{0}&=4-3x_{1}-2x_{2}+x_{5} \\
x_{3}&=5-4x_{1}-3x_{2}+x_{5} \\ 
x_{4}&= 3-5x_{1}-x_{2}+x_{5} \\ 
\end{aligned}$$
Following Anstee’s rule, our next entering variable is $x_{1}$.
$$\begin{aligned}
x_{0}&=4-3x_{1} \to  x_{1}= \frac{4}{3}\\ 
x_{3}&=5-4x_{1} \to x_{1} = \frac{5}{4} \\
x_{4}&=3-5x_{1} \to x_{1} =\frac{3}{5}
\end{aligned}$$
so our leaving variable is $x_{4}$.

$$\begin{aligned}
x_{1} &= \frac{3}{5}-\frac{1}{5}x_{2} -\frac{1}{5}x_{4} + \frac{1}{5}x_{5} \\
x_{0} &= 4-3x_{1}-2x_{2}+x_{5} \\
&= \frac{11}{5}-\frac{7}{5}x_{2} + \frac{3}{5}x_{4} + \frac{2}{5}x_{5} \\ 
x_{3} &=5-4x_{1}-3x_{2}+x_{5} \\ 
&=\frac{13}{5}-\frac{11}{5}x_{2}+\frac{4}{5}x_{4}+\frac{1}{5}x_{5}\\
w&=-4+3x_{1}+2x_{2}-x_{5} \\ 
&=-\frac{11}{5}+\frac{7}{5}x_{2}-\frac{3}{5}x_{4}-\frac{2}{5}x_{5}
\end{aligned}$$

Our third dictionary is then,
$$\begin{aligned}
w &= -\frac{11}{5}+\frac{7}{5}x_{2}-\frac{3}{5}x_{4}-\frac{2}{5}x_{5} \\
x_{0} &= \frac{11}{5}-\frac{7}{5}x_{2} + \frac{3}{5}x_{4} + \frac{2}{5}x_{5} \\ 
x_{1} &= \frac{3}{5}-\frac{1}{5}x_{2}-\frac{1}{5}x_{4}+\frac{1}{5}x_{5} \\ 
x_{3}&= \frac{13}{5}-\frac{11}{5}x_{2}+\frac{4}{5}x_{4} + \frac{1}{5}x_{5}
\end{aligned}$$

Again, since we’re not done, we need to find the next entering variable. Following Anstee’s rule once again, we can see that $x_{2}$ is the entering variable. Using this info,
$$\begin{aligned}
x_{0} &= \frac{11}{5} -\frac{7}{5}x_{2} \to x_{2}= \frac{11}{7} \\ 
x_{1} &= \frac{3}{5}-\frac{1}{5}x_{2} \to x_{2}=3 \\
x_{3}&=\frac{13}{5}-\frac{11}{5}x_{2} \to x_{2} =\frac{13}{11}
\end{aligned}$$
we can conclude that our leaving variable is $x_{3}$.

Let’s update our dictionary.

$$\begin{aligned}
x_{2} &= \frac{13}{11}-\frac{5}{11}x_{3}+\frac{4}{11}x_{4} + \frac{1}{11}x_{5} \\ 
x_{0}&=\frac{11}{5}-\frac{7}{5}x_{2}+\frac{3}{5}x_{4}+\frac{2}{5}x_{2} \\ 
&=\frac{30}{55}+\frac{35}{55}x_{3}+\frac{5}{55}x_{4}+\frac{15}{55}x_{5} \\ 
x_{1} &=\frac{3}{5}-\frac{1}{5}x_{2}-\frac{1}{5}x_{4}+\frac{1}{5}x_{5} \\
&=\frac{20}{55} + \frac{5}{55}x_{3} -\frac{15}{55}x_{4} + \frac{10}{55}x_{5} \\ 
w&=\frac{-11}{5}+\frac{7}{5}x_{2} - \frac{3}{5}x_{4}-\frac{2}{5}x_{5} \\
&= \frac{-30}{55}- \frac{35}{55}x_{3} - \frac{5}{55}x_{4} -\frac{15}{55}x_{5}
\end{aligned}$$

thus,
$$\begin{aligned}
w &= -\frac{30}{55}-\frac{35}{55}x_{3} - \frac{5}{55}x_{4} - \frac{15}{55}x_{5} \\
x_{0} &= \frac{30}{55}+\frac{35}{55}x_{3} + \frac{5}{55}x_{4} + \frac{15}{55}x_{5} \\
x_{1} &= \frac{20}{55}+\frac{5}{55}x_{3}  - \frac{15}{55}x_{4}+ \frac{10}{55}x_{5} \\
x_{2} &= \frac{13}{11} - \frac{5}{11}x_{3} + \frac{4}{11}x_{4} + \frac{1}{11}x_{5}
\end{aligned}$$
We can see that this is our final dictionary, however the optimal solution is $-\frac{65}{55}$ and not 0. Hence, our original Lp problem is not feasible.

We cannot solve the original Lp problem.

#### (c)
Similar to the previous question, let’s investigate feasibility and find the right initial dictionary.

$$\begin{aligned}
\text{maximize} &-x_{0}\\
&2x_{1}+x_{2}+x_{3}-x_{0}\leq 2\\
-&3x_{1}-4x_{2}-2x_{3} -x_{0} \leq -8
\end{aligned}$$
$$\begin{aligned}
w &=-x_{0} \\ 
x_{4}&=2+x_{0}-2x_{1}-x_{2}-x_{3} \\ 
x_{5}&=-8+x_{0}+3x_{1}+4x_{2}+2x_{3}
\end{aligned}$$

Our entering variable is $x_{0}$, and our leaving variable is
$$\begin{aligned}
x_{4} &= 2+x_{0}  \to x_{4} \neq{0} \\ 
x_{5} &=-8+x_{0} \to x_{0} =8
\end{aligned}$$
$x_5$.

Then,
$$\begin{aligned}
x_{0} &= 8-3x_{1}-4x_{2}-2x_{3}+x_{5} \\ 
x_{4} &= 2+x_{0}-2x_{1}-x_{2}-x_{3} \\ 
&= 10-5x_{1}-5x_{2}-3x_{3}+x_{5} \\ 
w&=-x_{0} \\ 
&=-8+3x_{1}+4x_{2}+2x_{3}-x_{5}
\end{aligned}$$
hence, the new dictionary is,
$$\begin{aligned}
w &=-8+3x_{1}+4x_{2}+2x_{3}-x_{5}\\
x_{0}&=8-3x_{1}-4x_{2}-2x_{3}+x_{5} \\ 
x_{4} &= 10-5x_{1}-5x_{2}-3x_{3}+x_{5}
\end{aligned}$$

In this dictionary, our entering variable is $x_2$ following Anstee’s rule. Let’s find the leaving variable.

$$\begin{aligned}
x_{0} &= 8-4x_{2}  \to x_{2}=2\\ 
x_{4} &= 10-5x_{2} \to x_{2}=2
\end{aligned}$$

thus, our leaving variable is $x_{0}$.

$$\begin{aligned}
x_{2} &= 2 - \frac{1}{4}x_{0} -\frac{3}{4}x_{1} - \frac{2}{4}x_{3} + \frac{1}{4}x_{5} \\ 
x_{4} &= 10-5x_{1}-5x_{2}-3x_{3}+x_{5} \\ 
&=\frac{5}{4}x_{0} - \frac{5}{4}x_{1} -\frac{2}{4}x_{3} -\frac{1}{4}x_{5} \\ 
w&= -8 + 3x_{1}+4x_{2}+2x_{3}-x_{5} \\ 
&=-x_{0}
\end{aligned}$$
therefore, our new dictionary is.
$$\begin{aligned}
w &= -x_{0} \\ 
x_{2} &= 2- \frac{1}{4}x_{0} - \frac{3}{4}x_{1} - \frac{2}{4}x_{3} + \frac{1}{4}x_{5} \\ 
x_{4} &= \frac{5}{4}x_{0} -\frac{5}{4}x_{1} - \frac{2}{4}x_{3} - \frac{1}{4}x_{5}
\end{aligned}$$
and this is our final dictionary. We can see that the original Lp problem is feasible since the optimal solution is $0$.

If we apply this to our original Lp problem,

$$\begin{aligned}
z&= 3x_{1}+2x_{2}+3x_{3} \\ 
&=3x_{1}+ 2\left( 2 -\frac{3}{4}x_{1} -\frac{2}{4}x_{3} +\frac{1}{4}x_{5}  \right)+3x_{3} \\ 
&=4 +\frac{3}{2}x_{1} +2x_{3} + \frac{1}{2}x_{5}  \\ 
x_{2} &= 2 - \frac{3}{4}x_{1} -\frac{2}{4}x_{3} +\frac{1}{4}x_{5} \\ 
x_{4} &= -\frac{5}{4}x_{1} -\frac{2}{4}x_{3} -\frac{1}{4}x_{5}
\end{aligned}$$

Let’s construct a new dictionary, following Anstee’s rule we can see that our entering variable is $x_3$, if we try to find the leaving variable.
$$\begin{aligned}
x_{2} &= 2- \frac{2}{4}x_{3} \to x_{3} = 4 \\ 
x_{4} &= -\frac{2}{4}x_{3} \to x_{3}= 0
\end{aligned}$$
hence, our leaving variable is $x_4$.

$$\begin{aligned}
x_{3} &= -\frac{5}{2}x_{1} -2x_{4} -\frac{1}{2}x_{5} \\ 
x_{2} &= 2 - \frac{3}{4}x_{1} -\frac{2}{4}\left( -\frac{5}{2}x_{1} -2x_{4} -\frac{1}{2}x_{5}\right) +\frac{1}{4}x_{5} \\ 
&= 2 +\frac{1}{2}x_{1} +x_{4} +\frac{1}{2}x_{5} \\ 
z&=4+ \frac{3}{2}x_{1} +2\left( -\frac{5}{2}x_{1}-2x_{4}-\frac{1}{2}x_{5} \right) +\frac{1}{2}x_{5} \\ 
&=4 -\frac{7}{2}x_{1}-4x_{4}-\frac{1}{2}x_{5}
\end{aligned}$$

Hence, our final dictionary is,
$$\begin{aligned}
z &= 4 - \frac{7}{2}x_{1} -4x_{4}  - \frac{1}{2}x_{5} \\ 
x_{2} &= 2 + \frac{1}{2}x_{1}+x_{4} + \frac{1}{2}x_{5} \\ 
x_{3} &= -\frac{5}{2}x_{1} -2x_{4}-\frac{1}{2}x_{5}
 \end{aligned}$$
Our optimal solution is
$$\left\{ x_{1},x_{2},x_{3},x_{4},x_{5} \right\} = \left\{ 0,2,0,0,0 \right\}$$
with the optimal value
$$ \therefore z= 4 -0 - 0 -0 = 4$$

### Q2
![[Pasted image 20250214220632.png]]
![[Pasted image 20250214220642.png]]
![[Pasted image 20250214220657.png]]
![[Pasted image 20250214220841.png]]

### Q3
#### (a)
Let’s define $f(\mathbf{x})$ as the following for $f:\mathbb{R}^3\to \mathbb{R}$,
$$f(\mathbf{x})=x_{1}^2+x_{2}^2+x_{3}^2$$

Now, let’s look at $f(\mathbf{u}),f(\mathbf{v})$,
$$\begin{aligned}
f(\mathbf{u})&= u_{1}^2+u_{2}^2+u_{3}^2 \\ f(\mathbf{v})&=v_{1}^2+v_{2}^2+v_{3}^2
\end{aligned}$$

If we consider $f((1-\lambda)\mathbf{u}+\lambda \mathbf{v})$ where $\lambda \in [0,1]$,
$$\begin{aligned}
f((1-\lambda)\mathbf{u}+\lambda \mathbf{v}) &= ((1-\lambda)u_{1}+\lambda v_{1})^2+((1-\lambda)u_{2}+\lambda v_{2})^2+((1-\lambda)u_{3}+\lambda v_{3})^2 \\
&\leq ((1-\lambda)u_{1})^2+(\lambda v_{1})^2+((1-\lambda)u_{2})^2+(\lambda v_{2})^2+((1-\lambda)u_{3})^2+(\lambda v_{3})^2 \\
&= ((1-\lambda)u_{1})^2+((1-\lambda)u_{2})^2+((1-\lambda)u_{3})^2 + (\lambda v_{1})^2+(\lambda v_{2})^2+(\lambda v_{3})^2
\end{aligned}$$

Since we know that $\lambda \in [0,1]$, we can also show that,
$$\begin{aligned}
f((1-\lambda)\mathbf{u}+\lambda \mathbf{v}) &\leq ((1-\lambda)u_{1})^2+((1-\lambda)u_{2})^2+((1-\lambda)u_{3})^2 + (\lambda v_{1})^2+(\lambda v_{2})^2+(\lambda v_{3})^2 \\ 
&\leq (1-\lambda)(u_{1})^2+(1-\lambda)(u_{2}){^2}+(1-\lambda)(u_{3})^2+\lambda(v_{1}^2)+\lambda(v_{2}^2)+\lambda(v_{3}^2) \\ 
&= (1-\lambda)(u_{1}^2+u_{2}^2+u_{3}^2) + \lambda(v_{1}^2+v_{2}^2+v_{3}^2) \\ 
&= (1-\lambda)f(\mathbf{u})+\lambda f(\mathbf{v})
\end{aligned}$$
$$\therefore f((1-\lambda)\mathbf{u}+\lambda \mathbf{v}) \leq (1-\lambda)f(\mathbf{u})+\lambda f(\mathbf{v})$$
Which is convex as we required.

#### (b)
Let’s consider one case where $\lambda \in [0,1]$ and,
$$g((1-\lambda)\mathbf{u}+\lambda \mathbf{v})= f_{1}((1-\lambda)\mathbf{u}+\lambda \mathbf{v})$$
which means that,
$$\text{max}(f_{1}((1-\lambda)\mathbf{u}+\lambda \mathbf{v}),f_{2}((1-\lambda)\mathbf{u}+\lambda \mathbf{v}))=f_{1}((1-\lambda)\mathbf{u}+\lambda \mathbf{v})$$
Then we can say that,
$$g((1-\lambda)\mathbf{u}+\lambda \mathbf{v})= f_{1}((1-\lambda)\mathbf{u}+\lambda \mathbf{v}) \leq (1-\lambda)f_{1}(\mathbf{u})+\lambda f_{1}(\mathbf{v})$$
since $f_1$ is convex. 

We can also see that,
$$f_{1}(\mathbf{x})\leq \text{max}(f_{1}(\mathbf{x}),f_{2}(\mathbf{x}))=g(\mathbf{x})$$
thus,
$$g((1-\lambda)\mathbf{u}+\lambda \mathbf{v})\leq (1-\lambda)f_{1}(\mathbf{u})+\lambda f_{1}(\mathbf{v}) \leq (1-\lambda)g(\mathbf{u})+\lambda g(\mathbf{v})$$
and hence showing that $g$ is convex.

This also suffices for the other case when,
$$g((1-\lambda)\mathbf{u}+\lambda \mathbf{v})= f_{2}((1-\lambda)\mathbf{u}+\lambda \mathbf{v})$$
using the same properties since it is also clear that,
$$f_{2}(\mathbf{x})\leq \text{max}(f_{1}(\mathbf{x}),f_{2}(\mathbf{x}))=g(\mathbf{x})$$
and $f_2$ is convex.