### Example for needing to solve many linear systems with the same $A$
Consider an invertible matrix $A\in \mathbb{R}^{n\times n}$. The inverse is the matrix $A^{-1}$ such that $AA^{-1}=A^{-1}A = I$.

Let us introduce the following vectors $\mathbf{e}^{(i)}$ such that
$$\mathbf{e}^{(i)} = \begin{bmatrix}
0  \\
\vdots \\
0 \\
1 \\
0 \\
\vdots \\
0
\end{bmatrix}$$

This is a vector of all zeros except 1 in the $i$-th element. Then, we can write the identity matrix as 
$$I = \begin{bmatrix} \vert  & \vert  & \cdots & |\\

\mathbf{e}^{(1)} & \mathbf{e}^{(2)} & \cdots & \mathbf{e}^{(n)}
 \\
| & | & \cdots & |
\end{bmatrix}$$

Use vectors $\mathbf{x}^{(i)}$ to denote the $i$-th column of matrix $A^{-1}$, that is 
$$A^{-1} = \begin{bmatrix} \vert  & \vert  & \cdots & |\\

\mathbf{x}^{(1)} & \mathbf{x}^{(2)} & \cdots & \mathbf{x}^{(n)}
 \\
| & | & \cdots & |
\end{bmatrix}$$

Then, our problem for finding the inverse can be written as,
$$AA^{-1}=I\leftrightarrow A\begin{bmatrix} \vert  & \vert  & \cdots & |\\

\mathbf{x}^{(1)} & \mathbf{x}^{(2)} & \cdots & \mathbf{x}^{(n)}
 \\
| & | & \cdots & |
\end{bmatrix} = \begin{bmatrix} \vert  & \vert  & \cdots & |\\

\mathbf{e}^{(1)} & \mathbf{e}^{(2)} & \cdots & \mathbf{e}^{(n)}
 \\
| & | & \cdots & |
\end{bmatrix}$$

By performing the matrix-matrix multiplication, this is simply,
$$\begin{bmatrix} \vert  & \vert  & \cdots & |\\

A\mathbf{x}^{(1)} & A\mathbf{x}^{(2)} & \cdots & A\mathbf{x}^{(n)}
 \\
| & | & \cdots & |
\end{bmatrix} $$

that is, each column of the result is $A$ multiplied by the corresponding column of $A^{-1}$. This gives us $n$ systems,
$$A\mathbf{x}^{(1)}=\mathbf{e}^{(1)}$$
$$A\mathbf{x}^{(2)}=\mathbf{e}^{(2)}$$
$$\vdots$$
$$A\mathbf{x}^{(n)}=\mathbf{e}^{(n)}$$

## Relative Error Analysis and Matrix Norms
It is pretty intuitive to know that a change of $A$ can lead to changes in the solution $\mathbf{x}$. We will focus on the effect of the changes in $\mathbf{b}$ in the solution of a linear system. In particular, we have
$$A\mathbf{x}=\mathbf{b}$$
and we want to see, if we observe instead $\mathbf{b}=\mathbf{b}+\Delta \mathbf{b}$ with the perturbation $\Delta \mathbf{b}$, how the solution to the system changes.
$$A(\mathbf{x}+\Delta \mathbf{x}) = \mathbf{b}+\Delta \mathbf{b}$$
By direct calculation, we have
$$A\Delta \mathbf{x}=\Delta\mathbf{b}$$

We want to aim the two quantities, the *relative change* in the solution, that is:
$$\frac{\Delta \mathbf{x}}{\mathbf{x}} \text{ and } \frac{\Delta \mathbf{b}}{\mathbf{b}}$$
### Vector Norms
In particular, we will use $\lvert \lvert x \rvert \rvert$ for $l_2$ (Euclidean norm) norm of $\mathbf{x}$, that is
$$\lvert \lvert x \rvert  \rvert =\sqrt{x_{1}^2+x_{2}^2+\cdots+x_{n}^2 }$$

#### Properties of norms
A **norm** on $\mathbb{R}^n$ is a function that is in the form $\lvert \lvert \cdot \rvert  \rvert$ such that:
- $\lvert \lvert x \rvert \rvert\geq 0$ for all $x\in\mathbb{R}^n$.
- $\lvert \lvert x \rvert \rvert =0$ if and only if $x=0$.
- $\lvert \lvert cx \rvert \rvert=\lvert c \rvert \lvert \lvert x \rvert \rvert$ for any $c\in \mathbb{R}$ and $x \in \mathbb{R}^n$.
- $\lvert \lvert x+y \rvert \rvert\leq \lvert \lvert x \rvert \rvert +\lvert \lvert y \rvert \rvert$ for all $x,y \in \mathbb{R}^n$.

