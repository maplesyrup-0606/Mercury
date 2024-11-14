import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# Stereo
import problem1 as part1

def rgb2gray(im):
    return np.mean(im, -1)


def load_image(path):
    return plt.imread(path)


def disparity_read(filename):
    """ Return disparity read from filename. """
    f_in = np.array(Image.open(filename))
    d_r = f_in[:,:,0].astype('float64')
    d_g = f_in[:,:,1].astype('float64')
    d_b = f_in[:,:,2].astype('float64')

    disparity = d_r * 4 + d_g / (2**6) + d_b / (2**14)
    return disparity


def problem1():
    """Example code implementing the steps in Problem 2"""

    # Given parameter. No need to change
    max_disp = 15

    alpha = part1.optimal_alpha()
    print("Alpha: {:4.3f}".format(alpha))

    # Window size. You can freely change, but it should be an odd number
    window_size = 11

    # from utils.py
    im_left = rgb2gray(load_image("part1_left.png"))
    im_right = rgb2gray(load_image("part1_right.png"))
    disparity_gt = disparity_read("part1_gt.png")
    padded_img_l = part1.pad_image(im_left, window_size, padding_mode='symmetric')
    padded_img_r = part1.pad_image(im_right, window_size, padding_mode='symmetric') 

    disparity_res = part1.compute_disparity(padded_img_l, padded_img_r, max_disp, window_size, alpha)
    aepe = part1.compute_aepe(disparity_gt, disparity_res)
    print("AEPE: {:4.3f}".format(aepe))

    interp = 'bilinear'
    fig, axs = plt.subplots(nrows=2, sharex=True)
    axs[0].set_title('disparity_gt')
    axs[0].imshow(disparity_gt, vmin=0, vmax=20, cmap='gray')
    axs[1].set_title('disparity_res')
    axs[1].imshow(disparity_res, vmin=0, vmax=20, cmap='gray')
    plt.show()


problem1()
