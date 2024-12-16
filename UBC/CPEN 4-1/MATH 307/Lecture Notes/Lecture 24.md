Just to re-iterate (I know, it’s redundant.. don’t really care),
#### Theorem
Let $bx=A\cos(2\pi k\mathbf{t}+\varphi)$. Then, we have 
$$DFT(\mathbf{x})= \frac{AN}{2}e^{i\varphi}\mathbf{e}_{k}+ \frac{AN}{2}e^{-i\varphi}\mathbf{e}_{N-k}$$
for $0 < k <N$, where $e^{i\varphi}=\cos(\varphi)+i\sin(\varphi)$ and $\mathbf{e}_{0},\cdots,\mathbf{e}_{N-1}$ are the standard basis vectors. In other words,
$$DFT(\mathbf{x})=\begin{bmatrix}
0 \\
\vdots \\
0 \\
\frac{AN}{2}e^{i\varphi} \\
0 \\
\vdots \\
0 \\
\frac{AN}{2}e^{-i\varphi} \\
0 \\
\vdots \\
0
\end{bmatrix}$$

In particular, when $N$ is even and $k = \frac{N}{2}$, we have
$$DFT(\mathbf{x})= \frac{AN}{2}e^{i\varphi}\mathbf{e}_{\frac{N}{2}}+ \frac{AN}{2}e^{-i\varphi}\mathbf{e}_{\frac{N}{2}}=\frac{AN}{2}\mathbf{e}_{\frac{N}{2}}(e^{i\varphi}+e^{-i\varphi})$$
$$=AN\mathbf{e}_{\frac{N}{2}}\cos(\varphi)=\begin{bmatrix}
0 \\
\vdots \\
0 \\
AN \cos(\varphi) \\
0 \\
\vdots \\
0
\end{bmatrix}$$

###### Remark
If $\mathbf{x}=A_{0}f_{0}$ is a constant, then $DFT(\mathbf{x})=AN\mathbf{e}_{0}$.

[Proof]
$$DFT(\mathbf{x})=\begin{bmatrix}
\overline{f_{0}}^T \\
\vdots \\
\overline{f_{N-1}}^T
\end{bmatrix}A_{0}f_{0}=A_{0}\begin{bmatrix}
N \\
0 \\
\vdots \\
0
\end{bmatrix}=AN\mathbf{e}_{0}$$
###### Proof of Theorem
$$\mathbf{x}=A\cos(2\pi k\mathbf{t}+\varphi)=A\cos(2\pi k\mathbf{t})\cos(\varphi)-A\sin(2\pi k\mathbf{t})\sin(\varphi)$$
$$=(A\cos(\varphi))\cos(2\pi k \mathbf{t})-(A\sin(\varphi))\sin(2\pi k\mathbf{t})$$
$$=(A\cos(\varphi))\left( \frac{\mathbf{f}_{k}+\overline{\mathbf{f}_{k}}}{2} \right)-(A\sin(\varphi))\left( \frac{\mathbf{f}_{k}-\overline{\mathbf{f}_{k}}}{2i} \right)$$
Also,
$$DFT(\mathbf{f}_{k})=\begin{bmatrix}
\overline{\mathbf{f}_{0}}^T \\
\vdots \\
\overline{\mathbf{f}_{N-1}}^T
\end{bmatrix}\mathbf{f}_{k}=N\mathbf{e}_{k}$$
since $\overline{\mathbf{f}_{k}}=\mathbf{f}_{N-k}$, we obtain
$$DFT(\mathbf{x})= A\cos (\varphi)\frac{(DFT(\mathbf{f}_{k})+DFT(\overline{\mathbf{f}}_{k}))}{2} - A\sin (\varphi)\frac{DFT(\mathbf{f}_{k})-DFT(\overline{\mathbf{f}}_{k})}{2i}$$
$$=\left( \frac{A\cos(\varphi)}{2} - \frac{A\sin(\varphi)}{2i} \right)N\mathbf{e}_{k}+\left(  \frac{A\cos(\varphi)}{2}+ \frac{ A\sin(\varphi)}{2i} \right)N\mathbf{e}_{N-k}$$
$$= \frac{A}{2} (\cos(\varphi)+ i\sin(\varphi))N\mathbf{e}_{k}+\frac{A}{2} (\cos(\varphi) - i\sin(\varphi))N\mathbf{e}_{N-k}$$
$$=\frac{AN}{2} e^{i\varphi}\mathbf{e}_{k}+\frac{AN}{2}e^{-i\varphi}\mathbf{e}_{N-k}$$

###### Remark
If $\mathbf{x}=A_{0}\mathbf{f}_{0}+ \sum_{k=1}^{N/2}A_{k}\cos(2\pi k\mathbf{t}+\varphi_{k})$ is a sum of sinusoids, then
$$DFT(\mathbf{x})=\begin{bmatrix}
A_{0}N \\
\frac{A_{1}N}{2}e^{i\varphi_{1}} \\
\frac{A_{2}N}{2}e^{i\varphi_{2}} \\ 
\vdots \\
\frac{A_{1}N}{2}e^{-i\varphi_{1}} \\
\end{bmatrix}$$


In another way, if $\mathbf{x} = A_{1}\cos(2\pi k_{1}\mathbf{t}+\varphi_{1})+\cdots+A_{m}\cos(2\pi k_{m}\mathbf{t}+\varphi_{m})$, then
$$DFT(\mathbf{x})=\left(  \frac{A_{1}N}{2}e^{i\varphi_{1}}\mathbf{e}_{k_{1}} +\frac{A_{1}N}{2}e^{-i\varphi_{1}}\mathbf{e}_{N-k_{1}} \right)$$
$$+\cdots+\left(  \frac{A_{m}N}{2}e^{i\varphi_{m}}\mathbf{e}_{k_{m}} +\frac{A_{m}N}{2}e^{-i\varphi_{m}}\mathbf{e}_{N-k_{m}} \right)$$

###### Example
Let $x \in \mathbb{R}^5$ such that $DFT(x)=\begin{bmatrix} 1 \\ 1+i\\2-i\\2+i \\ 1-i\end{bmatrix}$. Write $x$ as a sum of sinusoids.

Recall that from the previous remark that
$$x=A_{0}f_{0}+A_{1}\cos(2\pi k_{1} \mathbf{t}+\varphi_{1})+A_{2}(\cos{2}\pi k_{2}\mathbf{t}+\varphi_{2})$$

Note that $y[0]=A_{0}N= 1$ and since $N= 5$, we have that $A_{0}=\frac{1}{5}$.

Next, 
$$y[1]= \frac{A_{1}N}{2}e^{i\varphi}=1+i = \sqrt{ 2 }e^{i \pi/4}$$
Then, $\varphi_{1}=\frac{\pi}{4}$ and $A_{1}= \frac{2\sqrt{ 2 }}{5}$

Finally,
$$y[2]= \frac{A_{2}N}{2}e^{i\varphi_{2}}=2-i=\sqrt{ 5 }\left( \frac{2}{\sqrt{ 5 }} - \frac{i}{\sqrt{ 5 }} \right)=\sqrt{ 5 }e^{i\varphi_{2}}$$
Then we have $A_{2}= \frac{2\sqrt{ 5 }}{5}$ and $\varphi=\arctan\left( -\frac{1}{2} \right)$

