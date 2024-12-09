We showed that the Fourier basis of $\mathbb{C}^n$ was consisted of $f_k$ which was defined as,
$$f_{k}=\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^k \\
\omega_{N}^{2k} \\
\vdots \\
\omega_{N}^{k(N-1)}
\end{bmatrix} = \begin{bmatrix}
1 \\
e^{2\pi ik/N} \\
e^{2\pi i(2k)/N} \\
\vdots \\
e^{2\pi i(N-1)k/N}
\end{bmatrix}$$
for $k \in \left\{ 1,\cdots,N-1 \right\}$.

The standard basis of $\mathbb{C}^n$ is formed by the set of vectors $e_{1},\cdots,e_{N}$ where 
$$e_{k}=\begin{bmatrix}
0 \\
\vdots \\
0 \\
1 \\
0 \\
\vdots \\
0
\end{bmatrix}$$
where $e_{k} \in \mathbb{R}^n$ is a vector with the only nonzero element given at the index $k$.

#### Theorem
We have $\overline{f_{k}}=f_{N-k}$ where $0<k<N$.

[Proof]
$$\overline{f_{k}}=\overline{\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^k \\
\omega_{N}^{2k} \\
\vdots \\
\omega_{N}^{k(N-1)}
\end{bmatrix}} = 
\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^{-k} \\
\vdots \\
\omega_{N}^{-k(N-1)}
\end{bmatrix}=\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^{N-k} \\
\vdots \\
\omega_{N}^{(N-1)N-(N-1)k}
\end{bmatrix}$$
$$=\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^{N-k} \\
\vdots \\
\omega_{N}^{(N-1)(N-k)}
\end{bmatrix}=f_{N-k}$$
as required.


Also, if $N$ is even, then $\overline{f_{\frac{N}{2}}}=f_{N-\frac{N}{2}}=f_{\frac{N}{2}}$ hence showing that the entries of $f_{\frac{N}{2}}$ are all real numbers.

Moreover,
$$f_{\frac{N}{2}}=\begin{bmatrix}
\omega_{\frac{N}{2}}^0 \\
\omega_{\frac{N}{2}}^{\frac{N}{2}} \\
\omega_{\frac{N}{2}}^{\frac{N}{2} \times 2} \\
\vdots \\
\omega_{\frac{N}{2}}^{\frac{N}{2}\times(N-1)}
\end{bmatrix}
=\begin{bmatrix}
1 \\
e^{2\pi i} \\
e^{4\pi i} \\
\vdots \\
e^{(N-1)2\pi i}
\end{bmatrix}=\begin{bmatrix}
1 \\
-1 \\
1 \\
\vdots \\
-1
\end{bmatrix}$$

Given a vector $x \in \mathbb{C}^n$, we want to project it onto $f_{0},f_{1},\cdots,f_{N-1}$, which gives
$$x= \frac{\langle x,f_{0} \rangle }{\langle f_{0},f_{0} \rangle }f_{0}+\frac{\langle x,f_{1} \rangle }{\langle f_{1},f_{1} \rangle }f_{1}+\cdots+\frac{\langle x,f_{N-1} \rangle }{\langle f_{N-1},f_{N-1} \rangle }f_{N-1}$$
$$=\frac{1}{N}\begin{bmatrix}
f_{0} & f_{1} & \cdots & f_{N-1}
\end{bmatrix}\begin{bmatrix}
\langle x,f_{0} \rangle  \\
\langle x,f_{1} \rangle  \\
\vdots \\
\langle x,f_{N-1} \rangle 
\end{bmatrix}$$
$$= \frac{1}{N}\begin{bmatrix}
f_{0} & f_{1} & \cdots f_{N-1}
\end{bmatrix}\begin{bmatrix}
\overline{f_{0}}^T \\
\overline{f_{1}}^T \\
\vdots \\
\overline{f_{N-1}}^T
\end{bmatrix}x$$

The Discrete Fourier Transform (DFT) is 
$$DFT(x)= F_{N}x$$
where $F_{N}=\begin{bmatrix}\overline{f_{0}}^T \\ \overline{f_{1}}^T \\ \vdots \\ \overline{f_{N-1}}^T \end{bmatrix}$.

Why such $F_N$? Since,

$$F_{N}=\begin{bmatrix}\overline{f_{0}}^T \\ \overline{f_{1}}^T \\ \vdots \\ \overline{f_{N-1}}^T \end{bmatrix}=\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \overline{\omega_{N}} & \overline{\omega_{N}}^2  & \cdots & \overline{\omega_{N}}^{N-1} \\
1 & \overline{\omega_{N}}^2 & \overline{\omega_{N}}^4 & \cdots & \overline{\omega_{N}}^{2(N-1)} \\
1 & \vdots & \vdots & \ddots & \vdots \\
1 & \overline{\omega_{N}}^{N-1} & \overline{\omega_{N}}^{2(N-1)}  & \cdots & \overline{\omega_{N}}^{(N-1)(N-1)}
\end{bmatrix}$$
and
$$x= \frac{\langle x,f_{0} \rangle }{\langle f_{0},f_{0} \rangle }f_{0}+\frac{\langle x,f_{1} \rangle }{\langle f_{1},f_{1} \rangle }f_{1}+\cdots+\frac{\langle x,f_{N-1} \rangle }{\langle f_{N-1},f_{N-1} \rangle }f_{N-1}$$

