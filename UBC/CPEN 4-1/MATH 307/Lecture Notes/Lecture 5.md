### Examples
Given the following matrix, find the operator norm and the condition number.
$$A= \begin{bmatrix}
-5 & 0  \\
0 & 2
\end{bmatrix}\begin{bmatrix}
0 & 1  \\
-1 & 0 
\end{bmatrix}
\begin{bmatrix}
 7 & 0  \\
0  & 3
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{ 2 }}  & \frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }}
\end{bmatrix}=A_{1}A_{2}A_{3}A_{4}$$

Let’s see how this matrix transforms a unit vector. Corresponding to,
$$A\mathbf{x} = (A_{1}A_{2}A_{3}A_{4})\mathbf{x}$$
where $\mathbf{x}$ is a unit vector. 

We will see how each matrix will transform the unit vector.

First,
$$A_{4}=\begin{bmatrix}
\frac{1}{\sqrt{ 2 }}  & \frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$
This matrix actually corresponds to the matrix that rotates a vector by $\frac{7\pi}{4}$ counterclockwise.

##### Brief notation of rotation matrix
$$R=\begin{bmatrix}
\cos{\theta} & -\sin{\theta} \\
\sin \theta & \cos \theta 
\end{bmatrix}$$

![[Screenshot 2024-09-28 at 5.13.10 PM.png]]

Second,
$$A_{3}=\begin{bmatrix}
 7 & 0  \\
0  & 3
\end{bmatrix}$$

If we try with a vector $\mathbf{y}$, we can see that it scales the first row by 7, and the second row by 3.
$$A_{3}\mathbf{y}=\begin{bmatrix}
 7 & 0  \\
0  & 3
\end{bmatrix}\mathbf{y}=\begin{bmatrix}
7y_{1} \\
3y_{2}
\end{bmatrix}$$
![[Screenshot 2024-09-28 at 5.14.50 PM.png]]

Third,
$$A_{2}= \begin{bmatrix}
0 & 1  \\
-1 & 0 
\end{bmatrix}$$

This matrix corresponds to the rotation matrix that rotates the vector by $\frac{3\pi}{2}$ counterclockwise.
![[Screenshot 2024-09-28 at 5.15.49 PM.png]]

And lastly,
$$A_{1}=\begin{bmatrix}
-5 & 0 \\
0 & 2
\end{bmatrix}$$

Scales the first by –5 and the second by 2,
![[Screenshot 2024-09-28 at 5.16.34 PM.png]]


We not notice that the final plot has a maximum stretch of 15 and a minimum stretch of 14, giving
$$\lvert \lvert A \rvert  \rvert =15,\hspace{.5in}\lvert \lvert A^{-1} \rvert \rvert =\frac{1}{14},\hspace{.5in} \text{cond}(A)=\frac{15}{14}$$

### Theorem
Let $D \in \mathbb{R}^{n\times n}$ be a diagonal matrix that has the elements $d_{1},d_{2},\cdots,d_{n}$ in its diagonal where $d_{i}\in\mathbb{R}$ for $i \in \{1,\cdots,n\}$, that is
$$D=\begin{bmatrix}
d_{1} &  &  &  &  \\
 & d_{2} &  &  &  \\
 &  & d_{3} &  &  \\
 &  &  & \ddots &  \\
 &  &  &  & d_{n}
\end{bmatrix}$$

Then, we have that $\lvert \lvert D \rvert \rvert = \text{max}_{k\in\{1,\cdots,n\}}\lvert d_k \rvert$. That is the operator norm of $D$ is equal to the diagonal with the largest absolute value.

##### Proof
For convenience, let
$$d_{\text{max}}=\text{max}_{k\in \{1,\cdots,n\}}\lvert d_{k} \rvert$$
By definition, we know that
$$d_{i}\leq d_{\text{max}},\forall i \in\{1,\cdots,n\}$$

**1st Step:**
$$\lvert \lvert D \rvert  \rvert = \text{max}_{\lvert \lvert x \rvert  \rvert =1}\lvert \lvert D\mathbf{x} \rvert  \rvert  $$
$$=\text{max}_{\lvert \lvert \mathbf{x} \rvert  \rvert =1}\sqrt{ (d_{1}x_{1})^2+\cdots+(d_{n}x_{n})^2 }$$

The second inequality refers to the definition of the Euclidean norm for vector $D\mathbf{x}\in \mathbb{R}^n$, we also use that 
$$D\mathbf{x} = \begin{bmatrix}
d_{1}x_{1} \\
d_{2}x_{2} \\
d_{3}x_{3} \\
\vdots \\
d_{n}x_{n}
\end{bmatrix}$$

Then using both equalities and inequalities,
$$\lvert \lvert D \rvert  \rvert =\text{max}_{\lvert \lvert \mathbf{x} \rvert  \rvert =1}\sqrt{ (d_{1}x_{1})^2+\cdots+(d_{n}x_{n})^2 }$$
$$\leq\text{max}_{\lvert \lvert \mathbf{x} \rvert  \rvert =1}\sqrt{ (d_{\text{max}}x_{1})^2+\cdots+(d_{\text{max}}x_{n})^2 }$$
$$=\text{max}_{\lvert \lvert \mathbf{x} \rvert  \rvert =1}d_{\text{max}}\sqrt{ (x_{1})^2+\cdots+(x_{n})^2 }$$
$$=d_{\text{max}}$$
$$\therefore D \leq d_{\text{max}}$$

