""" Brief
Description
"""

import cv2
import math
import numpy as np

def dct1D(vector):
    """ Brief
    Description
    """

    N = vector.size
    X = np.zeros(N)

    for k in range(N):
        alpha = math.sqrt(1/N) if k == 0 else math.sqrt(2/N)
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

    dctmatrix = np.zeros((M,N))
    dctmatrix_t = np.zeros((M,N))

    dctmatrix = np.array([dct1D(matrix[i]) for i in range(M)])
    dctmatrix_t = np.array([dct1D(dctmatrix.T[i]) for i in range(M)])

    return dctmatrix_t.T
