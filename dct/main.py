#!/usr/bin/env python3

import argparse
import cv2
import numpy as np

import dct
import idct
import img_handler as ih
import pixel_selector as ps

def main():
    parser = argparse.ArgumentParser(description='Discrete Cosine Transform')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    parser.add_argument('-n', '--pixelNumber', action='store')
    args = parser.parse_args()

    if args.input is None or args.output is None or args.pixelNumber is None:
        parser.print_help()
        exit(2)

    print ("Reading image")
    img = cv2.imread(args.input)
    pxlfmt = ih.get_pixel_format(img)

    cv2.imshow("Original", img)

    if pxlfmt == ih.YIQ_FMT:
        print("Image in YIQ format")
        grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        dtc2d_ret = dct.dct2D(grayimg)
        cv2.imshow("DCT-2D Result", dtc2d_ret.astype(np.uint8))
        cv2.imwrite("DCT2DResult.jpg", dtc2d_ret.astype(np.uint8))

        important = ps.selectImportantPixels(dtc2d_ret, n=args.pixelNumber)
        cv2.imshow("Important pixels", important.astype(np.uint8))
        cv2.imwrite("DCT2DResult.jpg", important.astype(np.uint8))

        idtc2d_ret = idct.idct2D(dtc2d_ret)
        cv2.imshow("IDCT-2D Result", idtc2d_ret.astype(np.uint8))

        idtc2d_important = idct.idct2D(important)
        cv2.imshow("IDCT-2D important Result", idtc2d_important.astype(np.uint8))
        # import pdb; pdb.set_trace()

    else:
        print("Image in RGB format")
        r, g, b = ih.split_channels(img)

        print("Starting DCT-2D to R")
        r_dtc2d_ret = dct.dct2D(r)
        important_r = ps.selectImportantPixels(r_dtc2d_ret, n=args.pixelNumber)

        print("\nStarting DCT-2D to G")
        g_dtc2d_ret = dct.dct2D(g)
        important_g = ps.selectImportantPixels(g_dtc2d_ret, n=args.pixelNumber)

        print("\nStarting DCT-2D to B")
        b_dtc2d_ret = dct.dct2D(b)
        important_b = ps.selectImportantPixels(b_dtc2d_ret, n=args.pixelNumber)

        cv2.imshow("DCT-2D Result", ih.merge_channels(r_dtc2d_ret, g_dtc2d_ret, b_dtc2d_ret))

        cv2.imshow("Important pixels", ih.merge_channels(important_r, important_g, important_b))

        print("\nStarting IDCT-2D to R")
        r_idtc2d_ret = idct.idct2D(r_dtc2d_ret)
        print("\nstarting IDCT-2D to G")
        g_idtc2d_ret = idct.idct2D(g_dtc2d_ret)
        print("\nstarting IDCT-2D to B")
        b_idtc2d_ret = idct.idct2D(b_dtc2d_ret)
        cv2.imshow("IDCT-2D Result", ih.merge_channels(r_idtc2d_ret, g_idtc2d_ret, b_idtc2d_ret))


        # cv2.imshow("idct-important_r", idct.idct2D(important_r))
        # cv2.imshow("idct-important_g", idct.idct2D(important_g))
        # cv2.imshow("idct-important_b", idct.idct2D(important_b))
        
        cv2.imshow("idct-important_merged", ih.merge_channels(idct.idct2D(important_r),
                                                         idct.idct2D(important_g), idct.idct2D(important_b)))



    cv2.waitKey(0)

if __name__ == '__main__':
    main()
