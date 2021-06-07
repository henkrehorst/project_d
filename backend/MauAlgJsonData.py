import json
import random
from random import randint
import math
import sys
import PIL
sys.setrecursionlimit(10000)
from colorsys import hsv_to_rgb
from PIL import Image
import numpy as np
import filterCoords

#newdataload
xyzFile = open('goeree.xyz','r')
xyzData = xyzFile.read()
xyzFile.close()
TwoDArr = filterCoords.RunFilterOutput2DArray(xyzData, "./", 52590.5, 427698.9114832536, 52665.5, 427280.9114832536, 52630.5, 427706.0885167464, 52705.5, 427288.0885167464)
lengthy = TwoDArr.shape[0]
widthx = TwoDArr.shape[1]
nap=4
waitArr = []
#read file and parse Library
myLibrary = open('tiffdatawl2.json','r')
myData = myLibrary.read()
myLibrary.close()
obj = json.loads(myData)


class MDCreator:

    def setAllData(self):
        count=0
        for x in range (widthx):
            for y in range (lengthy):
                obj.append({
                    "NAME"      : "POINT" + str(count),
                    "RGB"       : TwoDArr[y,x].RGB,
                    "X"         : TwoDArr[y,x].x,
                    "Y"         : TwoDArr[y,x].y,
                    "Z"         : TwoDArr[y,x].height,
                    "POINTXY"   : str(TwoDArr[y,x].point.x) + " " + str(TwoDArr[y,x].point.y)
                                                                    
                    })
                count+=1
        with open('tiffdatawl2.json', 'w') as f:
            json.dump(obj, f, indent=len(obj[0]))
            f.close()

        
        # count=0
        # for _ in obj:
        #     obj[count]['NAME'] = "POINT"+ str(count)
        #     count+=1
        # count=0
        # for _ in obj:
        #     obj[count]['Z'] = random.uniform(0, 10)
        #     count+=1

        # counter=0
        # all=0
        # #MUST HAVE DICTIONARY OF 10000 different dictionary objects :)
        # for _ in range(500):
        #     counter+=1
        #     counter2=1
        #     for _ in range(500):
        #         obj[all]["Y"]=counter
        #         obj[all]["X"]=counter2
        #         counter2+=1
        #         all+=1

                
        # with open('tiffdatawl2.json', 'w') as f:
        #     json.dump(obj,f,indent=len(obj[0]))
        #     f.close()


class MAlgorithm:
    
    def checknode(self, snode,nap):
        if float(obj[snode]['Z'])<=nap:
            global checky #Kanstraksweg
            checky=0 #Kanstraksweg
            counts=0
            return(self.pathFinder(snode,nap,counts))
        else: 
            print("Path is above NAP, therefore safe")

 
    def pathFinder(self, snode,nap,counts):
        global checky
        obj[snode]['RGB']="#0000FF"
        counts+=1
        checky+=1 #Kanstraksweg
        print(obj[snode]['NAME'])
        if counts > 10000:
            print("WARNING!!! THIS AREA WILL BE FLOODED!")
            print(checky) #Kanstraksweg
            sys.exit()
        if obj[snode]['X']>1:
            if float(obj[snode-1]['Z']) <= nap and obj[snode-1]['RGB']!="#0000FF":
                # waitArr.append(obj[snode-1])
                self.pathFinder(snode-1,nap,counts)
            if obj[snode]['Y']<widthx:
                if float(obj[snode+widthx-1]['Z']) <= nap and obj[snode+widthx-1]['RGB']!="#0000FF":
                    # waitArr.append(obj[snode+widthx-1])
                    self.pathFinder(snode+widthx-1,nap,counts)
            if obj[snode]['Y']>1:
                if float(obj[snode-widthx-1]['Z']) <= nap and obj[snode-widthx-1]['RGB']!="#0000FF":
                    # waitArr.append(obj[snode-widthx-1])
                    self.pathFinder(snode-widthx-1,nap,counts)
                

        if obj[snode]['X']<widthx:
            if float(obj[snode+1]['Z']) <= nap and obj[snode+1]['RGB']!="#0000FF":
                # waitArr.append(obj[snode+1])
                self.pathFinder(snode+1,nap,counts)
            if obj[snode]['Y']<widthx:   
                if float(obj[snode+widthx+1]['Z']) <= nap and obj[snode+widthx+1]['RGB']!="#0000FF":
                    # waitArr.append(obj[snode+widthx+1])
                    self.pathFinder(snode+widthx+1,nap,counts)
            if obj[snode]['Y']>1:
                if float(obj[snode-widthx+1]['Z']) <= nap and obj[snode-widthx+1]['RGB']!="#0000FF":
                    # waitArr.append(obj[snode-widthx-1])
                    self.pathFinder(snode-widthx+1,nap,counts)


        if obj[snode]['Y']<widthx:
            if float(obj[snode+widthx]['Z']) <= nap and obj[snode+widthx]['RGB']!="#0000FF":
                # waitArr.append(obj[snode+widthx])
                self.pathFinder(snode+widthx,nap,counts)
        
        if obj[snode]['Y']>1:
            if float(obj[snode-widthx]['Z']) <= nap and obj[snode-widthx]['RGB']!="#0000FF":
                # waitArr.append(obj[snode-widthx])
                self.pathFinder(snode-widthx,nap,counts)
    
        
class MapCreator:
    def drawPath(self,start):
        array = np.zeros([widthx, lengthy, 3], dtype=np.uint8)
        array[:,:] = [248, 213, 104] #Sandy backside
        
        count=0
        for _ in obj:
            if obj[count]["RGB"] == "#0000FF":
                array[obj[count]["X"],obj[count]["Y"]] = [55, 102, 246] #blue line
            count+=1
        startpar=0
        for _ in range(0,start):
            array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
            startpar+=1
        for _ in range(start,secondhalf):
            array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
            startpar+=1
        img = Image.fromarray(array)
        img.save('testrgb.png')


# # Dit is om je data te vernieuwen
print("Hello")
# names = MDCreator()
# names.setAllData()

# # Dit is om het algoritme uit te voeren
start=int(widthx/2)
secondhalf=widthx


find = MAlgorithm()

startpar=0
for _ in range(0,start):
    find.checknode(startpar,nap) #lengte 1e rij meegeven voor werken met rechthoeken
    startpar+=1
# for _ in range(start,secondhalf):
#     find.checknode(startpar,nap) #lengte 1e rij meegeven voor werken met rechthoeken
#     startpar+=1

# while len(waitArr) > 0:
#     if waitArr[0]['RGB'] != "#0000FF":
#         find.pathFinder(waitArr[0]['X'], waitArr[0]['Y'], nap)
#         waitArr[0]['RGB'] = "#0000FF"
#     del waitArr[0]

# #Dit is om het pad te tekenen
draw = MapCreator()
draw.drawPath(start)