#### Type of norms
Let $1\leq p\leq \infty$. The $p$-**norm** of a vector $x\in\mathbb{R}^n$ is given by

**1-norm**:
$$\lvert \lvert x \rvert  \rvert_{1} = \lvert x_{1} \rvert +\cdots+\lvert x_{n} \rvert   $$

**2-norm**:
$$\lvert \lvert x \rvert  \rvert_{2}=\sqrt{ \lvert x_{1} \rvert^2+\cdots+\lvert x_{n} \rvert^2   } $$
**$\infty$-norm**:
$$\lvert \lvert x \rvert  \rvert _{\infty}=\text{max}\{\lvert x_{1} \rvert ,\cdots,\lvert x_{n} \rvert \}$$

## Back to [[#Relative Error Analysis and Matrix Norms]]
We introduce a term called the ***condition number***. Denoted by $\text{cond}(A)$, the condition number gives us a way of relating perturbations in the observations $\mathbf{b}$ to the perturbations in the solution:

$$\frac{\lvert \lvert \Delta \mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert } \leq \text{cond}(A) \frac{\lvert \lvert \Delta \mathbf{b} \rvert  \rvert }{\lvert \lvert \mathbf{b} \rvert  \rvert }$$

Let’s now derive $\text{cond}(A)$ from above. First, assume $A\in \mathbb{R}^{n\times n}$ is invertible. Then we have,
$$A\Delta \mathbf{x}=\Delta \mathbf{b} \leftrightarrow \Delta \mathbf{x}=A^{-1}\Delta \mathbf{b}$$
$$\frac{\lvert \lvert \Delta \mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert }=\frac{\lvert \lvert A^{-1}\Delta \mathbf{b} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert }= \frac{\lvert \lvert A^{-1}\Delta \mathbf{b} \rvert  \rvert \lvert \lvert \mathbf{b} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert \lvert \lvert \mathbf{b} \rvert  \rvert  } = \frac{\lvert \lvert A^{-1}\Delta \mathbf{b} \rvert  \rvert \lvert \lvert A\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert \lvert \lvert \mathbf{b} \rvert  \rvert  } $$

#### Matrix Norms
A **matrix norm** is a function on matrices that satisfies the properties:
- $\lvert \lvert A \rvert \rvert>0$ for all $A\neq {0}$.
- $\lvert \lvert A \rvert \rvert=0$ if and only if $A=0$.
- $\lvert \lvert cA \rvert \rvert=\lvert c \rvert \lvert \lvert A \rvert \rvert$ for any $c\in\mathbb{R}$.
- $\lvert \lvert A+B \rvert \rvert\leq \lvert \lvert A \rvert \rvert+\lvert \lvert B \rvert \rvert$.
- $\lvert \lvert AB \rvert \rvert\leq \lvert \lvert A \rvert \rvert\lvert \lvert B \rvert \rvert$.

The **Frobenius norm** of a matrix $A$ is given by
$$\lvert \lvert A \rvert  \rvert _{F}=\sqrt{ \sum_{i=1}^m \sum_{j=1}^n \lvert a_{i,j} \rvert^2  }$$
Where $a_{i,j}$ are the entries of $A$.
#### Definition of operator norm
$$\lvert \lvert A \rvert  \rvert = \text{max}_{\mathbf{x}\neq 0} \frac{\lvert \lvert A\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert },$$
which can be seen as the maximum stretch $A$ does among all non-zero vectors. 

