import json
import numpy as np
from PIL import Image
import filterCoords



#newdataload
xyzFile = open('goeree.xyz','r')
xyzData = xyzFile.read()
xyzFile.close()
TwoDArr = filterCoords.RunFilterOutput2DArray(xyzData, "./", 52590.5, 427698.9114832536, 52665.5, 427280.9114832536, 52630.5, 427706.0885167464, 52705.5, 427288.0885167464)
lengthy = TwoDArr.shape[0]
widthx = TwoDArr.shape[1]

#read file and parse Library
myLibrary = open('tiffdatawl2.json','r')
myData = myLibrary.read()
myLibrary.close()
obj = json.loads(myData)

class DataConv:
    def setAllData(self):
        obj = []
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


class MauAlg:
    def iteratieAlg(self, nap):
        count = 0
        for _ in obj:
            if float(obj[count]["Z"]) < nap:
                obj[count]["RGB"] = "#0000FF"
                print(obj[count])
            count+=1    

class MapDrawing:
    def drawPath(self, nap):
        array = np.zeros([lengthy, widthx, 4], dtype=np.uint8)
        array[:,:] = [248, 213, 104, 20] #Sandy backside #Transparent
    
        count =0
        for _ in obj:
            if str(obj[count]["Z"]) == "-9999":
                array[obj[count]["X"],obj[count]["Y"]] = [55, 102, 246, 90] #blue
            elif obj[count]["RGB"] == "#0000FF" and str(obj[count]["Z"]) != -9999 and nap - float(obj[count]["Z"]) > 2:
                array[obj[count]["X"],obj[count]["Y"]] = [255, 0, 0, 90] #red
            elif obj[count]["RGB"] == "#0000FF" and str(obj[count]["Z"]) != -9999 and nap - float(obj[count]["Z"]) > 1:
                array[obj[count]["X"],obj[count]["Y"]] = [255, 165, 0, 90] #orange
            elif obj[count]["RGB"] == "#0000FF" and str(obj[count]["Z"]) != -9999 and nap - float(obj[count]["Z"]) <= 1:
                array[obj[count]["X"],obj[count]["Y"]] = [255, 255, 0, 90] #yellow
            
            count+=1
        img = Image.fromarray(array)
        img.save('testrgb.png')

class GetRealCoords:
    def getRealCoords(self):
        print(str(TwoDArr[0,0].point.x) + " " + str(TwoDArr[0,0].point.y)
        +"\n"+str(TwoDArr[0,widthx-1].point.x) + " " + str(TwoDArr[0,widthx-1].point.y)
        +"\n"+str(TwoDArr[lengthy-1,0].point.x) + " " + str(TwoDArr[lengthy-1,0].point.y)
        +"\n"+str(TwoDArr[lengthy-1,widthx-1].point.x) + " " + str(TwoDArr[lengthy-1,widthx-1].point.y))

createdata = DataConv()
createdata.setAllData()
nap = 2 
depths = MauAlg()
depths.iteratieAlg(nap)
start = 0
drawmap = MapDrawing()
drawmap.drawPath(nap)
getrealcoords = GetRealCoords() #De coordinaten worden nog niet goed meegegeven (roep ik ze verkeerd aan of niet goed meegegeven in de 2DArray@Kasper)
getrealcoords.getRealCoords()