import rasterio

#Makes a square of 2 coordinates (width = 40 meters)
def makeSquare(coor1x, coor1y, coor2x, coor2y):
    yGrowth = -1*((coor2x - coor1x) / (coor2y - coor1y))
    
    x = 0
    y = 0

    while 400 > (x*x) + (y*y):
        x += 1
        y += yGrowth

    SquareCorners = {
        "left1": {
            "x": coor1x - x,
            "y": coor1y - y
        },
        "right1": {
            "x": coor1x + x,
            "y": coor1y + y
        },
        "left2": {
            "x": coor2x - x,
            "y": coor2y - y
        },
        "right2": {
            "x": coor2x + x,
            "y": coor2y + y
        },
    }
    return SquareCorners


#Function needs location tiff file and encapsulated coordinates
def pathFinding(tiff, coor1x, coor1y, coor2x, coor2y):

    #Make square of coor1 and coor2
    square = makeSquare(coor1x, coor1y, coor2x, coor2y)

    #Get size between points
    

    #Get next point x,y,z (point must be in square)
        #Check if higher than water stand
        #Change color if higher
        #check point as done
    
print(makeSquare(55764.5, 429232.5, 52610.5, 427702.5))