#### Question 1
```julia
function A = hilbertMatrix(n)
    A = zeros(n, n);
    for i = 1:n 
        for j = 1:n
            A(i, j) = 1 / (i + j - 1);
        end
    end
end

n = 4:12;

condVals = zeros(1, length(n));

for i = 1 : length(n)
    A = hilbertMatrix(n(i));
    condVals(i) = cond(A);
end

figure
semilogy(n, condVals, '-o', 'LineWidth', 1.5)
xlabel('n')
ylabel('Condition Number')
title('Condition Numbers for Hilbert Matrices')
grid on
```
![[Pasted image 20250301201722.png]]
We can see that as $n$ grows the condition number grows linearly in log-scale, meaning that in linear-scale that the condition number grows exponentially, to elaborate on the exact numerical values,
```
n = 4, condition number = 1.551374e+04
n = 5, condition number = 4.766073e+05
n = 6, condition number = 1.495106e+07
n = 7, condition number = 4.753674e+08
n = 8, condition number = 1.525758e+10
n = 9, condition number = 4.931539e+11
n = 10, condition number = 1.602490e+13
n = 11, condition number = 5.226829e+14
n = 12, condition number = 1.636072e+16
```


#### Question 2

##### (a)
First, let’s start with the monomial basis. Also, let’s start with constructing $\tilde{\mathbf{b}}$, given $n=2$,
$$\begin{aligned}
\tilde{b_{0}} &= \int_{0}^1 \sin(\pi t) dt = \frac{2}{\pi} \\ 
\tilde{b_{1}} &= \int_{0}^1t\sin(\pi t)dt=\frac{1}{\pi} \\ 
\tilde{b_{2}} &= \int _{0}^1t^2\sin(\pi t)dt =\frac{\pi^2-4}{\pi^3}
\end{aligned}$$

We also have the Hilbert matrix,
$$\begin{aligned}
\tilde{B}_{j,k} &= \int_{0}^1x^{j+k}dx= \frac{1}{j+k+1} \quad 0\leq j,k \leq 2 \\ 
\tilde{B} &= \begin{bmatrix}
1 & \frac{1}{2} & \frac{1}{3} \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4}  \\
\frac{1}{3} & \frac{1}{4} & \frac{1}{5}
\end{bmatrix}
\end{aligned}$$

Then,
$$\begin{aligned}
\tilde{B} \mathbf{c} &= \tilde{\mathbf{b}} \\ 
\begin{bmatrix}
1 & \frac{1}{2} & \frac{1}{3} \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4}  \\
\frac{1}{3} & \frac{1}{4} & \frac{1}{5}
\end{bmatrix}\mathbf{c} &= \begin{bmatrix}
\frac{2}{\pi} \\ \frac{1}{\pi} \\ \frac{\pi^2-4}{\pi^3}
\end{bmatrix} \\ 
\therefore \mathbf{c}&=\begin{bmatrix}
\frac{12}{\pi} - \frac{120}{\pi^3} \\
-\frac{60}{\pi}+\frac{720}{\pi^3}\\
\frac{60}{\pi}-\frac{720}{\pi^3}
\end{bmatrix}
\end{aligned} $$

therefore, our polynomial is,
$$q_{2}(x) = \frac{12}{\pi} - \frac{120}{\pi^3} -(\frac{60}{\pi}-\frac{720}{\pi^3})x+(\frac{60}{\pi}-\frac{720}{\pi^3})x^2$$

Now, let’s compute using the Legendre polynomials. We first have to acknowledge that our bound is $[0,1]$, not $[-1,1]$. Converting $x$ from some $t \in [-1,1]$ will be,
$$x = \frac{1}{2} ((b-a)t + (a+b)) = \frac{1}{2}(t + 1) \to t =2x-1 $$

Now using the following,
$$\begin{aligned}
\phi_{0}(t) &= 1 \\ \phi_{1}(t) &= t \\ 
\phi_{2}(t) &= \frac{3}{2}t\phi_{1}(t) -\frac{1}{2}\phi_{0}(t) = \frac{3}{2}t^2-\frac{1}{2}
\end{aligned}$$
for some $t \in [-1,1]$, we can construct for $x \in [0,1]$,
$$\begin{aligned}
\phi_{0}(x) &= 1 \\ 
\phi_{1}(x) &= 2x-1  \\ 
\phi_{2}(x) &= \frac{3}{2}(2x-1)^2-\frac{1}{2}  = 6x^2-6x+1
\end{aligned}$$

