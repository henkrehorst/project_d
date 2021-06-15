from squareMaker import makeSquare
import filterCoords as fc
import algo
import convert_coordinates as cc

def MinValues(xLine, yLine):
    xmin = xLine[0]
    ymin = yLine[0]

    for x in xLine:
        if x < xmin:
            xmin = x
    
    for y in yLine:
        if y < ymin:
            ymin = y
    return (xmin, ymin)
    
def Image(data, name):
    #Make a square from the 2 given points
    point1 = cc.convertWGS84toRD(data["punt_a"]["x"],data["punt_a"]["y"])
    point2 = cc.convertWGS84toRD(data["punt_b"]["x"],data["punt_b"]["y"])

    square = makeSquare(point1[0],point1[1],point2[0],point2[1],data["breedte"])

    #Convert lose coordinates to points
    if square['left1']['y'] > square["left2"]["y"]:
        l1 = fc.Point(square["left1"]["x"], square["left1"]["y"])
        l2 = fc.Point(square["left2"]["x"], square["left2"]["y"])
        r1 = fc.Point(square["right1"]["x"], square["right1"]["y"])
        r2 = fc.Point(square["right2"]["x"], square["right2"]["y"])
    else:
        l2 = fc.Point(square["left1"]["x"], square["left1"]["y"])
        l1 = fc.Point(square["left2"]["x"], square["left2"]["y"])
        r2 = fc.Point(square["right1"]["x"], square["right1"]["y"])
        r1 = fc.Point(square["right2"]["x"], square["right2"]["y"])

    #Create a tuple with the starting points
    startingPoints = (fc.Point(point1[0],point1[1]), fc.Point(point2[0],point2[1]))

    #Get a tuple with starting points and the array with heights that are needed
    tp = fc.RunFilterOutput2DArray(data["locatie"]+ ".xyz", './', l1.x, l1.y, l2.x, l2.y, r1.x, r1.y, r2.x, r2.y, startingPoints)

    #First make an array and then convert the array to an image
    imgArr = algo.algorithm(tp[0], data['waterlevel'], tp[1])
    
    minValues = MinValues([square["left1"]["x"],square["left2"]["x"],square["right1"]["x"],square["right2"]["x"]],[square["left1"]["y"],square["left2"]["y"],square["right1"]["y"],square["right2"]["y"]])

    arrTemp = []
    i = len(imgArr)-1
    while i >= 0:
        arrTemp.append(imgArr[i])
        i -= 1
    imgArr = arrTemp
    lowLeft = (minValues[0], minValues[1])
    upperRight = (minValues[0]+len(imgArr[0]), minValues[1] + len(imgArr))

    algo.makeImage(imgArr,name)
    
    lowLeft = cc.convertRDtoWGS84(lowLeft[0],lowLeft[1])
    upperRight = cc.convertRDtoWGS84(upperRight[0],upperRight[1])

    return (lowLeft,upperRight) #ToDo: give here the corner points