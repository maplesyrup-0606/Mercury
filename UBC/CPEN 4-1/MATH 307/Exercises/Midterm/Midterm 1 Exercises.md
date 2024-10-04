### 1.
Let $A$ be a $m\times n$ matrix, determine whether the statements are **True** or **False**.

- If $m>n$ and $\text{rank}(A) = n$, then here is a unique solution of $A\mathbf{x}=\mathbf{b}$ for any $\mathbf{b}$.
	**False**,  only a unique solution can happen if $\text{rank}(A)=\text{rank}(A\vert\mathbf{b})=m$


- If $m<n$ and $\text{rank}(A) = m$, then here are infinitely many solutions of $A\mathbf{x}=\mathbf{b}$ for any $\mathbf{b}$.
	**True**, If there are more columns than rows and still the rank is $m$ then there exists elements
	in $\mathbf{x}$ such that can take infinitely many values.

- If $m>n$ and $\text{rank}(A)= n$, then if the system $A\mathbf{x} = \mathbf{b}$ has one solution then there is only one solution.
	**True**

- If $m>n$ and $\text{rank}(A) < n$, then if the system $A\mathbf{x} = \mathbf{b}$ has one solution then there are infinitely many solutions.
	**True**

- If $A=LU$ is the LU decomposition of $A$ then $\text{det}(L) \neq 0$.
	**True**, if a decomposition exists it means that $A$ is invertible thus $\text{det}(A)\neq 0$ and hence the statement is true.

### 2.
Determine whether the statement is **True** or **False**. If $A$ is the form
$$A=\begin{bmatrix}
* & * & 0 & 0 \\
* & * & * & 0 \\
0 & * & * & * \\
0 & 0 & * & *
\end{bmatrix}$$
and the LU decomposition $A=LU$ exists, then $L$ and $U$ are of the form
$$L=\begin{bmatrix}
1 & 0 & 0 & 0 \\
* & 1 & 0 & 0 \\
0 & * & 1 & 0 \\
0 & 0 & * & 1
\end{bmatrix},U=\begin{bmatrix}
* & * & 0 & 0 \\
0 & * & * & 0 \\
0 & 0 & * & * \\
0 & 0 & 0 & *
\end{bmatrix}$$

**True**, we can apply row operations on $A$ for $R_{1},R_{2}$, $R_{2},R_{3}$ and $R_{3},R_{4}$ to get to $U$.

### 3.
Let $I$ be the identity matrix of size $n$ and let $R$ be the $n$ by $n$ matrix with all zeros except for the nonzero scalar $c$ at row $i$ and column $j$ where $i\neq j$. Let $E=I+R$ and let $A$ be any $n$ by $n$ matrix.

- What matrix multiplication $EA$ is equivalent to which elementary row/column operation on $A$?
	$EA=(I+R)A=A+RA$ so it is equivalent to adding $c$ times row $j$ to row $i$ .

- What matrix multiplication $AE$ is equivalent to which elementary row/column operation on $A$?
	$AE=A(I+R)=A+AR$  is equivalent to adding $c$ times col $i$ to col $j$.

### 4.
Find a value c such that the system $A\mathbf{x}=\mathbf{b}$ has infinitely many solutions where
$$A=\begin{bmatrix}
3 & -1 & 2 \\
1 & 1 & -1  \\
2 & -2 & 3
\end{bmatrix},\mathbf{b}=\begin{bmatrix}
3 \\
2 \\
c
\end{bmatrix}$$

We get the augmented matrix and apply Gaussian elimination,
$$[A\vert \mathbf{b}]=\begin{bmatrix}
3 & -1 & 2 & \vert & 3 \\
1 & 1 & -1 & \vert & 2  \\
2 & -2 & 3 & \vert & c
\end{bmatrix} \to^{R_{2} \leftarrow R_{2}-\frac{R_{1}}{3}} \begin{bmatrix}
3 & -1 & 2 & \vert & 3 \\
0 & \frac{4}{3} & -\frac{5}{3}  & \vert & 1 \\
2 & -2 & 3 & \vert & c
\end{bmatrix}$$
$$\to^{R_{3}\leftarrow R_{3}-\frac{2R_{1}}{3}} \begin{bmatrix}
3 & -1 & 2 & \vert & 3 \\
0 & \frac{4}{3} & -\frac{5}{3} & \vert & 1 \\
0 & -\frac{4}{3} & \frac{5}{3} & \vert & c-2
\end{bmatrix}\to^{R_{2}+R_{3}}\begin{bmatrix}
3 & -1 & 2 & \vert & 3 \\
0 & \frac{4}{3} & -\frac{5}{3} & \vert & 1 \\
0 & 0 & 0 & \vert & c-1
\end{bmatrix}$$

