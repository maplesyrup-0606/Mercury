import numpy as np
from numpy.linalg import norm

def cost_ssd(patch1, patch2):
    """Compute the Sum of Squared Pixel Differences (SSD):

    Args:
        patch1: input patch 1 as (m, m, 1) numpy array
        patch2: input patch 2 as (m, m, 1) numpy array

    Returns:
        cost_ssd: the calcuated SSD cost as a floating point value
    """

    # START your code here
    # NOTE: You should remove the next line while coding

    patch1_flatten = patch1.flatten()
    patch2_flatten = patch2.flatten()

    cost_ssd = np.sum((patch1_flatten - patch2_flatten) ** 2)
    # END your code here

    assert np.isscalar(cost_ssd)
    return cost_ssd


def cost_nc(patch1, patch2):
    """Compute the normalized correlation cost (NC):

    Args:
        patch1: input patch 1 as (m, m, 1) numpy array
        patch2: input patch 2 as (m, m, 1) numpy array

    Returns:
        cost_nc: the calcuated NC cost as a floating point value
    """

    # START your code here
    # HINT: You can use the norm() function imported from numpy.linalg
    # NOTE: You should remove the next line while coding
    patch1_flatten = patch1.flatten()
    patch2_flatten = patch2.flatten()

    size_1 = norm(patch1_flatten)
    size_2 = norm(patch2_flatten)

    cost_nc = patch1_flatten.T @ patch2_flatten / (size_1 * size_2)
    # END your code here

    assert np.isscalar(cost_nc)
    return cost_nc


def cost_function(patch1, patch2, alpha):
    """Compute the cost between two input window patches given the disparity:

    Args:
        patch1: input patch 1 as (m, m) numpy array
        patch2: input patch 2 as (m, m) numpy array
        input_disparity: input disparity as an integer value        
        alpha: the weighting parameter for the cost function
    Returns:
        cost_val: the calculated cost value as a floating point value
    """
    assert patch1.shape == patch2.shape

    # START your code here
    # NOTE: You should remove the next line while coding
    m = len(patch1)

    patch1_3d = np.expand_dims(patch1, axis=-1)
    patch2_3d = np.expand_dims(patch2, axis=-1)

    ssd_cost = cost_ssd(patch1_3d,patch2_3d)
    nc_cost = cost_nc(patch1_3d, patch2_3d)

    cost_val = (1 / (m ** 2)) * (ssd_cost + alpha * nc_cost)
    # END your code here

    assert np.isscalar(cost_val)
    return cost_val


def pad_image(input_img, window_size, padding_mode='symmetric'):
    """Output the padded image

    Args:
        input_img: an input image as a numpy array
        window_size: the window size as a scalar value, odd number
        padding_mode: the type of padding scheme, among 'symmetric', 'reflect', or 'constant'

    Returns:
        padded_img: padded image as a numpy array of the same type as image
    """
    assert np.isscalar(window_size)
    assert window_size % 2 == 1

    # START your code here
    # HINT: You can use the np.pad() function with mode=padding_mode
    # NOTE: You should remove the next line while coding
    k = window_size // 2
    

    if padding_mode == "constant" :
        padded_img = np.pad(input_img,k,mode="constant",constant_values=0)
    elif padding_mode == "symmetric" :
        padded_img = np.pad(input_img,k,mode="symmetric")
    elif padding_mode == "reflect" :
        padded_img = np.pad(input_img,k,mode="reflect")
    else :
        print("error") 
    # END your code here

    return padded_img


def compute_disparity(padded_img_l, padded_img_r, max_disp, window_size, alpha):
    """Compute the disparity map by using the window-based matching:

    Args:
        padded_img_l: The padded left-view input image as 2-dimensional (H,W) numpy array
        padded_img_r: The padded right-view input image as 2-dimensional (H,W) numpy array
        max_disp: the maximum disparity as a search range
        window_size: the patch size for window-based matching, odd number
        alpha: the weighting parameter for the cost function
    Returns:
        disparity: numpy array (H,W) of the same type as image
    """
    assert padded_img_l.ndim == 2 
    assert padded_img_r.ndim == 2 
    assert padded_img_l.shape == padded_img_r.shape
    assert max_disp > 0
    assert window_size % 2 == 1
    # START your code here
    # HINT: in numpy, there is a function named argmin
    # NOTE: You should remove the next line while coding
    H, W = padded_img_l.shape
    k = window_size // 2

    disparity = np.zeros((H, W),dtype=np.float32)
    print(disparity.shape)
    for y in range(k, H - k) :
        for x in range(k, W - k) :
            patch_L = padded_img_l[y - k : y + k + 1, x - k : x + k + 1]
            costs = []

            for d in range(max_disp + 1) :
                if y - d - k >= 0 and x - d - k >= 0:
                    patch_R = padded_img_r[y - d - k : y - d + k + 1, x - d - k : x - d + k + 1]

                    cost = cost_function(patch_L, patch_R, alpha)
                    costs.append(cost)
                else :
                    costs.append(float('inf'))

            best_disp = np.argmin(costs)
            disparity[y, x] = best_disp
    # END your code here

    assert disparity.ndim == 2
    return disparity


def compute_aepe(disparity_gt, disparity_res):
    """Compute the average end-point error of the estimated disparity map:

    Args:
        disparity_gt: the ground truth of disparity map as (H, W) numpy array
        disparity_res: the estimated disparity map as (H, W) numpy array

    Returns:
        aepe: the average end-point error as a floating point value
    """
    assert disparity_gt.ndim == 2 
    assert disparity_res.ndim == 2 
    assert disparity_gt.shape == disparity_res.shape

    # START your code here
    # NOTE: You should remove the next line while coding
    H, W = disparity_gt.shape
    N = H * W

    difference_abs = np.abs(disparity_gt - disparity_res)
    aepe = np.sum(difference_abs) / N
    # END your code here

    assert np.isscalar(aepe)
    return aepe


def optimal_alpha():
    """Return alpha that leads to the smallest EPE
    (w.r.t. other values)"""

    # TODO: You need to fix the alpha value
    alpha = np.random.choice([-0.06, -0.01, 0.04, 0.1])
    return alpha
