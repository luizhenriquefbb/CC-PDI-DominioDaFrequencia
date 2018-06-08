#!/usr/bin/env python3

import argparse
import cv2
import math
import numpy as np

def dct1D(vector):
    N = vector.size
    X = np.zeros(N)

    for k in range(N):
        alpha = math.sqrt(1/N) if k == 0 else math.sqrt(2/N)
        sum = 0
        for n in range(N):
            sum += vector[n] * math.cos( (math.pi * (2*n+1) * k) / (2*N) )

        X[k] = alpha * sum

    return X

def idct1D(vector):
    N = vector.size
    x = np.zeros(N)

    for n in range(N):
        sum = 0
        for k in range(N):
            alpha = math.sqrt(1/N) if k == 0 else math.sqrt(2/N)
            sum += alpha * vector[k] * math.cos( (math.pi * (2*n+1) * k) / (2*N) )
        x[n] = sum

    return x

def dct2D(matrix):
    M, N = matrix.shape


def main():
    parser = argparse.ArgumentParser(description='Discrete Cosine Transform')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    args = parser.parse_args()

    if args.input is None:
        parser.print_help()
        exit(2)

    # input_img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    # result = dct(input_img)

    input = np.array([3, -4, 2, 1])
    result = dct1D(input)
    print("ida:", result)

    result2 = idct1D(result)
    print("volta:", result2)

    cv2.imshow("DCT Result", result.astype(np.uint8))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
