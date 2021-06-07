#!/bin/python3
import csv
import numpy
import math

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
		edgeLength = math.sqrt(xDiff**2 + yDiff**2)
		print("Edge length: " + str(math.ceil(edgeLength)))
		return edgeLength


	# Returns y value for given X
	def GetYForX(self, x):
		diffX = x - self.p1.x
		moveY = diffX * self.CalculateSlope()
		print()
		print(self.p1.x)
		print(x)
		print("difference X: " + str(diffX) + " = " + str(x)+ " - " + str(self.p1.x))
		print("Move Y: " + str(moveY) + " = "+ str(diffX) + " * " + str(self.slope))
		print("Y value for X: " + str(self.p1.y+moveY))
		print()
		return self.p1.y + moveY

	def GetXForY(self, y):
		diffY = y - self.p1.y
		moveX = diffY / self.CalculateSlope()
		return moveX + self.p1.x

	# calculates intersection point of line 90 degrees from this edge of a given point
	# Takes as input the corner edge
	# ONLY WORKS FROM THE BOTTOM EDGE
	# GIVE LEFT EDGE AS INPUT
	def IntersectionPoint(self, point, edge):
		# return Point(0, intersectionPointY)
		xModifier = point.x - edge.p1.x  
		xValue = xModifier * (1 + abs(self.slope))
		yValue = self.GetYForX(xValue)
		print(xValue, yValue)
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
		# check = False
		if self.topEdge.GetYForX(p.x) < p.y:
			# if check:
			# 	print(self.topEdge.GetYForX(p.x), p.y)
			return False
		if self.bottomEdge.GetYForX(p.x) > p.y:
			# if check:
			# 	print(self.bottomEdge.GetYForX(p.x), p.y)
			return False
		if self.leftEdge.GetXForY(p.y) > p.x:
			# print(self.leftEdge.GetXForY(p.y), p.x)
			return False
		if self.rightEdge.GetXForY(p.y) < p.x:
			# print(self.rightEdge.GetXForY(p.y), p.x)
			return False
		print('true')
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

class TwoDimensionalXYZArrayStraight:
	def __init__(self, QFilter):
		self.QFilter = QFilter
		self.arr = self.createArray()
		#self.fillArray(xyzFile)

	# Creates an empty numpy 2D array with the length and width of the edges	
	def createArray(self):
		# Calculates X and Y proportions for the array
		proportions = {
			"x" : self.QFilter.bottomEdge.CalculateLength(), 
			"y" : self.QFilter.rightEdge.CalculateLength()
			}
		return numpy.empty((int(proportions["x"]), int(proportions["y"])), dtype=float)

	# Fills the array with the values inside of the .xyz file
	def fillArray(self, xyzFile):
		# calculate length from given point in pointlist to its edge
		offsetX = self.QFilter.left2.x
		offsetY = self.QFilter.left2.y
		print("OffsetX: ", str(offsetX))
		print("OffsetY: ", str(offsetY))
		xyzFileHandle = open(xyzFile, 'r')
		# Implement xyzFile class here
		i = 0
		for line in xyzFileHandle:
			for val in line.strip().split(" "):
				i+= 1
				if i % 3 == 1:
					x = float(val)
				if i % 3 == 2:
					y = float(val)
				if i % 3 == 0:
					point = Point(x,y,val)
					if self.QFilter.withinQuadrilateral(point):
						print("passed test")
						coords = self.QFilter.bottomEdge.IntersectionPoint(point, self.QFilter.leftEdge)
						if self.arr[int(round(coords[0])-offsetX), int(round(coords[1])-offsetY)] != None:
							input("collision found")
						self.arr[int(round(coords[0])-offsetX), int(round(coords[1])-offsetY)] = point.height
						print(point.height)
		print("Filled array succesfully")
		print("Writing text file..")
		numpy.savetxt("arr.csv", self.arr, delimiter=",")


class XYZFileHandler:
	def __init__(self, xyzFile):
		self.xyzFileHandle = open(xyzFile, 'r')

	def getPointList(self):
		pointList = []
		i = 0
		for line in self.xyzFileHandle:
			for val in line.strip().split(" "):
				i+= 1
				if i % 3 == 1:
					x = float(val)
				if i % 3 == 2:
					y = float(val)
				if i % 3 == 0:
					height = val
					tempPoint = Point(x, y, height)
					pointList.append(tempPoint)
		print(pointList[0].x, pointList[0].y)
		return pointList