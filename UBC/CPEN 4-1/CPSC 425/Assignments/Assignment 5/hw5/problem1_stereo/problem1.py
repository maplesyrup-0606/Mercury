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
    
    # Flatten each pach into a 1-dimensional array
    patch1_flatten = patch1.flatten()
    patch2_flatten = patch2.flatten()

    # Compute the SSD by taking the sum of the differences squared
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

    # Flatten each patch into a 1-dimensional array
    patch1_flatten = patch1.flatten()
    patch2_flatten = patch2.flatten()

    # Compute the Mean of each patch
    patch1_mean = np.mean(patch1)
    patch2_mean = np.mean(patch2)

    # Normalize each patch by subtracting the mean
    patch1_new = patch1_flatten - patch1_mean
    patch2_new = patch2_flatten - patch2_mean

    # Compute the norm of each 1d patch
    size_1 = norm(patch1_new)
    size_2 = norm(patch2_new)

    # Compute normalized correlation
    cost_nc = patch1_new.T @ patch2_new / (size_1 * size_2)
    # END your code here

    assert np.isscalar(cost_nc)
    return cost_nc


def cost_function(patch1, patch2, alpha):
    """Compute the cost between two input window patches:
    Args:
        patch1: input patch 1 as (m, m) numpy array
        patch2: input patch 2 as (m, m) numpy array
        alpha: the weighting parameter for the cost function
    Returns:
        cost_val: the calculated cost value as a floating point value
    """
    assert patch1.shape == patch2.shape

    # START your code here
    # NOTE: You should remove the next line while coding

    # Compute the length of one side of the patch
    m = len(patch1)

    # Expand each patch to 3d to match input types
    patch1_3d = np.expand_dims(patch1, axis=-1)
    patch2_3d = np.expand_dims(patch2, axis=-1)

    # Compute the ssd cost and nc cost
    ssd_cost = cost_ssd(patch1_3d,patch2_3d)
    nc_cost = cost_nc(patch1_3d, patch2_3d)

    # Compute the total cost
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

    # Get padding amount
    k = window_size // 2
    
    if padding_mode == "constant" :
        # Pad k 0's to each side
        padded_img = np.pad(input_img,k,mode="constant",constant_values=0)
    elif padding_mode == "symmetric" :
        # Pad symmetrically each side by k
        padded_img = np.pad(input_img,k,mode="symmetric")
    elif padding_mode == "reflect" :
        # Pad by reflecting each side by k
        padded_img = np.pad(input_img,k,mode="reflect")
    else :
        print("error") 
    # END your code here

    return padded_img


def compute_disparity(padded_img_l, padded_img_r, max_disp, window_size, alpha):
    """Compute the disparity map by using the window-based matching:
    Args:
        padded_img_l: The padded left-view input image as 2-dimensional numpy array (H,W) 
        padded_img_r: The padded right-view input image as 2-dimensional numpy array (H,W)
        max_disp: the maximum disparity as a search range
        window_size: the patch size for window-based matching, odd number
        alpha: the weighting parameter for the cost function
    Returns:
        disparity: numpy array (H + window - 1, W + window  - 1) of the same size as the input image without padding
    """
    assert padded_img_l.ndim == 2 
    assert padded_img_r.ndim == 2 
    assert padded_img_l.shape == padded_img_r.shape
    assert max_disp > 0
    assert window_size % 2 == 1
    # START your code here
    # HINT: in numpy, there is a function named argmin
    # NOTE: You should remove the next line while coding

    # Get padded patch size
    H_padded, W_padded = padded_img_l.shape
    
    # Get window radiues
    k = window_size // 2
    
    # Get original patch size
    H, W = H_padded - 2 * k, W_padded - 2 * k
    
    # Prepare disparity array of size H * W
    disparity = np.zeros((H, W))

    for y in range(k, H_padded - k) :
        for x in range(k, W_padded - k) :

            # Get the patch of the left image in size of patch size
            patchL = np.expand_dims(padded_img_l[y - k : y + k + 1, x - k : x + k + 1], axis=-1)
            
            # Array for costs
            costs = []
            
            # Iterate for disparity range from 0 to max_disparity
            for d in range(max_disp): 

                # Out of bounds check for patch of right image
                if x - d - k >= 0 :

                    # Get the patch of the right image in size of patch size
                    patchR = np.expand_dims(padded_img_r[y - k : y + k + 1, (x - d) - k : (x - d) + k + 1],axis=-1)
                    
                    # Compute the cost of the left and right patch
                    cur_cost = cost_function(patchL, patchR, alpha)
                    
                    # Append to costs
                    costs.append(cur_cost)
                else :
                    # If out of bound append cost of infinity
                    costs.append(float('inf'))
            
            # Find disparity with minimum cost
            index = np.argmin(costs)

            # Add to disparity array
            disparity[y - k,x - k] = index
    
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

    # Get dimensions of ground truth shape
    H, W = disparity_gt.shape

    # Compute total number of pixels
    N = H * W

    # Get absolute difference of ground truth and estimated disparity map
    difference_abs = np.abs(disparity_gt - disparity_res)

    # Compute the AEPE by getting the sum of absolute differences divided by size of map
    aepe = np.sum(difference_abs) / N
    # END your code here

    assert np.isscalar(aepe)
    return aepe


def optimal_alpha():
    """Return alpha that leads to the smallest EPE
    (w.r.t. other values)"""

    # TODO: You need to fix the alpha value
    
    # alpha with minimum AEPE
    # alpha = {-0.06, -0.01, 0.04, 0.1}
    alpha = -0.01
    return alpha
