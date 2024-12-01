## Scale Detection
Intuitively, we find local maxima in both position and scale. Since depending on scale, corners might appear more edgy or less edgy. 
![[Screenshot 2024-10-19 at 11.42.03 AM.png]]

### Blobs
![[Screenshot 2024-10-19 at 11.42.25 AM.png]]
Blobs are locally distinct features, but they are more of the circular regions in the image.
The laplacian can helps us in detecting such blobs!

Formally,
![[Screenshot 2024-10-19 at 11.46.07 AM.png]]
Think of the signal as a 1D blob (hopefully), in reality it is rotated, we will get the strongest response when the signal has the same **characteristic scale** as the filter.
=> This is because the filter can perfectly capture the transition within the image when perfectly aligned. (The size of the structure and the scale $\sigma$ has somewhat of a relation)

#### Characteristic Scale
The scale that produces peak filter response. We can detect these blobs among different scales by finding where the peak response is for different sizes.
=> The scale at which “corner-ness” or “blob-ness” is maximized.

Based off the laplacian itself we can see the scale of the blob.
![[Screenshot 2024-10-19 at 11.51.13 AM.png]]

![[Screenshot 2024-10-19 at 11.54.30 AM.png]]
For a certain patch of the image, we can apply the laplacian for different sigmas and the find the peak response. Then, the sigma is going to give locally a scale for that corner (blob).

For every blob, looking at the max can give us the scale of that blob.

#### Scale Selection
A Laplacian (DOG) Pyramid is formed with multiple scale per octave. By taking difference between successive Gaussians (at same resolutions), and taking the difference among them. Across these laplacians, for every position within this laplacian, we can look at the neighbourhood and neighbour across scales (26) if any point is maxima => That is our detection and correspond to the scale at which maxima was found.

![[Screenshot 2024-10-19 at 12.01.16 PM.png]]
![[Screenshot 2024-10-19 at 12.01.32 PM.png]]
Gives blob (position) and the scale (sigma) where it was found.

Implementation:
```python
1. For each level of the Gaussian Pyramid compute feature response 
(Harris, Laplacian) -> With Harris, orientation is also possible to find.
2. For each level of the Gaussian Pyramid, if local maximum and cross-scale
	1. Save scale and location of feature (x,y,s).
```

## Texture
**Texture** is detail in an image that is at a scale too small to be resolved into its constituent elements and at a scale large enough be apparent in the spatial distribution of image measurements.

We don’t name each individual element, more likely a description of a region.

Sometimes, textures are thought of as patterns composed of repeated instances of one (or more) identifiable elements, called **textons**.

#### Uses of Texture
Texture can be a strong cue to **object identity** if the object has distinctive material properties.

Texture can be a strong cure to an **object’s shape** based on the deformation of the texture from point to point.

### Texture Synthesis (Efros and Leung)
Why would we want to synthesize texture?
- To fill holes in images (inpainting).
- To produce large quantities of texture for computer graphics.

**Objective**: Generate new examples of a texture. We take a “data-driven” approach.
**Idea**:
- Draw samples directly from the actual texture.
- Can account for more type of structure.
- Very simple to implement.
- Success depends on choosing a correct “distance”.

Just attaching small textures would not look natural, we need a more statistic approach of nature.

![[Screenshot 2024-10-19 at 12.25.36 PM.png]]

![[Screenshot 2024-10-19 at 12.26.47 PM.png]]
Consider that we have an infinite sample image, what is the **conditional probability** distribution of a point $p$, given the neighbourhood window?
We can directly search the input image for all such neighbourhoods to produce a **histogram** for $p$.

![[Screenshot 2024-10-19 at 12.28.05 PM.png]]
![[Screenshot 2024-10-19 at 12.28.38 PM.png]]
To synthesize $p$, pick one match at random.
Or we can just copy over at random and move on.

- **But**, since the sample image is finite, an exact neighbourhood match might not be present.
- Find the **best match** using SSD error, weighted by Gaussian to emphasize local structure, and take all samples within some distances from that match.

==Look at all possible patches, compute distance to filling patch only for places that do have pixels. Order those based on similarity and use the highest one to fill pixel. But this would lead to always filling in the same pixel for that patch. So pick a threshold, and choose random among those that pass the threshold.==

1. How big of a neighbourhood do we want to consider?![[Screenshot 2024-10-19 at 12.36.34 PM.png]]![[Screenshot 2024-10-19 at 12.38.13 PM.png]]
2. How much down in the list of matches do we want to go?
	1. High threshold would result in more repeating pixels, since we only choose a few matches.
	2. If we have a low threshold, the image would be much more randomized. Maybe not fulfilling the task of filling the pixel in properly.


#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 11|Lecture 11]]

