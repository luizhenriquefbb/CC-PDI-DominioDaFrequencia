#!/usr/bin/env python3

import argparse
import cv2
import numpy as np

import dct
import idct
import imghandler

def main():
    parser = argparse.ArgumentParser(description='Discrete Cosine Transform')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    args = parser.parse_args()

    if args.input is None or args.output is None:
        parser.print_help()
        exit(2)

    img = cv2.imread(args.input)
    pxlfmt = imghandler.get_pixel_format(img)

    cv2.imshow("Original", img)

    if pxlfmt == imghandler.YIQ_FMT:
        grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        dtc2d_ret = dct.dct2D(grayimg)
        cv2.imshow("DCT Result", dtc2d_ret.astype(np.uint8))

        idtc2d_ret = idct.idct2D(dtc2d_ret)
        cv2.imshow("IDCT Result", idtc2d_ret.astype(np.uint8))

    else:
        r, g, b = imghandler.split_channels(img)

        r_dtc2d_ret = dct.dct2D(r)
        g_dtc2d_ret = dct.dct2D(g)
        b_dtc2d_ret = dct.dct2D(b)
        cv2.imshow("DCT Result", imghandler.merge_channels(r_dtc2d_ret, g_dtc2d_ret, b_dtc2d_ret))

        r_idtc2d_ret = idct.idct2D(r_dtc2d_ret)
        g_idtc2d_ret = idct.idct2D(g_dtc2d_ret)
        b_idtc2d_ret = idct.idct2D(b_dtc2d_ret)
        cv2.imshow("IDCT Result", imghandler.merge_channels(r_idtc2d_ret, g_idtc2d_ret, b_idtc2d_ret))

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