Now let’s show the other way,
$$\lvert \lvert D \rvert  \rvert = \text{max}_{\lvert \lvert x \rvert  \rvert =1}\lvert \lvert D\mathbf{x} \rvert  \rvert  $$
$$\geq \lvert \lvert D\mathbf{y} \rvert  \rvert $$
for any $\mathbf{y}$ such that $\lvert \lvert \mathbf{y} \rvert \rvert =1$.

Let’s pick a specific $\mathbf{y}$. Let $l$ be the index in $\{1,\cdots,n\}$ for which $\lvert d_{l} \rvert$ is largest. That is, assume that $l$ is the index such that $d_{\text{max}}=\lvert d_{l} \rvert\geq \lvert d_{i} \rvert$ for any $i \in\{1,\cdots,n\}$.

We will pick the standard basis vector $\mathbf{e}^{(l)}\in \mathbb{R}^n$ which is all zeros except index $l$, that is
$$\mathbf{e}^{(l)}=\begin{bmatrix}
0 \\
\vdots \\
0 \\
1 \\
0 \\
\vdots \\
0
\end{bmatrix}$$

Then, we have that $D\mathbf{e}^{(l)}=d_{l}$. As a result, we have that
$$\lvert \lvert D\mathbf{e}^{(l)} \rvert  \rvert =\lvert d_{l} \rvert $$

Also since we know that $\mathbf{e}$ is a unit vector,
$$\lvert \lvert D  \rvert  \rvert =\text{max}_{\lvert \lvert x \rvert  \rvert  =1}\lvert \lvert D\mathbf{x} \rvert  \rvert $$
$$\geq \lvert \lvert D\mathbf{e}^{(l)} \rvert  \rvert =\lvert d_{l} \rvert =d_{\text{max}}$$

Since we showed both directions, we showed that,
$$\lvert \lvert D \rvert  \rvert =d_{\text{max}}$$

## Interpolation
Given data points, $(t_{0},y_{0}),(t_{1},y_{1}),\cdots,(t_{d},y_{d})$ such that $t_{i}\neq t_{j}$ for $i\neq j$, we wish to find a function $f$ that 
$$f(t_k)=y_{k},\hspace{.1in}k \in \{ 0,\cdots,d \}$$

Such a function is called an *interpolant*.

## Polynomial Interpolation
We want to find a polynomial $p(t)$ given as 
$$p(t) = c_{0}+c_{1}t+c_{2}t^2 + \cdots +c_{d}t^d$$
such that $p(t)$ interpolates data points $(t_{0},y_{0}),(t_{1},y_{1}),\cdots,(t_{d},y_{d})$.

Let’s collect the unknowns in a vector $\mathbf{c}\in \mathbb{R}^d$:
$$\mathbf{c}=\begin{bmatrix}
c_{0}  \\
c_{1} \\
\vdots \\
c_{d}
\end{bmatrix}$$

We can see that there are $d+1$ unknowns, 
$$p(t_{0})=y_{0}\implies c_{0}+c_{1}t_{0}+c_{2}t_{0}^2+\cdots+c_{d}t_{0}^d=y_{0}$$
$$p(t_{1})=y_{1}\implies c_{0}+c_{1}t_{1}+c_{2}t_{1}^2+\cdots+c_{d}t_{1}^d=y_{1}$$
$$\vdots$$
$$p(t_{d})=y_{d}\implies c_{0}+c_{1}t_{d}+c_{2}t_{d}^2+\cdots+c_{d}t_{d}^d=y_{d}$$
and $d+1$ equations. Let us write equations in a more compact form:
$$\begin{bmatrix}
1 & t_{0} & t_{0}^2 & \cdots & t_{0}^d \\
1 & t_{1} & t_{1}^2 & \cdots & t_{1}^d \\
\vdots & \vdots & \vdots &  & \vdots \\
1 & t_{d} & t_{d}^2 & \cdots & t_{d}^d
\end{bmatrix}
\begin{bmatrix}
c_{0}  \\
c_{1} \\
\vdots \\
c_{d}
\end{bmatrix}=\begin{bmatrix}
y_{0}  \\
y_{1} \\
\vdots \\
y_{d}
\end{bmatrix}$$

Recall that interpolations is determined by $c_{0},c_{1},\cdots,c_{d}$ which form $\mathbf{c}$. To understand the existence and uniqueness of the polynomial, we have to understand if a solution exists to the linear system,
$$A\mathbf{c}=\mathbf{y}.$$

For this, we will check if the determinant of $A$ and argue that if $\text{det}(A) \neq 0$ then the interpolating polynomial exists and is unique because there is a unique solution to the system $A\mathbf{c}=\mathbf{y}$ in this case. 

This matrix is so called a **Vandermonde matrix**.

### Theorem
The ***Vandermonde matrix*** of dimension $d+1$ has the determinant computed as
$$\text{det}(A) = \prod_{0 \leq i < j \leq d}(t_{j}-t_{i})$$
For instance, when $d=3$,
$$\text{det}(A) = (t_{3}-t_{0})(t_{3}-t_{1})(t_{3}-t_{2})(t_{2}-t_{0})(t_{2}-t_{1})(t_{1}-t_{0})$$

### Theorem
There is a unique polynomial of degree at most $d$ which interpolates $(t_{0},y_{0}),(t_{1},y_{1}),\cdots,(t_{d},y_{d})$ when $t_{i}\neq t_{j}$, for $i \neq j$.


#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 6|Lecture 6]]