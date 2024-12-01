Let’s recall some complex numbers,
$$z=a+bi=re^{i\theta}$$
$$\theta=\tan ^{-1}\left( \frac{b}{a} \right),r=\sqrt{ a^2+b^2 },a=r\cos \theta,b=r\sin \theta$$
where $a,b \in \mathbb{R}$ and $i^2=-1$.

Euler’s formula states that
$$e^{i\theta}=\cos \theta+i\sin \theta$$
and particularly $e^{i\pi}=-1$.

We have some neat properties for complex numbers,
$$\lvert z \rvert =r=\sqrt{ a^2+b^2 },\text{ angle (argument)} = \theta, \bar{z}=a-bi=e^{-i\theta}$$
$$z^{-1}=\frac{1}{z}=\frac{z}{\lvert z \rvert ^2} \leftarrow \bar{z}z=(a- bi)(a+bi)=a^2+b^2=\lvert z \rvert ^2$$

The conjugate of a complex vector is
$$\bar{v}=\begin{bmatrix}
\bar{v_{0}} \\
\bar{v_{1}} \\
\vdots \\
\bar{v_{N-1}}
\end{bmatrix}$$

Note that
$$\bar{(z_{1}z_{2})}=\bar{z_{1}z_{2}}$$
$$\bar{Az}=\bar{A}\bar{z}$$
$$\bar{(z_{1}+z_{2})}=\bar{z_{1}}+\bar{z_{2}}$$
$$\bar{cz}=\bar{c}\bar{z}$$

#### Definition of Complex Inner Product
$$\langle v,w \rangle=v^T \bar{w}=\begin{bmatrix}
v_{0} & v_{1} & \cdots & v_{N-1}
\end{bmatrix} \bar{\begin{bmatrix}
w_{0} \\
w_{1} \\
\vdots \\
w_{N-1}
\end{bmatrix}}=v_{0}\bar{w_{0}}+v_{1}\bar{w_{1}}+\cdots+v_{N-1}\bar{w_{N-1}}$$

We also have that,
$$\langle v,w \rangle=\overline{\langle w,v \rangle }=\overline{w_{0}\overline{v_{0}}+\cdots+w_{N-1}\overline{v_{N-1}}} $$

###### Example
Compute the inner product between, $u=(i,2i,1-i,4),v=(1-i,1+i,i,i)$.
$$\langle u,v \rangle =i*(1+i)+2i*(1-i)+(1-i)*(-i)+4*(-i)$$
$$=i-1+2i+2-i-1-4i=-2i\neq_{}0$$


#### Hermitian Matrix
Note that,
$$\langle Av,w \rangle =(Av)^T\overline{w}=v^TA^T\overline{w}=v^T\overline{(\overline{A}^Tw)}=\langle v,\overline{A}^Tw \rangle $$

A matrix is hermitian if $\overline{A}^T=A$. Then, we have
$$\langle Av,w \rangle =\langle v,Aw \rangle $$
This is what a symmetric real matrix would look like in the complex world.

What we know about orthogonal matrices is that $Q^{-1}=Q^T$. This gave us properties like $\lvert \lvert Qu \rvert \rvert=\lvert \lvert u \rvert \rvert$ and $\langle Qu,Qv \rangle=\langle u,v \rangle$ for a real orthogonal matrix $Q$ and real vectors $u,v$.

Now, let $A \in \mathbb{C}^{n\times n}$
$$\langle Ax,Ay \rangle =(Ax)^T\overline{Ay}=x^TA^T\overline{Ay}=x^T\overline{\overline{A^T}Ay}$$
$$=\langle x^T,\overline{A^T}Ay \rangle $$

hence, we require $\overline{A^T}A=I$ to have that $\langle Ax,Ay \rangle=\langle x,y \rangle$. This property is called being **unitary**.

#### Roots of Unity
A complex number is an $N$th root of unity if $\omega^N=1$. Given $N$, set $\omega_{N}=e^{2\pi i/N}$ and let $w_{N}^k=e^{2\pi ik/N}$ for $k=0,1,\cdots,N-1$.

