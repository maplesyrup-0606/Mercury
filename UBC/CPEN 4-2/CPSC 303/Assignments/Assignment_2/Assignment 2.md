#### Question 1
##### (a)
```MATLAB
alphas = [0.1 1 12];
x = linspace(0, pi, 11);
xx = 0:0.001:pi;

interpolants = {
    'Polynomial 10th Degree', @(x, y, xx) polyval(polyfit(x, y, 10), xx);
    'Cubic Spline', @(x, y, xx) spline(x, y, xx);
    'Piecewise Cubic Hermite', @(x, y, xx) pchip(x, y, xx);
    'Piecewise Linear', @(x, y, xx) interp1(x, y, xx, "linear");
    'Piecewise Constant', @(x, y, xx) interp1(x, y, xx, 'nearest');
};

for i = 1:length(alphas)
    alpha = alphas(i);
    fx = @(x) sin(alpha * x);
    y = fx(x);

    figure 
    hold on 

    for j = 1:length(interpolants)
        interpolation_name = interpolants{j, 1};
        interpolation_method = interpolants{j, 2};

        interpolant_vals = interpolation_method(x, y, xx);

        plot(xx, interpolant_vals, "DisplayName", interpolation_name, 'LineWidth', 1.5);
    end
    
    plot(x, y, 'o');

    hold off
    legend 
    xlabel('x')
    ylabel('f(x)')
    title(['Interpolation Comparison for \alpha = ' num2str(alpha)])
    grid on
end
```
![[Pasted image 20250211205107.png]]
![[Screenshot 2025-02-11 at 8.51.24 PM.png]]
![[Screenshot 2025-02-11 at 8.51.33 PM.png]]


##### (b)
```MATLAB
alphas = [0.1 1 12];
x = linspace(0, pi, 11);
xx = 0:0.001:pi;

interpolants = {
    'Polynomial 10th Degree', @(x, y, xx) polyval(polyfit(x, y, 10), xx);
    'Cubic Spline', @(x, y, xx) spline(x, y, xx);
    'Piecewise Cubic Hermite', @(x, y, xx) pchip(x, y, xx);
    'Piecewise Linear', @(x, y, xx) interp1(x, y, xx, "nearest");
    'Piecewise Constant', @(x, y, xx) interp1(x, y, xx, 'previous');
};

for i = 1:length(alphas)
    alpha = alphas(i);
    fx = @(x) sin(alpha * x);   
    y = fx(x);                  
    true_values = fx(xx);       

    figure
    hold on

    for j = 1:size(interpolants, 1)
        method_name = interpolants{j, 1};
        method_func = interpolants{j, 2};

        interpolant_values = method_func(x, y, xx);

        error = abs(true_values - interpolant_values);
        
        semilogy(xx, error, 'DisplayName', [method_name ' Error'], 'LineWidth', 1.5);
    end

    hold off
    legend('show', 'Location', 'best')
    xlabel('x')
    ylabel('Absolute Error (log scale)')
    title(['Interpolation Error (Log Scale) for \alpha = ' num2str(alpha)])
    grid on
end
```
![[Pasted image 20250211205230.png]]
![[Pasted image 20250211205243.png]]
![[Pasted image 20250211205259.png]]
1. **10th Degree Global Polynomial**
Let’s first look at the error bound of the 10th degree polynomial,
$$\begin{aligned}
\lvert e_{n}(x) \rvert &\leq \text{max}_{{t \in [0,\pi]}} \frac{\lvert f^{(11)}(t) \rvert }{11!} \text{max}_{s \in[0,\pi]}\left\lvert  \prod_{j=0}^{10} (s-x_{j})  \right\rvert\\
&= \text{max}_{t\in[0,\pi]} \frac{\lvert \alpha^{11}\sin(\alpha t) \rvert }{11!}\text{max}_{s \in[0,\pi]}\left\lvert  \prod_{j=0}^{10} (s-x_{j})  \right\rvert
\end{aligned} $$

