from numpy.core.records import array
import filterCoords as fc
import squareMaker as sm

def straightSquare(square):
    #check highest and lowest y
    lowY = square["left1"]["y"]
    if lowY > square["left2"]["y"]:
        lowY = square["left2"]["y"]
    if lowY > square["right1"]["y"]:
        lowY = square["right1"]["y"]
    if lowY > square["right2"]["y"]:
        lowY = square["right2"]["y"]

    highY = square["left1"]["y"]
    if highY < square["left2"]["y"]:
        highY = square["left2"]["y"]
    if highY < square["right1"]["y"]:
        highY = square["right1"]["y"]
    if highY < square["right2"]["y"]:
        highY = square["right2"]["y"]
    
    #check highest and lowest x
    lowX = square["left1"]["x"]
    if lowX > square["left2"]["x"]:
        lowX = square["left2"]["x"]
    if lowX > square["right1"]["x"]:
        lowX = square["right1"]["x"]
    if lowX > square["right2"]["x"]:
        lowX = square["right2"]["x"]

    highX = square["left1"]["x"]
    if highX < square["left2"]["x"]:
        highX = square["left2"]["x"]
    if highX < square["right1"]["x"]:
        highX = square["right1"]["x"]
    if highX < square["right2"]["x"]:
        highX = square["right2"]["x"]
    
    array = [[fc.Point(lowX,highY,10000) for x in range(int(highX - lowX))] for y in range(int(highY - lowY))]
    print(len(array))
    print(len(array[0]))
    return array

def fillSquare(array, filter, file):
    startX = array[0][0].x
    startY = array[0][0].y
    i = 0
    while i < len(array):
        y = startY - i
        j = 0
        while j < len(array[i]):
            x = startX + j
            array[i][j].x = x
            array[i][j].y = y
            j += 1
        i += 1

    pointAmount = 0
    print("Reading file...")
    reader = open(file, 'r')

    for line in reader:
        i = 0
        x = 0
        y = 0
        z = 0
        for elem in line.strip().split(" "):
            i+= 1
            if i % 3 == 1:
                x = float(elem)
            if i % 3 == 2:
                y = float(elem)
            if i % 3 == 0:
                z = float(elem)
        point = fc.Point(x,y,z)
        if filter.withinQuadrilateral(point):
            pointAmount += 1
            array[int(startY - point.y)][int(startX - point.x)] = fc.Point(point.x, point.y,round(point.height, 2))
    
    return array



square = sm.makeSquare(52610.5,427702.5,52685.5,427284.5)

left1 = fc.Point(square["left1"]["x"], square["left1"]["y"])
left2 = fc.Point(square["left2"]["x"], square["left2"]["y"])
right1 = fc.Point(square["right1"]["x"], square["right1"]["y"])
right2 = fc.Point(square["right2"]["x"], square["right2"]["y"])

filter = fc.QuadrilateralFilter(left1,left2,right1,right2)

arr = straightSquare(square)

arr2 = fillSquare(arr,filter, "goeree.xyz")

print(square)