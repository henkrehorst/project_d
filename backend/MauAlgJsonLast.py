# from MauAlg2DArray import MauAlgorithm
import json
import PIL
import numpy as np
from colorsys import hsv_to_rgb
from PIL import Image
# import filterCoords

#newdataload
# xyzFile = open('goeree.xyz','r')
# xyzData = xyzFile.read()
# xyzFile.close()
# TwoDArr = filterCoords.RunFilterOutput2DArray(xyzData, "./", 52590.5, 427698.9114832536, 52665.5, 427280.9114832536, 52630.5, 427706.0885167464, 52705.5, 427288.0885167464)
# lengthy = TwoDArr.shape[0]
# widthx = TwoDArr.shape[1]
# nap=4
#read file and parse Library
myLibrary = open('tiffdatawl.json','r')
myData = myLibrary.read()
myLibrary.close()
obj = json.loads(myData)

print(obj[5])
# class MDCreator:
#     def setAllData(self):
#         count=0
#         for x in range (widthx):
#             for y in range (lengthy):
#                 obj.append({
#                     "NAME"      : "POINT" + str(count),
#                     "RGB"       : TwoDArr[y,x].RGB,
#                     "X"         : TwoDArr[y,x].x,
#                     "Y"         : TwoDArr[y,x].y,
#                     "Z"         : TwoDArr[y,x].height,
#                     "POINTXY"   : str(TwoDArr[y,x].point.x) + " " + str(TwoDArr[y,x].point.y)
                                                                    
#                     })
#                 count+=1
#         with open('tiffdatawl2.json', 'w') as f:
#             json.dump(obj, f, indent=len(obj[0]))
#             f.close()

class MAlgorithmm:
    
    def depthLocator(self, nap):
        count=0
        for _ in obj:
            if obj[count]["Z"]< nap:
                obj[count]["RGB"]="#0000FF"
                print(obj[count]["RGB"] + " " +str(obj[count]["X"]) + " " +str(obj[count]["Y"]))
            count+=1
        
        
class MapCreator:
    def drawPath(self):
        array = np.zeros([501, 501, 3], dtype=np.uint8)
        array[:,:] = [248, 213, 104] #Sandy backside
       
        count=0
        for _ in obj:
            if obj[count]["RGB"] == "#0000FF":
                array[obj[count]["X"],obj[count]["Y"]] = [55, 102, 246] #blue part
                count+=1
            
        # startpar=0
        # for _ in obj:
        #     array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
        #     startpar+=1
        # for _ in range(start,secondhalf):
        #     array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
        #     startpar+=1
        img = Image.fromarray(array)
        img.save('testrgb.png')


# # Dit is om je data te vernieuwen
# names = MDCreator()
# names.setAllData()
#run algoritme
path = MAlgorithmm()
nap = 5
count=0

path.depthLocator(nap) 
print(len(obj))
# #Dit is om het pad te tekenen
draw = MapCreator()
draw.drawPath()