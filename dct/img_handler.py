""" Brief
Description
"""

import numpy as np

YIQ_FMT = 0
RGB_FMT = 1

def get_pixel_format(image):
    """ Brief
    Description
    """

    rows, columns, channels = image.shape
    for i in range(rows):
        for j in range(columns):
            if len(set(image[i][j])) > 1:
               return RGB_FMT

    return YIQ_FMT

def split_channels(rgb_image):
    """ Brief
    Description
    """

    rows, columns, _ = rgb_image.shape
    rch = np.zeros((rows, columns), dtype=np.uint8)
    gch = np.zeros((rows, columns), dtype=np.uint8)
    bch = np.zeros((rows, columns), dtype=np.uint8)

    for i in range(rows):
        for j in range(columns):
            rch[i][j], gch[i][j], bch[i][j] = rgb_image[i][j]

    return rch, gch, bch

def merge_channels(r_image, g_image, b_image):
    """ Brief
    Description
    """

    rows, columns = r_image.shape
    rgb_image = np.zeros((rows, columns, 3), dtype=np.uint8)

    for i in range(rows):
        for j in range(columns):
            rgb_image[i][j] = [r_image[i][j], g_image[i][j], b_image[i][j]]

    return rgb_image
