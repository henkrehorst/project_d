from GetPoints import straightSquare
from numpy.core.records import array
import filterCoords as fc

def heightNumber(height, waterLevel):
    return 0


def algorithm(arr, waterLevel, startingPoint):
    
    imgArray = [[0 for x in range(len(arr))] for y in range(len(arr[0]))]
    ToCheck = []

    startX = startingPoint.x - arr[0][0].x
    startY = arr[0][0].y - startingPoint.y
    
    ToCheck.append([startX,startY])

    while len(ToCheck) > 0:
        x = ToCheck[0][0]
        y = ToCheck[0][1]
        
        #check left
        if x - 1 > 0:
            if filter.withinQuadrilateral(arr[y][x-1]):
                imgArray[y][x-1] = heightNumber(arr[y][x-1].height, waterLevel)

        #check right
        if x + 1 < len(arr[y]):
            if filter.withinQuadrilateral(arr[y][x+1]):
                imgArray[y][x+1] = heightNumber(arr[y][x-1].height, waterLevel)
        
        #check under
        if y + 1 < len(arr):
            if filter.withinQuadrilateral(arr[y+1][x]):
                imgArray[y+1][x] = heightNumber(arr[y][x-1].height, waterLevel)
        
        #check above
        if y - 1 > 0:
            arr[y-1][x]





    # i = 0

    # while i < len(arr):
    #     j = 0
    #     while j < len(arr[i]):
    #         x = arr[i][j].x
    #         y = arr[i][j].y
    #         z = arr[i][j].z
    #         point = fc.Point(x,y,z)
    #         if filter.withinQuadrilateral(point):
    #             measurement = waterLevel // 3
    #             if z <= measurement:
    #                 imgArray[i][j] = 3
    #             elif z > measurement and z <= (measurement * 2):
    #                 imgArray[i][j] = 2
    #             elif z > (measurement * 2) and z < waterLevel:
    #                 imgArray[i][j] = 1