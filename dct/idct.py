""" Brief
Description
"""

import cv2
import math
import numpy as np

def idct1D(vector):
    """ Brief
    Description
    """

    N = vector.size
    x = np.zeros(N)

    for n in range(N):
        sum = 0
        for k in range(N):
            alpha = math.sqrt(1/N) if k == 0 else math.sqrt(2/N)
            sum += alpha * vector[k] * math.cos( (math.pi * (2*n+1) * k) / (2*N) )
        x[n] = sum

    return x

def idct2D(matrix):
    """ Brief
    Description
    """

    M, N = matrix.shape

    dctmatrix = np.zeros((M,N))
    dctmatrix_t = np.zeros((M,N))

    dctmatrix = np.array([idct1D(matrix[i]) for i in range(M)])
    dctmatrix_t = np.array([idct1D(dctmatrix.T[i]) for i in range(M)])

    return dctmatrix_t.T
