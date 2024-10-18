## Logistics
Closed book, calculators allowed.
Format similar to practice problems,
- mcq + TF - no credit
- short ans - partial credit

No coding questions
No complex math - can leave numbers in simplified form (e.g. sqrt(3))

## Overview
Image formation process depends on
- Light condition
- Scene geometry
- Surface properties
- Camera optics

Sensor captures amount of light reflected from the object.

Light - behaves like particles and waves (wave-particle duality)

Spectral Power distribution
- spectral distribution of energy in a light ray determines its color
- Surface reflects light energy according to this distribution
- combination of incident and reflectance determines observed colour

surface reflection depends on both viewing and illumination.
For lambertian, light is reflected equally in all directions.
For mirror, light will all be reflected in single direction, sensor needs to be in line of reflection direction to capture reflected light.

==how to distinguish mirror vs. lambertian surface?==

Pinhole Camera
- let’s one photon through per point to make sharp image.
- irrespective of focal length, image is sharp.
- just depends on where image plane is placed.
- focal length determines fov.

Properties of projection
- point → point
- line → line
- plane → whole / half image
- angles are not preserved
	- parallel lines meet at vanishing point, no longer parallel
	- multiple parallels lines converge to horizon line which is the linear vanishing points.
		- good to detect fakes.

Perspective Projection
- focal length * point in the world / depth $\frac{f'x}{z}$
	- Are these equations linear? → not linear
- weak perspective → constant $m$, $m=\frac{f'}{z_{0}}$
	- is linear
	- accurate for defined one depth, otherwise not accurate for under/over that depth
	- good for planar objects, volume is much less than depth
- Orthographic → drop $z$
	- The sensor has to be the size of the object imaging

Pinhole uses orthographic → False, perspective projection.

Limitations of pinhole
- pinhole big → blurry image
- pinhole small → diffraction, also blur
- dark and slow since small amount of light come in

Lens
- thin lens equation
	- object closer → image plane is further away in camera and vice versa
		- The blurry circle → circle of confusion
- where the objects are is negative, and where the image is formed is positive
- Lens also has artifacts
	- spherical aberration
	- vignetting
		- light enters the first lens might not reflect to hit the second lens
	- chromatic aberration
		- diff wavelengths might focus at different depths
	- lens distortion

snell’s law describes how much light is reflected and how much passes through the boundary between two materials → False. describes how light bends, not reflection

Linear filters
- convolve filter with image
- boundary effects
	- ignore locations
	- zero padding
	- assume periodicity
	- reflect boarder

when would you pad and why? → artificially creating an edge at the border etc.
convolution $\iff$ linear + shift invariant

box filter doesn’t have symmetry in general → only 90 degree symmetry

==rank of filter 1 → filter is separable.==

Is the following filter applied as correlation shift invariant?
→ Any correlation is shift invariant

If we cube every pixel as a convolution
→ we cannot it’s not a linear operation

$$\begin{bmatrix}
-1 & -1 & -1 \\
0 & 0 & 0 \\
1 & 1 & 1 
\end{bmatrix}$$
→ edge detecting filter, along the vertical (derivative filter)


highest cosine similarity → lowest SSD

is normalized correlation robust to a constant scaling in the image brightness (would correlation map be the same)
→ True, normalized correlation!

why is non-maximum suppression applied in the Canny edge detector → 