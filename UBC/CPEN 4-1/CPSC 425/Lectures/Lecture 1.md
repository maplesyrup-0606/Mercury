## Computer Vision
What is computer vision? → Broadly speaking, it is a research field aimed to enable computers to **process and interpret visual data,** as sighted humans can.
![[Screenshot 2024-09-29 at 8.16.23 PM.png]]

## Image Formation, Cameras and Lenses
The **image formation process** that produces a particular image depends on:
- Lighting Condition.
- Scene Geometry.
- Surface Properties.
- Camera optics and viewpoint.

![[Screenshot 2024-09-29 at 8.17.25 PM.png]]
The **sensor (or eye)** captures amount of light reflected from the object.

#### Light / Color
Light has a property such called a wave-particle duality.
- Light exhibits particle or wave like properties.

**Visible** light is electromagnetic radiation in the 400nm - 700nm band of wavelengths.
- Black is absence of light.
- Sunlight is a spectrum of light.

#### Spectral Power Distribution
![[Screenshot 2024-09-29 at 8.21.04 PM.png]]
- The **spectral distribution of energy** in a light ray determines color.
- Surface **reflects** light energy according to a spectral distribution as well.
- The combination of **incident** and **reflectance** spectra determines observed color.


#### Graphics
Surface reflection depends on both the **viewing $(\theta_{v},\phi_{v})$** and **illumination** $(\theta_{i},\phi_{i})$ direction with,
- Bidirectional Reflection Distribution Function: $\text{BRDF}(\theta_{i},\phi_{i},\theta_{v},\phi_{v})$.
	- This governs surface reflection.
![[Screenshot 2024-09-29 at 8.27.14 PM.png]]
 
For a **Lambertian Surface**:
$$\text{BDRF}(\theta_{i},\phi_{i},\theta_{v},\phi_{v}) = \frac{\rho_{d}}{\pi}$$
And this constant, $\rho_{d}$ is called ‘albedo’.
- It refers to the fraction of light getting reflected. 
The $\pi$ is to make sure no light is added. 
- Ensures that reflected light is less or equal to amount of incident light on the surface.

$$L=\frac{\rho_{d}}{\pi}I(\vec{i}\cdot \vec{n})$$
$L$ here refers to the actual light being reflected. (For lambertian)
- Amount and color of incident light $I$.
- Fraction of light being reflected (material) $\rho_{d}$.
- Angle between the light and the surface (geometry) $\vec{i}\cdot \vec{n}$.

==A Lambertian surface appears equally bright in ALL directions and this brightness is a function of how close the incident light direction is to the normal of the surface.==

For a **Mirror** surface,
- All of the incident light is reflected in one direction where is reciprocal of the incident direction over the normal.


#### Phong Illumination Model
Includes **ambient, diffuse and specular** reflection.
$$I=k_{a}i_{a}+k_{d}i_{d}\cos \theta+k_{s}i_{s}\cos^\alpha \phi$$
![[Screenshot 2024-09-29 at 8.33.37 PM.png]]
![[Screenshot 2024-09-29 at 8.34.02 PM.png]]


#### Bare-sensor Imaging
![[Screenshot 2024-10-14 at 9.14.03 PM.png]]

Consider this situation, what would an image look like?

![[Screenshot 2024-10-14 at 9.14.30 PM.png]]
With just a bare-sensor all the points will contribute to all the sensors, hence the image projected on the sensor will be very blurry.

#### Pinhole Camera
Since we don’t want the above situation to happen, we use a thing called a **pinhole** so that 
all rays but on is blocked and projected on the sensor.

![[Screenshot 2024-10-14 at 9.15.56 PM.png]]
Hence, each scene point can only contribute to one sensor pixel.

![[Screenshot 2024-10-14 at 9.17.20 PM.png]]
A pinhole camera is a box with a small hall (aperture) in it.

##### Pinhole Camera (1D)
![[Screenshot 2024-10-14 at 9.18.39 PM.png]]

$f'$ is the focal length of the camera. And this is the distance between the centre of a lens and its focus. By changing the focal length, this will change the size of the resulting image.
Irrespective of focal length, the image is sharp → just depends on where image plane is placed. 

![[Screenshot 2024-10-14 at 9.20.00 PM.png]]
It is quite convenient to think of the **image plane** which is in front of the pinhole.

