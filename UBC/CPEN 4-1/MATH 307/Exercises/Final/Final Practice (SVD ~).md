
#### Exercise 1
Find the singular value decomposition of the matrix
$$A=\begin{bmatrix}
1 & 2 & -1 \\
2 & 1 & 4
\end{bmatrix}$$

Let’s get $AA^T$,
$$AA^T=\begin{bmatrix}
1 & 2 & -1 \\
2 & 1 & 4
\end{bmatrix}\begin{bmatrix}
1 & 2 \\
2 & 1 \\
-1 & 4
\end{bmatrix} = \begin{bmatrix}
6 & 0 \\
0 & 21
\end{bmatrix}$$
$$\det(AA^T-\lambda I) = (\lambda-21)(\lambda-6) \to \sigma_{1}=\sqrt{ 21},\sigma_{2}=\sqrt{ 6 }$$

$$p_{1} = \begin{bmatrix}
0 \\
1
\end{bmatrix},p_{2}=\begin{bmatrix}
1 \\
0
\end{bmatrix} $$
No $p_{3}$ since $p_{1},p_{2}$ already form the basis of $\mathbb{R}^2$.

Now,
$$q_{1}= \frac{1}{\sigma_{1}}A^Tp_{1} = \frac{1}{\sqrt{ 21 }}\begin{bmatrix}
1 & 2 \\
2 & 1 \\
-1 & 4
\end{bmatrix}\begin{bmatrix}
0 \\
1
\end{bmatrix}=\frac{1}{\sqrt{ 21 }}\begin{bmatrix}
2 \\
1 \\
4
\end{bmatrix}$$
$$q_{2}=\frac{1}{\sigma_{2}}A^Tp_{2}=\frac{1}{\sqrt{ 6 }}\begin{bmatrix}
1 & 2 \\
2 & 1 \\
-1 & 4
\end{bmatrix}\begin{bmatrix}
1 \\
0
\end{bmatrix}=\frac{1}{\sqrt{ 6} }\begin{bmatrix}
1 \\
2 \\
-1
\end{bmatrix}$$

Let’s get the orthogonal complement of $\text{span}\left\{ q_{1},q_{2} \right\}$. $q_{3}$ is then $q_{3}= \frac{1}{\sqrt{ 14 }} \begin{bmatrix} -3 \\ 2 \\ 1\end{bmatrix}$.

Thus,
$$A = P\Sigma Q^T = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}\begin{bmatrix}
\sqrt{ 21 } & 0 & 0 \\
0 & \sqrt{ 6 } & 0 \\
0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
\frac{2}{\sqrt{ 21 }} & \frac{1}{\sqrt{ 21 }} & \frac{4}{\sqrt{ 21 }} \\
\frac{1}{\sqrt{ 6 }} & \frac{2}{\sqrt{ 6 }} & -\frac{1}{\sqrt{ 6 }} \\
-\frac{3}{\sqrt{ 14 }} & \frac{2}{\sqrt{ 14 }} & \frac{1}{\sqrt{ 14 }}
\end{bmatrix}$$

#### Exercise 2
Find the singular value decomposition of the matrix,
$$A=\begin{bmatrix}
1 & 1 & 1 \\
-1 & 2 & -1 \\
1 & 0 & -1
\end{bmatrix}$$
As usual,
$$AA^T=\begin{bmatrix}
1 & 1 & 1 \\
-1 & 2 & -1 \\
1 & 0 & -1
\end{bmatrix}\begin{bmatrix}
1 & -1 & 1 \\
1 & 2 & 0 \\
1 & -1 & -1
\end{bmatrix} =\begin{bmatrix}
3 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 2
\end{bmatrix}$$
Then we have eigen values,$\lambda=3,6,2\to \sigma_{1}=\sqrt{ 6 },\sigma_{2}=\sqrt{ 3 },\sigma_{3}=\sqrt{ 2 }$.

$$p_{1} = \begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix},p_{2}=\begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix},p_{3}=\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}$$

Given $$A^T=\begin{bmatrix}
1 & -1 & 1 \\
1 & 2 & 0 \\
1 & -1 & -1
\end{bmatrix}$$

$$q_{1} = \frac{1}{\sigma_{1}}A^Tp_{1} = \frac{1}{\sqrt{ 6 }}\begin{bmatrix}
-1 \\
2 \\
-1
\end{bmatrix}$$
$$q_{2}=\frac{1}{\sigma_{2}}A^Tp_{2}=\frac{1}{\sqrt{ 3 }}\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix}$$
$$q_{3}=\frac{1}{\sigma_{3}}A^Tp_{3}=\frac{1}{\sqrt{ 2 }}\begin{bmatrix}
1 \\
0 \\
-1
\end{bmatrix}$$


