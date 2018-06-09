#!/usr/bin/env python3

import argparse
import cv2
from numpy import uint8, array

from dct import dct2D
from idct import idct2D

def main():
    parser = argparse.ArgumentParser(description='Discrete Cosine Transform')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    args = parser.parse_args()

    if args.input is None or args.output is None:
        parser.print_help()
        exit(2)

    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)

    dtc2d_ret = dct2D(img)
    idtc2d_ret = idct2D(dtc2d_ret)

    cv2.imwrite(args.output, dtc2d_ret)

    cv2.imshow("Original", img)
    cv2.imshow("DCT Result", dtc2d_ret.astype(uint8))
    cv2.imshow("IDCT Result", idtc2d_ret.astype(uint8))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
