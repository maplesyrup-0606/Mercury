## Computer Vision
What is computer vision? → Broadly speaking, it is a research field aimed to enable computers to **process and interpret visual data,** as sighted humans can.
![[Screenshot 2024-09-29 at 8.16.23 PM.png]]

## Image Formation, Cameras and Lenses
The **image formation process** that produces a particular image depends on:
- Lightening Condition.
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
Bidirectional Reflection Distribution Function: $\text{BDRF}(\theta_{i},\phi_{i},\theta_{v},\phi_{v})$.
![[Screenshot 2024-09-29 at 8.27.14 PM.png]]
 
For a **Lambertian Surface**:
$$\text{BDRF}(\theta_{i},\phi_{i},\theta_{v},\phi_{v}) = \frac{\rho_{d}}{\pi}$$
And this constant, $\rho_{d}$ is called ‘albedo’.
It refers to the fraction of light getting reflected. The $\pi$ is to make sure no light is added.

$$L=\frac{\rho_{d}}{\pi}I(\vec{i}\cdot \vec{n})$$
#### Phong Illumination Model
Includes **ambient, diffuse and specular** reflection.
$$I=k_{a}i_{a}+k_{d}i_{d}\cos \theta+k_{s}i_{s}\cos^\alpha \phi$$
![[Screenshot 2024-09-29 at 8.33.37 PM.png]]
![[Screenshot 2024-09-29 at 8.34.02 PM.png]]



