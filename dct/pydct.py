#!/usr/bin/env python3

import cv2
import numpy as np
from scipy.fftpack import dct, idct

img = cv2.imread("/home/wesnydy/lena256.jpg", cv2.IMREAD_GRAYSCALE)
M, N = img.shape

dctmatrix = np.zeros((M,N))
idctmatrix = np.zeros((M,N))

for i in range(M):
    dctmatrix[i] = dct(img[i], type=2, norm='ortho')
    idctmatrix[i] = idct(dctmatrix[i], type=2, norm='ortho')

cv2.imshow("DCT Result", dctmatrix.astype(np.uint8))
cv2.imshow("IDCT Result", idctmatrix.astype(np.uint8))
cv2.waitKey(0)
