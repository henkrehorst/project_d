#!/bin/python3

import rasterio
from PIL import Image
import numpy as np
import json
import sys


def manual():
    print("\n\tUsage: \n\textractCoords.py [tiff filename] [x coordinate 1] [x coordinate 2] [y coordinate 1] [y coordinate 2]\n")
    quit()

if len(sys.argv) <= 5:
    manual()
else:
    try:
        fileName = sys.argv[1]
        x_coordinate_1 = int(sys.argv[2])
        x_coordinate_2 = int(sys.argv[3])
        y_coordinate_1 = int(sys.argv[4])
        y_coordinate_2 = int(sys.argv[5])
    except ValueError:
        manual()

def createPoint(iterator,x,y,z):
    newJson = {}    
    newJson["NAME"] = "POINT" + str(iterator)
    newJson["RGB"] = "#FF0000"
    newJson["X"] = x
    newJson["Y"] = y
    newJson["Z"] = z
    return newJson

band_id = 1
raster = rasterio.open("./" + fileName)
band_arr= raster.read(band_id)
multiplier = 10
band_arr = band_arr[x_coordinate_1:x_coordinate_2,y_coordinate_1: y_coordinate_2]

iterate = 0

with open('data.json', 'w') as json_file:     
    jsonList = []
    i = 0
    for arr1 in band_arr:
        i += 1
        j = 0
        for val in arr1:
            j += 1
            y = createPoint(iterate, int(i),int(j), float(val))
            jsonList.append(y)
            iterate += 1
    json.dump(jsonList, json_file, indent=len(jsonList[0]))
    json_file.close()