For the maximum of $\left\lvert  \prod_{j=0}^{10}(s-x_{j})  \right\rvert$ we can use the following matlab script,
```MATLAB
xx = linspace(0, pi, 11);
P = poly(xx);
x = 0:0.001:pi;

result = polyval(P, x);
max_val = max(abs(result)); 
disp(max_val);


check_roots = polyval(P, xx);
disp('Values at roots (should be near zero):');
disp(check_roots);
```
We get that it is 1.2257, therefore
$$\lvert e_{n} \rvert \leq \frac{\alpha^{11}\cdot 1.2257}{11!}$$
Since $\alpha = 0.1,1,12$, we will have different maximum bounds when $\alpha=0.1$ and $\alpha=1,12$.
This is because when $\alpha=0.1$, in the range $t\in[0,\pi]$ the maximum is $\sin(\alpha \cdot \pi)$ where as when $\alpha=1,12$, the maximum is $1$. However this is still dominated by $\alpha^{11}$.

- **not-a-knot cubic spline**
Ignoring the constant $c$, the error bound will be in the form,
$$\lvert e_{n} \rvert \leq \lvert f'''' \rvert_{\infty }h^4 = \alpha^{4}\left( \frac{\pi}{10} \right)^4 $$

- **Piecewise-cubic Hermite**
$$\lvert e_{n} \rvert \leq  \lvert f'''' \rvert_{\infty} \frac{h^4}{384} =  \alpha^4 \left( \frac{\pi}{10} \right)^4 \frac{1}{384}$$
- **Piecewise-linear polynomial**
$$\lvert e_{n} \rvert \leq c \cdot  \lvert f'' \rvert _{\infty} \frac{h^2}{8}=c \cdot  \alpha^2\left( \frac{\pi}{10} \right)^2 \frac{1}{8}$$
- **Piecewise-constant polynomial**
$$\lvert e_{n} \rvert \leq \lvert f' \rvert _{\infty} \frac{h}{2} \leq \alpha \left( \frac{\pi}{10} \right) \frac{1}{2}$$

We can see that in general cases ($\alpha=0.1,1$) that the 10th degree polynomial has the lowest error bound and this is because the error bound we found shows that $\alpha^{11} \cdot \frac{1.2257}{11!} <\alpha^{11} \cdot 10^{-7}$. In cases where $\alpha = 0.1,1$ this trend follows. However, when $\alpha=12$, we can see that $\alpha^{11}$ grows exponentially showing that the error exceeds the other interpolants. This is due to the high-sensitivity on $\alpha$ for the error bound.

If we consider not-a-knot cubic spline and piecewise-cubic hermite, they follow similar error bounds. However, they are much sensitive to $\alpha$, hence when $\alpha=12$ we can observe that the error increases. 

Piecewise-linear shows a higher error bound from the previous options. And this trend is shown within the figures when plotted. As $\alpha=12$, the error overall becomes similar and this is due to the low-sensitivity on $\alpha$. This applies similarly, yet less on piece-wise linear. As for  piece-wise constant, it generally shows one of the highest errors when $\alpha=0.1,1$, however as $\alpha=12$, we can see that the error is now not as different. And this is because it is less sensitive to $\alpha$.


#### Question 2
Is is known that $\forall x_{1},x_{2},x_{3} \in \mathbb{R}$, that 
$$\begin{aligned}
f[x_{0},x_{1},x_{2}] &= 1 \\
&= \gamma_{2,2}
\end{aligned}$$
And we also know that,
$$\gamma_{2,2}= \begin{cases}
\frac{\gamma_{2,1}-\gamma_{1,1}}{x_{2}-x_{0}},\quad x_{2}\neq x_{0}  \\
\frac{f^{(2)}(x_{2})}{2!},\quad \text{otherwise}
\end{cases}$$
Thus, let’s consider the case when $x_{2}=x_{0}$, then for all $x_{0},x_{1},x_{2}$ where $x_{0},x_{2}$,
$$\frac{f^{(2)}(x_{2})}{2!} = 1$$
And this can only be when $f$ is a polynomial of degree 2. Therefore, let’s set $f(x)$ as 
$$f(x) =ax^2+b x + c$$
Now let’s consider the constraints $f(0)=0,f(1)=2$,
$$\begin{aligned}
f(0)&=a\cdot 0^2+b\cdot 0+c=c=0 \to c=0 \\ 
f(2)&=a\cdot 1^2+b\cdot 1+c=a+b+c=2 \to a+b=2
\end{aligned}$$