Given the information above, we can find $\tilde{\mathbf{b}}$ once again,
$$\begin{aligned}
\tilde{b_{1}} &= \int_{0}^1 \sin(\pi t)dt = \frac{2}{\pi} \\ 
\tilde{b_{2}} &= \int_{0}^1(2t-1)\sin(\pi t)dt = 2\int_{0}^1t\sin(\pi t)dt-\int_{0}^1\sin(\pi t)dt \\ &=2 \cdot \frac{1}{\pi}-\frac{2}{\pi}=  0 \\ 
\tilde{b_{3}}&= \int_{0}^1(6t^2-6t+1)\sin(\pi t)dt = 6\int_{0}^1t^2\sin(\pi t)dt -6\int_{0}^1t\sin(\pi t)dt +\int_{0}^1\sin(\pi t)dt \\ 
&=6 \cdot  \frac{\pi^2-4}{\pi^3}-6\cdot  \frac{1}{\pi} + \frac{2}{\pi} = \frac{6}{\pi} -\frac{24}{\pi^3} -\frac{6}{\pi} + \frac{2}{\pi} = \frac{2\pi^2-24}{\pi^3}
\end{aligned}$$

Let’s also compute $d_{0},d_{1},d_{2}$,
$$\begin{aligned}
d_{0} &= \lvert \lvert \phi_{0} \rvert  \rvert ^2 = \int_{0}^11dt= 1 \\ 
d_{1} &= \lvert \lvert \phi_{1} \rvert  \rvert ^2 = \int_{0}^1 (2t-1)^2dt = \int_{0}^1(4t^2-4t+1)dt = \frac{4}{3}-2+1 = \frac{1}{3} \\ 
d_{2} &= \lvert \lvert \phi_{2} \rvert  \rvert ^2 = \int_{0}^1(6t^2-6t+1)dt = \frac{1}{5}
\end{aligned}$$

Then our final polynomial is,
$$\begin{aligned}
q_{2}(x) &= \frac{2}{\pi} + 5\left( \frac{2\pi^2-24}{\pi^3} \right)(6x^2-6x+1) \\ 
&= \frac{2}{\pi}+5\left( \frac{2\pi^2-24}{\pi^3} \right) -30\left( \frac{2\pi^2-24}{\pi^3} \right)x +30 \left( \frac{2\pi^2-24}{\pi^3} \right)x^2 \\ 
&=\left( \frac{12}{\pi}-\frac{120}{\pi^3} \right) - \left( \frac{60}{\pi} -\frac{720}{\pi^3} \right)x + \left( \frac{60}{\pi}-\frac{720}{\pi^3} \right)x^2
\end{aligned}$$
showing that both polynomials are identical.

##### (b)
```julia
q = @(x) (12/pi - 120/pi^3) - (60/pi -720/pi^3) * x + (60/pi-720/pi^3) * x.^2;
g = @(x) sin(pi * x);

x = 0:0.001:1;

figure 
hold on 
plot(x, g(x),"Color", "b", "DisplayName","original")
plot(x, q(x),"Color", "r", "DisplayName","interpolant")
xlabel("x")
ylabel("y")
grid on
legend("show")
hold off
```
![[Pasted image 20250305200421.png]]
#### Question 3
Let’s alter the current integration form where $x \in [-1,1]$ to $t \in [a,b]$,
$$\int_{-1}^1 \phi_{j}(x)\phi_{k}(x)dx$$
We can translate the current $x \in [-1,1]$ to $[a,b]$ by setting,
$$\frac{(b-a)x+(b+a)}{2}, x \in [-1,1]$$
then we can set,
$$\int_{-1}^1 \phi_{j}\left( \frac{(b-a)x+(b+a)}{2} \right)\phi_{k}\left( \frac{(b-a)x+(b+a)}{2} \right)dx = \begin{cases}
0 ,\quad &j\neq k \\
\frac{2}{2j+1},\quad &j=k
\end{cases}$$

setting $t =  \frac{(b-a)x+(b+a)}{2}$, we get $dt = \frac{b-a}{2}dx$, thus,
$$\int_{a}^b \phi_{j}(t)\phi_{k}(t) \frac{2}{b-a}dt= \begin{cases}
0 ,\quad &j\neq k \\
\frac{2}{2j+1},\quad &j=k
\end{cases}$$

in other words,
$$\int_{a}^b \phi_{j}(t)\phi_{k}(t)dt = \begin{cases}
0, \quad &j\neq k  \\
\frac{b-a}{2j+1},\quad &j=k
\end{cases} $$
as required.