$DFT(x)$ is the vector of coefficients to $x$ with respect to the Fourier basis,
$$\therefore DFT(x)=F_{N}x$$

Also, note that we have
$$F_{N}\overline{F_{N}}^T=I$$

$$F_{N}\overline{F_{N}}^T=\begin{bmatrix}
\overline{f_{0}}^T \\
\overline{f_{1}}^T \\
\vdots \\
\overline{f_{N-1}}^T
\end{bmatrix}\begin{bmatrix}
f_{0} & f_{1} & \cdots & f_{N-1}
\end{bmatrix}$$
$$ = \begin{bmatrix}
\overline{f_{0}}^T{f_{0}} & \overline{f_{0}}^T{f_{1}} & \cdots & \overline{f_{0}}^T{f_{N-1}} \\
\overline{f_{1}}^T{f_{0}} & \overline{f_{1}}^T{f_{1}} & \cdots & \overline{f_{1}}^T{f_{N-1}} \\
\vdots &  & \vdots  & \vdots \\
\overline{f_{N-1}}^T{f_{0}} & \overline{f_{N-1}}^T{f_{1}} & \cdots & \overline{f_{N-1}}^T{f_{N-1}}
\end{bmatrix}$$

Since we know that,
$$\overline{f_{k}}^Tf_{l}=\langle \overline{f_{k}},\overline{f_{l}} \rangle = \begin{cases}
0, \text{if }k\neq l \\
N, \text{if }k=l
\end{cases} $$
we get
$$F_{N}\overline{F_{N}}^T=\begin{bmatrix}
N & 0 & \cdots & 0 \\
0 & N & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & N
\end{bmatrix}$$

$F_N$ is not unitary, but $\frac{1}{\sqrt{ N }}F_{N}$ is.

###### Example
Compute $DFT(x)$ for $x=\begin{bmatrix}1\\2\\2\\1\end{bmatrix}$.

$$\omega_{N}=\omega_{4}=e^{2\pi i/4}=i$$
$$f_{0}=\begin{bmatrix}
1 \\
1 \\
1 \\
1
\end{bmatrix},f_{1}=\begin{bmatrix}
1 \\
i \\
-1 \\
-i
\end{bmatrix},f_{2}=\begin{bmatrix}
1 \\
-1 \\
1 \\
-1
\end{bmatrix},f_{4}=\begin{bmatrix}
1 \\
-i \\
-1 \\
i
\end{bmatrix}$$

then we have,
$$y_{0}=\langle x,f_{0}  \rangle= x^T\overline{f_{0}}=6 $$
$$y_{1}=\langle x,f_{1} \rangle =x^T\overline{f_{1}}=1\times 1 + 2 \times -i + 2 \times - 1+ 1 \times i=1-2i-2+i=-1-i$$
$$y_{2}=\langle x,f_{2} \rangle =x^T\overline{f_{2}}=1\times 1 + 2 \times -1 + 2 \times 1 + 1 \times -1 = 1-2+2-1=0$$
$$y_{3}=\langle x,f_{3} \rangle=x^T\overline{f_{3}} =1\times 1 +2 \times i + 2 \times -1 + 1 \times -i =1+2i-2-i=-1+i$$


#### Theorem
Let us have $x \in \mathbb{R}^n$ and denote $y\in DFT(x) \in \mathbb{C}^n$. Then, we have that
$$\overline{y[k]}=y[N-k]$$
for $0 < k  < N$.

###### Terminology
We use the notation $x[k]=x_{k}$ for a vector x.

###### Inverse Fourier Transform
$$IDFT(y) = \frac{1}{N}\overline{F_{N}}^Ty$$

[Proof]
$$\overline{y[k]}=\overline{\langle x,f_{k} \rangle }=\overline{x^T\overline{f_{k}}}=\overline{x^Tf_{N-k}}=x^T\overline{f_{N-k}}=\langle x,f_{N-k} \rangle =y[N-k]$$


#### Sinusoids
Let $N$ be a positive integer and let
$$\mathbf{n}=\begin{bmatrix}
0 \\
1 \\
\vdots \\
N-1
\end{bmatrix},\hspace{.2in} \mathbf{t} = \frac{1}{N}\mathbf{n}=\begin{bmatrix}
0 \\
\frac{1}{N} \\
\vdots \\
\frac{N-1}{N}
\end{bmatrix}$$

Then, for the Fourier basis vectors, we have
$$f_{k}=\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^k \\
\omega_{N}^{2k} \\
\vdots \\
\omega_{N}^{(N-1)k}
\end{bmatrix}=\begin{bmatrix}
1 \\
e^{2\pi ik/N} \\
e^{2\pi i (2k)/N} \\
\vdots \\
e^{2\pi i(N-1)/N}
\end{bmatrix}=e^{2\pi i k \mathbf{t}}$$