And now we use the fact that $f[x_{0},x_{1},x_{2}]=1$,
$$\begin{aligned}
f[x_{0},x_{1},x_{2}] &= \frac{f[x_{1},x_{2}]-f[x_{0},x_{1}]}{x_{2}-x_{0}} \\ 
&=\frac{ \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}-\frac{f(x_{1})-f(x_{0})}{x_{1}-x_{0}} }{x_{2}-x_{0}} \\ 
&= \frac{ \frac{ax_{2}^2+b x_{2} -ax_{1}^2 - b x_{1}}{x_{2}-x_{1}} - \frac{ax_{1}^2+b x_{1}-ax_{0}^2-b x_{0}}{x_{1}-x_{0}} }{x_{2}-x_{0}} \\ &= \frac{a(x_{2}+x_{1})+b - a(x_{1}+x_{0})-b}{x_{2}-x_{0}} \\ 
&= \frac{a(x_{2}-x_{0})}{x_{2}-x_{0}} \\
&= a=1
\end{aligned}$$
Then, using that $a+b=2$, we get $b=2-a=1$, hence,
$$ \therefore f(x)=x^2+x$$
#### Question 3 

##### (a) 
$$\begin{aligned}
p_{1}(x) &= \frac{101-98}{14-7}(x-7)+98 \\ 
&= \frac{3}{7}x+95
\end{aligned}$$

Now, let’s compute the quadratic interpolants for data points $\left\{ (0,100),(7,98),(14,101) \right\}$ and $\left\{ (7,98),(14,101),(21,50) \right\}$ in the forms,
$$\begin{aligned}
p_{2}(x)&=a_{1}x^2+b_{1}x+c_{1} \\ 
p_{3}(x)&=a_{2}x^2+b_{2}x+x_{2}
\end{aligned}$$

We can construct the linear system for $p_2(x)$,
$$\begin{bmatrix}
196 & 14 & 1 \\
49 & 7 & 1 \\
0 & 0 & 1
\end{bmatrix}\begin{bmatrix}
a_{1} \\
b_{1} \\
c_{1}
\end{bmatrix}=\begin{bmatrix}
101 \\
98 \\
100
\end{bmatrix}$$
thus,
$$\therefore \begin{bmatrix}
a_{1} \\
b_{1} \\
c_{1}
\end{bmatrix}= \begin{bmatrix}
\frac{5}{98}  \\
-\frac{9}{14} \\
100
\end{bmatrix}$$

For $p_{3}(x)$,
$$\begin{bmatrix}
441 & 21 & 1 \\
196 & 14 & 1 \\
49 & 7 & 1
\end{bmatrix}\begin{bmatrix}
a_{2} \\
b_{2} \\
c_{3}
\end{bmatrix}= \begin{bmatrix}
50 \\
101 \\
98
\end{bmatrix}$$
thus,
$$\therefore \begin{bmatrix}
a_{2} \\
b_{2} \\
c_{2}
\end{bmatrix}=\begin{bmatrix}
-\frac{27}{49} \\
12 \\
41
\end{bmatrix}$$

and we can conclude that,
$$\begin{aligned}
p_{1}(x)&=\frac{3}{7}x+95\\
p_{2}(x)&= \frac{5}{98}x^2-\frac{9}{14}x+100 \\
p_{3}(x)&= -\frac{27}{49}x^2+12x+41
\end{aligned}$$

we use the following `MATLAB` code to plot these interpolants,
```MATLAB
fx1 = @(x) 3/7 * x + 95;
fx2 = @(x) 5/98 * x.^2 - 9/14 * x +100;
fx3 = @(x) -27/49 * x.^2 + 12 * x + 41;

x = [0 7 14 21];
y = [100 98 101 50];


x1 = [7 14];
xx1 = linspace(x1(1), x1(end), 100);
y1 = [98, 101];

x2 = [0 7 14];
xx2 = linspace(x2(1), x2(end), 100);
y2 = [100 98 101];

x3 = [7 14 21];
xx3 = linspace(x3(1), x3(end), 100);
y3 = [98 101 50];

figure
plot(x,y,'o')
hold on
plot(xx1, fx1(xx1), "-b", "DisplayName", "Linear");
plot(xx2, fx2(xx2), "-g", "DisplayName", "Quadratic with day 0");
plot(xx3, fx3(xx3), "-m", "DisplayName", "Quadratic with day 21");
hold off

disp(fx1(12))
disp(fx2(12))
disp(fx3(12))
```

