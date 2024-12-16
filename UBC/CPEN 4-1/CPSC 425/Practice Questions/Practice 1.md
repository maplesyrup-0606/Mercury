### Question 1: True / False

(A) A pinhole camera is a box with a small hole in it.
**True**

(B) Images in a pinhole camera are upside down.
**True**, pinhole camera uses perspective projection → Upside down.

(C) A pinhole camera has a fixed focal length, $f$.
**False**, we can move the image plane. → Focal length can change.

(D) Images in a pinhole camera are a perspective projection.
**True**, as mentioned in (B).

### Question 2: True / False
Let’s now consider an actual pinhole camera.

(A) It takes too long to acquire an image.
**True**, the pinhole itself is too small to quickly collect photons.

(B) It uses an orthographic projection.
**False**, still uses perspective projection.

(C) It works only for black and white, not for colour.
**False**, colour can be used.

(D) It has too small a depth of field.
**False**, due to the small hole size, the depth of field is actual large. (sharp focus)

### Question 3: True /  False

(A) Vignetting is a slight curvature of straight lines away from the center of the image.
**False**, vignetting is when the corner of images tend to appear darker.

There is spherical abberation that happens from light bending differently moving off from the center.

(B) Vignetting is a shift in colour owing to the varying refraction of light at different wavelengths.
**False**, this is chromatic abberation.

Chromatic abberation leads to blurring in the image due to different wavelengths spreading at different directions.

(C) Vignetting is a darkening of an image towards its edges.
**True**

Vignetting occurs due to light not reaching the next stage of lens. And hence darkening the edges.

(D) Vignetting makes it difficult to bring all parts of an image into focus at the same time.
**False**, this is more of spherical abberation or chromatic abberation not really vignetting.

### Question 4: True / False
Snell’s law

(A) It describes how light bends when passing from one material into another.
**True**

(B) It describes how fast light travels in one material compared to another.
**True**, the bending happens due to this effect.

(C) It describes the angle at which light bounces off a mirror surface.
**False**, snell’s law is related to refraction, not reflection.

(D) It describes how much light is reflected and how much passes through the boundary between two materials.
**False**

### Question 5: True / False
Consider a human eye.

(A) Images are upside down.
**True**, humans refer to light just like a pinhole camera would do.

(B) It uses an iris to control the amount of light entering the lens.
**True**

(C) The imaging plane is similarly planar.
**False**

(D) It has light sensors evenly spaced to provide optimal resolution over the image.
**False**, the human eye does not have evenly spaced light sensors. + resolution is not optimal.

### Question 6
Consider a scene that contains 5 collinear points. A, B, C, D and E, where collinearity is defined in 3D coordinates. We know that under perspective projection, the projected features are also collinear in the 2D image plane.

(A) Suppose A, B, C, D and E are all equidistant. Will the order of the project points (along the projected line) always be the same in the camera image?

Yes, a line will project into a line in the image plane. Hence, the order would still maintain the same.

(B) Will the observed points also be equidistant in the image plane?

No, let’s consider the case where the points are collinear in a line not parallel to the image plane. And we know the following,
$$x'=f' \frac{x}{z},y'=f' \frac{y}{z}$$
Then, since $z$ differs for all, they would not end up in general to be equidistant.

(C) Now suppose we find five collinear features a, b, c, d, e in the image. Does this imply these points are collinear in the 3D world?

No, any point on the line from the focal length to the a that points would project onto the same point. That being said, there are an infinite amount of possibilities that can end up having the collinear points on the image plane.

### Question 7
Suppose we fold a uniformly painted Lambertian plane to form a non-planar, continuous, piecewise planar surface. This surface consists of just two half-planes joined along a single line. Suppose both sides of this fold are clearly visible inn the image. Is it possible for such a surface to generate a constant (non-zero) image when lit with a single distant light source?

Suppose a light source projects light rays far enough from the image that the light rays appear to be parallel facing the plane. Then these light rays would form the same angle at any point of the surface. We know,
$$L= \frac{\rho_{d}}{\pi}I \cdot(\vec{i}\cdot \vec{n})$$
Then, since the angle is the same along with other properties, we can create a non-zero constant surface.

### Question 8
Recall that the thin lens equation is: $$\frac{1}{f'}=\frac{1}{z'} - \frac{1}{z}$$
Find where a focal length for the lens for which an object is size $x$ that is placed 10m in front of the camera would focus at 10mm. What would be the size of the imaged object?

$$f'=\frac{1}{\frac{1}{10mm}-\frac{1}{-10m}} \approx 10mm$$
Thus, we can imagine the object is very far from the lens.
And,
$$x'=f' \frac{x}{z} = 10mm \frac{x}{-10m}= -\frac{1}{1000}x$$
So the size would be 1/1000 of the original (and inverted).

### Question 9
Explain in a few sentences how you would increase the field of view for a pinhole camera with a fixed sized sensor. What impact such a design would have on projection?

I propose two ways,

(1) Move the image plane closer to the pinhole, this would increase the field of view. But at the same time this would reduce the resolution of objects.

(2) Increase the size of the pinhole, this would increase field of view but cause blur of the image.