Thus,
$$A=\begin{bmatrix}
0  & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
\sqrt{ 6 } & 0 & 0 \\
0 & \sqrt{ 3 } & 0 \\
0 & 0 & \sqrt{ 2 }
\end{bmatrix}\begin{bmatrix}
-\frac{1}{\sqrt{ 6 }} & \frac{2}{\sqrt{ 6 }} & -\frac{1}{\sqrt{ 6 }} \\
\frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 3 }} & \frac{1}{\sqrt{ 3 }} \\
\frac{1}{\sqrt{ 2 }} & 0 & -\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$


#### Exercise 3
Let $X$ be a $n \times p$ normalized data matrix, let $x_{i},x_{j} \in \mathbb{R}^p$ be two different rows of $X$ and let $w_{1}$ be the first weight vector of $X$. Determine whether the statements are true or false.

- if $\lvert \lvert x_{i} \rvert \rvert < \lvert \lvert x_{j} \rvert \rvert$ then $\lvert \langle x_{i},w_{1} \rangle \rvert < \lvert \langle x_{j},w_{1} \rangle \rvert$.
$$\sum \lvert \lvert \langle w_{1},x_{k} \rangle  \rvert  \rvert^2 = \lvert \lvert Aw_{1} \rvert  \rvert ^2$$
is maximized.


Since it’s a sum of projections of the data points on the weight vector $w_{1}$ being maximized. Just because $x_j$  has a longer length than $x_{i}$ doesn’t mean the projections to $w_{1}$ would follow the same.

- if $\langle x_{i},x_{j} \rangle=0$ and $\langle x_{i},w_{1} \rangle=0$ then $\langle x_{j},w_{1} \rangle = 0$ .
They can always be in the same direction.

#### Exercise 4
Let $X$ be a $n\times 2$ data matrix and let $Y$ be the matrix with the same columns as $X$ but switched. In other words, the first column of $Y$ is the same as the the second column of $X$, and the second column of $Y$ is the first column of $X$. Determine whether the statement is true or false.

- If $X$ and $Y$ represent the same set of data points, then all singular values of $X$ are equal.

True, this means that $X$’s columns are symmetric, so
$$X=\begin{bmatrix}
a_{1} & a_{1} \\
\vdots & \vdots \\
a_{n} & a_{n}
\end{bmatrix}$$

$$X^TX = \begin{bmatrix}
a_{1}^2+\cdots+a_{n}^2 & a_{1}^2+\cdots+a_{n}^2  \\
a_{1}^2+\cdots+a_{n}^2  & a_{1}^2+\cdots+a_{n}^2
\end{bmatrix}=\begin{bmatrix}
A & A \\
A & A
\end{bmatrix}$$
Given there is only the singular value of $A$. 

- If $X$ and $Y$ represents the same set of data points, then $w_{1}=\begin{bmatrix} \frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }} \end{bmatrix}^T$.

Given the only eigen value of $A$, 
$$N(X^TX-AI) = N( \begin{bmatrix}
0 & A \\
A & 0
\end{bmatrix} )=\text{span}\left\{ \begin{bmatrix}
1 \\
0
\end{bmatrix} \right\}$$
Hence,
$$w_{1}=q_{1}=\begin{bmatrix}
\frac{1}{\sqrt{ 2 }} & 0
\end{bmatrix}$$
False!

#### Exercise 5
Suppose $X$ is a 100 x 4 data matrix such that 
$$X^TX=\begin{bmatrix}
2 & 0 & 0 & 0 \\
0 & 1.5 & 0 & 0 \\
0 & 0 & 2 & 1 \\
0 & 0 & 1 & 2
\end{bmatrix}$$

$$\det(X^TX-I) = (\lambda-2)(\lambda-1.5)((\lambda-2)(\lambda-2) - 1)$$
$$\to(\lambda-2)(\lambda-1.5)(\lambda-1)(\lambda-3)$$