If $c=1$ then $\text{rank}(A)=\text{rank}(A\vert\mathbf{b})=2<3$. So we want $c=1$.


### 5.
Compute the LU decomposition of the matrix
$$A=\begin{bmatrix}
2 & 0 & 1 & 1 \\
-2 & -1 & 2 & -1 \\
0 & 2 & -5 & -1 \\
4 & 0 & 6 & 0
\end{bmatrix}$$

Let’s apply Gaussian Elimination,
$$A=\begin{bmatrix}
2 & 0 & 1 & 1 \\
-2 & -1 & 2 & -1 \\
0 & 2 & -5 & -1 \\
4 & 0 & 6 & 0
\end{bmatrix} \to^{R_{2}\leftarrow R_2+R_{1}} \begin{bmatrix}
2 & 0 & 1 & 1 \\
0 & -1 & 3 & 0 \\
0 & 2 & -5 & -1 \\
4 & 0 & 6 & 0
\end{bmatrix}\to^{R_{3}\leftarrow R_{3}+2R_{2}} \begin{bmatrix}
2 & 0 & 1 & 1 \\
0 & -1 & 3 & 0 \\
0 & 0 & 1 & -1 \\
4 & 0 & 6 & 0
\end{bmatrix}$$
$$\to^{R_{4}\leftarrow R_{4}-2R_{1}} \begin{bmatrix}
2 & 0 & 1 & 1  \\
0 & -1 & 3 & 0 \\
0 & 0 & 1 & -1  \\
0 & 0 & 4 & -2
\end{bmatrix}\to^{R_{4}\leftarrow R_{4}-4R_{2}} \begin{bmatrix}
2 & 0 &1 & 1 \\
0 & -1 & 3 & 0 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 2
\end{bmatrix}$$

Then we get,
$$A=\begin{bmatrix}
2 & 0 &1 & 1 \\
0 & -1 & 3 & 0 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 2
\end{bmatrix},L=\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -2 & 1 & 0 \\
2 & 4 & 0 & 1
\end{bmatrix}$$

### 6.
Consider the matrix
$$A=\begin{bmatrix}
-3 & 1 & 2 & 0 \\
3 & 1 & -2 & 1 \\
-6 & 2 & 5 & 1 \\
-9 & 3 & 4 & 2
\end{bmatrix}$$
Find the $LU$ decomposition of $A$ and compute $\text{det}(A)$.

As usual, Gaussian Elimination,
$$A=\begin{bmatrix}
-3 & 1 & 2 & 0 \\
3 & 1 & -2 & 1 \\
-6 & 2 & 5 & 1 \\
-9 & 3 & 4 & 2
\end{bmatrix}\to^{R_{2}\leftarrow R_{2}+R_{1}} \begin{bmatrix}
-3 & 1 & 2 & 0 \\
0 & 2 & 0 & 1 \\
-6 & 2 & 5 & 1 \\
-9 & 3 & 4 & 2
\end{bmatrix}\to^{R_{3}\leftarrow R_{3}-2R_{1}} \begin{bmatrix}
-3 & 1 & 2 & 0 \\
0 & 2 & 0 & 1 \\
0 & 0 & 1 & 1 \\
-9 & 3 & 4 & 2
\end{bmatrix}$$
$$\to^{R_{4}\leftarrow R_{4}-3R_{1}}\begin{bmatrix}
-3 & 1 & 2 & 0 \\
0 & 2 & 0 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & -2 & 2
\end{bmatrix}\to^{R_{4}+2R_{3}} \begin{bmatrix}
-3 & 1 & 2 & 0 \\
0 & 2 & 0 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 4
\end{bmatrix}$$

$$L=\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1& 1 & 0 & 0 \\
2 & 0 & 1 & 0 \\
3 & 0 & -2 & 1
\end{bmatrix},U=\begin{bmatrix}
-3 & 1 & 2 & 0 \\
0 & 2 & 0 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 4
\end{bmatrix}$$
And hence,
$$\det(A)=\det(LU) =\det(U)=-3\times 2\times 1 \times 4=-24$$

### 7.
Find the solution of the system $A\mathbf{x}=\mathbf{b}$ for
$$\mathbf{b}=\begin{bmatrix}
 2 \\