With this notation, we can also write
$$f_{k}=\begin{bmatrix}
\cos\left( \frac{2\pi(0)}{N} \right)+i\sin\left( \frac{2\pi (0)}{N} \right) \\
\cos\left( \frac{2\pi k}{N} \right)+i\sin\left( \frac{2\pi k}{N} \right) \\
\vdots \\
\cos\left( \frac{2\pi(N-1)k}{N} \right)+i\sin\left( \frac{2\pi (N-1)k}{N} \right)
\end{bmatrix}=\cos(2\pi k\mathbf{t}) +i\sin(2\pi k\mathbf{t})$$

#### Definition of sinusoid
A sinusoid is a vector $\mathbf{x} \in \mathbb{R}^n$ of the form
$$\mathbf{x}=A\cos(2\pi k\mathbf{t}+\varphi)$$
where $A\in \mathbb{R}$ is the amplitude, $k \in \mathbb{Z}$ is the frequency and $\varphi \in \mathbb{R}$ is the phase shift. Usually we have
$$0\leq k<N,-\pi\leq \varphi\leq \pi,A\geq 0$$

#### Theorem
We have
1. $\mathbf{f}_{k}=\cos(2\pi k\mathbf{t})+i\sin(2\pi k\mathbf{t})$
2. $\cos(2\pi k\mathbf{t})=\frac{1}{2}(\mathbf{f}_{k}+\overline{\mathbf{f}_{k}})$ $$\frac{1}{2}(\mathbf{f}_{k}+\overline{\mathbf{f}_{k}})=\frac{1}{2}(\cos(2\pi k\mathbf{t})+i\sin(2\pi k\mathbf{t})+\cos(2\pi k\mathbf{t})-i\sin(2\pi k\mathbf{t}))=\cos(2\pi k\mathbf{t})$$
3. $\sin(2\pi k\mathbf{t})=\frac{1}{2i}(\mathbf{f}_{k}-\overline{\mathbf{f}_{k}})$

#### Theorem
Let $\mathbf{x}=A\cos(2\pi k\mathbf{t}+\varphi)$, then we have
$$DFT(\mathbf{x})= \frac{AN}{2}e^{i\varphi}\mathbf{e}_{k}+\frac{AN}{2}e^{-i\varphi}\mathbf{e}_{N-k}$$
for $0<k<N$, where $e^{i\varphi}=\cos \varphi+i\sin \varphi$ and $\mathbf{e}_{0},\cdots,\mathbf{e}_{N-1}$ are the standard basis vectors.

We first use the fact that,
$$DFT(f_{k})=N\mathbf{e}_{k}$$
$$F_{N}f_{k}=F_{N}=\begin{bmatrix}\overline{f_{0}}^T \\ \overline{f_{1}}^T \\ \vdots \\ \overline{f_{N-1}}^T \end{bmatrix}f_{k} = \begin{bmatrix}
0 \\
0 \\
\vdots \\
0 \\
N \\
0 \\
\vdots \\
0
\end{bmatrix}=\mathbf{e}_{k}$$

$$DFT(\cos(2\pi k\mathbf{t}))=\frac{1}{2}DFT(\mathbf{f}_{k}+\overline{\mathbf{f}_{k}})=\frac{1}{2}DFT(\mathbf{f}_{k}+\mathbf{f}_{N-k})$$
$$=\frac{1}{2}(N\mathbf{e}_{k}+N\mathbf{e}_{N-k})$$
And,

$$DFT(\sin(2\pi k\mathbf{t}))=\frac{1}{2i}DFT(\mathbf{f}_{k}-\overline{\mathbf{f}_{k}})=\frac{1}{2i}DFT(\mathbf{f_{k}-\mathbf{f}_{N-k}})$$
$$=\frac{1}{2i}(N\mathbf{e}_{k}-N\mathbf{e}_{N-k})$$


Then,
$$DFT(\mathbf{x})=DFT(A\cos(2\pi k\mathbf{t}+\varphi))$$
$$=A\cos(\varphi)DFT(\cos(2\pi k\mathbf{t}))-A\sin(\varphi)DFT(\sin(w\pi k\mathbf{t}))$$
$$=A\cos(\varphi)\times \frac{1}{2}N(\mathbf{e}_{k}+\mathbf{e}_{N-k})-A\sin(\varphi)\times \frac{1}{2i}N(\mathbf{e}_{k}-\mathbf{e}_{N-k})$$
$$= \frac{AN}{2}(\cos(\varphi)+i\sin(\varphi))\mathbf{e}_{k} + \frac{AN}{2}(\cos(\varphi)-i\sin(\varphi))\mathbf{e}_{N-k}$$
$$\therefore \frac{AN}{2}e^{i\varphi}\mathbf{e}_{k}+ \frac{AN}{2}e^{-i\varphi}\mathbf{e}_{N-k}$$