![[Screenshot 2025-02-06 at 5.41.30 PM.png]]
Now, let’s evaluate the interpolants at $x=12$.
$$\begin{aligned}
p_{1}(12) &= 12 \cdot \frac{3}{7} + 95  = 100.1429 \\
p_{2}(12) &= \frac{5}{98}\cdot 12^2 -\frac{9}{14}\cdot 12 + 100 = 99.6327 \\ 
p_{3}(12) &= -\frac{27}{49}\cdot 12^2 +12\cdot 12+41 = 105.6531
\end{aligned}$$

Considering the stock drop between day 14 and day 21, one could argue that $p_{3}$ would be more accurate for the evaluation at $x=12$ as it captures the stock drop as well. However, I argue that $p_2$ is more accurate. In terms of stock, it is referring to more information from the past capturing a more collective trend of the data for $x=12$. Also, the constant yet rapid drop of $p_3$ is not very representative to be accurate. As for $p_1$, it has less data captured compared to $p_{2},p_{3}$ hence it is not considered as accurate in my opinion. 

##### (b)
The following code was used to plot the two polynomials $p_{2}(x),p_{3}(x)$ from part (a) with the corresponding interval $[0,21]$.

```MATLAB
fx2 = @(x) 5/98 * x.^2 - 9/14 * x +100;
fx3 = @(x) -27/49 * x.^2 + 12 * x + 41;

x = [0 7 14 21];
y = [100 98 101 50];

xx = linspace(x(1), x(end), 100);

figure
plot(x,y,'o')
hold on
plot(xx, fx2(xx), "-g", "DisplayName", "Quadratic with day 0");
plot(xx, fx3(xx), "-m", "DisplayName", "Quadratic with day 21");
hold off
```
Which gives the following plot,
![[Screenshot 2025-02-06 at 5.53.13 PM.png]]
We can observe that the two polynomials show very different trends from one another. Depending on the data that was used to create the interpolant, we can see that $p_2(x)$ is a quadratic that is concave up while $p_3(x)$ is concave down. Showing that  according to $p_2$ there will be a constant increase where as for $p_{3}$ there will be a constant increase. We can also see that there is a faster gradient in change in $p_{3}$.

#### Question 4

```MATLAB
f = @(x) 1 ./ (1 + 25 * x.^2); % runge function
xx = -1:.001:1;
n = 10:10:170;

max_errors = zeros(1, length(n));

for j = 1:length(n) 
    ni = n(j);
    i = 0: ni;
    % chebyshev points
    x = cos( (2 * i + 1) * pi / (2 * (ni + 1)) );
    y = f(x);
    
    interpolant = polyfit(x, y, ni);
    interpolant_values = polyval(interpolant, xx);

    error = abs(f(xx) - interpolant_values);

    max_errors(j) = max(error); 

end

figure
semilogy(n, max_errors, '-o', 'LineWidth', 1.5, 'MarkerSize', 6);
xlabel('n (Degree of Polynomial)')
ylabel('Maximum Absolute Error')
title('Maximum Absolute Error of Polynomial Interpolation with Chebyshev Points')
grid on
```
![[Pasted image 20250209200823.png]]
We can see that the minimum error is when $n=40$ below $10^{-3}$ and it ranges from $10^{-1}$ to $10^{-3}$. Although it hits the minimum of the maximum error is at $n=40$, it does not decrease afterwards but shows an irregular oscillation. And this tendency is more frequent in higher degrees of $n$.
#### Question 5
$$f[z_{2},z_{3}] = \frac{f[z_{3}]-f[z_{2}]}{z_{3}-z_{2}} = \frac{2.0-4.0}{4.0-6.0} = 1.0$$
$$f[z_{1},z_{2},z_{3}] = \frac{f[z_{2},z_{3}]-f[z_{1},z_{2}]}{z_{3}-z_{1}} = \frac{1.0 - 5.0}{4.0-5.0} = 4.0$$
$$f[z_{0},z_{1},z_{2},z_{3}] = \frac{f[z_{1},z_{2},z_{3}]-f[z_{0},z_{1},z_{2}]}{z_{3}-z_{0}} = \frac{4.0-(-3.0)}{4.0-5.0}=-7.0$$
$$f[z_{0},z_{1},z_{2}]=-3.0=  \frac{f[z_{1},z_{2}]-f[z_{0},z_{1}]}{z_{2}-z_{0}} = \frac{5.0-f[z_{0},z_{1}]}{6.0-5.0} \to f[z_{0},z_{1}]=8.0$$
$$f[z_{1},z_{2}]= \frac{f[z_{2}]-f[z_{1}]}{z_{2}-z_{1}}= \frac{4.0-f[z_{1}]}{6.0-5.0}=5.0 \to f[z_{1}]=-1.0$$
$$f[z_{0}]=f[5.0]=f[z_{1}]=-1.0$$