#### Question 4
##### (a)
First, let’s use Legendre polynomials and find $q_2(t)$. Before we start, we need to derive an expression for $t$ since $t \in [0,3]$. When $x\in [-1,1]$, we can describe $x$ in $t$ as the following,
$$t = \frac{(b-a)x+(b+a)}{2} = \frac{3x+3}{2} \to x = \frac{2t-3}{3}$$
Then our basis functions $\phi_{j}(t),j=0,1,2,3$ are 
$$\begin{aligned}
\phi_{0}(x)=1 &\to \phi_{0}(t) = 1\\
\phi_{1}(x)=x &\to \phi_{1}(t) = \frac{2t-3}{3} \\ 
\phi_{2}(t)= \frac{3}{2}\left( \frac{2t-3}{3} \right)\phi_{1}(t)- \frac{1}{2}\phi_{0}(t) &\to \phi_{2}(t) = \frac{3}{2}\left( \frac{2t-3}{3} \right)^2 -\frac{1}{2} \\ 
&\to \phi_{2}(t) = \frac{1}{6} (4t^2-12t+6) = \frac{2}{3}t^2 -2t+1 \\
\phi_{3}(t)=\frac{5}{3}\left( \frac{2t-3}{3} \right)\phi_{2}(t) -\frac{2}{3}\phi_{1}(t)&\to \phi_{3}(t) = \frac{5}{3}\left( \frac{2t-3}{3}\right)\left( \frac{2}{3}t^2-2t+1 \right) \\
&\quad\quad\quad\quad- \frac{2}{3}\left( \frac{2t-3}{3} \right) \\
&\to \phi_{3}(t) = \frac{20}{27}t^3-\frac{10}{3}t^2+4t-1
\end{aligned}$$

And using the results from Question 3, let’s compute $\int_{0}^3 \phi_{j}^2(t)dt,j=0,1,2$.
$$\begin{aligned}
\int_{0}^3 \phi_{0}^2(t)dt &= \frac{3}{1} = 3 \\ 
\int_{0}^3\phi^2_{1}(t)dt &= \frac{3}{3} = 1\\
\int_{0}^3\phi_{2}^2(t)dt &= \frac{3}{5}  \\
\int_{0} \phi_{3}^2(t)dt &= \frac{3}{7}
\end{aligned}$$

Now, we have to compute $\int_{0}^3 f(t)\phi_{j}(t)dt,j=0,1,2,3$. 
$$\begin{aligned}
\int_{0}^3e^{-3t}\phi_{0}(t)dt &= \int_{0}^3e^{-3t}dt = -\frac{1}{3}\left[e^{-3t}\right]_{0}^3 = \frac{1}{3}(1-e^{-9})
\end{aligned}$$
$$\begin{aligned}
\int_{0}^3e^{-3t}\phi_{1}(t)dt &= \int_{0}^3e^{-3t}\left( \frac{2}{3}t-1 \right)dt \\
&= \left[ -\frac{e^{-3t}}{3} \left( \sum_{j=0}^1  \frac{\left( \frac{2}{3}t-1 \right)^{(j)}}{3^j}  \right) \right]_{0}^3 \\ 
&=\left[ - \frac{e^{-3t}}{3}\left( \left( \frac{2}{3}t-1 \right) + \left( \frac{2}{9} \right) \right) \right]_{0}^3 \\ 
&= - \frac{e^{-9}}{3}\left( 2-1+\frac{2}{9} \right)-\left( -\frac{1}{3} \right)\left( -1+\frac{2}{9} \right) \\ 
&=-\frac{11}{27}e^{-9}-\frac{7}{27}
\end{aligned}$$
$$\begin{aligned}
\int_{0}^3e^{-3t}\phi_{2}(t)dt &= \int_{0}^3e^{-3t}\left( \frac{2}{3}t^2-2t+1 \right)dt \\
&= \left[ -\frac{e^{-3t}}{3} \left( \sum_{j=0}^2  \frac{\left( \frac{2}{3}t^2-2t+1 \right)^{(j)}}{3^j}  \right) \right]_{0}^3  \\
&=\left[ - \frac{e^{-3t}}{3}\left( \left( \frac{2}{3}t^2-2t+1 \right) + \frac{1}{3}\left( \frac{4}{3}t-2 \right) + \frac{1}{9}\left( \frac{4}{3} \right)  \right)    \right]_{0}^3 \\ 
&= \left[-\frac{e^{-3t}}{3}\left(\frac{2}{3}t^2-\frac{14}{9}t+\frac{13}{27} \right)  \right]_{0}^3 \\ 
&=-\frac{e^{-9}}{3}\left( \frac{2}{3}\cdot 9 -\frac{14}{9}\cdot 3 +\frac{13}{27} \right) -\left( -\frac{1}{3} \right)\left( \frac{13}{27} \right) \\
&= -\frac{49}{81}e^{-9} +\frac{13}{81}
\end{aligned}$$
$$\begin{aligned}
\int_{0}^3e^{-3t}\phi_{3}(t)dt &= \int_{0}^3e^{-3t}\left(\frac{20}{27}t^3-\frac{10}{3}t^2+4t-1\right)dt \\ 
&= \left[ -\frac{e^{-3t}}{3} \left( \sum_{j=0}^3  \frac{\left( \frac{20}{27}t^3-\frac{10}{3}t^2+4t-1 \right)^{(j)}}{3^j}  \right) \right]_{0}^3  \\
&= [ -\frac{e^{-3t}}{3}( \left( \frac{20}{27}t^3-\frac{10}{3}t^2+4t-1 \right)+\frac{1}{3}\left( \frac{20}{9}t^2-\frac{20}{3}t+4 \right) \\
&+ \frac{1}{9}\left( \frac{40}{9}t-\frac{20}{3} \right) + \frac{1}{27}\left( \frac{40}{9} \right)) ] \\
&=\left[e^{-3t}\left( -\frac{20}{81}t^3+ \frac{70}{81}t^2 - \frac{184}{243}t + \frac{59}{729}  \right)\right] ^3_{0} \\ 
&=  -\frac{787}{729} e^{-9} - \frac{59}{729}
\end{aligned}$$

