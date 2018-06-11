'''

'''

import numpy as np
from math import sqrt

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
    result = np.zeros((L,C))
    
    importantPixels = _getPixelsList(M)[:int(n)]

    for pixel in importantPixels:
        result[pixel.x][pixel.y] = pixel.grayScale

    # import pdb; pdb.set_trace()
    
    return result


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
    
    
    # sortedList = sorted(
    #     pixels, key=lambda pixel: pixel._getgrayScaleModule(), reverse=True)
    
    
    sortedList = sorted(
        pixels, key=lambda pixel: pixel._getgrayScaleModule(), reverse=True)
    # import pdb; pdb.set_trace()

    # for i in sortedList:
        # i.grayScale = i._getgrayScaleModule()


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

    def _getgrayScaleModule(self):
        return self.grayScale if self.grayScale > 0 else self.grayScale * -1