Hence, we can make the table,
$$
\begin{array}{c|c|c|c|c|c|c}  
i & z_{i} & f[\cdot] & f[\cdot ,\cdot ] & f[\cdot ,\cdot ,\cdot ] & f[\cdot ,\cdot ,\cdot ,\cdot ] \\  
\hline  0 & 5.0 & -1.0 \\  
1 & 5.0 & -1.0 & 8.0 \\
2 & 6.0 & 4.0 & 5.0 & -3.0 \\
3 & 4.0 & 2.0 & 1.0 & 4.0 & -7.0
\end{array}  
$$
#### Question 6
Let’s set this polynomial $p_2$ as,
Let’s use the Netwonian Basis,
$$\begin{aligned}
p(x) &= f[z_{0}]+f[z_{0},z_{2}](x-z_{0})+f[z_{0},z_{1},z_{2}](x-z_{0})(x-z_{1}) \\ 
&=-1+8(x-5)-3(x-5)(x-5) \\
&= -1 + 8x-40 -3x^2+33x-90 \\ 
&= -3x^2+38x+116
\\ \\
&\therefore p(x) =-3x^2+38x+116
\end{aligned}$$
#### Question 7
##### (a)
We are aware that,
$$s_{i}(x) =a_{i}+b_i(x-x_{i})+c_{i}(x-x_{i})^2,\quad x_{i}\leq x \leq x_{i+1},\quad i=0,\cdots,n-1$$
Since we want a $C^1$ piecewise quadratic interpolation, we need to satisfy the following,
$$\begin{aligned}
s_{i}(x_{i}) &= f(x_{i}) \to n\text{ equations} \\ 
s_{i}(x_{i+1})&=f(x_{i+1}) \to n\text{ equations} \\
s'_{i}(x_{i+1}) &= s'_{i+1}(x_{i+1}) \to n-1 \text{ equations}\\
f'(a)&=s'(x_{0})\to 1\text{ equations}
\end{aligned}$$
Hence, with these constraints we have $3n$ equations making it possible to determine the $3n$ coefficients. Also, we know that $x_{i+1}-x_{i}=h$. Then,

$$\begin{aligned}
s_{i}(x_{i})=a_{i}&=f(x_{i}),\;i=0,\cdots,n-1 \\
s_{i}(x_{i+1})=a_{i}+b_{i}h+c_{i}h^2&=f(x_{i+1}),\; i=0,\cdots,n-1 \\
s'_{i}(x_{i+1})=b_{i}+2c_{i}h&=b_{i+1}=s'_{i+1}(x_{i+1}),\; i=0,\cdots,n-2\\
s'(x_{0})=b_{0}&=f'(a)
\end{aligned}$$