Then, we can get $q_{2},q_{3}$,
$$\begin{aligned}
q_{2}(x) &= \frac{1}{9}(1-e^{-9}) + \left( -\frac{11}{27}e^{-9}-\frac{7}{27} \right)\left( \frac{2t-3}{3} \right)\\ 
&+ \left( \frac{5}{3} \right) \left(  -\frac{49}{81}e^{-9} +\frac{13}{81} \right)\left( \frac{2}{3}t^2 -2t+1  \right)   \\
q_{3}(x) &= \frac{1}{9}(1-e^{-9}) + \left( -\frac{11}{27}e^{-9}-\frac{7}{27} \right)\left( \frac{2t-3}{3} \right)\\ 
&+ \left( \frac{5}{3} \right) \left(  -\frac{49}{81}e^{-9} +\frac{13}{81} \right)\left( \frac{2}{3}t^2 -2t+1  \right)  \\
&+  \left( \frac{7}{3} \right)\left(  -\frac{787}{729} e^{-9} - \frac{59}{729} \right)\left( \frac{20}{27}t^3-\frac{10}{3}t^2+4t-1 \right)
\end{aligned}$$

```julia
p2 = @(t) (1/9)*(1-exp(-9)) + (-11/27*exp(-9) - 7/27) * ((2*t - 3)/3) ...
    + (5/3) * (-49/81*exp(-9) + 13/81) * ((2/3)*t.^2 - 2*t + 1);


p3 = @(t) p2(t) + (7/3) * (-787/729*exp(-9) - 59/729) * ((20/27)*t.^3 - (10/3)*t.^2 + 4*t - 1);

f = @(t) exp(-3*t); 

x = 0:0.0001:3;

f_x = f(x);
p2_x = p2(x);
p3_x = p3(x);

figure;
plot(x, f(x), 'b','DisplayName', 'original', 'LineWidth', 1.5);
hold on;
plot(x, p2(x), 'r','DisplayName','q2', 'LineWidth', 1.5);
plot(x, p3(x), 'g','DisplayName','q3', 'LineWidth', 1.5);
xlabel('x');
ylabel('y');
title('Plots for each function f, q2, q3');
legend("show");
grid on;
hold off;


figure;
plot(x, f_x - p2_x, 'b', 'LineWidth', 1.5); 
hold on;
plot(x, f_x - p3_x, 'r', 'LineWidth', 1.5);
xlabel('x');
ylabel('Difference');
title('Plot of f(x) - q_2(x) and f(x) - q_3(x)');
legend('f(x) - q_2(x)', 'f(x) - q_3(x)');
grid on;
hold off;
```
![[Pasted image 20250305202033.png]]
##### (b)
![[Pasted image 20250305202022.png]]
Let’s compare the errors,
```julia
diff_1 = sqrt(integral(@(t) (p2(t) - f(t)).^2, 0, 3));
diff_2 = sqrt(integral(@(t) (p3(t) - f(t)).^2, 0, 3));

L2 norm of q2 - f:  0.13967
L2 norm of q3 - f: 0.064598
```
We can see that the polynomial $q_3$ provides a smaller error.

##### (c)
First of all, we can notice that $q_{3}(x)= q_{2}(x) + c \cdot \alpha(x)$ for some $c \in \mathbb{R}$ and $\text{deg}(\alpha (x)) = 3$. 

