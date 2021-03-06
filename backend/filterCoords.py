#!/bin/python3
import csv
import numpy
import math
from PIL import Image as im


class Point:
    def __init__(self, x, y, height=-9999):
        self.x = x
        self.y = y
        self.height = height


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

    # Calculates the length of the line with pythagoras formula
    def CalculateLength(self):
        if self.p1.x > self.p2.x:
            xDiff = self.p1.x - self.p2.x
        else:
            xDiff = self.p2.x - self.p1.x
        if self.p1.y > self.p2.y:
            yDiff = self.p1.y - self.p2.y
        else:
            yDiff = self.p2.y - self.p1.y
        edgeLength = math.sqrt(xDiff ** 2 + yDiff ** 2)
        return edgeLength

    # Returns y value for given X
    def GetYForX(self, x):
        diffX = x - self.p1.x
        moveY = diffX * self.CalculateSlope()
        return self.p1.y + moveY

    def GetXForY(self, y):
        diffY = y - self.p1.y
        moveX = diffY / self.CalculateSlope()
        return moveX + self.p1.x

    # calculates inDtersection point of line 90 degrees from this edge of a given point
    # Takes as input the corner edge
    # ONLY WORKS FROM THE BOTTOM EDGE
    # GIVE LEFT EDGE AS INPUT
    def IntersectionPointHorizontal(self, point, edge):
        xModifier = point.x - edge.p1.x
        xValue = xModifier * (1 + abs(self.slope))
        xValue += self.p1.x
        yValue = self.GetYForX(xValue)
        # print((xValue, yValue))
        input()
        return (xValue, yValue)

    # MADE FOR THE LEFT EDGE
    # GIVE BOTTOM EDGE AS INPUT
    def IntersectionPointVertical(self, point, edge):
        yModifier = point.y - edge.p1.y
        yValue = yModifier * (1 + abs(self.slope))
        yValue += self.p1.y
        xValue = self.GetXForY(yValue)
        input()
        return (xValue, yValue)


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

    # Gets width and height of a numpy array
    def getProportions(self):
        values = self.getMinMaxValues()
        yMinDif = values[3] - int(values[3])
        if yMinDif > 0 and yMinDif <= 0.5:
            return [int(values[0] - values[1]), (math.ceil(values[2] - values[3])+1)]
        else:
            return [int(values[0] - values[1]), math.ceil(values[2] - values[3])]


# x and y is the array position, realx and realy are the actual coordinates from the xyz file
class MauricePoint:
    def __init__(self, height, realx, realy, x, y, isPoint):
        self.height = height
        self.isPoint = isPoint
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
            "x": int(point.x - minMaxValues[1]),
            "y": int(point.y - minMaxValues[3])
        }
        return coordinates

    def addPoint(self, mauricePoint):
        self.arr[mauricePoint.x, mauricePoint.y] = mauricePoint
        return

    def fillEmptyArrayPoints(self):
        for x in range(0, self.arr.shape[0]):
            for y in range(0, self.arr.shape[1]):
                if self.arr[x, y] == None:
                    self.arr[x, y] = MauricePoint(-9999, 0, 0, x, y, False)


def RunFilterOutput2DArray(xyzFile, workingFolder, left1x, left1y, left2x, left2y, right1x, right1y, right2x, right2y,
                           startingPoints):
    filePath = workingFolder + xyzFile
    xyzFileHandle = open(filePath, 'r')

    left1 = Point(left1x, left1y)
    left2 = Point(left2x, left2y)
    right1 = Point(right1x, right1y)
    right2 = Point(right2x, right2y)

    qFilter = QuadrilateralFilter(left1, left2, right1, right2)
    output2DArray = TwoDimensionalXYZArray(qFilter)

    # Calculate the starting indexes
    startingIndexes = (
    output2DArray.coordinateToIndex(startingPoints[0]), output2DArray.coordinateToIndex(startingPoints[1]))

    i = 0
    for line in xyzFileHandle:
        for val in line.strip().split(" "):
            i += 1
            if i % 3 == 1:
                x = float(val)
            if i % 3 == 2:
                y = float(val)
            if i % 3 == 0:
                tempPoint = Point(x, y, val)
                if qFilter.withinQuadrilateral(tempPoint):
                    indexValues = output2DArray.coordinateToIndex(tempPoint)
                    tempMauricePoint = MauricePoint(val, x, y, indexValues["x"], indexValues["y"], True)
                    output2DArray.addPoint(tempMauricePoint)

    output2DArray.fillEmptyArrayPoints()
    csvOutputArr = numpy.empty((output2DArray.arr.shape[0], output2DArray.arr.shape[1]), dtype=float)

    for col in output2DArray.arr:
        for mp in col:
            csvOutputArr[mp.x, mp.y] = float(mp.height)

    return csvOutputArr, startingIndexes
