#### Question 1
The K-means algorithm can converge to different solutions depending on which points are selected at random as the initial cluster centers. If we ran the algorithm 10 separate times with different random selections and wanted to select the best solution, how would we determine which solution is the best?

For each iteration we can get the overall sum of distances for each centroid and the points of the cluster. And choose the one with the minimum sum.

#### Question 2
We have six locations (1,3) , (2,1), (2,6), (3,2), (3,5), (4,7). We attempt to find two clusters A and B, we select (1,3) for the center of A and (3,5) for the center of B.

- After the first iteration of the algorithm, what points will be assigned to cluster A? What points will be assigned to cluster B? What will be the new, adjusted locations of the cluster centers?
First we determine, where each point is close to A and B.
A: (2,1), (3,2)
B: (2,6), (4,7)

Then the new centers A’ = (2,2), B’ = (3,6)

- Will subsequent iterations of the algorithm change the assignment of the points in the clusters?
No, now the mean distance is minimized.

#### Question 3
We examine loss in a classifier. Assume we have two probability distributions, $P(A|x)$ and $P(B|x)$, both Gaussians with the same $\sigma = 1$, but $A$ has mean 0 and $B$ has mean 1.

- Draw the two distributions so that they are qualitatively correct.
![[Screenshot 2024-12-14 at 1.11.57 AM.png]]

- Where is the decision boundary determining the classifier deciding whether, given $x$, you have an $A$ or a $B$? 
It would be  0.5.

- Now, assume that we have a loss function$L$ and that $L(A\to B)=10$ and $L(B\to A)= 1$. The bayes estimator incorporates the loss function to reflect the cost of errors. In which direction will the the decision boundary move to reflect the cost of errors?
We can see that the penalty of misclassifying A to B is higher, so we want to reduce the risk of misclassifying A. Moves to the right.

- Assume we are testing to identify $A$, what is the term used in classification for the case where we classify something as $B$, when it is in fact $A$?
False negative.