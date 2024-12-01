import numpy as np
from scipy import interpolate
from scipy import signal
from scipy.signal import convolve2d
from functools import partial
conv2d = partial(convolve2d, mode="same", boundary="symm")
import math

def compute_derivatives(im1, im2):
    """Compute dx, dy and dt derivatives.

    Args:
        im1: first image
        im2: second image

    Returns:
        Ix, Iy, It: derivatives of im1 w.r.t. x, y and t
    """
    assert im1.shape == im2.shape

    # START your code here
    # HINT: You can use the conv2d defined in Line 5 for convolution operations
    # NOTE: You should remove the next three lines while coding
    
    # Create a central difference convolution filter
    diff_x = np.array([[1, 0, -1]]) * 0.5
    diff_y = np.array([[1],[0],[-1]]) * 0.5

    # Compute x derivative via convolution with x-derivative filter    
    Ix = conv2d(im1, diff_x) 
    
    # Compute y derivative via convolution with y-derivative filter 
    Iy = conv2d(im1, diff_y)

    # Compute t derivative via subtracting each image
    It = im2 - im1
    # END your code here

    assert Ix.shape == im1.shape and \
           Iy.shape == im1.shape and \
           It.shape == im1.shape

    return Ix, Iy, It


def compute_motion(Ix, Iy, It, patch_size=15, aggregate="const", sigma=2):
    """Computes one iteration of optical flow estimation.

    Args:
        Ix, Iy, It: image derivatives w.r.t. x, y and t
        patch_size: specifies the side of the square region R in Eq. (1)
        aggregate: indicates whether to use Gaussian weighting
        sigma: if aggregate=='gaussian', use this sigma for the Gaussian kernel
    Returns:
        u: optical flow in x direction
        v: optical flow in y direction

    All outputs have the same dimensionality as the input
    """
    assert Ix.shape == Iy.shape and \
            Iy.shape == It.shape

    # START your code here
    # HINT: You can use the conv2d defined in Line 5 for convolution operations
    # NOTE: You should remove the next two lines while coding

    # Create a window of ones for 'const'
    if aggregate == "const" :
        window = np.ones((patch_size, patch_size),dtype=np.float32)
    
    # Create a gaussian kernel with same size and sigma
    else : 
        window = gaussian_kernel(patch_size, sigma)
    
    # Compute dimensions of the image
    height, width = Ix.shape

    # ========================================================== 
    """ This part was inspired by ChatGPT, this process was used to preconvolve the whole image so that each entry stores the sum of Ix^2, Iy^2.
        The following parts were adapted from this approach to compute the sum of IxIy and compute the matrix multiplications, for instance,
        when computing A^T @ b = -[sum of IxIt \\ sum of IyIy] instead of computing partial patches at a time, I used convolution to compute 
        the matrix multiplication.
    """

    # Use convolution with kernel to compute sum of Ix^2
    Ix2 = conv2d(Ix * Ix, window)

    # Use convolution with kernel to compute sum of Iy^2
    Iy2 = conv2d(Iy * Iy, window)
    # ==========================================================

    # Use convolution with kernel to compute sum of IxIy
    IxIy = conv2d(Ix * Iy, window)

    # Use convolution with kernel to compute sum of IxIt, used for A^Tb
    IxIt = conv2d(Ix * It, window)
    
    # Use convolution with kernel to compute sum of IyIt, used for A^Tb
    IyIt = conv2d(Iy * It, window)

    # Prepare u and v
    u = np.zeros_like(Ix)
    v = np.zeros_like(Iy)

    # For all pixels in image
    for y in range(height) :
        for x in range(width) :
            
            # Compute A^T @ A by getting sum of Ix^2, IxIy, Iy^2 at each pixel (Covariance Matrix)
            ATA = np.array([[Ix2[y, x], IxIy[y, x]],
                            [IxIy[y, x], Iy2[y, x]]])

            # Compute A^T @ b by getting sum of IxIt and IyIt 
            ATB = np.array([-IxIt[y,x],
                            -IyIt[y,x]])

            # Compute vector via (A^T @ A)^-1 @ A^T @ b
            vector = np.linalg.inv(ATA) @ ATB
            
            # Record u and v
            u[y,x], v[y,x] = vector

    assert u.shape == Ix.shape and \
            v.shape == Ix.shape
    return u, v


def warp(im, u, v):
    """Warping of a given image using provided optical flow.

    Args:
        im: input image
        u, v: optical flow in x and y direction

    Returns:
        im_warp: warped image (of the same size as input image)
    """
    assert im.shape == u.shape and \
            u.shape == v.shape
    
    # START your code here
    # HINT: You can use the np.meshgrid() function
    # HINT: You can use the interpolate.griddata() function with method='linear' and fill_value=0
    # NOTE: You should remove the next line while coding

    # Compute dimensions of image
    height, width = im.shape

    # Create meshgrid of x,y coordinates
    X, Y = np.meshgrid(np.arange(width), np.arange(height))

    # Based on u and v compute the estimated new coordinates
    X_new = X + u
    Y_new = Y + v

    # Prepare original and estimated new coordinates in form [X, Y]
    og_coords = np.vstack((X.flatten(), Y.flatten())).T
    new_coords = np.vstack((X_new.flatten(), Y_new.flatten())).T

    # Compute warped image via interpolation and new coordinates / old coordinates
    im_warp = interpolate.griddata(og_coords, im.flatten(), new_coords,method='linear',fill_value=0).reshape(height,width)
    # END your code here

    assert im_warp.shape == im.shape
    return im_warp


def compute_cost(im1, im2):
    """Implementation of the cost minimised by Lucas-Kanade."""
    assert im1.shape == im2.shape

    # START your code here
    # NOTE: You should remove the next line while coding

    # Compute L2 Norm by getting sum of squared differences
    norm = np.sum((im1 - im2) ** 2)

    # Compute dimensions of image
    height, width = im1.shape

    # Compute cost by dividing L2 norm with total number of pixels
    d = norm / (height * width) 

    # END your code here

    assert isinstance(d, float)
    return d

# Helper function for creating Gaussian Kernel
""" This function was adapted from the gauss_2d, gauss_1d functions in assignment 1.
    Instead of computing the size via (sigma * 6) to the next odd integer, 
    the gaussian kernel size was used by the given 'patch_size' input.     
"""
def gaussian_kernel(patch_size=15, sigma=2) :

    # Get window radius
    k = patch_size // 2

    # Prepare x, y distances
    x = np.arange(-k, k + 1)
    y = np.arange(-k, k + 1)

    # Create meshgrid of distances
    X, Y = np.meshgrid(x, y)

    # Compute Gaussian Kernel 
    kernel = np.exp(-(X**2 + Y**2) / (2 * (sigma ** 2)))

    # Normalize Gaussian Kernel
    kernel /= np.sum(kernel)

    return kernel

