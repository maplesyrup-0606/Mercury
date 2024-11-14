import numpy as np
from scipy import interpolate
from scipy.signal import convolve2d
from functools import partial
conv2d = partial(convolve2d, mode="same", boundary="symm")

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
    Ix = np.empty_like(im1)
    Iy = np.empty_like(im1)
    It = np.empty_like(im1)
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
    u = np.empty_like(Ix)
    v = np.empty_like(Iy)
    # END your code here

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
    im_warp = np.empty_like(im)
    # END your code here

    assert im_warp.shape == im.shape
    return im_warp


def compute_cost(im1, im2):
    """Implementation of the cost minimised by Lucas-Kanade."""
    assert im1.shape == im2.shape

    # START your code here
    # NOTE: You should remove the next line while coding
    d = 0.0
    # END your code here

    assert isinstance(d, float)
    return d
