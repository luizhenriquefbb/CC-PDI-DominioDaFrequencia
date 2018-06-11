'''

'''

import numpy as np
from math import sqrt

import img_handler as ih

def selectImportantPixels(M, n = 1):
    '''
    Select important pixels from matrix

    Parameters:
        M - Matrix
        n - number of pixels

    return:
        Matrix with most important pixels
    '''
    L,C = M.shape

    BLOCK_SIZE = 8
    blocksmatrix = ih.block_shaped(M, (BLOCK_SIZE, BLOCK_SIZE))

    important_matrix = np.zeros(blocksmatrix.shape)

    for idx, block in enumerate(blocksmatrix):
        importantPixels = _getPixelsList(block)[:int(n)]
        for pixel in importantPixels:
            important_matrix[idx][pixel.x][pixel.y] = pixel.grayScale

    return ih.unblock_shaped(important_matrix, (L, C))

def _getPixelsList(M):
    '''
    Return a sorted list of pixels
    '''
    L, C = M.shape

    pixels = []
    for i in range(L):
        for j in range(C):
            pixels.append(_Pixel(i,j,M[i][j]))

    # sortedList = sorted(pixels, key=lambda pixel: _getDistanceFromDC(pixel.x,pixel.y), reverse=False)
    sortedList = sorted(
        pixels, key=lambda pixel: pixel.grayScale, reverse=True)
    return sortedList

def _getDistanceFromDC(x,y):
    '''
    Euclidian distance from 0,0

    Paramans:
        x,y - coordenates
    '''

    return sqrt(x**2 + y**2)

class _Pixel(object):
    def __init__(self, x, y, grayScale):
        self.x = x
        self.y = y
        self.grayScale = grayScale

    def __str__(self):
        return "{ "+str(self.x) + str(self.y) + str(self.grayScale) + " } \n"