We then have some initial conditions,
$$\begin{aligned}
a_{0}&=f(x_{0})=f(a) \\
b_{0}&=f'(a) \\ 
c_{0}&=\frac{f(x_{1})-a_{0}}{h^2}-\frac{b_{0}}{h}= \frac{f(x_{1})-f(a)}{h^2}- \frac{f'(a)}{h}
\end{aligned}$$

with 
$$\begin{aligned}
a_{i}&=f(x_{i}) \;\;\; i=1,\cdots,n-1\\
b_{i}&=b_{i-1}+2c_{i-1}h \;\;\; i=1,\cdots,n-1 \\
c_{i}&= \frac{f(x_{i+1})-f(x_{i})}{h^2}- \frac{b_{i}}{h}\;\;\;i=1,\cdots, n-1
\end{aligned}$$

Thus, the algorithm could be written as,
$$\begin{aligned}
&\text{Initial Conditions: } \\ 
&a_{0}=f(x_{0}),b_{0}=f(a),c_{0}= \frac{f(x_{1})-f(a)}{h^2}-\frac{f'(a)}{h} \\ \\
&\text{For $i=1,\cdots,n-1$} \\
&\quad a_{i}\leftarrow f(x_{i} )\\
& \quad b_{i} \leftarrow b_{i-1} +2c_{i-1}h \\
&\quad c_{i} \leftarrow \frac{f(x_{i+1})-f(x_{i})}{h^2}- \frac{b_{i}}{h} \\ \\
& \text{Return } a_{0},\cdots,a_{n-1},b_{0},\cdots,b_{i-1},c_{0},\cdots,c_{i-1}
\end{aligned}$$

##### (b)
Piecewise quadratic interpolation error is as the following, 
$$\begin{aligned}
\lvert e_{2} \rvert &\leq\text{max}_{\xi \in [x_{i-1},x_{i}]} \frac{\lvert f'''(\xi) \rvert }{3!}\text{max}_{\zeta \in [x_{i-1},x_{i}] } \left\lvert  (\zeta-x_{i})(\zeta-x_{i-1})^2 \right\rvert   \\
&=  \frac{\lvert f''' \rvert _{\infty}}{3!} \cdot  h^3 \cdot  \frac{2^2}{3^3} \\ 
&= \frac{2h^3}{81}\lvert f''' \rvert _{\infty} \\ \\ 
\therefore \lvert e_{2} \rvert  \leq \frac{2h^3}{81}\lvert f''' \rvert _{\infty}
\end{aligned}$$

Let’s dig in a bit,
$$ \begin{aligned}
g(\zeta)&=(\zeta-x_{i})(\zeta-x_{i-1})^2  \\
g'(\zeta)&= 2(\zeta-x_{i})(\zeta-x_{i-1}) +(\zeta-x_{i-1})^2 \\
&=(\zeta - x_{i-1})(3\zeta -2x_{i}-x_{i-1}) \\
&\to g'(\zeta)=0, \zeta=x_{i-1}, \frac{2x_{i}+x_{i-1}}{3}
\end{aligned} $$

Since $g(x_{i-1})=0$, we shall look at $g\left(  \frac{2x_{i}+x_{i-1}}{3}  \right)$,
$$\begin{aligned}
g\left(  \frac{2x_{i}+x_{i-1}}{3}  \right)&= \left( \frac{-x_{i}+x_{i-1}}{3} \right)\left(  \frac{2x_{i}-2x_{i-1}}{3}  \right)^2 \\ \\ 
\text{max}_{\zeta \in [x_{i-1},x_{i}] } \left\lvert  (\zeta-x_{i})(\zeta-x_{i-1})^2 \right\rvert &= \left( \frac{h}{3} \right)\left( \frac{2h}{3} \right)^2 = \frac{4h^3}{3^3}
\end{aligned}$$
Which explains our error bound above.
#### Question 8
First, let’s set $s_{i}(x)$ as the following,
$$s_{i}(x)=a_{i}+b_{i}(x-t_{i})+c_{i}(x-t_{i})^2+d_{i}(x-t_{i})^3$$
$$s_{i}'(x)=b_{i}+2c_{i}(x-t_{i}) +3d_{i}(x-t_{i})^2$$
Then,
$$\begin{aligned}
s_{i}(t_{i})&= a_{i} =f_{i} \\ 
s_{i}'(t_{i})&=b_{i}=f'_{i} \\ 
s_{i}(t_{i+1})&=a_{i}+b_{i}(t_{i+1}-t_{i})+c_{i}(t_{i+1}-t_{i})^2+d_{i}(t_{i+1}-t_{i})^3=f_{i+1} \\ 
s'_{i}(t_{i+1}) &= b_{i} + 2c_{i}(t_{i+1}-t_{i}) + 3d_{i}(t_{i+1}-t_{i})^2 =f'_{i+1}
\end{aligned}$$

If we re-arrange $s_{i}(t_{i+1}),s_{i}'(t_{i+1})$ using the values of $a_i,b_i$ we got, and also letting $h_{i}=t_{i+1}-t_{i}$,
$$\begin{aligned}
2h_{i}c_{i}+3h_{i}^2d_{i}&=f_{i+1}'-f_{i}' =A \\
h_{i}^2c_{i} +h_{i}^3d_{i} &= f_{i+1} - f_{i}-h_{i}f_{i}' =B

\end{aligned}$$

Then, if we compute for $c_{i},d_{i}$ we get,
$$\begin{aligned}
d_{i}&= \frac{A}{h_{i}^2}-\frac{2B}{h_{i}^3} = \frac{f_{i+1}'-f_{i}'}{h_{i}^2} -\frac{2(f_{i+1}-f_{i}-h_{i}f_{i}')}{h_{i}^3} \\ 
&= \frac{f_{i+1}'+f_{i}'}{h_{i}^2} - \frac{2(f_{i+1}-f_{i})}{h_{i}^3}
\end{aligned}$$
$$\begin{aligned}
c_{i}&= -\frac{A}{h_{i}}+\frac{3B}{h_{i}^2} = \frac{-(f_{i+1}'-f_{i}')}{h_{i}} + \frac{3(f_{i+1}-f_{i}-h_{i}f_{i}')}{h_{i}^2} \\ 
&= \frac{-f_{i+1}'-2f_{i}'}{h_{i}} + \frac{3(f_{i+1}-f_{i})}{h_{i}^2}
\end{aligned}$$

Thus, we can express $s_i(x)$ as the following,
$$\begin{aligned}
s_{i}(x)&=a_{i}+b_{i}(x-t_{i})+c_{i}(x-t_{i})^2+d_{i}(x-t_{i})^3 \\
&= f_{i}+f_{i}'(x-t_{i})+\left\{\frac{-f_{i+1}'-2f_{i}'}{h_{i}} + \frac{3(f_{i+1}-f_{i})}{h_{i}^2}\right\}(x-t_{i})^2 \\ &+ \left\{  \frac{f_{i+1}'+f_{i}'}{h_{i}^2} - \frac{2(f_{i+1}-f_{i})}{h_{i}^3} \right\}(x-t_{i})^3
\end{aligned}$$

Now, by letting $\tau = \frac{x-t_{i}}{h_{i}}$,
$$\begin{aligned}
\therefore s_{i}(x) &=f_{i} +(h_{i}f_{i}')\tau + \left(3(f_{i+1}-f_{i})-h_{i}(f_{i+1}'+2f_{i}')\right)\tau^2  \\
&+ \left( (f_{i+1}'+f_{i}')h_{i} - 2(f_{i+1}-f_{i})\right)\tau^3
\end{aligned}
$$
as required.
#### Question 9
###### (a)
The following script was used to compute the polynomial interpolant of degree 4,
```MATLAB
x = [1 2 3 4 5];
y = [1 1 2 6 24];

xx = linspace(x(1), x(end), 100);

interpolant = polyfit(x,y,4);
interpolant_values = polyval(interpolant, xx);
figure
plot(x,y,'o')
hold on
plot(xx, interpolant_values);
hold off
```
![[Pasted image 20250206201915.png]]
##### (b)
```MATLAB
x = [1 2 3 4 5];
y = [1 1 2 6 24];

xx = linspace(x(1), x(end), 100);
yy = spline(x, y, xx);
figure
plot(x,y,'o')
hold on
plot(xx, yy);
hold off
```
![[Screenshot 2025-02-06 at 8.23.07 PM.png]]
##### (c)
```MATLAB
x = [1 2 3 4 5];
y = [1 1 2 6 24];

xx = linspace(x(1), x(end), 100);

interpolant = polyfit(x,y,4);
interpolant_values = polyval(interpolant, xx);
yy = spline(x, y, xx);
yyy = gamma(xx);
figure
plot(x,y,'o')
hold on
plot(xx, interpolant_values, 'r-');
plot(xx, yy, '--k');
plot(xx, yyy, '-.b');
hold off

legend('points','polynomial','cubicspline','gamma');
```
![[Screenshot 2025-02-06 at 8.30.31 PM.png]]
##### (d)
The following is the code to plot the absolute and relative errors between the gamma function and the interpolants from part (a) and part (b).
```MATLAB
x = [1 2 3 4 5];
y = [1 1 2 6 24];

xx = linspace(x(1), x(end), 100);

interpolant = polyfit(x,y,4);
interpolant_values = polyval(interpolant, xx);
yy = spline(x, y, xx);
yyy = gamma(xx);

error_polynomial_abs = abs(interpolant_values - yyy);
error_cubicspline_abs = abs(yy - yyy);
error_polynomial_rel = error_polynomial_abs ./ abs(yyy);
error_cubicspline_rel = error_cubicspline_abs ./ abs(yyy);

figure(1);
hold on
plot(xx, error_polynomial_abs, "r");
plot(xx, error_cubicspline_abs, "g");
hold off

legend("polynomial absolute error", "cubicspline absolute error");

figure(2); 
hold on
plot(xx, error_polynomial_rel);
plot(xx, error_cubicspline_rel);
hold off

legend("polynomial relative error", "cubicspline relative error");
```
Figure 1 refers to the absolute error, and figure 2 refers to the relative error.
![[Screenshot 2025-02-06 at 9.04.30 PM.png]]

We can see that in the interval $[0,3]$ that the absolute / relative error for the 4-th degree polynomial interpolant is higher than cubic spline interpolation. However, in the interval $[3,5]$ we can see that the absolute / relative error for cubic spline interpolation higher than that of the 4-th degree polynomial.
#### Question 10
##### (a)
```MATLAB
x = [0.1 0.15 0.2 0.3 0.35 0.5 0.75];
y = [3.0 2.0 1.2 2.1 2.0 2.5 2.5];

xx = 0.05:0.01:0.8;

interpolant = polyfit(x, y, length(x) - 1);
interpolant_values = polyval(interpolant, xx);

figure 
plot(x,y,'o')
hold on
plot(xx, interpolant_values);
hold off
```
![[Pasted image 20250209201922.png]]

##### (b)
```MATLAB
x = [0.1 0.15 0.2 0.3 0.35 0.5 0.75];
y = [3.0 2.0 1.2 2.1 2.0 2.5 2.5];

xx = 0.05:0.01:0.8;

yy = spline(x, y, xx);

figure 
plot(x,y,'o')
hold on
plot(xx, yy);
hold off
```
![[Screenshot 2025-02-09 at 8.19.56 PM.png]]

##### (c)
```MATLAB
N = 7;
funcs = cell(1, N + 1);

xx = [0.1 0.15 0.2 0.3 0.35 0.5 0.75];
yy = [3.0 2.0 1.2 2.1 2.0 2.5 2.5];

x = 0.05:0.01:0.8;

epsilons = [0.1 0.01 0.001];

figure
hold on

plot(xx, yy, 'o');


for k = 1:length(epsilons)
    epsilon = epsilons(k);

    funcs{1} = @(x) 1;

    for i = 2: N + 1
        funcs{i} = @(x) sqrt((x - xx(i - 1)).^2 + epsilon^2) - epsilon; % each psi_i
    end


    A = zeros(length(xx), length(funcs));

    for j = 1:length(funcs)
        A(:, j) = funcs{j}(xx);
    end

    A = [A; ones(1, N + 1)];

    yyy = [yy, 0]';

    c = (A\yyy)';

    polynomial = @(x) c(1) * funcs{1}(x) + c(2) * funcs{2}(x) + ...
                    c(3) * funcs{3}(x) +  c(4) * funcs{4}(x) + ... 
                    c(5) * funcs{5}(x) + c(6) * funcs{6}(x) + ...
                    c(7) * funcs{7}(x) + c(8) * funcs{8}(x);

    interpolant_values = polynomial(x);

    plot(x, interpolant_values, 'DisplayName', ['\epsilon = ' num2str(epsilon)]);
end

hold off
legend('show', 'Location', 'best')
xlabel('x')
ylabel('y')
title('Interpolation with Different \epsilon Values')
grid on
```
![[Pasted image 20250209233935.png]]
We can see that as $\epsilon$ increases the interpolant is smoother, on the other hand, as $\epsilon$ becomes smaller we can see that the interpolants are less smoother, and they are more localized.

Also,
$$\lim_{ \epsilon \to 0 } \phi_{j}(x) =\lim_{ \epsilon \to 0 } \sqrt{ (x - x_{j-1})^2 + \epsilon^2 }-\epsilon = x-x_{j-1}$$
it becomes linear, and thus becomes a piecewise linear interpolant.

