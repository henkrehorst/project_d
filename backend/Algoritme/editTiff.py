#!/bin/python3

import rasterio
from PIL import Image
import numpy as np
import sys


def manual():
    print("\n\tTO EDIT: \n\teditTiff.py -e [tiff filename] [x coordinate] [y coordinate] [new value]\n")
    print("\n\tTO GET VALUE: \n\teditTiff.py -g [tiff filename] [x coordinate] [y coordinate]\n")
    quit()

if len(sys.argv) <= 4:
    manual()
else:
    try:
        mode = sys.argv[1]
        if mode == "-e":
            if len(sys.argv) <= 5:
                manual()
            else:
                insertValue = sys.argv[5]
        fileName = sys.argv[2]
        x_coordinate_1 = int(sys.argv[3])
        y_coordinate_1 = int(sys.argv[4])
    except ValueError:
        manual()

band_id = 1
src = rasterio.open("./" + fileName, 'r')
band_arr= src.read(band_id)

if mode == '-e':
    band_arr[x_coordinate_1,y_coordinate_1] = insertValue
    with rasterio.open('./'+fileName, 'w', **src.profile) as dst:
        dst.write(band_arr.astype(rasterio.float32), indexes=1)
elif mode == '-g':
    print(band_arr[x_coordinate_1,y_coordinate_1])
