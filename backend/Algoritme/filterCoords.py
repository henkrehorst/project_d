#!/bin/python3

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
        
originalXyzFile = 'goeree.xyz'
newXyzFile = 'newGoeree2.xyz'

fhandle = open(originalXyzFile, 'r')

left1 = Point(55755.5, 429251.05294117646)
right1 = Point(55773.5, 429213.94705882354)
left2 = Point(52601.5, 427721.05294117646)
right2 = Point(52619.5, 427683.94705882354)

qFilter = QuadrilateralFilter(left1, left2, right1, right2)

filteredXyz = open(newXyzFile, 'w')

# Here we parse through each line of the original XYZ file, test if its point is in the quadrilateral, and if it does we add it to the new xyz file
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
                filteredXyz.write(str(tempPoint.x) + " " + str(tempPoint.y) + " " + str(val) + "\n")