This definition gives us the useful inequality,
$$\lvert \lvert A\mathbf{x} \rvert  \rvert \leq \lvert \lvert A \rvert  \rvert \lvert \lvert \mathbf{x} \rvert  \rvert $$
With his we can upper bound the equation in [[#Back to Relative Error Analysis and Matrix Norms]]
$$\frac{\lvert \lvert \Delta \mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert }=\frac{\lvert \lvert A^{-1}\Delta \mathbf{b} \rvert  \rvert \lvert \lvert A\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert \lvert \lvert \mathbf{b} \rvert  \rvert  } \leq \frac{\lvert \lvert A^{-1}\Delta \mathbf{b} \rvert  \rvert \lvert \lvert A \rvert  \rvert \lvert \lvert \mathbf{x} \rvert  \rvert   }{\lvert \lvert \mathbf{x} \rvert  \rvert \lvert \lvert \mathbf{b} \rvert  \rvert  } \le \lvert \lvert A \rvert  \rvert \lvert \lvert A^{-1} \rvert  \rvert \frac{\lvert \lvert  \Delta \mathbf{b} \rvert  \rvert }{\lvert \lvert \mathbf{b} \rvert  \rvert }$$

Which is exactly the expression we wanted, this means that,
$$\text{cond}(A)=\lvert \lvert A \rvert  \rvert \lvert \lvert A^{-1} \rvert  \rvert $$

#### More on the operator norm
Let us now understand the operator norm. The equivalent definition of the operator norm is,
$$\lvert \lvert A \rvert  \rvert = \text{max}_{\lvert \lvert \mathbf{z} \rvert  \rvert = 1}\lvert \lvert A \mathbf{z} \rvert  \rvert $$
To show this, we start from the definition,
$$\lvert \lvert A \rvert  \rvert = \text{max}_{\mathbf{x}\neq 0} \frac{\lvert \lvert A\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert } = \text{max}_{\mathbf{x} \neq 0}\left\lvert  \left\lvert  A\left( \frac{\mathbf{x}}{\lvert \lvert \mathbf{x} \rvert  \rvert } \right)  \right\rvert   \right\rvert $$
And this is possible because for any scalar, $\lvert c \rvert \lvert \lvert \mathbf{x} \rvert \rvert = \lvert \lvert c \mathbf{x} \rvert \rvert$.
We can then define the vector $\mathbf{z} = \frac{\mathbf{x}}{\lvert \lvert \mathbf{x} \rvert \rvert}$ which has unit norm.

Since the condition number is related to the operator norm of the inverse, let us also derive this. Start with,
$$\lvert \lvert A^{-1} \rvert  \rvert =\text{max}_{\mathbf{x}\neq 0} \frac{\lvert \lvert A^{-1}\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert }$$

Let’s define a new variable $\mathbf{z}$ such that $\mathbf{z} =A^{-1}\mathbf{x}$ and as a result $\mathbf{x}=A\mathbf{z}$. Also notice that $\mathbf{z}\neq 0\leftrightarrow \mathbf{x}\neq 0$.

We then have
$$\lvert \lvert A^{-1} \rvert  \rvert =\text{max}_{\mathbf{x}\neq 0} \frac{\lvert \lvert A^{-1}\mathbf{x} \rvert  \rvert }{\lvert \lvert \mathbf{x} \rvert  \rvert }$$
$$\implies \lvert \lvert A^{-1} \rvert  \rvert =\text{max}_{\mathbf{z}\neq 0} \frac{\lvert \lvert \mathbf{z} \rvert  \rvert }{\lvert \lvert A\mathbf{z} \rvert  \rvert }$$
$$\implies \lvert \lvert A^{-1} \rvert  \rvert =\text{max}_{\mathbf{z}\neq 0} \frac{1}{\lvert \lvert A (\frac{\mathbf{z}}{\lvert \lvert  \mathbf{z} \rvert  \rvert }) \rvert  \rvert }$$
$$= \text{max}_{\lvert \lvert \mathbf{y} \rvert  \rvert =1} \frac{1}{\lvert \lvert A\mathbf{y} \rvert  \rvert } = \frac{1}{\text{min}_{\lvert \lvert \mathbf{y} \rvert  \rvert =1}\lvert \lvert A\mathbf{y} \rvert  \rvert }$$

### Condition Number
From the above proofs, we can lead to the conclusion:
$$\text{cond}(A) = \lvert \lvert A \rvert  \rvert \lvert \lvert A^{-1} \rvert  \rvert = \frac{\text{max}_{\lvert \lvert \mathbf{z} \rvert  \rvert = 1}\lvert \lvert A \mathbf{z} \rvert  \rvert}{\text{min}_{\lvert \lvert \mathbf{y} \rvert  \rvert =1}\lvert \lvert A\mathbf{y} \rvert  \rvert} =\frac{\text{maximum strech on a unit norm vector by } A}{\text{minimum stretch on a unit norm vector by }A}$$
![[Screenshot 2024-09-26 at 11.28.17 PM.png]]

From the definition $\text{cond}(A)\geq 1$, since this is acquired at the identity matrix.

==By convention, we define $\text{cond}(A)=\infty$ if $\det(A)=0$.==
#### Next Lecture [[UBC/CPEN 4-1/MATH 307/Lecture Notes/Lecture 5|Lecture 5]]