-1 \\
2
\end{bmatrix}$$
given the LU decomposition
$$A=LU=\begin{bmatrix}
1 & 0 & 0 \\
-1 & 1 & 0 \\
1 & 1 & 1
\end{bmatrix}\begin{bmatrix}
3 & 0 & 1 \\
0 & -1 & 1 \\
0 & 0 & 1
\end{bmatrix}$$

First, solve for $L\mathbf{y}=\mathbf{b}$,
$$\begin{bmatrix}
1 & 0 & 0 \\
-1 & 1 & 0 \\
1 & 1 & 1
\end{bmatrix}\mathbf{y}=\begin{bmatrix}
2 \\
-1 \\
2
\end{bmatrix}$$

Then we can conclude that $y_{1}=2,y_{2}=1,y_{3}=-1$.
Now we solve for $U\mathbf{x}=\mathbf{y}$,
$$\begin{bmatrix}
3 & 0 & 1 \\
0 & -1 & 1 \\
0 & 0 & 1
\end{bmatrix}\mathbf{x}=\begin{bmatrix}
2 \\
1 \\
-1
\end{bmatrix}$$

Then,
$$
\therefore \mathbf{x}=\begin{bmatrix}
1 \\
-2 \\
-1
\end{bmatrix}$$

### 8.
Suppose we compute a decomposition $A=L_{0}U_{0}$ such that $U_0$ is the *unit* upper triangular and $L_0$ is the lower triangular. Describe a method to derive a decomposition $A=LU$ such that $L$ is *unit* lower triangular and $U$ is upper triangular.

Factor out the diagonal entries of $L$ to $D$ and let $U=DU_0$.
$$A=L_{0}U_{0}=LDU_{0}=LU$$

### 9.
Show that the 1-norm satisfies the properties of a norm.
$$\lvert \lvert x \rvert  \rvert_1=\lvert x_{1} \rvert +\cdots+ \lvert x_{n} \rvert   \geq 0 $$
$$\lvert x_{1} \rvert +\cdots +\lvert x_{n} \rvert = 0 \implies x_{1}=\cdots=x_{n} = 0\implies x=0 $$
$$\lvert \lvert cx \rvert  \rvert_{1}=\lvert cx_{1} \rvert+\cdots+\lvert cx_{n} \rvert = \lvert c \rvert \cdot (\lvert x_{1} \rvert +\cdots+ \lvert x_{n} \rvert  )  =\lvert c \rvert \cdot \lvert \lvert x \rvert  \rvert_{1}    $$
$$\lvert \lvert x+y \rvert  \rvert_{1} = \lvert x_{1}+y_{1} \rvert +\cdots+\lvert x_{n} +y_{n} \rvert \leq \lvert x_{1} \rvert+\cdots+\lvert x_{n} \rvert+\lvert y_{1} \rvert+\cdots+\lvert y_{n} \rvert  \leq \lvert \lvert x \rvert  \rvert_{1} + \lvert \lvert y \rvert  \rvert_{1}     $$

### 10.
Show that the $\infty$-norm satisfies the properties of a norm.
$$\lvert \lvert x \rvert  \rvert _{\infty}=\text{max}\{\lvert x_{1} \rvert ,\cdots,\lvert x_{n} \rvert \} = \lvert x_{\text{max}} \rvert \geq 0 $$
$$\text{max}\{\lvert x_{1} \rvert ,\cdots,\lvert x_{n} \rvert \}=0 \implies \lvert x_{1} \rvert =\cdots=\lvert x_{n} \rvert = 0 \implies x=0 $$
$$\lvert \lvert cx \rvert  \rvert_{\infty}=\text{max}\{\lvert cx_{1} \rvert ,\cdots,\lvert cx_{n} \rvert \} \implies \lvert c \rvert \cdot \text{max}\{\lvert x_{1} \rvert ,\cdots,\lvert x_{n} \rvert \}=\lvert c \rvert\cdot\lvert \lvert x \rvert  \rvert_{\infty}   $$\
$$\lvert \lvert x+y \rvert  \rvert_{\infty}=\text{max}\{\lvert x_{1}+y_{1} \rvert ,\cdots,\lvert x_{n}+y_{n} \rvert \} = \lvert (x+y)_{max} \rvert\leq \lvert x_{\text{max}} \rvert+\lvert y_{\text{max}} \rvert =\lvert \lvert x \rvert  \rvert _{\infty}+\lvert \lvert y \rvert  \rvert _{\infty}   $$