###### Example
$N=8$ then the we have $\omega_{8}^k=e^{2i\pi k/8}$. 
$$w_{8}^0=1,w_{8}^1=e^{i\pi/4}=\frac{1}{\sqrt{ 2 }}+\frac{1}{\sqrt{ 2 }}i,\cdots$$

##### Properties
- $\overline{\omega_{N}}=\omega_{N}^{N-1}$

$$\overline{e^{2\pi i/N}}=e^{-2\pi i/N}=e^{2\pi i}*e^{-2\pi i/N}=e^{2\pi i(\frac{N-1}{N})}=\omega_{N}^{N-1}$$

- $\overline{\omega_{N}}=\omega_{N}^{-1}$

$$\omega_{N}^{-1}=\frac{1}{e^{2\pi i/N}}=e^{-2\pi i/N}=\overline{\omega_{N}}$$

- $\omega_{N}^N=1$

$$\omega_{N}^N=(e^{2\pi i/N})^N=e^{2\pi i}=1$$

- $\omega_{N}^k=\cos \frac{2\pi k}{N}+i \sin \frac{2\pi k}{N}$
$$\omega_{N}^k=(e^{2\pi i/N})^k=e^{2\pi i(k/N)}= \cos \frac{2\pi k}{N}+i \sin \frac{2\pi k}{N}$$

#### Theorem
Fix $N$, Let $0<k<N$ with $k,N \in \mathbb{Z}$. Then
$$\sum_{n=0}^{N-1}\omega_{N}^{kn}=0$$

[Proof]
$$\sum_{n=0}^{N-1}\omega _{N}^{kn}= \frac{1-\omega_{N}^{kN} }{1-\omega_{N}^k} = \frac{1-e^{2\pi ik}}{1-\omega_{N}^k} = \frac{1-1^k}{1-\omega_{N}^k} = 0$$

#### Definition of Fourier Basis
The Fourier Basis of $\mathbb{C}^n$ is $f_{0},f_{1},\cdots,f_{N-1}$ where
$$f_{k}=\begin{bmatrix}
w_{N}^0 \\
w_{N}^k \\
\vdots \\
w_{N}^{N-1}
\end{bmatrix}$$


###### Example
Let $N=2$ then we have $\omega_{2}^0=1,\omega_{2}^1=e^{2\pi i/2}=e^{\pi i}=-1$, thus
$$f_{0}=\begin{bmatrix}
1 \\
1
\end{bmatrix},f_{1}=\begin{bmatrix}
1 \\
-1
\end{bmatrix}$$

for $N=4$, then $\omega_{4}^0=1,\omega_{4}^1=e^{2\pi i/4}=i$
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
\end{bmatrix}, f_{3} = \begin{bmatrix}
1 \\
-i \\
-1 \\
i
\end{bmatrix}$$

#### Theorem
The Fourier basis $f_{0},f_{1},\cdots,f_{N-1} \in \mathbb{C}^n$ is an orthogonal basis. In particular,
$$  
\begin{equation}
    \langle f_{k},f_{l} \rangle =
    \begin{cases}
      0, & \text{if}\ k\neq l \\
      N, & \text{if}\ k = l
    \end{cases}
  \end{equation}
$$

[Proof]

$$\langle f_{k},f_{l} \rangle =\begin{bmatrix}
\omega_{N}^0 & \omega_{N}^k & \cdots & \omega_{N}^{(N-1)k}
\end{bmatrix}\overline{\begin{bmatrix}
\omega_{N}^0 \\
\omega_{N}^l \\
\vdots \\
\omega_{N}^{l(N-1)}
\end{bmatrix}}$$
$$=\omega_{N}\overline{\omega_{N}} + \omega_{N}^k \overline{\omega_{N}^l}+\cdots+\omega_{N}^{k(N-1)}\overline{\omega_{N}^{l(N-1)}}$$
$$=\omega_{N}+\omega_{N}^{k-l}+\cdots+\omega_{N}^{(N-1)(k-l)}=\sum_{n=0}^{N-1}\omega_{N}^{n(k-l)}$$
and if $k = l$, 
$$\sum_{n=0}^{N-1}\omega_{N}^{n(k-l)}=\sum_{n=0}^{N-1}1=N$$
and if $k\neq l$,
$$\sum_{n=0}^{N-1}\omega_{N}^{n(k-l)}=0$$
according to the theorem above.