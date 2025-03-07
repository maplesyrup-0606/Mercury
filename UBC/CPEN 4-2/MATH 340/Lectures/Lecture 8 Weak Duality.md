Now let’s talk about weak duality, essentially,
$$\text{max of primal} \leq \text{min of dual}$$

Note that
$$F(\vec{y},\vec{w}) \geq \text{max }_{A \vec{x} \leq \vec{b} , \vec{x} \geq \vec{0}} \vec{c}^T \vec{x}\quad \text{for }\vec{y},\vec{w}\geq \vec{0}$$
and 
$$\text{min}_{\vec{y},\vec{w} \geq \vec{0}}F(\vec{y},\vec{w}) = \text{min}_{A^T \vec{y}\geq  \vec{c}, \vec{y} \geq \vec{0}} \vec{b}^T \vec{y}$$
so we have that,
$$\text{min}_{A^T \vec{y}\geq \vec{c}, \vec{y}\geq \vec{0}}\vec{b}^T \vec{y} \geq \text{max}_{A \vec{x} \leq \vec{b}, \vec{x} \geq \vec{0}}\vec{c}^T \vec{x}$$
and this is called weak-duality.

Let’s consider some questions, consider the primal problem,
$$\text{max }_{A \vec{x} \leq \vec{b}, \vec{x} \geq \vec{0}} \vec{c} \cdot  \vec{x}$$
and its dual problem,
$$\text{min}_{A^T \vec{y} \geq \vec{c}, \vec{y} \geq \vec{0}} \vec{b}^T \cdot  \vec{y} $$

Assume that both problems are feasible. Let $\vec{x}^*$ be a feasible solution of the primal problem and $\vec{y}^*$ be a feasible solution of the dual problem. Then,
- The primal / dual problem **must** be bounded.
- It is possible that $\vec{c} \cdot  \vec{x}^* < \vec{b} \cdot  \vec{y}^*$.
- In $\vec{c} \cdot  \vec{x}^* = \vec{b} \cdot  \vec{y}^*$, then $\vec{x}^*,\vec{y}^*$ are the optimal solutions to each problem respectively.
- When $\vec{x}^*, \vec{y}^*$ are optimal solutions of the primal and dual problems, respectively, it may happen that $\vec{c} \cdot   \vec{x}^* < \vec{b} \cdot  \vec{y}^*$.
	- **False**!

In weak duality,

if the dual problem is feasible → the primal solution is bounded.
←>
If the primal problem is unbounded → the dual problem is infeasible.

if the primal problem is feasible → the dual problem is bounded.
←>
if the dual problem is unbounded → the primal problem is infeasible.

- Some Consequences,
	- Any feasible solution to the dual problem provides an upper bound of the objective function for the primal problem.
	- If the dual LP is unbounded (objective → $-\infty$) then the primal problem is not feasible.
	- If the primal LP is unbounded (objective → $\infty$) then the dual problem is not feasible.

###### Optimality and Weak Duality
Suppose,
$\vec{x}_{0}$ is a feasible solution of an LP $\text{max } \vec{c}^T \vec{x}$ and $\vec{y}_{0}$ is a feasible solution of the dual problem $\text{min }\vec{b}^T \vec{y}$.

If $\vec{c}^T  \vec{x}_{0} = \vec{b}^T \vec{y}_{0}$, then
- $\vec{x}_{0}, \vec{y}_{0}$ is an optimal solution for the primal / dual LP problem respectively.

[Proof]
$$\vec{c} \cdot  \vec{x}_{0} \leq \text{max of primal} \leq \text{ min of dual} \leq \vec{b} \cdot  \vec{y}_{0}$$
then if $\vec{c} \cdot  \vec{x}_{0} = \vec{b} \cdot  \vec{y}_{0}$, the above becomes an equality,
$$\vec{c} \cdot   \vec{x}_{0} = \text{max of primal} = \text{min of dual} = \vec{b} \cdot  \vec{y}_{0} $$
Hence, both are optimal solutions.

#### Next Lecture [[Lecture 9 Strong Duality]]
