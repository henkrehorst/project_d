def makeSquare(coor1x, coor1y, coor2x, coor2y, breedte):
    yGrowth = -1*((coor2x - coor1x) / (coor2y - coor1y))
    
    x = 0
    y = 0

    while (breedte*breedte) > (x*x) + (y*y):
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