### 11.
Is the function $\lvert \lvert x \rvert \rvert=x_{1}+\cdots+x_{n}$ a vector norm?
No, for instance let’s look at 
$$\mathbf{x}=\begin{bmatrix}
1 \\
-1
\end{bmatrix}$$
Then,
$$\lvert \lvert x \rvert  \rvert =1-1=0$$
but 
$$x\neq {0}$$
Contradicts with the fact that only the zero vector can have a norm of 0.
### 12.
The function
$$\lvert \lvert x \rvert  \rvert _{p}=\left( \sum_{k=1}^n \lvert x_{k} \rvert^p \right)^{\frac{1}{p}}$$
does not satisfy the triangle inequality if $0<p<1$. Prove this for $n=2$ and $p=0.5$. In other words, fund vectors $\mathbf{x},\mathbf{y}\in \mathbb{R}^2$ such that
$$\lvert \lvert x+y\rvert  \rvert_{0.5}>\lvert \lvert x \rvert  \rvert _{0.5}+\lvert \lvert y \rvert  \rvert _{0.5} $$
%% $$\mathbf{x}=\begin{bmatrix}
0  \\
4
\end{bmatrix},\mathbf{y}=\begin{bmatrix}
4 \\
0
\end{bmatrix}$$ %%

### 13.
Is it true that $\lvert \lvert x \rvert \rvert_{1}\leq \lvert \lvert x \rvert \rvert_{2}\leq \lvert \lvert x \rvert \rvert_{\infty}$ for all $x \in \mathbb{R}^n$?
Let, 
$$x=\begin{bmatrix}
2  \\
2
\end{bmatrix}$$

Then, $\lvert \lvert x \rvert \rvert_{\infty}=2,\lvert \lvert x \rvert \rvert_{2}=2\sqrt{ 2 }$ and $\lvert \lvert x \rvert \rvert_{1}=4$ hence false.

### 14.
Determine whether the statement is **True** or **False**: if $\lvert \lvert A \rvert \rvert=1$ then $A=I$.
That is,
$$\lvert \lvert A \rvert  \rvert =\text{max}_{\lvert \lvert \mathbf{x} \rvert  \rvert =1}\lvert \lvert A\mathbf{x} \rvert  \rvert =1$$

Consider the matrix,
$$ A =\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} & -\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$

Then, $\lvert \lvert A \rvert \rvert=1$. However, $A\neq I$.


### 15.
Suppose $A$ is a 2 by 2 matrix such that the image of the unit circle under the linear transformation $A$ is:

![[Pasted image 20240930155622.png]]
determine $\text{cond}(A)$.

We can see that the max stretch is $5\sqrt{ 2 }$ and the min stretch is $2\sqrt{ 2 }$, thus,
$$\text{cond}(A)=\frac{5\sqrt{ 2 }}{2\sqrt{ 2 }}=\frac{5}{2}$$
### 16.
Find the unique polynomial of degree 3 which interpolates the points
$$(0,-1),(1,-1),(2,1),(3,-1)$$
Solve the system $A\mathbf{c}=\mathbf{y}$
$$A=\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
1 & 2 & 4 & 8 \\
1 & 3 & 9 & 27
\end{bmatrix},\mathbf{y}=\begin{bmatrix}
-1  \\
-1 \\
1 \\
-1
\end{bmatrix}$$

$$A=\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
1 & 2 & 4 & 8 \\
1 & 3 & 9 & 27
\end{bmatrix}\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
 1 & 2 & 4 & 8 \\
1 & 3 & 9 & 27
\end{bmatrix}\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 2 & 4 & 8 \\
1 & 3 & 9 & 27
\end{bmatrix}\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 2 & 4 & 8 \\
0 & 3 & 9 & 27
\end{bmatrix}$$
$$\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 2 & 6 \\
0 & 3 & 9 & 27
\end{bmatrix}\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 2 & 6 \\
0 & 0 & 6 & 24
\end{bmatrix}\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 2 & 6 \\
0 & 0 & 0 & 6
\end{bmatrix}=U$$

$$L=\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 2 & 1 & 0  \\
1 & 3 & 3 & 1
\end{bmatrix}$$

Then we solve for $c$,
$$L\mathbf{x}=\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 2 & 1 & 0  \\
1 & 3 & 3 & 1
\end{bmatrix}\mathbf{x}=\begin{bmatrix}
-1  \\
-1 \\
1 \\
-1
\end{bmatrix}$$
$$\mathbf{x}=\begin{bmatrix}
-1 \\
0 \\
2 \\
-6
\end{bmatrix}$$

