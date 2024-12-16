### Question 1: True / False

(A) Texture depends on scale, illumination and viewpoint.
**True**

(B) The “spots” and (oriented) “bars” approach to texture representation described in Forsyth and Ponce is motivated, in part, by properties of human vision.
**True**

(C) The Laplacian pyramid provides no explicit representation of orientation. But, if we process each layer of the Laplacian pyramid further with a set of oriented filters then we can represent energy at distinct scales and orientations as an “oriented pyramid.”
**True**

### Question 2: True / False
Consider when we increase the degree of randomization for patches.

(A) Unrealistic repeating patterns may appear in the texture.
**False**, this would be the case for low randomization.

(B) The accuracy of selected patches from the sample texture may decrease, leading to unrealistic textures.  
**True**

(C) We will need to use a larger training sample of the texture to maintain similar performance.  
**True**

(D) The method can run faster since we no longer need to compute the actual best match.
**False**, the computation is still needed just a matter of choosing among those results is the problem.

### Question 3
It is common to use normalization of image patches when they are being ”matched” in template matching as we saw earlier; we saw this improves detection. For the Efros and Leung texture synthesis method (as in Assignment 3) would it further improve the results to also normalize patches in the matching step? Explain your answer with just one or two sentences

**Normalization would hurt performance.** If normalized, then textures of different brightnesses will be considered similar. Hence, creating a sharp edge between intensity when patched.