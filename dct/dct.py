""" Brief
Description
"""

import cv2
import math
import numpy as np

import img_handler as ih
import progress_bar

def dct1D(vector):
    """ Brief
    Description
    """

    N = vector.size
    X = np.zeros(N)

    for k in range(N):
        alpha = math.sqrt(1.0/N) if k == 0 else math.sqrt(2.0/N)
        sum = 0
        for n in range(N):
            sum += vector[n] * math.cos( (math.pi * (2*n+1) * k) / (2*N) )

        X[k] = alpha * sum

    return X

def dct2D(matrix):
    """ Brief
    Description
    """

    M, N = matrix.shape

    BLOCK_SIZE = 8
    blocksmatrix = ih.block_shaped(matrix, (BLOCK_SIZE, BLOCK_SIZE))

    dctmatrix = np.zeros(blocksmatrix.shape)

    for idx, block in enumerate(blocksmatrix):
        dct = np.array([dct1D(block[i]) for i in range(BLOCK_SIZE)])
        dct_t = np.array([dct1D(dct.T[j]) for j in range(BLOCK_SIZE)])
        dctmatrix[idx] = dct_t.T

    return ih.unblock_shaped(dctmatrix, (M, N))