Now,
$$U\mathbf{c}=\mathbf{x}$$
$$\to \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 2 & 6 \\
0 & 0 & 0 & 6
\end{bmatrix}\mathbf{c}=\begin{bmatrix}
-1 \\
0 \\
2 \\
-6
\end{bmatrix}$$

$$\therefore \mathbf{c}=\begin{bmatrix}
-1 \\
-3 \\
4 \\
-1
\end{bmatrix}$$

Therefore, the polynomial is $p(t)=-1-3t+4t^2-t^3$.

### 17.
Construct the natural cubic spline interpolating points
$$(0,0),(1,2),(2,1),(3,3),(4,2),(5,4),(6,2),(7,3),(8,1),(9,2),(10,0)$$
```python
x = [0,1,2,3,4,5,6,7,8,9,10]

y = [0,2,1,3,2,4,2,3,1,2,0]

  

p4 = CubicSpline(x, y, bc_type='natural')
```

### 18.
Let $p(t)$ be the natural cubic spline which interpolates the data
$$(0,1),(1,3),(2,8),(3,10),(4,9),(5,-1),(6,-17)$$
Suppose the coefficient matrix of $p(t)$ is
$$C=\begin{bmatrix}
1 & -2 & 1 & a_{4} & 1 & 1 \\
0 & 3 & -3 & b_{4} & -6 & -3 \\
1 & 4 & 4 & c_{4} & -5 & -14 \\
1 & 3 & 8 & 10 & 9 & -1
\end{bmatrix}$$

Determine the coefficients $a_{4},b,c_{4}$, then compute the value $p''(2.5)$

First,
$$L_{k}=t_{k}-t_{k-1}=1,\forall k$$
Then the continuity of $p(t),p’(t)$ and $p’’(t)$ yields the equations,
$$p_{k}(t_{k})=p_{k+1}(t_{k})\implies a_{k}+b_{k}+c_{k}+d_{k}=d_{k+1}$$
$$p'_{k}(t_{k})=p'_{k+1}(t_{k})\implies 3a_{k}+2b_{k}+c_{k}=c_{k+1}$$
$$p''_{k}(t_{k})=p''_{k+1}(t_{k})\implies 6a_{k}+2b_{k}=2b_{k+1}$$

Then, 
$$6a_{3}+2b_{3}=2b_{4}\implies 6 -6=2b_{4}\to b_{4}=0$$
$$3a_{3}+2b_{3}+c_{3}=c_{4}\implies {3}-6+4=1=c_{4}\to c_{4}=1$$
$$6a_{4}+2b_{4}=2b_{5}\implies 6a_{4}+0=-12 \to a_{4}=-2$$

And then,
$$p''(2.5)=p''_{3}(2.5)=6a_{3}\times(2.5-2)+2b_{3}=6\times 0.5+2\times-3=-3$$
We use $k=3$ since the $[t_{k-1},t_{k}]=[2,3]$.

### 19.
Consider $d$ data points $(t_{1},y_{1}),\cdots,(t_{d},y_{d})$ such that $t_i \neq t_j$ for $i\neq j$. Determine whether the statement is **True** or **False**.
- There exists a unique polynomial of degree at most $d-1$ which interpolates the data.
	**True**

- There exists a unique polynomial $p(t)$ of degree at most $d$ which interpolates the data and also satisfies $p’(t_1)=0$ and $p’’(t_1)=0$.
	**False**, we have $d+1$ coefficients (hence unknowns), and $d$ equations by adding 2 more constraints we end up with $d+2$ constraints which overwhelm the number of unknowns.

- There exists a unique polynomial $p(t)$ of degree at most $d$ which interpolates the data and $p’(t_1)=0$.
	**True**, we have $d+1$ coefficients and $d+1$ equations!

### 20.
Consider $N+1$ data points $(t_{0},y_{0}),\cdots,(t_{N},y_{N})$. Let $A_{1}\mathbf{c}_{1}=\mathbf{b}_{1}$ such that the solution $c_1$ consists of the coefficients of the interpolating polynomial with respect to the monomial basis. Let $A_{2}\mathbf{c}_{2}=\mathbf{b}_{2}$ such that the solution $c_{2}$ consists of the coefficients of the interpolating natural cubic spline. Do we expect $\text{cond}(A_{1})<\text{cond}(A_{2})$ or $\text{cond}(A_{1}) > \text{cond}(A_{2})$ for large values of $N$?

