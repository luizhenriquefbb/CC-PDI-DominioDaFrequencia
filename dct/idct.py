""" Brief
Description
"""

import cv2
import math
import numpy as np

import img_handler as ih
import progress_bar

def idct1D(vector):
    """ Brief
    Description
    """

    N = vector.size
    x = np.zeros(N)

    for n in range(N):
        sum = 0
        for k in range(N):
            alpha = math.sqrt(1.0/N) if k == 0 else math.sqrt(2.0/N)
            sum += alpha * vector[k] * math.cos( (math.pi * (2*n+1) * k) / (2*N) )
        x[n] = sum

    return x

def idct2D(matrix):
    """ Brief
    Description
    """

    M, N = matrix.shape

    BLOCK_SIZE = 8
    blocksmatrix = ih.block_shaped(matrix, (BLOCK_SIZE, BLOCK_SIZE))

    dctmatrix = np.zeros(blocksmatrix.shape)

    for idx, block in enumerate(blocksmatrix):
        dct = np.array([idct1D(block[i]) for i in range(BLOCK_SIZE)])
        dct_t = np.array([idct1D(dct.T[j]) for j in range(BLOCK_SIZE)])
        dctmatrix[idx] = dct_t.T

    return ih.unblock_shaped(dctmatrix, (M, N))
