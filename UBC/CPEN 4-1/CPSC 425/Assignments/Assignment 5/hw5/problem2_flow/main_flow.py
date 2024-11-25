import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from utils import *
# Flow
import problem2 as part2

def show_two(im1, im2):
    fig = plt.figure(figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')

    (ax1, ax2) = fig.subplots(1, 2)

    ax1.imshow(im1, cmap='gray')
    ax2.imshow(im2)

    plt.show()


def problem2(image1, image2, aggregate="const", sigma=2):
    # Loading the image and scaling to [0, 1]
    im1 = np.array(Image.open(image1).convert('L')) / 255.0
    im2 = np.array(Image.open(image2).convert('L')) / 255.0

    Ix, Iy, It = part2.compute_derivatives(im1, im2)  # gradients
    u, v = part2.compute_motion(Ix, Iy, It, aggregate=aggregate, sigma=sigma)  # flow

    # stacking for visualisation
    of = np.stack([u, v], axis=-1)
    # convert to RGB using wheel colour coding
    rgb_image = flow_to_color(of, clip_flow=5)
    # display
    show_two(im1, rgb_image)
    # warping 1st image to the second
    im1_warped = part2.warp(im1, u, v)
    cost = part2.compute_cost(im1_warped, im2)
    print("Cost: {:4.3e}".format(cost))


def problem2_start():
    # the things frames
    print ("The things example - aggregate='const': ")
    problem2("part2_things_frame1.png", "part2_things_frame2.png", aggregate="const")
    print ("")
    print ("The things example - aggregate='gaussian': ")
    problem2("part2_things_frame1.png", "part2_things_frame2.png", aggregate="gaussian", sigma=2)
    print ("")
    # the street frames
    print ("The street example - aggregate='const': ")
    problem2("part2_street_frame1.png", "part2_street_frame2.png", aggregate="const")
    print ("")
    print ("The street example - aggregate='gaussian': ")
    problem2("part2_street_frame1.png", "part2_street_frame2.png", aggregate="gaussian", sigma=2)
    print ("")


problem2_start()
