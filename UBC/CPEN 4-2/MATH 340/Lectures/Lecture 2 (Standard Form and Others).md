
We will focus on the following form for LP problems,
$$\text{Maximize }c_{1}x_{1}+ c_{2}x_{2}+\cdots+ c_{n}x_{n}$$
$$\text{subject to } a_{11}x_{1}+a_{12}x_{2}+\cdots a_{1n}x_{n} \leq b_{1}$$
$$a_{21}x_{1}+a_{22}x_{2}+\cdots a_{2n}x_{n} \leq b_{2}$$
$$\vdots$$
$$a_{m1}x_{1}+a_{m_{2}}x_{2}+\cdots a_{mn}x_{n} \leq b_{m}$$
$$x_{1},x_{2},\cdots,x_{n} \geq \sigma$$

A non-standard form can be reduced to the standard form, for instance,
$$\text{minimize } 3x_{1}-2x_{2}+x_{3} + 1$$
$$\text{subject to }-x_{1}+x_{2}\geq-3$$
$$2x_{1}+x_{2} \leq 2$$
$$x_{1}+x_{2}+x_{3}= 4$$
$$x_{1}\geq-2,x_{2}\leq 2$$

[Principles]
- $\text{min }f = -\text{max }(-f)$ 
- $\text{max}(f + const) \iff \text{max}(f)$
- $x\geq a \iff -x \leq -a$
- $x=a \iff x \leq a \text{ and }-x \leq -a$
- $x \geq a \iff x-a \geq 0$
- $\text{no restriction on }x \iff x = x^+ - x^-,x^+ \geq 0, x^- \geq 0$

Following the form, we can set $x_{1}\geq-2,x_{2}\leq{2} \to x_{1}+2\geq 0, 2-x_{2} \geq 0$.
So let $x_{1}'=x_{1}+2$ and $x_{2}' = 2-x_{2}$ as well as $x_{3}=x_{3}^+ - x_{3}^-$,

1.
$$-x_{1}+x_{2} \geq -3 \to -(x_{1}'-2) + (2-x_{2}') \geq -3 \to x_{1}'+x_{2}' \leq 7$$
2.
$$2x_{1}+x_{2} \leq 2 \to 2(x_{1}'-2)+(2-x_{2}') \leq 2 \to 2x_{1}'-x_{2}' \leq 4$$
3.
$$x_{1}+x_{2}+x_{3} =4 \to (x_{1}' - 2) + (2-x_{2}') +x_{3} = 4 \to x_{1}'-x_{2}' +x_{3} = 4$$
$$\to x_{1}'-x_{2}'+x_{3}^+ - x_{3}^- \leq 4, -x_{1}'+x_{2}'-x_{3}^+ + x_{3}^- \leq -4$$4.
$$x_{1}',x_{2}',x_{3}^+,x_{3}^- \geq 0$$

5.
$$\text{min} (3x_{1}-2x_{2}+x_{3} + 1) \to -\text{max}( -3x_{1}+2x_{2}-x_{3} - 1)$$
$$\to 1 -\text{max}(-3x_{1}+2x_{2}-x_{3})$$


With all of these, we can get the optimal solution.


**Observation to generalize:**
- The feasible set is of polygonal shape (polyhedron in general dimensions).
- The maximum occurs at the vertex (corner) of the polygonal shape.

###### Convexity
A set $S \subseteq \mathbb{R}^n$ is **convex** if $$\forall  \vec{x},\vec{y} \in S,t \in[0,1] \to (1-t) \vec{x} + \vec{y} \in S$$
That is, for any two points in S, the line segment connecting them also belongs to S.

Let’s look at some examples of convex, non-convex sets,

e.g. Non-convex
![[Screenshot 2025-01-25 at 11.26.12 PM.png]]
In this case, the line segment connecting the two points partially belongs in $S$, hence not convex.

e.g. Convex
$$S=\mathbb{R}^n$$
is convex.

e.g. Convex
$$H= \left\{ \vec{x} \in \mathbb{R}^n \vert \vec{a} \cdot \vec{x} \leq b \right\}$$
a.k.a the half-plane is convex.

![[Screenshot 2025-01-25 at 11.28.01 PM.png]]
[Proof]
Pick any two points $\vec{x}, \vec{y}$ in $H$, that is $\vec{a} \cdot   \vec{x} \leq b$ and $\vec{a} \cdot   \vec{y} \leq b$. Let’s consider any point $\vec{z}$ in the line segment between $\vec{x},\vec{y}$.
$$\vec{z} = (1-t)\vec{x}+t \vec{y}, t \in [0,1]$$
$$\vec{a}\cdot  \vec{z} = (1-t)(\vec{a} \cdot  \vec{x}) + t(\vec{a}  \cdot  \vec{y})$$
$$ \leq (1-t)b + tb = b$$
$$\therefore \vec{z} \in H$$
so $H$ is a convex set.

e.g. The empty set is convex.
e.g. Hyperplanes are convex.
e.g. Intersections of hyperplanes are convex.

#### Theorem
Let $S_{1},S_{2} \subset \mathbb{R}^n$ suppose $S_{1},S_{2}$ are both convex, then $S_{1} \cap S_{2}$ is convex.

[Proof]
Let $\vec{x},\vec{y} \in \mathbb{R}^n$ such that $\vec{x},\vec{y} \in S_{1}$ and $\vec{x},\vec{y} \in S_{2}$. Then by consequence, we have that $\vec{x},\vec{y} \in S_{1} \cap S_{2}$.

For some $t \in [0,1]$ we also have that $(1-t)\vec{x} + t \vec{y} \in S_{1},S_{2}$. Consequently, we have that
$$(1-t) \vec{x} + t \vec{y} \in S_{1}\cap S_{2}$$
Hence, the intersection is also convex.


For the empty set, we can get two convex sets that are disjoint.
###### Convex functions
A function $f: \mathbb{R}^n \to \mathbb{R}$ is said to be a **convex function** if the set]\
$$\left\{ (x,t) \in \mathbb{R}^n \times \mathbb{R}\hspace{.05in} \vert \hspace{.05in} f(x) \leq t \right\}$$
is convex.
![[Screenshot 2025-01-25 at 11.29.23 PM.png]]

A set of points in $\mathbb{R}^{n+1}$ “above” the graph of $f$.

###### Intersection of Half Spaces
As any half space is **convex**, for any half-space,
$$H_{i} = \left\{  \vec{x} \in \mathbb{R}^n \hspace{.05in} \vert \hspace{.05in} \vec{a}_{i} \cdot  \vec{x} \le b_{i} \right\}$$
for $i = 1,2,3,\cdots,N$. We have that,
$$H_{1} \cap H_{2} \cap \cdots \cap H_{N}$$
is also **convex**!