When getting the least squares fit, in the option of choosing 3rd degree or less polynomials to reduce the continuous L2-norm, if there were no 3rd degree polynomial that provides a better fit, we can always choose $c=0$ and get the same error from $q_2(x)$. Hence, the error never gets worse.

#### Question 5
##### (a)
Let’s expand the expression,
$$\int_{a}^b w(x)L_{j}(x)L_{k}(x)dx,\quad j\neq k $$

$$\begin{aligned}
L_{j}(x)L_{k}(x) &= \prod_{i=1,i\neq j}^n \frac{(x-x_{i})}{(x_{j}-x_{i})}  \prod_{i = 1, i\neq k}^n \frac{(x-x_{i})}{(x_{k}-x_{i})} \\ 
&=\beta \cdot \left((x-x_{1})\cdots(x-x_{j-1})(x-x_{j+1})\cdots(x-x_{n})\right) \\
&\quad\times \left((x-x_{1})\cdots(x-x_{k-1})(x-x_{k+1})\cdots(x-x_{n})\right) \\
&= \beta \cdot \phi_{n}(x)\cdot ((x-x_{1})\cdots(x-j_{i-1})(x-x_{j+1})\cdots \\ 
&\quad \times (x-x_{k-1})(x-x_{k+1})\cdots(x-x_{n}))
\end{aligned}$$

Where $\beta$ is a constant made from the non-zero, real numerators of the Lagrange polynomials.

If we look carefully at, the last expression, re-written elegantly,
$$\beta \cdot  \phi_{n}(x) \cdot  \prod_{i=0,i\neq j,i\neq k}^n (x-x_{i})$$
The latter term has a degree less than $n$, therefore it can than be written as a linear combination of the orthogonal polynomials $\phi_{0}(x),\phi_{1}(x),\cdots$.

Therefore,
$$\begin{aligned}
\int_{a}^bw(x)L_{j}(x)L_{k}(x)dx &= \int_{a}^bw(x)\phi_{n}(x)\sum_{i=0}^{n-1}c_{i}\phi_{i}(x) \\ 
&=\sum_{i=0}^{n-1} c_{i} \int_{a}^bw(x)\phi_{n}(x)\phi_{i}(x) dx
\end{aligned}$$

Since $\phi_{0}(x),\phi_{1}(x),\cdots$ are orthogonal polynomials, 
$$\int_{a}^b w(x)\phi_{j}(x)\phi_{k}(x)dx=0,\quad j\neq k$$

$$\int_{a}^bw(x)L_{j}(x)L_{k}(x)dx =\sum_{i=0}^{n-1} c_{i} \int_{a}^bw(x)\phi_{n}(x)\phi_{i}(x) dx = 0$$
as required.

##### (b)
We have that $p_{n-1}(x)$ interpolates $f(x)$, for points $x_{1},\cdots,x_{n}$. Hence, we can use the Lagrange Basis to represent $p_{n-1}(x)$. Like the following,
$$p_{n-1}(x) = \sum_{k=1}^n c_{k}L_{k}(x)$$
And since this is the Lagrange Basis, $c_{k}=y_{k}$ for $k=1,\cdots,n$.

$$\begin{aligned}
\lvert \lvert p_{n-1} \rvert  \rvert ^2 &= \int_{a}^bw(x)[p_{n-1}(x)]^2dx \\ 
&= \int_{a}^bw(x)\left(\sum_{k=1}^nc_{k}L_{k}(x)\right)^2 dx \\ 
&=\int_{a}^bw(x) \left(c_{1}^2L_{1}^2(x) + \cdots + c_{n}^2L_{n}^2(x) + 2\sum_{m=1}^n\sum_{j=1,j\neq m}^n\left(c_{m}c_{j}L_{m}(x)L_{j}(x)\right)\right)
\end{aligned}$$

From part (a) we showed that
$$\int_{a}^bw(x)L_{j}(x)L_{k}(x)dx = 0,\quad j\neq k$$

Hence, we can reduce our expression for $\lvert \lvert p_{n-1} \rvert \rvert^2$ as the following,
$$\begin{aligned}
\lvert \lvert p_{n-1} \rvert  \rvert ^2 &= \int_{a}^b w(x)\left(\sum_{k=1}^nc_{k}^2L_{k}^2(x)\right)dx \\ 
&=\sum_{k=1}^nc_{k}^2 \int_{a}^b w(x)L_{k}^2(x)dx \\
&= \sum_{k=1}^ny_{k}^2 \int_{a}^b w(x)L_{k}^2(x)dx \\ 
&= \sum_{k=1}^n y_{k}^2 \lvert \lvert L_{k} \rvert  \rvert ^2
\end{aligned}$$
As required.

