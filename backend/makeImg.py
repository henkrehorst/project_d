from squareMaker import makeSquare
import filterCoords as fc
import algo
    
def Image(data, name):
    #Make a square from the 2 given points
    square = makeSquare(data["punt_a"]["x"],data["punt_a"]["y"],data["punt_b"]["x"],data["punt_b"]["y"],data["breedte"])

    #Convert lose coordinates to points
    l1 = fc.Point(square["left1"]["x"], square["left1"]["y"])
    l2 = fc.Point(square["left2"]["x"], square["left2"]["y"])
    r1 = fc.Point(square["right1"]["x"], square["right1"]["y"])
    r2 = fc.Point(square["right2"]["x"], square["right2"]["y"])

    #Create a tuple with the starting points
    startingPoints = (fc.Point(data["punt_a"]["x"],data["punt_a"]["y"]), fc.Point(data["punt_b"]["x"],data["punt_b"]["y"]))

    #Get a tuple with starting points and the array with heights that are needed
    #ToDo: path
    tp = fc.RunFilterOutput2DArray(data["locatie"]+ ".xyz", './', l1.x, l1.y, l2.x, l2.y, r1.x, r1.y, r2.x, r2.y, startingPoints)

    #First make an array and then convert the array to an image
    imgArr = algo.algorithm(tp[0], 4, tp[1][0])
    algo.makeImage(imgArr,name)

    return (0,0) #ToDo: give here the corner points