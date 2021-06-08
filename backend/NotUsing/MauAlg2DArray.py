from os import path
from numpy.core.defchararray import asarray
from numpy.lib import twodim_base
import filterCoords
import numpy
from numpy import save
from numpy import load
import numpy as np
import sys
from PIL import Image
from colorsys import hsv_to_rgb
sys.setrecursionlimit(10**8)

xyzFile = open('goeree.xyz','r')
xyzData = xyzFile.read()
xyzFile.close()
county = 0
TwoDArr = filterCoords.RunFilterOutput2DArray(xyzData, "./", 52590.5, 427698.9114832536, 52665.5, 427280.9114832536, 52630.5, 427706.0885167464, 52705.5, 427288.0885167464)
waitArr = []
nap = 1
lengthy = TwoDArr.shape[0]-1
widthx = TwoDArr.shape[1]-1


class MauAlgorithm:
    global county
    def checkNode(self, y, x, nap):
        if float(TwoDArr[y,x].height) < nap :
                return(self.pathFinder(y,x,nap))
        else: 
            print("Path is above NAP, therefore safe")

    def pathFinder(self,y,x,nap):
        global county
        global waitArr
        print(county)
        print(TwoDArr[y,x].RGB)
        county+=1
        TwoDArr[y,x].RGB = "#FFB6C1"
            
        if y>0 and TwoDArr[y-1,x].RGB != "#FFB6C1" and float(TwoDArr[y-1,x].height) < nap:
            waitArr.append(TwoDArr[y-1,x])
            # return self.pathFinder(y-1,x,nap)

        if y<lengthy and TwoDArr[y+1,x].RGB != "#FFB6C1" and float(TwoDArr[y+1,x].height) < nap:
            waitArr.append(TwoDArr[y+1,x])
            # return self.pathFinder(y+1,x,nap)

        if x>0 and TwoDArr[y,x-1].RGB != "#FFB6C1" and float(TwoDArr[y,x-1].height) < nap:
            waitArr.append(TwoDArr[y,x-1])
            # return self.pathFinder(y,x-1,nap)
        if x<widthx and TwoDArr[y,x+1].RGB != "#FFB6C1" and float(TwoDArr[y,x+1].height) < nap:
            waitArr.append(TwoDArr[y,x+1])
            # return self.pathFinder(y,x+1,nap)

        if y>0 and x>0 and TwoDArr[y-1,x-1].RGB != "#FFB6C1" and float(TwoDArr[y-1,x-1].height) < nap:
            waitArr.append(TwoDArr[y-1,x-1])
            # return self.pathFinder(y-1,x-1,nap)
        if y<lengthy and x<widthx and TwoDArr[y+1,x+1].RGB != "#FFB6C1" and float(TwoDArr[y+1,x+1].height) < nap:
            waitArr.append(TwoDArr[y+1,x+1])
            # return self.pathFinder(y+1,x+1,nap)

        if y>0 and x<widthx and TwoDArr[y-1,x+1].RGB != "#FFB6C1" and float(TwoDArr[y-1,x+1].height) < nap:
            waitArr.append(TwoDArr[y-1,x+1])
            # return self.pathFinder(y-1,x+1,nap)
        if y<lengthy and x>0 and TwoDArr[y+1,x-1].RGB != "#FFB6C1" and float(TwoDArr[y+1,x-1].height) < nap:
            waitArr.append(TwoDArr[y+1,x-1])
            # return self.pathFinder(y+1,x-1,nap)

# class GetLine:
#     def getLine(self,lengthy,widthx):
#         X=0
#         Y=0
#         pointArray = []
#         for _ in range(0,widthx+1):
#             value = lengthy+2
#             Y=0
#             for _ in range(0,lengthy+1):
#                 if TwoDArr[Y,X].height == -9999 and TwoDArr[Y,X].y < value:
#                     value = TwoDArr[Y,X].y
#                 Y+=1
#             pointArray.append(value)
#             X+=1
            
#         return pointArray

class MapCreator:
    def drawPath(self):
        array = np.zeros([widthx+1, lengthy+1, 4], dtype=np.uint8)
        array[:,:] = [248, 213, 104, 0] #Sandy backside
        
        #x=0
        #y=0
        for x in range(0,widthx):
            for y in range(0,lengthy):
                if nap - float(TwoDArr[y,x].height) > 2 and TwoDArr[y,x].RGB=="#FFB6C1":
                    TwoDArr[y,x].RGB="#FF0000"
                elif nap - float(TwoDArr[y,x].height) > 1 and TwoDArr[y,x].RGB=="#FFB6C1":
                    TwoDArr[y,x].RGB="#FFA500"
                elif nap - float(TwoDArr[y,x].height) > 0 and TwoDArr[y,x].RGB=="#FFB6C1":
                    TwoDArr[y,x].RGB="#FFFF00"
                #y+=1
            #x+=1
        #x=0
        #y=0
        for x in range(0,widthx):
            for y in range(0,lengthy):
                if TwoDArr[y,x].RGB == "#FF0000":
                    array[x,y] = [255, 0, 0,100] #red area
                if TwoDArr[y,x].RGB == "#FFA500":
                    array[x,y] = [255, 165, 0,100] #orange area
                if TwoDArr[y,x].RGB == "#FFFF00":
                    array[x,y] = [255, 255, 0,100] #yellow area
                if TwoDArr[y,x].RGB == "#39ff14":
                    array[x,y] = [57, 255, 20,100] #green? area
                #y+=1
            #x+=1

        #x=0
        img = Image.fromarray(array)
        img.save('testrgb.png')




        # for _ in TwoDArr:
        #     if obj[count]["RGB"] == "#0000FF":
        #         array[obj[count]["X"],obj[count]["Y"]] = [55, 102, 246] #blue line
        #     count+=1
        # startpar=0
        # for _ in range(0,start):
        #     array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
        #     startpar+=1
        # for _ in range(start,secondhalf):
        #     array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
        #     startpar+=1
        # img = Image.fromarray(array)
        # img.save('testrgb.png')






# dothing = GetLine()

# startline = dothing.getLine(114,424)

find = MauAlgorithm()
nap=0
count=0
for _ in range(0,widthx+1):
    find.checkNode(0,count,nap)
    count+=1


while len(waitArr) > 0:

    if waitArr[0].RGB != "#FFB6C1":
        find.pathFinder(waitArr[0].x, waitArr[0].y, nap)
    print(str(waitArr[0].x) +" "+ str(waitArr[0].y))
    del waitArr[0]

#Dit is om het pad te tekenen
draw = MapCreator()
draw.drawPath()

# print(TwoDArr[lengthy-1,0].x)
# TwoDArr2 = asarray(TwoDArr)

# save('ndata.npy', TwoDArr2)

# new2Darr=load('ndata.npy')
# print(new2Darr[0,0].RGB)

#LENGTH X komt als 2e maar 1 is wel y

