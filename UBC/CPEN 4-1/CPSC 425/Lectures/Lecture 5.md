## Sampling
Images are discrete, or a sampled representation of a continuous world.
A **continuous function** $i(x,y,\lambda)$ is presented at the image sensor at each time instant.
How can we convert this to a **digital signal** (array of numbers) $I(x,y,\lambda)$?
→ $\lambda$ represents the three color channels.

==The ultimate question is how do we manipulate, resample this digital signal correctly?==

![[Screenshot 2024-10-17 at 4.31.29 PM.png]]
==How can we warp this image correctly?==

#### Resampling
Let’s try to get a lower resolution counterpart of an image.
Say we wanted to produce an image 1/5 of the original size?
→ Take a pixel at every 5th pixel.

The Naive method is taking every $n$ th pixel of the original image.
![[Screenshot 2024-10-17 at 4.33.43 PM.png]]
![[Screenshot 2024-10-17 at 4.33.47 PM.png]]
Aliasing causes undesirable artifacts, if we take an audio signal and simply drop every $n$ th sample, the signals will be aliased and cause distortion.

### Image Sampling: Continuous Case Observations
In images, the sampling rate is spacial resolution and bit depth is how many values we have to interpret the color channel.

- $i(x,y)$ is a real-valued function of real spatial variables, $x$ and $y$.
- $i(x,y)$ is bounded above and below:$$0\leq i(x,y)\leq M$$
- $i(x,y)$ is bounded in extent. That is, $i(x,y)$ is zero or above over, at most, a bounded region.

#### Pixel Bit Rate
Quantize the bit depth (color).
Recall that $0 \leq i(x,y) \leq M$, we divide the range $[0,M]$ into a finite number of equivalence classes. → Quantization.

And these values are called **grey-levels**.
Typically $n=8$ resulting in grey-levels in the range $[0,255]$.

![[Screenshot 2024-10-17 at 4.40.39 PM.png]]

#### Sampling Theory
- When is $I(X,Y)$ an exact characterization of $i(x,y)$?
- When can we reconstruct $i(x,y)$ exactly from $I(X,Y)$?

We would reconstruct some kind of interpolation!

**Case 0**:
![[Screenshot 2024-10-17 at 4.42.19 PM.png]]
Suppose $i(x,y)=k$ (where $k$ is one of our grey levels).
$I(X,Y) = k$! Very simple. 

**Case 1**:
![[Screenshot 2024-10-17 at 4.43.03 PM.png]]
Suppose $i(x,y)$ has a discontinuity not falling precisely at integer $x,y$.
We have know idea where the edge is between some samples → a.k.a we don’t know where the discontinuity lies. => We cannot reconstruct!

![[Screenshot 2024-10-17 at 4.44.30 PM.png]]
How many samples do we take? → Of course, if we take more samples we can approximate it easier.

But if we sample less,
![[Screenshot 2024-10-17 at 4.45.02 PM.png]]
The signal can be confused with one at a lower frequency.
![[Screenshot 2024-10-17 at 4.45.17 PM.png]]


### Nyquist Sampling Theorem
To avoid aliasing a signal, it must be sampled at twice the maximum frequency:
$$f_{s} > 2 \times f_{\text{max}}$$
Where $f_s$ is the sampling frequency, and $f_{\text{max}}$ is the maximum frequency present in the signal.

- Nyquist’s theorem states that a signal is **exactly recoverable** from its samples if sampled at the **Nyquist rate** (or higher).

==It is important to note that a signal must be band-limited for this to apply (i.e. it has a maximum frequency).==
