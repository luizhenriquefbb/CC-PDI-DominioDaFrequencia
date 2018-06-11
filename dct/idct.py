""" Brief
Description
"""

import cv2
import math
import numpy as np
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

    dctmatrix = np.zeros((M,N))
    dctmatrix_t = np.zeros((M,N))

    # dctmatrix = np.array([idct1D(matrix[i]) for i in range(M)])
    for i in range(M):
        progress_bar.printProgressBar(i, M-1)
        dctmatrix[i] = np.array([idct1D(matrix[i])])

    dctmatrix_t = np.array([idct1D(dctmatrix.T[i]) for i in range(M)])

    return dctmatrix_t.T