$$N(X^TX-3I)=N(\begin{bmatrix}
-1 & 0 & 0 & 0 \\
0 & -1.5 & 0 & 0 \\
0 & 0 & -1 & 1 \\
0 & 0 & 1 & -1
\end{bmatrix}) \to q_{1}=\begin{bmatrix}
0 \\
0 \\
1 \\
1
\end{bmatrix}$$
$$N(X^TX-2I)=N(\begin{bmatrix}
0  & 0 & 0 & 0 \\
0 & -0.5 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix})\to q_{2}=\begin{bmatrix}
1 \\
0 \\
0 \\
0
\end{bmatrix}$$
$$N(X^TX-1.5I)=N(\begin{bmatrix}
0.5 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0.5 & 1 \\
0 & 0 & 1 & 0.5 
\end{bmatrix}) \to q_{3}=\begin{bmatrix}
0 \\
1 \\
0  \\
0
\end{bmatrix}$$
$$q_{4}=N(X^TX-I)=N(\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0.5 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1
\end{bmatrix})\to q_{4}=\begin{bmatrix}
0  \\
0 \\
1 \\
-1
\end{bmatrix}$$


Thus,
$$w_{1}=\begin{bmatrix}
0 \\
0 \\
\frac{1}{\sqrt{ 2 }} \\
\frac{1}{\sqrt{ 2 }}
\end{bmatrix},w_{2}=\begin{bmatrix}
1 \\
0 \\
0 \\
0
\end{bmatrix},w_{3}=\begin{bmatrix}
0 \\
1 \\
0 \\
0
\end{bmatrix},w_{4}=\begin{bmatrix}
0 \\
0 \\
\frac{1}{\sqrt{ 2 }} \\
-\frac{1}{\sqrt{ 2 }}
\end{bmatrix}$$


#### Exercise 6
Determine whether the statement is true or false.

- If $N$ is an even integer then the $f_{\frac{N}{2}}$ in the Fourier basis of $\mathbb{C}^N$ has real entries.
$$\overline{f_{\frac{N}{2}}} = f_{ N -\frac{N}{2}}=f_{\frac{N}{2}}$$
true!

- Let $x \in \mathbb{R}^N$ and let $\mathbf{y}=DFT(x)$. Then $\overline{\mathbf{y}[k]}=\mathbf{y}[N-k]$ for all $0<k<N$.

$$\overline{y[k]} = \overline{\langle f_{k},x \rangle } = \overline{f_{k}^T\overline{x}} = \overline{f_{k}^T}x=\langle \overline{f_{k}},x \rangle = \langle f_{N-k},x \rangle =y[N-k] $$
true!

#### Exercise 7
Suppose a signal $x \in \mathbb{R}^9$ of length 9 has real values and let $y=DTX(x)$. Determine all the values of $y$ given the values at even indices.

Using the exercise from above.

$$y[0]=1,y[2]=2+i,y[4]=1+2i,y[6]=1-3i,y[8]=1-i$$
$$y[1]=\overline{y[9-1]}=\overline{y[8]}=1+i$$
$$y[3]=\overline{y[9-3]}=\overline{y[6]}=1+3i$$
$$y[5]=\overline{y[9-5]}=\overline{y[4]}=1-2i$$
$$y[7]=\overline{y[9-7]}=\overline{y[2]}=2-i$$

#### Exercise 8
Let $N$ be an even integer and let $x \in \mathbb{R}^N$ such that $x[n]=1$ if $n$ is even and $x[n]=0$ if $n$ is odd. Find $DFT(x)$.

$$x=\begin{bmatrix}
1 \\
0 \\
1 \\
0 \\
\vdots \\
1 \\
0
\end{bmatrix}$$

$$DFT(x)=F_{N}x = \begin{bmatrix}
\langle f_{0},x \rangle  \\
\langle f_{1},x \rangle  \\
\langle f_{2},x \rangle  \\
\langle f_{3},x \rangle  \\
\vdots \\
\langle f_{N-1},x \rangle  \\
\langle f_{N},x \rangle 
\end{bmatrix}$$

for some $f_k$, $\langle f_{k},x \rangle$ would be
$$\overline{\omega_{N}^0 + \omega_{N}^{2k} + \cdots+\omega_{N}^{k(N-2)}}$$
$$= \sum_{j=0}^{(N-2)/2}\omega_{N}^{-2kj}$$
If $k = 0, \frac{N}{2}$, then $\langle f_{k},x \rangle = \frac{N}{2}$. Else, $\langle f_{k},x \rangle=0$.

$$DFT(x) = \begin{bmatrix}
\frac{N}{2} \\
0 \\
0 \\
\vdots \\ 0 
 \\
\frac{N}{2} \\
0 \\
\vdots \\
0
\end{bmatrix}$$

#### Exercise 9
Let $N$ be an even integer and let $x \in \mathbb{R}^N$ such that $x[n]= 1$ if $n$ is even and $x[n] = -1$ if $n$ is odd. Find $DFT(x)$.

$$x=\begin{bmatrix}
1 \\
-1 \\
1 \\
-1 \\
\vdots \\
1 \\
-1
\end{bmatrix}$$