#### Question 6
We know the following for ChebyShev Polynomials,
$$T_{n}(x) = \cos(n\theta), x=\cos(\theta)$$
Given the information above, let’s prove by induction. When $n=1$,
$$T_{1}(x) = \cos(\theta) = x = 2^{1-1}(x-0)$$
as required.

Now let’s assume for $k \leq n$, that the following is satisfied,
$$T_{n}(x) =2^{n-1}(x-x_{1})(x-x_{2})\cdots(x-x_{n})=\cos(n\theta)$$
where $x_{i},i=1,\cdots,n$ are the $n$ roots of $T_n(x)$.

Using the definition along with the recurrence relation,
$$\begin{aligned}
T_{n+1}(x) &= 2xT_{n}(x) -T_{n-1}(x) \\
&=2x\cdot \cos(n\theta)-\cos((n-1)\theta) \\
&= 2\cos(\theta)\cos(n\theta)-\left(\cos(n\theta)\cos(\theta)+\sin(n\theta)\sin(\theta)\right)\\
&=\cos(n\theta)\cos(\theta)-\sin (n\theta)\sin(\theta) \\
&=\cos((n+1)\theta)
\end{aligned}$$

We know that  $T_{n+1}(x)=\cos((n+1)\theta)=0$ when $(n+1)\theta = \frac{2k-1}{2}\pi,k \in \mathbb{Z}$. 
Since $x=\arccos((n+1)\theta)$, $T_{n+1}(x)=0$ happens at
$$x= \frac{2k-1}{2(n+1)}\pi,k=1,\cdots,n+1 $$
which is $n+1$ roots.

From the recurrence relation, $T_{n}(x) = 2^{n-1}x^n +\cdots$ and $T_{n-1}(x)=2^{n-2}x^{n-1}+\cdots$ thus, when following $T_{n+1}(x) = 2xT_{n}(x)-T_{n-1}(x)$ we can still see that the highest degree is $n+1$ with leading coefficient $2^n$.