A bit more about focal length.
For a fixed sensor size, focal length determines the field of view (fov).
![[Screenshot 2024-10-14 at 9.22.26 PM.png]]
We can see that $\theta$ becomes wider the small the focal length $f$ hence having a wider fov.

Consider this figure,
![[Screenshot 2024-10-18 at 1.18.35 AM.png]]
Then,
$$\tan\left( \frac{\theta}{2} \right)=\frac{\left( \frac{w}{2} \right)}{f'}=\frac{w}{2f'}$$
$$\implies \theta = 2\arctan\left( \frac{w}{2f'} \right)$$

What is the fov of a full frame (35mm) camera with a 50mm lens, 100mm lens?
$$FOV_{50}=2\arctan\left( \frac{35}{50\times 2} \right)$$
$$FOV_{100}=2\arctan\left( \frac{35}{100 \times 2} \right)$$

The **depth of field** is the distance between the nearest and furthest elements in a scene that appear to be sharp in the image. → How much of the scene in depth will be sharp.

In terms of the pinhole camera, a.k.a a small aperture,
- Will have a large depth of field, nearly everything in field of view would be in focus.

##### Perspective Effects
We know that **far objects** appear **smaller** than close ones.
![[Screenshot 2024-10-14 at 9.25.23 PM.png]]
And relative size of objects that are equally far from the camera is preserved. (If A was half of B, then a would be have of b from the figure)

Size is inversely proportioned to distance.

##### Vanishing Points
Parallel lines meet at a point which is so called a **vanishing point**.
![[Screenshot 2024-10-14 at 9.27.03 PM.png]]
- Each set of parallel lines meet at a different point.
- Sets of parallel lines on the same plane lead to **collinear** vanishing points.
	- The line is called a **horizon** for that plane.
- This is a good way to spot fake images.
	- Scale / Perspective don’t work.
	- Vanishing points behave badly.

![[Screenshot 2024-10-14 at 9.29.33 PM.png]]

#### Properties of Projection
- Points project to points.
- Lines project to lines.
- Planes project to the whole or half image.
- Angles are not preserved.

##### Perspective Projection
![[Screenshot 2024-10-14 at 9.30.47 PM.png]]
Given the above,
The world point $P=\begin{bmatrix}x \\ y\\ z\end{bmatrix}$ projects to 2D image point $P'=\begin{bmatrix}x'\\y'\end{bmatrix}$ where $x'=f' \frac{x}{z},y'=f' \frac{y}{z}$.
These project, that these points are inversely proportional to depth and proportional to the **focal length**.

We can use the camera matrix,
$$\mathbf{C}= \begin{bmatrix}
f' & 0 & 0 & 0 \\
0 & f' & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}$$
where $P'=\mathbf{C}P$.
$$P'=CP=\begin{bmatrix}
f' & 0 & 0 & 0 \\
0 & f' & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}=\begin{bmatrix}
f'x \\
f'y \\
z
\end{bmatrix}
=\begin{bmatrix}
f' \frac{x}{z}  \\
f' \frac{y}{z}
 \\ 1
\end{bmatrix}$$


##### Weak Perspective
![[Screenshot 2024-10-14 at 9.47.12 PM.png]]
Let’s consider a scenario where we are effectively imaging something without a lot of depth (always same distance from sensor, like a scanner).

The 3D object point projects to the 2D image point,
$$P=\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} \to P'=\begin{bmatrix}
x' \\
y'
\end{bmatrix}, \hspace{.3in} x'=mx,y'=my \hspace{.3in}m=\frac{f'}{z_{0}}$$
- Is accurate for flat scenes or scenes where relief of an object is relatively small w.r.p to the distance of the object from the camera.
- $z_0$ here is the average distance of points on the object to the camera.
- Yet, we still get an inverted image.
##### Orthographic Projection
![[Screenshot 2024-10-14 at 9.48.17 PM.png]]
Just simply drop the depth component. We need a image plane big enough to compensate what we’re actually imaging. We don’t get any inverted image.

$$P=\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}\to P=\begin{bmatrix}
x' \\
y'
\end{bmatrix},\hspace{.3in}x'=x,y'=y$$


#### Projection Models Pros and Cons
- Weak perspective (including orthographic) has simple math.
	- Accurate when object is small or distant.
	- Useful for recognition.
- Perspective.
	- More accurate for real scenes.

When **maximum accuracy** is required, it is necessary to model additional details of a particular camera. → Use perspective with more parameters (lens distortion etc.).

### Why not a pinhole camera?
If the pinhole is too big
→ Many directions are averaged, blurring the image.

If the pinhole is too small (what we should do theoretically)
→ Blocks a lot of light, takes a lot of time to collect photons.
→ Diffraction becomes a factor (photons bounce of the whole) also blurring the image.

Generally, pinhole cameras are **dark**.
→ Because only a small set of rays from a scene point hit the image plane.

Pinhole cameras are **slow**.
→ Only a fraction of the light from a scene point hits the image plane per unit time.

==That’s why we need lens, so that it can still capture more photons and make them still project to the focus point.==

#### Reason for Lenses
A real camera must have as finite aperture:
- **That captures more light.**
- **While preserving as much of the pinhole abstraction as possible.**

![[Screenshot 2024-10-14 at 9.55.30 PM.png]]

However, something happens at the boundary between the medium → refraction.

##### Snells’s Law
![[Screenshot 2024-10-14 at 9.56.56 PM.png]]
$$n_{1}\sin(\alpha_{1})=n_{2}\sin (\alpha_{2})$$
If we had a lens made from material who’s index of refraction equals to air, that is the same as having no lens and just be a pinhole.

##### Pinhole Model with Lens
The one problem is that light will actual get refracted twice, since there are two medium boundaries. But if we use thin lens, we can assume that light actually only gets refracted once since the lengths is really thin → Thus negligible distance. 

![[Screenshot 2024-10-14 at 9.59.22 PM.png]]

$$\frac{1}{z'}-\frac{1}{z}=\frac{1}{f}$$
- $f$ is focal length, distance where image is going to be in focus.
- $z$ is the position of the object.
- $z’$ is distance from lens to the imaging plane.

If we know our focal length and where the object is in the world → we can figure where to place our image plane to be in focus. Where pinhole would be focus anywhere.
==Only objects at particular depth from the camera will be in focus on the imaging plane.==
==Any where else further or closer than z’ will be blurred since they form a circle of confusion on the image plane.==

If we have light rays that are parallel (objects really far away and the rays become nearly parallel),
$$\lim_{ z \to -\infty } \frac{1}{z'}-\frac{1}{z}=\frac{1}{z'}=\frac{1}{f}$$
Where everything is going to be focused a focal length.

But say if we had an object, that is relatively closer than infinity, then the light would focus closer than the image plane and get blurred.

For closer objects, the image plane exists before the light is focus and hence be blurred.

![[Screenshot 2024-10-14 at 10.10.57 PM.png]]

*Distance towards the actual object is negative, distance towards the image plane is positive.*


##### Exercise
Consider a scenario with a lens who’s focal length is 50mm = 0.05m, where an object being imaged is 5m away. Where should we place the image plane to ensure the object is in focus?

$$\frac{1}{f'}=\frac{1}{z'}-\frac{1}{z}$$
$$\to \frac{1}{0.05m}=\frac{1}{z'}-\frac{1}{-5m}$$
$$\frac{1}{z'}=\frac{1}{0.05m}+\frac{1}{5m} \implies z' \approx 0.05m$$

**Why is the optimal placement so close to the focal length?**
→ Because the object is very far away.

##### Exercise
Consider a scenario with a lens who’s focal length is 5m, where an object being imaged is 5m away. Where should we place the image plane to ensure the object is in focus?

$$\frac{1}{z'}=\frac{1}{f'}+\frac{1}{z}=\frac{1}{5m}+\frac{1}{-5m}\implies z'\approx \infty$$

##### Note ⭐⭐⭐
When combining the thin lens equation and a pinhole camera. Effectively in the camera, $z'=f'$, hence we have to use the relation,
$$x'=z' \frac{x}{z},\hspace{.1in}y'=z' \frac{y}{z},\hspace{.1in} \frac{1}{z'}- \frac{1}{z} = \frac{1}{f}$$
So if we place an object at 2 x focal length.
$$\frac{1}{z'} - \frac{1}{-2f} = \frac{1}{f} \implies z' = 2f$$
$$x'=2f \frac{x}{-2f} = -x,\hspace{.1in}y'= 2f \frac{y}{-2f} = -y$$
So the object is equal in size but inverted in the projection.
#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 2|Lecture 2]]