We expect $\text{cond}(A_{1})>\text{cond}(A_{2})$.

==The condition number of a Vandermonde matrix gets _very_ large as the size of the matrix increases. This means that interpolation by the monomial basis is very sensitive to changes in the data for polynomials of large degree.==

==The condition number of the matrix for constructing the natural cubic spline does not increase as drastically with the number of points $N+1$  as compared with the Vandermonde matrix.==

### 21.
Suppose we have 4 points $(0,y_{0}),(1,y_{1}),(2,y_{2}),(3,y_{3})$ and we want to interpolate the data using a spline $p(t)$ constructed from 3 of 2 degree polynomials $p_{1},p_{2},p_{3}$ where
$$p_{k}(t)=a_{k}(t-t_{k-1})^2+b_{k}(t-t_{k-1})+c_{k},t\in[t_{k-1},t_{k}]$$
We require that $p(t)$ and $p’(t)$ are continuous and $p’’(t_0)=0$. Setup a linear system $A\mathbf{x}=\mathbf{b}$ where the solution is
$$x=\begin{bmatrix}
a_{1} & b_{1} & a_{2} & b_{2} & a_{3} & b_{3}
\end{bmatrix}^{T}$$

$$p_{1}(0)=c_{1}=y_{0}$$
$$p_{1}(1)=a_{1}+b_{1}+c_{1}=y_{1}=c_{2}=p_{2}(1)$$
$$p_{2}(2)=a_{2}+b_{2}+c_{2}=y_{2}=c_{3}=p_{3}(2)$$
$$p_{3}(3)=a_{3}+b_{3}+c_{3}=y_{3}$$

$$
p_{1}'(1)=2a_{1}+b_{1}=p'_{2}(1)=b_{2}
$$
$$p'_{2}(2)=2a_{2}+b_{2}=p'_{2}(2)=b_{3}$$


$$p''(0)=p_{1}''(0)=2a_{0}=0\implies a_{0}=0$$




$$\therefore A=\begin{bmatrix}
1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 1 \\
2 & 1 & 0 & -1 & 0 & 0 \\
0 & 0 & 2 & 1 & 0 & -1 \\
1 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
a_{1} \\ b_{1} \\ a_{2} \\ b_{2} \\ a_{3} \\ b_{3}
\end{bmatrix}=\begin{bmatrix}
y_{1}- y_{0} \\
y_{2}-y_{1} \\
y_{3}-y_{2} \\
0 \\
0 \\
0
\end{bmatrix}$$

**Tips on how to solve this**:
1. Notice that it is not a cubic spline.
2. Compute each left / right end point.
3. Compute derivative at each intersection.
4. Use last hint.
5. Construct the matrix.


### 22.
Consider the natural cubic spline $p(t)$ represented by the coefficient matrix
$$C=\begin{bmatrix}
3 & a_{2} & 2 & -4 & -2 & -2 & 8 \\
0 & 9 & b_{3} & b_{4} & b_{5} & -18 & -24 \\
0 & 9 & 12 & 6 & c_{5} & -36 & -78 \\
0 & 3 & 16 & 24 & d_{5} & 6 & -50
\end{bmatrix}$$

where $t_{0}=0,t_{1}=1,t_{2}=2,t_{3}=3,t_{4}=4,t_{5}=5,t_{6}=6,t_{7}=7$. Find the value $b_4$ and compute $p’’(5.5)$.

Since it’s natural cubic spline, notice that $p''(0)=0,p''(7)=0$.

$$p'_{3}(3)=p'_{4}(3)$$
$$\implies 3a_{3}+2b_{3} +c_{3}=c_{4}\to 6+2b_{3}+12=6\to b_{3}=-6$$
$$p''_{3}(3)=p''_{4}(3)$$
$$\implies6a_{3}+2b_{3}=2b_{4}\to 12-12=0=2b_{4}\to b_{4}=0$$
$$\therefore b_{4}=0$$

Now compute $p''(5.5)$,
$$p''(5.5)=p''_{6}(5.5)=6a_{6}\times 0.5+2b_{6}$$

$$p''_{4}(4)=p''_{5}(4)$$
$$\implies 6a_4+2b_{4}=2b_{5}\to-24+0=2b_{5}\to b_{5}=-12$$

Thus,
$$\therefore p''(5.5)=p''_{6}(5.5)=6a_{6}\times 0.5+2b_{6}=3\times-2+2\times-18=-42$$

==Note that $p_5(t)$ belongs to the interval $[4,5]$ not $[5,6]$.