$$\langle f_{k},x \rangle = x^Tf_{N-k}$$
$$ = \omega_{{N}}^0 -\omega_{N}^{N-k} + \omega_{N}^{2(N-k)} -\omega^{3(N-k)} + \cdots + \omega_{N}^{(N-2)(N-k)} - \omega_{N}^{(N-1)(N-k)}$$
$$= -(\omega_{N}^0 + \omega_{N}^{N-k}+\cdots+\omega_{N}^{(N-1)(N - k)}) + 2(\omega_{N}^0 + \omega_{N}^{2(N-k)}+\cdots+\omega_{N}^{(N-2)(N-k)})  + $$
$$=2(\omega_{N}^0 + \omega_{N}^{2(N-k)}+\cdots+\omega_{N}^{(N-2)(N-k)})$$
$$=\begin{bmatrix}
N \\
0 \\
0 \\
\vdots \\
0 \\
N \\
0 \\
\vdots \\
0
\end{bmatrix}$$


#### Exercise 10 
Let $N$ be an integer and let $x \in \mathbb{R}^n$ such that $x[0]=0$ and $x[n]=1$ for $0 < n < N$. Find $DFT(x)$.

$$x = \begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
1
\end{bmatrix}$$
$$\langle x,f_{k} \rangle = \omega_{N}^{N-k}+\cdots+\omega_{N}^{(N - 1)(N-k)} 
$$
$$=(\omega_{N}^0 + \cdots+\omega_{N}^{(N-1)(N-k)}) - \omega_{N}^0$$if $k = 0$, we get $N - 1$; otherwise we get $-1$.

$$DFT(x) = \begin{bmatrix}
N-1 \\
-1 \\
-1 \\
\vdots \\
-1
\end{bmatrix}$$

#### Exercise 11
Find a formula for $x$ as a sum of sinusoids given
$$DFT(x)=\begin{bmatrix}
1 & 3-3i & 2\sqrt{ 3 }+2i & -4i & 4i & 2\sqrt{ 3 }-2i & 3+3i 
\end{bmatrix}^T$$

It will be in the form,
$$x = A_{0}f_{0}+A_{1}\cos(2\pi \mathbf{t}+\varphi_{1})+A_{2}\cos(4\pi \mathbf{t}+\varphi_{2}) + A_{3}\cos(6\pi \mathbf{t}+\varphi_{3})$$

$$DFT(A_{0}f_{0})=NA_{0}\mathbf{e}_{0} = 1\mathbf{e_{0}} \to A_{0}  = \frac{1}{7}$$
$$3-3i = 3\sqrt{ 2 } \left( \frac{1}{\sqrt{ 2 }} - \frac{1}{\sqrt{ 2 }}i \right) =3\sqrt{ 2 }e^{-\pi/4 i} = \frac{NA_{1}}{2}e^{\varphi_{1}i}$$
$$A_{1} = \frac{6\sqrt{ 2 }}{7},\varphi_{1}=-\frac{\pi}{4}$$

$$2\sqrt{ 3 }+2i = 4\left( \frac{\sqrt{ 3}}{2}+\frac{1}{2}i \right)=4e^{\pi/6i}= \frac{NA_{2}}{2}e^{\varphi_{2}i}$$
$$A_{2}=\frac{8}{7},\varphi_{2}= \frac{\pi}{6}$$
$$-4i  =4(-i) = 4e^{ - \pi/2i} = \frac{NA_{3}}{2}e^{\varphi_{3}i}$$
$$A_{3}= \frac{8}{7},\varphi_{3}=-\frac{\pi}{2}$$


$$x= \frac{1}{7}f_{0} + \frac{6\sqrt{ 2 }}{7}\cos\left( 2\pi \mathbf{t} -\frac{\pi}{4} \right) + \frac{8}{7}\cos\left( 4\pi \mathbf{t} + \frac{\pi}{6} \right) + \frac{8}{7}\cos\left( 6\pi \mathbf{t}-\frac{\pi}{2} \right)$$

#### Exercise 12
![[Screenshot 2024-12-17 at 8.59.15 PM.png]]
Sketch the signal $x$ such that the magnitude and phase plots of $y=DFT(x)$ are like the above.

$$A_{0} = 100, A_{4}=50$$
$$\varphi_{4} = \frac{3\pi}{4}$$
$$\therefore 100 + 50 \cos\left( 8\pi \mathbf{t} + \frac{3\pi}{4} \right)$$

#### Exercise 13
![[Screenshot 2024-12-17 at 9.17.54 PM.png]]
![[Pasted image 20241217211821.png]]
