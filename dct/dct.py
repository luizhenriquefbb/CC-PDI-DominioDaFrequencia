#!/usr/bin/env python3

import argparse
import cv2

from math import cos, sqrt
from numpy import zeros

PI = 3.141592

def ck(k):
    return 1/sqrt(2) if k == 0 else 1

# def summation(matrix, N, k):
#     sum = 0
#     for n in range(N-1):
#         sum += cos( ((PI*k)/(2*N)) * (2*n+1) ) * matrix[k][n]
#
#     return sum
#
# def dct(input_matrix):
#     M, N = input_matrix.shape
#     dct_matrix = zeros((M,N))
#
#     for r in range(M):
#         for c in range(N):
#             dct_matrix[r][c] = sqrt(2/N) * ck(r) * summation(input_matrix, N, r)
#
#     return dct_matrix

def summation(matrix, N, k):
    sum = 0
    for n in range(1, N-1):
        sum += matrix[k][n] * cos(PI*k*n/(N-1))

    return sum

def dct(input_matrix):
    M, N = input_matrix.shape
    dct_matrix = zeros((M,N))

    for r in range(M):
        for c in range(N):
            dct_matrix[r,c] = input_matrix[r, 0] + ((-1)**r) * input_matrix[r, N-1] + 2 * summation(input_matrix, N, r)

    return dct_matrix

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

    cv2.imshow("DCT Result", result)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
