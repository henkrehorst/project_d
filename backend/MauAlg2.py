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

class MauAlgorithm:

    def checkNode(self, y, x, nap):
        if TwoDArr[y,x].height < nap :
                return(self.pathFinder(y,x,nap))
        else: 
            print("Path is above NAP, therefore safe")

    def pathFinder(self,y,x,nap):
        if TwoDArr[y,x].height != -9999:
            TwoDArr[y,x].RGB = "#FFB6C1"
            print(str(TwoDArr[y,x].height) +" "+ str(TwoDArr[y,x].RGB) +" "+ str(TwoDArr[y,x].x) +" "+ str(TwoDArr[y,x].y))
            
        if y>0 and TwoDArr[y-1,x].RGB != "#FFB6C1" and float(TwoDArr[y-1,x].height) < nap:
                return self.pathFinder(y-1,x,nap)
        if y<lengthy and TwoDArr[y+1,x].RGB != "#FFB6C1" and float(TwoDArr[y+1,x].height) < nap:
                return self.pathFinder(y+1,x,nap)

        if x>0 and TwoDArr[y,x-1].RGB != "#FFB6C1" and float(TwoDArr[y,x-1].height) < nap:
            return self.pathFinder(y,x-1,nap)
        if x<widthx and TwoDArr[y,x+1].RGB != "#FFB6C1" and float(TwoDArr[y,x+1].height) < nap:
            return self.pathFinder(y,x+1,nap)

        if y>0 and x>0 and TwoDArr[y-1,x-1].RGB != "#FFB6C1" and float(TwoDArr[y-1,x-1].height) < nap:
            return self.pathFinder(y-1,x-1,nap)
        if y<lengthy and x<widthx and TwoDArr[y+1,x+1].RGB != "#FFB6C1" and float(TwoDArr[y+1,x+1].height) < nap:
            return self.pathFinder(y+1,x+1,nap)

        if y>0 and x<widthx and TwoDArr[y-1,x+1].RGB != "#FFB6C1" and float(TwoDArr[y-1,x+1].height) < nap:
            return self.pathFinder(y-1,x+1,nap)
        if y<lengthy and x>0 and TwoDArr[y+1,x-1].RGB != "#FFB6C1" and float(TwoDArr[y+1,x-1].height) < nap:
            return self.pathFinder(y+1,x-1,nap)



find = MauAlgorithm()
nap=4
count=0
for _ in range(0,widthx):
    find.checkNode(0,count,nap)
    count+=1

# print(TwoDArr[lengthy-1,0].x)
# TwoDArr2 = asarray(TwoDArr)

# save('ndata.npy', TwoDArr2)

# new2Darr=load('ndata.npy')
# print(new2Darr[0,0].RGB)

#LENGTH X komt als 2e maar 1 is wel y

