#!/usr/bin/env python3

import argparse
import cv2

import math
import numpy as np

def dct(input_matrix):
    M, N = input_matrix.shape
    dct_matrix = np.zeros((M,N))
    dct_matrix2 = np.zeros((M,N))

    sum = 0.0
    alfa = 0.0
    offset = 256

    for k in range(M):
        for l in range(N):
            sum = 0.0
            for i in range(M):
                sum += (input_matrix[i][l] + offset) * math.cos( (math.pi * (2*i+1) * k) / (2 * M))
        alfa = 1 / math.sqrt(M) if k == 0 else math.sqrt(2 / M)
        dct_matrix[k][l] = (alfa * sum)

    for l in range(N):
        for k in range(M):
            sum = 0.0
            for j in range(N):
                sum += dct_matrix[k][j] * math.cos((math.pi * (2*j+1) * 1) / (2 * N))
            alfa = 1 / math.sqrt(N) if l == 0 else math.sqrt(2 / N)
            dct_matrix2[k][l] = (alfa * sum)

    return dct_matrix2

def main():
    parser = argparse.ArgumentParser(description='Discrete Cosine Transform')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    args = parser.parse_args()

    if args.input is None:
        parser.print_help()
        exit(2)

    input_img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    result = dct(input_img)

    cv2.imshow("DCT Result", result.astype(np.uint8))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
