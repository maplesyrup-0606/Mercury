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
    diff_x = np.array([[1, 0, -1]]) * 0.5
    diff_y = np.array([[1],[0],[-1]]) * 0.5

    
    Ix = conv2d(im1, diff_x) 
    Iy = conv2d(im1, diff_y)
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

    if aggregate == "const" :
        window = np.ones((patch_size, patch_size),dtype=np.float32)
    else : 
        window = gaussian_kernel(patch_size, sigma)
    
    height, width = Ix.shape
    
    Ix2 = conv2d(Ix * Ix, window)
    Iy2 = conv2d(Iy * Iy, window)
    IxIy = conv2d(Ix * Iy, window)
    IxIt = conv2d(Ix * It, window)
    IyIt = conv2d(Iy * It, window)


    u = np.zeros_like(Ix)
    v = np.zeros_like(Iy)

    for y in range(height) :
        for x in range(width) :
            ATA = np.array([[Ix2[y, x], IxIy[y, x]],
                            [IxIy[y, x], Iy2[y, x]]])


            ATB = np.array([-IxIt[y,x],
                            -IyIt[y,x]])

            vector = np.linalg.inv(ATA) @ ATB

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
    height, width = im.shape

    X, Y = np.meshgrid(np.arange(width), np.arange(height))

    X_new = X + u
    Y_new = Y + v

    og_coords = np.vstack((X.flatten(), Y.flatten())).T
    new_coords = np.vstack((X_new.flatten(), Y_new.flatten())).T

    im_warp = interpolate.griddata(og_coords, im.flatten(), new_coords,method='linear',fill_value=0).reshape(height,width)
    # END your code here

    assert im_warp.shape == im.shape
    return im_warp


def compute_cost(im1, im2):
    """Implementation of the cost minimised by Lucas-Kanade."""
    assert im1.shape == im2.shape

    # START your code here
    # NOTE: You should remove the next line while coding

    norm = np.sum((im1 - im2) ** 2)
    height, width = im1.shape

    d = norm / (height * width) 

    # END your code here

    assert isinstance(d, float)
    return d

def gaussian_kernel(patch_size=15, sigma=2) :
    k = patch_size // 2
    x = np.arange(-k, k + 1)
    y = np.arange(-k, k + 1)

    X, Y = np.meshgrid(x, y)

    kernel = np.exp(-(X**2 + Y**2) / (2 * (sigma ** 2)))

    kernel /= np.sum(kernel)

    return kernel

