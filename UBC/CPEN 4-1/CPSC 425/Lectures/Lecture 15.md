### Optical Flow
**Problem**: Determine how objects (or camera itself) move in the 3D world. (World is not static anymore)
**Key Idea**: Image(s) acquired as a continuous function of time provided additional constraint.
Formulate motion analysis as finding (dense) point correspondences over time.

#### Dense / Sparse Matching
**Sparse**: correspondence / depth estimated at discrete feature points, e.g. SIFT
**Dense**: correspondence / depth estimated at all locations, e.g. stereo matching

We focus on,
- Dense Flow
	- Compute correspondence / flow at every pixel.
- Short baselines
	- Assume small distances between frames, e.g. successive frames in video.

If we have very fast motions, traditional optical flow will fail.
Ultimately for every pixel, we want to estimate where the pixel is in the next frame.
![[Screenshot 2024-11-28 at 9.54.20 PM.png]]
![[Screenshot 2024-11-28 at 9.54.39 PM.png]]
Color is mapped to direction, strength is mapped to magnitude of the vector.


#### Optical Flow and 2D Motion
Why do we care about optical flow? Optical flow is the apparent motion of brightness patterns in the image.

Applications:
- Image and video stabilization in digital cameras.
- Motion-compensated video compression.
- Image registration for medical imaging.
- Action recognition.
- Motion segmentation.


###### Motion vs. Optical Flow
**Motion** is geometric.
**Optical flow** is radiometric.

Motion is how a thing in the world moves. Optical flow is *how that motion is projected on an image* and *how we see that*.

==We assume they are the same for now.==

Optical flow but no motion?
→ Moving light sources, shadows etc.

Motion but no optical flow can also exist.

#### Optical Flow Constraint Equation
Consider image intensity to be a function of time, $t$. We write
$$I(x(t),y(t),t)$$
Then,
$$\frac{dI(x,y,t)}{dt}=I_{x} \frac{dx}{dt} + I_{y} \frac{dy}{dt} + I_{t}$$
to determine the change of intensity for a small time step.

Define
$$u= \frac{dx}{dt},v=\frac{dy}{dt}$$
then $\begin{bmatrix}u,v\end{bmatrix}$ is the 2-D motion and the space of all such $u,v$ is the 2-D velocity space.

Suppose $\frac{dI(x,y,t)}{dt}=0$, then we obtain the classic optical flow constraint equation
$$I_{x}u+I_{y}v+I_{t}=0$$
We assume the intensity of a pixel doesn’t change (remains constant) as it moves.
(If the time step is really really small, we can linearize the intensity function.)

#### How to compute the constraint equation
**Spatial derivative**
$$I_{x}= \frac{\partial I}{\partial x},I_{y}= \frac{\partial I}{\partial y}$$
can be computed through forward difference, sobel filter and so on..

**Temporal derivative**
$$I_{t}= \frac{\partial I}{\partial t}$$
is just frame differencing 
$$I_{t}=I(t+1)-I(t)$$

![[Screenshot 2024-11-28 at 10.31.03 PM.png]]

What’s the issue with solving the equation for optical flow?
→ We have 1 equation and 2 unknowns → can’t find unique solution.

We will get a straight line for one instance,
![[Screenshot 2024-11-28 at 10.32.02 PM.png]]

This is an **Aperture problem**, we can’t uniquely determine the actual motion based on the one instance. We can only measure component orthogonally.

![[Screenshot 2024-11-28 at 10.33.01 PM.png]]


#### Lucas-Kanade
We use the neighborhood of pixels to solve for the unique solution.

**Observations**:
1. 2D motion at given point has two degrees of freedom.
2. Partial derivatives provide one constraint.
3. 2D motion cannot be determined locally from partial derivatives alone.

**Idea**:
- Obtain additional local constraint by computing the partial derivatives in a window centered at the given point $[x,y]$.

**Assumption**:
- Nearby pixels will likely have same optical flow.

Considering $n$ points in the window, one obtains
$$I_{x_{1}}u+I_{y_{1}}v=-I_{t_{1}}$$
$$I_{x_{2}}u+I_{y_{2}}v=-I_{t_{2}}$$
$$\vdots$$
$$I_{x_{n}}u+I_{y_{n}}v=-I_{t_{n}}$$

which can be written as the matrix equation,
$$\mathbf{A}\mathbf{v}=\mathbf{b}$$
$$\mathbf{A}=\begin{bmatrix}
I_{x_{1}} & I_{y_{1}} \\
I_{x_{2}} & I_{y_{2}} \\
\vdots  & \vdots \\
I_{x_{n}} & I_{y_{n}}
\end{bmatrix},\mathbf{v=\begin{bmatrix}
u & v
\end{bmatrix}}^T, \mathbf{b}=-\begin{bmatrix}
I_{t_{1}} \\
I_{t_{2}} \\
\vdots \\
I_{t_{n}}
\end{bmatrix}$$

Since this is an over-constraint system, we can get the least squares solution, $\bar{\mathbf{v}}$,
$$\bar{\mathbf{v}}=(\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{b}$$
Again provided that $u,v$ are the same in all equations and provided that rank of $\mathbf{A}^T\mathbf{A}$ is 2 (so that the inverse exists).

But $\mathbf{A}^T\mathbf{A}$ is 
$$\mathbf{A}^T\mathbf{A}=\begin{bmatrix}
\sum I_{x}^2 & \sum I_{x}I_{y} \\
\sum I_{x}I_{y} & \sum I_{y}^2
\end{bmatrix}=C$$
the ==covariance matrix!==.
For structures like corners we can estimate the optical flow really accurately.

**Key Assumptions**:
- Motion is slow enough and smooth enough that differential methods apply ($I_{x},I_{y},I_{t}$ is well defined).
- The optical flow constraint equation holds $\frac{dI(x,y,t)}{dt}=0$.
- A window size is chosen so that $\begin{bmatrix}u,v\end{bmatrix}$ is constant in the window.
- A window size is chosen so that the rank of $\mathbf{A}^T\mathbf{A}$ is 2 for the window.

#### Horn-Schunck Optical Flow
$$\text{min}_{u,v} \sum_{i,j} \left\{ E_{s}(i,j) + \lambda E_{d}(i,j) \right\}$$
Where $E_{s}$ is the smoothness term, $E_{d}$ is the brightness constancy term.

$$E_{d}(i,j)= [I_{x}u_{i,j}+I_{y}v_{i,j}+I_{t}]^2$$
$$E_{s}(i,j)=\frac{1}{4}[(u_{i,j}-u_{i+1,j})^2+(u_{i,j}-u_{i,j+1})^2+(v_{i,j}-v_{i+1,j})^2+(v_{i,j}-v_{i,j+1})^2]$$

Smoothness would penalize nearby pixels where there is too much difference of optical flow and we would want the brightness constancy to be minimized (generally 0).

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 16|Lecture 16]]
