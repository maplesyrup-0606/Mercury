###### Intro
Optimization problems,
$$\text{maximize/minimize }f(\vec{x})$$
where
$$\vec{x}\in C$$

such $C$ is called the feasible set, those $\vec{x}$ belonging to the feasible set are called “feasible solutions”.

Linear programming (LP) problems:
- The function $f(x)$ is a linear function.
- The constraint is given by combinations of linear inequalities / equations.

$$f(\vec{x})=\vec{c}\cdot \vec{x} = f(x_{1},x_{2},\cdots,x_{n})=c_{1}x_{1}+c_{2}x_{2}+\cdots+c_{n}x_{n}$$

with linear constraints for instance,
$$3x_{1}+2x_{2} \leq 1,\hspace{.1in} 2x_{1}+x_{2}=1,\hspace{.1in}x_{1}\geq{0},\hspace{.1in}2x_{1}+3x_{2}+5x_{4}+7x_{11} \leq 0$$
the feasible set will be the collection of $\vec{x}$ such that the constraints are held all together → feasibility refers to that there is a feasible $\vec{x}$, the feasible set is non-empty.

###### A Planning Problem (Dantzig)
How to most efficiently assign $N$ people to $N$ tasks (allow a person to do multiple tasks).

Assume:
- $c_{ij}$ = the benefit of assigning a person $i$ to task $j$.
- $x_{ij}$ = the portion of person $i$’s time spent on doing task $j$.
- $0\leq x_{ij}$ and $\sum_{j=1}^N x_{ij} = 1$ for each person $i$.
- each job must be done $\sum_{i=1}^N x_{ij} =1$ for each task $j$.

Decision variables : $x_{ij}$ for $1\leq i \leq N, 1 \leq j \leq N$.

The LP problem is:
→ Assigning $i$ to $j$ with $x_{ij}$ portion of time of person $i$ has benefit $c_{ij}x_{ij}$.

→ Maximize the total benefit (objective function)
$$\sum_{j=1}^N \sum_{i=1}^N c_{ij}x_{ij}$$

→ Subject to
$$\sum_{j=1}^N x_{ij} = 1,\hspace{.1in} \sum_{i=1}^N x_{ij} =1,\hspace{.1in} x_{ij} \geq 0$$

- $N \times N$ variables $x_{ij}$, $1\leq i\leq N$, $1\leq j \leq N$.
- and $N+N+N\times N$ constraint.

