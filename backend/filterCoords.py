#!/bin/python3
import csv
import numpy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Contains both points, and the slope value (how many +Y for +1X)
class Edge:
    def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.slope = self.CalculateSlope()

    def CalculateSlope(self):
        xDiff = self.p1.x - self.p2.x
        yDiff = self.p1.y - self.p2.y
        return yDiff / xDiff

    # Returns y value for given X
    def GetYForX(self, x):
        diffX = x - self.p1.x
        moveY = diffX * self.slope
        return self.p1.y + moveY

    def GetXForY(self, y):
        diffY = y - self.p1.y
        moveX = diffY / self.slope
        return moveX + self.p1.x

# Takes 4 points as input, simulates a quadrilateral, and provides functionality to check whether a point appears within this quadrilateral
class QuadrilateralFilter:
    def __init__(self, left1, left2, right1, right2):
        self.left1 = left1
        self.left2 = left2
        self.right1 = right1
        self.right2 = right2 

        self.topEdge = Edge(self.left1, self.right1)
        self.bottomEdge = Edge(self.left2, self.right2)
        self.leftEdge = Edge(self.left2, self.left1)
        self.rightEdge = Edge(self.right2, self.right1)

    # Takes point as input, returns True if it appears in this rectangle
    def withinQuadrilateral(self, p):
        if self.topEdge.GetYForX(p.x) < p.y:
            return False
        if self.bottomEdge.GetYForX(p.x) > p.y:
            return False
        if self.leftEdge.GetXForY(p.y) > p.x:
            return False
        if self.rightEdge.GetXForY(p.y) < p.x:
            return False
        return True

    # Gets width and height of a numpy array
    def getProportions(self):
    	values = self.getMinMaxValues()
    	return [int(values[0] - values[1]), int(values[2] - values[3])]

    # returns minimum and maximum x and y values
    def getMinMaxValues(self):
    	if self.left1.x > self.left2.x:
    		leftXValue = self.left2.x
    	else:		
    		leftXValue = self.left1.x

    	if self.right1.x > self.right2.x:
    		rightXValue = self.right1.x
    	else:
    		rightXValue = self.right2.x

    	if self.left1.y > self.right1.y:
    		topYValue = self.left1.y
    	else:
    		topYValue = self.right1.y

    	if self.left2.y < self.right2.y:
    		botYValue = self.left2.y
    	else:
    		botYValue = self.right2.y

    	return [rightXValue, leftXValue, topYValue, botYValue]

# x and y is the array position, realx and realy are the actual coordinates from the xyz file
class MauricePoint:
	def __init__(self, height, realx, realy, x, y, RGB):
		self.height = height
		self.RGB = RGB
		self.x = x
		self.y = y
		self.point = Point(realx, realy)

class TwoDimensionalXYZArray:
	def __init__(self, QFilter):
		self.QFilter = QFilter
		self.arr = self.createArray()

	def createArray(self):
		proportions = self.QFilter.getProportions()
		return numpy.empty((proportions[0], proportions[1]), dtype=MauricePoint)

	def coordinateToIndex(self, point):
		minMaxValues = self.QFilter.getMinMaxValues()
		coordinates = {
			"x" : int(point.x - minMaxValues[1]),
			"y" : int(point.y - minMaxValues[3])
		}
		return coordinates

	def addPoint(self, mauricePoint):
		self.arr[mauricePoint.x, mauricePoint.y] = mauricePoint
		return

	def fillEmptyArrayPoints(self):
		for x in range(0, self.arr.shape[0]):
			for y in range(0, self.arr.shape[1]):
				if self.arr[x,y] == None:
					self.arr[x,y] = MauricePoint(-9999, 0, 0, x, y, '#FFFFFF')


def RunFilterOutput2DArray(xyzFile, workingFolder, left1x, left1y, left2x, left2y, right1x, right1y, right2x, right2y):
	filePath = workingFolder + xyzFile
	xyzFileHandle = open(xyzFile, 'r')

	left1 = Point(left1x, left1y)
	left2 = Point(left2x, left2y)
	right1 = Point(right1x, right1y)
	right2 = Point(right2x, right2y)

	qFilter = QuadrilateralFilter(left1, left2, right1, right2)
	output2DArray = TwoDimensionalXYZArray(qFilter)

	i = 0
	for line in xyzFileHandle:
		for val in line.strip().split(" "):
			i+= 1
			if i % 3 == 1:
				x = float(val)
			if i % 3 == 2:
				y = float(val)
			if i % 3 == 0:
				tempPoint = Point(x,y)
				if qFilter.withinQuadrilateral(tempPoint):
					indexValues = output2DArray.coordinateToIndex(tempPoint)
					tempMauricePoint = MauricePoint(val, x, y, indexValues["x"], indexValues["y"], "#000000")
					output2DArray.addPoint(tempMauricePoint)
	output2DArray.fillEmptyArrayPoints()
	return output2DArray.arr


# Here we parse through each line of the original XYZ file, test if its point is in the quadrilateral, and if it does we add it to the new xyz file
def RunFilter(oldFile, left1x, left1y, right1x, right1y, right2x, right2y, left2x, left2y):
    originalXyzFile = oldFile
    newXyzFile = "new" + oldFile[:-3] + "csv"

    fhandle = open(originalXyzFile, 'r')
    filteredXyz = open(newXyzFile, 'w')
    filteredXyzWriter = csv.writer(filteredXyz)


    left1 = Point(left1x, left1y)
    left2 = Point(left2x, left2y)
    right1 = Point(right1x, right1y)
    right2 = Point(right2x, right2y)

    qFilter = QuadrilateralFilter(left1, left2, right1, right2)

    i = 0
    for line in fhandle:
        for val in line.strip().split(" "):
            i+= 1
            if i % 3 == 1:
                x = float(val)
            if i % 3 == 2:
                y = float(val)
            if i % 3 == 0:
                tempPoint = Point(x,y)
                if qFilter.withinQuadrilateral(tempPoint):
#                    filteredXyz.write(str(tempPoint.x) + " " + str(tempPoint.y) + " " + str(val) + "\n")
                    filteredXyzWriter.writerow([str(tempPoint.x), str(tempPoint.y), str(val)])
    return newXyzFile