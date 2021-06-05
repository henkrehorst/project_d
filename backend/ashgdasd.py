from os import path
from numpy.core.defchararray import asarray
import filterCoords
import numpy
from numpy import save
from numpy import load
import sys
sys.setrecursionlimit(10**8)

xyzFile = open('goeree.xyz','r')
xyzData = xyzFile.read()
xyzFile.close()

TwoDArr = filterCoords.RunFilterOutput2DArray(xyzData, "./", 52590.5, 427698.9114832536, 52665.5, 427280.9114832536, 52630.5, 427706.0885167464, 52705.5, 427288.0885167464)

nap = 4
lengthy = TwoDArr.shape[0]-1
widthx = TwoDArr.shape[1]-1
x=0
count=0

for _ in range(0,widthx+1):
    y=int(lengthy/2)
    value = lengthy
    for _ in range(0,int(lengthy/2)+1):
        if TwoDArr[y,x].height == -9999 and TwoDArr[y,x].y <= value:
            myval = str(TwoDArr[y,x].x) + " " + str(TwoDArr[y,x].y) + str(TwoDArr[y,x].height)
            value = TwoDArr[y,x].y
            count+=1
        y+=1
       
    print(myval)
    x+=1
print(count)