#### Discussion of RANSAC

**Advantages**:
- General method suited for a wide range of model fitting problems.
- Easy to implement and easy to calculate its failure rate.

**Disadvantages**:
- Only handles a moderate percentage of outliers without cost blowing up.
- Many real problems have high rate of outliers (but sometimes selective choice of random subsets can help).
- Hard to deal with multiple solutions.

==Hough transform can handle high percentage of outliers and detect multiple matches.==

### Hough Transformation

#### Motivation
![[Screenshot 2024-11-28 at 1.55.23 PM.png]]
Say we want to find lines here, how would we do that? → We can do edge pixels as the coordinates of points and use RANSAC. 

But, we want to find all possible solutions.

#### Idea
- For each token / data point vote for all model to which it could belong.
- Return models that get many votes / distribution of possible models.

Ex. For each point, vote for all lines that could pass through it; the true lines will pass through many points and so receive many points. If incorporated with a threshold, all lines above the threshold are a solution.


###### Image and Parameter Space
Consider the line equation,
$$y=mx+b$$
Considered of variables $x,y$ and parameters $m,b$. We can alternatively plot the parameters in the parameter space. Which would look like a point,
![[Screenshot 2024-11-28 at 2.05.15 PM.png]]
Generally, we won’t know what the lines are but we will know what the points are. And a point would look like this in the parameter space.

![[Screenshot 2024-11-28 at 2.06.00 PM.png]]
So a point gives a family of line solutions. And intersections of crossing lines at a particular point, we can see how many votes a particular solution has.

The best fitting line would be the intersection the points in parameter space.
![[Screenshot 2024-11-28 at 2.08.02 PM.png]]

Is it robust to noise? Not really, we would have some lines shifting (still close). So in hough transformation, we would not look at actually ‘points’ that are crossing, we would do some discretization and see what lines end up in the same ‘bin’.

[Algorithm]
```
1. Quantize parameter space (m,c)
2. Create Accumulator Array A(m,c)
3. Set A(m,c) = 0 for all m,c
4. For each image edge (xi,yi)
	1. For each element in A(m,c)
	2. If (m,c) lies on the line : c = -xi * m + yi
		1. Increment A(m,c) += 1
5. Find local maxima in A(m,c)
```

![[Screenshot 2024-11-28 at 2.11.40 PM.png]]

There is still a bit of a problem, how big should $A(m,c)$ be? $m,c$ are unbounded. It is problematic to parameterize the unbounded parameters.

###### Line: Normal form
$$x\sin \theta+y\cos \theta = r,\hspace{.2in} r \geq 0,0\leq \theta\leq {2}\pi$$
Now since the parameters are bounded, discretizing is possible.

But, with the new parameterization would be a curve in the new space.

![[Screenshot 2024-11-28 at 2.15.29 PM.png]]
![[Screenshot 2024-11-28 at 2.17.25 PM.png]]

Let’s do this in practice.
![[Screenshot 2024-11-28 at 2.17.53 PM.png]]
Consider these points,
$$-5\sin{(5)}+3\cos(5) + r  = 0 \implies r=3.42$$
$$-5\sin(15)+3\cos(15) +r = 0 \implies r=4.18$$
$$\vdots$$

And consistently solve for $r$ with discrete $\rho$ and vote in the array.
![[Screenshot 2024-11-28 at 2.20.48 PM.png]]
And once detected (maybe by setting a threshold) we get points in the parameter space which is a line in the original space.

If we have some noise,
![[Screenshot 2024-11-28 at 2.23.46 PM.png]]

###### Affine Transformation (FYI)
If we were to do this for affine transform or homography, discretizing becomes way too expensive due to the number of unknowns (parameter space becomes high dimensions)

###### Mechanics
1. Construct a quantized array to represent $\theta$ and $r$.
2. For each point, render curve $(\theta,r)$ into this array adding one vote at each cell.

**Difficulties**:
- How big should the cells be? → Too big, then we merge quite different lines; To small, and noise causes lines to be missed.

**How many lines?**
- Count the peaks in Hough array.
- Treat adjacent peaks as a single peak.

###### Practical Details
It is best to **vote** for the two closest bins in each dimension, as the locations of the bins are arbitrary.
- This means that peaks are blurred and noise will not cause similar votes to fall into separate bins.

We can use a **hash table** rather than an array to store the votes.
- This means that no effort is wasted on initializing and checking empty bins.
- It avoids the need to predict the maximum size of the array, which can be non-rectangular.

Votes can be more informative.
- We don’t need to vote for the entire family of solutions, in the case of lines we can vote only to the line orthogonal to the gradient. 

#### Generalized Hough Transform
What if we want to detect an **arbitrary** geometric shape (of any contour)?
We use the idea of ‘informed voting’, for a sample object, compute the edge detections.
For each point, compute gradient orientation → create a database with keys being the gradient orientation. 

We know the center of the object, by using the key as gradient orientation (shown below with arrow along with $\theta$) we store the offset of that point compared to the center.
→ We have a database of all these points.

We can have duplicate entries with same $\theta$ but different offset.

![[Screenshot 2024-11-28 at 3.23.07 PM.png]]

The idea is,
- We compute gradients and get edges.
- For each edge point, compute gradient and go to database → find all entries matching gradient → apply offset matching those entries and vote into that position.
- All points along the contour would vote for same center.

![[Screenshot 2024-11-28 at 3.32.31 PM.png]]

###### Pros and Cons
- **Pros**
	- Can handle high percentage of outliers: each point votes separately.
	- Can detect multiple instances of a model in a single pass.
- **Cons**
	- Search time increases exponentially with the number of model parameters.
	- Can be tricky to pick a good bin size.
#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 14|Lecture 14]]
