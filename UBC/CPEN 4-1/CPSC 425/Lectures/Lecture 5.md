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

**Sampling Theorem (Informal)**:
- Exact reconstruction requires a constraint on the rate at which $i(x,y)$ can change between samples.
	- “rate of change” means derivative.
		- Also, is linked to **band-limited signal**.
- Since undesirable artifacts exist, we can pre-filter with a low-pass filter to get rid of these artifacts.

![[Screenshot 2024-10-17 at 7.39.40 PM.png]]
Consider this grid above, $f_\text{max}$ denotes how often the black and white squares repeat.
And the little circles are the sampling point.

The above two grids have more than double the amount of sampling points per $f_{\text{max}}$ meaning that if we think of the red line as one “sample” of the max frequency then they are more than double the amount of sampling.
=> Hence, these can be sampled fine.

However, for the bottom cases, we don’t satisfy the Nyquist sampling theorem.
=> Hence, it will be sampled poorly.
![[Screenshot 2024-10-17 at 7.48.35 PM.png]]
==But, some information may be lost when we work on a discrete pixel grid.==

#### Back to Re-sampling Images
Since we want to get rid of artifacts, we can blur the image (with a low-pass filter) then take the $n$-th pixel.
Also, this is possible since with the correct sigma value for a Gaussian, no information is lost.

Normally, we want,
$$\sigma=\frac{1}{2s}$$
where $s$ is the sampling rate.

![[Screenshot 2024-10-17 at 7.53.56 PM.png]]![[Screenshot 2024-10-17 at 7.54.05 PM.png]]

**Why we need low-pass filtering**:
High-frequency details, like sharp edges, change rapidly in an image, but if the sampling rate is too low, these details aren’t captured frequently enough, leading to distortions like aliasing. To prevent this, a low-pass filter (blurring) is applied to smooth out the high-frequency content, effectively creating a band-limited version of the image. This reduces the need for a high sampling rate and ensures the image can be resampled accurately without introducing artifacts.

- If we shifted the original image 1 pixel to the right, the aliased image would look completely different, but the low-pass filtered image would look almost the same.
- How much smoothing is needed?
	- Until the image is band-limited “enough” to ensure we can sample every other pixel.
- It’s more efficient to apply the Gaussian filter / sub-sample successively rather than larger values and sub-sampling the large image again and again.

### Image Pyramids
![[Screenshot 2024-10-17 at 8.10.27 PM.png]]

We blur with the Gaussian kernel, then we select every 2nd pixel (maybe $n$ th, but this is sampling).

**For a band-limited signal, what if we over sample? (higher than Nyquist rate)**
=> *It’s fine, samples are redundant and there are wasted bits.*

**For a band-limited signal, what if we under sample?**
=> *We might have artifacts and we might miss details.*

**How can we prevent aliasing?**
- Reduce $f_{\text{max}}$, by low-pass filtering - i.e. Smoothing before sampling.
- Sample more frequently - i.e. oversample, increase $f_s$.

**Sometimes under-sampling is unavoidable**
- **Medical Imaging:** Usually try to maximize information content, tolerate some artifacts.
- **Computer Graphics:** Usually try to minimize artifacts, tolerate some information missing.

## Color
“Color” is **not** an objective physical property of light. Instead, light is characterized by its wavelength.
- What we call “color” is how we subjectively perceive a very small range of these wavelengths.

#### CFA (Color Filter Arrays)
![[Screenshot 2024-10-17 at 8.30.07 PM.png]]
*Quantum Efficiency: fraction of photons being “detected” through this process*

The problem is that the CFA by itself has no way to distinguishing wavelengths of light, just has the ability to record the amount of light incident on an element.

So we have different color filters that record only certain wavelengths of light at a given pixel. (They pass only certain range of wavelengths.)
![[Screenshot 2024-10-17 at 8.32.19 PM.png]]

We have to design choices:
1. What is the sensitivity functions $f(\lambda)$ to use for each filter?
2. How can we spatially arrange these filters?

![[Screenshot 2024-10-17 at 8.33.23 PM.png]]
*We have more green pixels, since that’s the light human’s are most sensitive to perceive.*
There are of course, different patterns.

The actual raw output from a camera is like the following,
![[Screenshot 2024-10-17 at 8.36.54 PM.png]]
All we does it count the photons, we get a grey scale image. 
The distribution of the color is shown by the checker board grid.

#### CFA Demosaicking
We produce the full RGB image from mosaicked sensor output. But we saw that the filters are placed in a sense that RGB color filters are not in all the pixel sensors.
=> We interpolated from neighbours to fill it out:
- Bilinear interpolation (needs 4 neighbours).
- Bicubic interpolation (needs more neighbours, may over-blur).
- Edge-aware interpolation.

![[Screenshot 2024-10-17 at 8.40.09 PM.png]]

#### Image Processing Pipeline
![[Screenshot 2024-10-17 at 8.40.24 PM.png]]

#### White balance
We generally perceive the world in the color irrespective of the light present in the scene.
Pixel-wise the scene is different, but we perceive the same.

We want to is to be able to adjust the fact that the image might be taken in different light conditions.

==We are correcting for the illuminant in white balancing.==

A simple white balancing algorithm is to assume the scene is grey on average.

##### Tone reproduction
![[Screenshot 2024-10-17 at 8.43.15 PM.png]]

#### Next Lecture [[UBC/CPEN 4-1/CPSC 425/Lectures/Lecture 6|Lecture 6]]