Combining the information that $T_{n+1}(x)$ has $n+1$ roots and has the leading coefficient $2^n$, we can therefore conclude that,
$$T_{n+1}(x)= 2^n(x-x_{1}')(x-x_{2}')\cdots(x-x_{n+1}')$$
as required for our induction.

#### Question 7
Let’s denote the function that we want to find of degree $n$ as $v(x)$. Then we want to find $v(x)$ such that
$$\text{max }_{-1\leq x\leq_{1}}\lvert v(x)-f(x) \rvert $$
is minimized.

We know that for a monic polynomial of degree $n$, $\tilde{T}_{n}(x)$ uniquely has the smallest maximum magnitude over $x \in [-1,1]$. Thus, we will try creating $v(x)$ such that it follows this.

First, let’s set $f(x)$ as the following,
$$f(x) = a_{n+1}x^{n+1} +\cdots$$
we know that $a_{n+1}\neq {0}$ since $f(x)$ is of degree $n+1$.

Now, we let 
$$v(x) = f(x) - \frac{a_{n+1}}{2^n}T_{n+1}(x)$$
From the previous question, we know that 
$$T_{n+1}(x) = 2^nx^{n+1} +\cdots$$
Hence, 
$$\begin{aligned}
v(x)&=f(x) -\frac{a_{n+1}}{2^n}T_{n+1}(x) \\ 
&= (a_{n+1}x^{n+1} +\cdots) - a_{n+1} (x^{n+1}+\cdots) \to \text{degree $n$}
\end{aligned}$$
Also,
$$\begin{aligned}
\lvert f(x)-v(x) \rvert &= \left\lvert  \frac{a_{n+1}}{2^n} T_{n+1}(x)  \right\rvert\\ &= \lvert a_{n+1}\tilde{T}_{n+1}(x) \rvert  \\
&=\lvert a_{n+1} \rvert \cdot  \lvert \tilde{T}_{n+1}(x) \rvert 
\end{aligned}$$
we are guaranteed that the maximum would be minimized now on the interval $x \in [-1,1]$.

Therefore, Jane here’s the polynomial,
$$\therefore v(x) = f(x) - \frac{a_{n+1}}{2^n}T_{n+1}(x)$$

#### Question 8
We have that,
$$v(x) = \frac{a_{0}}{2}+a_{l}\cos(lx) + \sum_{k=1}^{l-1}\left( a_{k}\cos(kx) + b_{k}\sin(kx) \right)$$
where $l=50, f(x) = \cos(3x)-\frac{1}{2}\sin(5x) + \frac{1}{20}\cos(54x)$.

$$\begin{aligned}
a_{0} &= \frac{1}{\pi}\int_{-\pi}^\pi f(x) dx \\ 
&= \frac{1}{\pi}\int_{-\pi}^\pi\cos(3x)-\frac{1}{2}\sin(5x) + \frac{1}{20}\cos(54x)dx \\
&= \frac{1}{\pi}\int_{-\pi}^\pi \cos(3x) + \frac{1}{20}\cos(54x)dx \\
&=\frac{1}{\pi} \left[ \frac{1}{3}\sin(3x) +\frac{1}{20\cdot 54}\sin(54x) \right]_{-\pi}^\pi \\ 
&= \frac{1}{\pi}\left(  \frac{1}{3} \sin(3\pi) + \frac{1}{20\cdot 54}\sin(54\pi)\right)\\
&= 0
\end{aligned}$$

Now, let’s compute $a_k,b_k$ for $k=1,\cdots,l=50$,
$$\begin{aligned}
a_{k} &= \frac{1}{\pi}\int_{-\pi}^\pi \cos(kx)\left\{ \cos(3x)-\frac{1}{2}\sin(5x) + \frac{1}{20}\cos(54x) \right\}dx \\
&= \frac{1}{\pi}\int_{-\pi}^\pi \cos(kx)\left(\cos(3x) +\frac{1}{20}\cos(54x)\right)dx \quad \because(\cos(kx)\sin(mx)\text{ is odd}) \\
&= \frac{1}{\pi}\cdot \pi \cdot \delta_{k{3}} \quad \because \text{($k\leq 50 <54$)} \\
&= \delta _{k 3}
\end{aligned} $$
$$\begin{aligned}
b_{k} &= \frac{1}{\pi}\int_{-\pi}^\pi \sin(kx)\left\{ \cos(3x)-\frac{1}{2}\sin(5x) + \frac{1}{20}\cos(54x) \right\}dx  \\
&= \frac{1}{\pi}\int_{-\pi}^\pi \sin(kx)\left( -\frac{1}{2}\sin(5x) \right)dx \\ 
&= \frac{1}{\pi} \cdot  \left( -\frac{1}{2} \right) \cdot  \pi \cdot  \delta_{k 5} \\
&= -\frac{1}{2}\delta_{k 5}
\end{aligned}$$

Then our $v(x)$ is,
$$v(x) = \cos(3x) -\frac{1}{2}\sin(5x)$$
```julia
v = @(x) cos(3 * x) -1/2 * sin(5*x);
f = @(x) cos(3 * x) -1/2 * sin(5 *x) + 1/20*cos(54*x);

x = -pi:0.0001:pi;

figure 
plot(x, f(x),"b")
hold on
plot(x, v(x), "r")
hold off
```
![[Pasted image 20250301221801.png]]
We can see that the resulting Fourier transformation almost roughly approximates the original function. The reason it doesn’t approximate it one-to-one is due to the fact that $l=50$. If we had $l = 54$ or even larger, than we would have 
$$v(x) = \cos(3x) -0.5\sin(5x) + 0.05\cos(54x)=f(x)$$
since the coefficient at $k=54$ would not vanish anymore.
#### Question 9
```julia
f = @(x) (0 <= x & x <= pi) .* x + (pi < x & x <= 2 * pi) .* (2*pi - x);

x = 0:0.01*pi:2*pi;

l_vals = [2, 4, 8, 16, 32];
colors = lines(length(l_vals));
max_errors = zeros(size(l_vals));


figure;
plot(x, f(x), 'k--', 'LineWidth', 2, 'DisplayName', 'Exact Values');
hold on;

for idx = 1:length(l_vals) 
    l = l_vals(idx);

    n = 2 * l - 1;
    i = 0:n;
    xi = pi * i / l;
    yi = f(xi);

    a = zeros(l + 1, 1);
    b = zeros(l - 1, 1);

    for k = 0:l
        a(k + 1) = 1/l * sum(yi .* cos(k*xi));
    end

    for k = 1:l-1
        b(k) = 1/l * sum(yi .* sin(k*xi));
    end

    px = 1/2 * (a(1) + a(l + 1)*cos(l*x));

    for k = 1:l-1 
        px = px + a(k + 1) .* cos(k * x) + b(k) .* sin(k * x);
    end
    max_errors(idx) = max(abs(f(x) - px));
    plot(x, px, 'Color', colors(idx, :), 'LineWidth', 1, 'DisplayName', sprintf('l = %d', l));
end

hold off;
grid on;
xlabel('x');
ylabel('f(x)');
title('Trigonometric Interpolation of Hat Function');
legend('Location', 'Best');

table(l_vals(:), 2*l_vals(:)-1, max_errors(:), 'VariableNames', {'l', 'n', 'Max_Absolute_Error'})
```
![[Pasted image 20250301221837.png]]
And the max error per $l$ is,
```julia

    l     n     Max_Absolute_Error
    __    __    __________________

     2     3          0.33067     
     4     7          0.15371     
     8    15         0.075208     
    16    31         0.036362     
    32    63         0.017967   
```
If we look at the maximum absolute error per $l$, we can see that whenever $l$ is multiplied by 2, the maximum absolute error is reduced by the same factor 2. Hence, improvement is linear in $l$.

#### Question 10
##### (a)
```julia
f = @(x) log(x + 1);

x = 0:0.001:2*pi;

l_vals = [16, 32];
colors = lines(length(l_vals));
max_errors = zeros(size(l_vals));


figure;
plot(x, f(x), 'k--', 'LineWidth', 2, 'DisplayName', 'Exact Values');
hold on;

for idx = 1:length(l_vals) 
    l = l_vals(idx);

    n = 2 * l - 1;
    i = 0:n;
    xi = (1 * pi) * i / l;
    yi = f(xi);

    a = zeros(l + 1, 1);
    b = zeros(l - 1, 1);

    for k = 0:l
        a(k + 1) = 1/l * sum(yi .* cos(k*xi));
    end

    for k = 1:l-1
        b(k) = 1/l * sum(yi .* sin(k*xi));
    end

    px = 1/2 * (a(1) + a(l + 1)*cos(l*x));

    for k = 1:l-1 
        px = px + a(k + 1) .* cos(k * x) + b(k) .* sin(k * x);
    end
    max_errors(idx) = max(abs(f(x) - px));
    plot(x, px, 'Color', colors(idx, :), 'LineWidth', 1, 'DisplayName', sprintf('l = %d', l));
end

hold off;
grid on;
xlabel('x');
ylabel('f(x)');
title('10-a');
legend('Location', 'Best');

T = table(l_vals', max_errors', 'VariableNames', {'l', 'MaxAbsoluteError'});

disp(T);
```
![[Pasted image 20250301232809.png]]
```julia
    l     MaxAbsoluteError
    __    ________________

    16         1.9843     
    32          1.983     
```
We can see that the difference increase rapidly as we progress to the ends of the interval $[0,2\pi]$. When considering interpolation, DFT would produce a satisfying result if the function is smooth and periodic. Though in the interval $[0,2\pi]$ the function $f(x)$ is smooth, it is not periodic, hence the results are not satisfying.

##### (b)
```julia
f = @(x) log(x + 1);
g = @(x) (0 <= x & x < 2*pi) .* f(x) + (2*pi <= x & x < 4 * pi) .* f(4*pi - x);


x = 0:0.001:4*pi;
sub_x = 0:0.001:2*pi;

l_vals = [16, 32];
colors = lines(length(l_vals));
max_errors = zeros(size(l_vals));


figure;
plot(sub_x, g(sub_x), 'k--', 'LineWidth', 2, 'DisplayName', 'Exact Values');
hold on;

for idx = 1:length(l_vals) 
    l = l_vals(idx);

    n = 2 * l - 1;
    i = 0:n;
    xi = (2 * pi) * i / l;
    yi = g(xi);

    a = zeros(l + 1, 1);
    b = zeros(l - 1, 1);

    for k = 0:l
        a(k + 1) = 1/l * sum(yi .* cos(k*xi/2));
    end

    for k = 1:l-1
        b(k) = 1/l * sum(yi .* sin(k*xi/2));
    end

    px = 1/2 * (a(1) + a(l + 1)*cos(l*sub_x/2));

    for k = 1:l-1 
        px = px + a(k + 1) .* cos(k * sub_x/2) + b(k) .* sin(k * sub_x/2);
    end
    max_errors(idx) = max(abs(f(sub_x) - px));
    plot(sub_x, px, 'Color', colors(idx, :), 'LineWidth', 1, 'DisplayName', sprintf('l = %d', l));
end

hold off;
grid on;
xlabel('x');
ylabel('g(x)');
title('10-b');
legend('Location', 'Best');

T = table(l_vals', max_errors', 'VariableNames', {'l', 'MaxAbsoluteError'});
disp(T);
```
![[Pasted image 20250301233115.png]]
```julia
    l     MaxAbsoluteError
    __    ________________

    16           0.074    
    32        0.037227    
```

Compared to (a), we can see that the maximum absolute error reduced significantly. In this question, we made $g(t)$ which is periodic in intervals $[0,4\pi]$, thus comparing to $f(x)$ our function $g(t)$ is not only smooth but periodic. Which makes DFT more accurate. When $n$ increases now, the convergence of the interpolation is very fast; i.e. the error decreases fast.