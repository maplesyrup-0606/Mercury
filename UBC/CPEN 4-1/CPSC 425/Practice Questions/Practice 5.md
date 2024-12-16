#### Question 1
There are advantages to using a hash table rather than an accumulator array to store votes in Hough transform. Which of the following statements are **true** and which are **false**?

- It is faster to enter each vote into a hash table.
**False**, technically it is slower than an array.

- There are more votes in each bin when the fitted model is present.
**False**, the number of votes would be the same. On the other hand, the number of filled bins (a.k.a with votes) would be less.

- Less storage is required since empty bins in a hash table are not represented explicitly.
**True**, non-voted entries are not allocated.

- It is not necessary to predict the maximum range of each parameter in advance in order to determine the array size.
**True**, we only need keys that we’ve voted for. It is dynamic.

#### Question 2
Both the Hough transform and RANSAC are techniques for fitting data to a model. Which of the following statements are **true** and which are **false**?

- RANSAC performs better than the Hough transform as the number of parameters increase.
**True**, it becomes exponentially harder to have higher dimension of hyper parameters for Hough.

- The Hough transform performs better than RANSAC as the number of outliers increases significantly over 50%.
**True**, RANSAC cannot perform well under a lot of outliers. On the other hand, Hough is insensitive to outliers.

- Performance of the Hough transform improves when the points used to fit to the model are more distinctive.
**True**, if more distinctive, we have more distinctive peaks.

- For a particular data set, RANSAC finds, at most, one instance of the model. On the other hand, the Hough transform can find more than one instance, if multiple instances exist.
**True**, RANSAC would find the best solution while Hough would find all good solutions.

#### Question 3
In the context of CPSC 425, what does the term non-parametric mean?

The model is data-driven, there are no assumptions on the particular form of model.

#### Question 4
Suppose we want to fit a circle to a set of points using RANSAC. Assume that 75% of the points are outliers. How many random samples of 3 points are needed to detect the circle with 95% probability.

The probability that all 3 samples fail, hence choose outliers is 
$$1-\left( \frac{1}{4} \right)^3$$

Then we want,
$$\left( \frac{63}{64} \right)^k < 0.05 \to k > \frac{\log(0.05)}{\log\left( \frac{63}{64} \right)}$$
We have the lower bound for the sample number $k$.