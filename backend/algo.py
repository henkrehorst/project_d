from GetPoints import straightSquare
from numpy.core.records import array
from PIL import Image
import numpy as np

def heightNumber(height, waterLevel):
    niveau = waterLevel // 3

    #check if point exists
    if height == -9999:
        return 0
    #check if point is very low beneath the waterlevel
    elif height <= niveau:
        return 3
    #check if point is medium low beneath the waterlevel
    elif height > niveau and height <= (niveau*2):
        return 2
    #check if point is net very low beneath the waterlevel
    elif height > (niveau*2) and height <= waterLevel:
        return 1
    #height is above waterlevel
    else:
        return 0


def algorithm(arr, waterLevel, startingPoint):

    imgArray = [[-1 for x in range(len(arr))] for y in range(len(arr[0]))]
    ToCheck = []
    sp = [startingPoint["x"],startingPoint["y"]]
    
    #giving starting point right color
    sx = sp[0]
    sy = sp[1]
    level = heightNumber(arr[sx][sy], waterLevel)
    imgArray[sy][sx] = level
    
    ToCheck.append(sp)

    arr
    while len(ToCheck) > 0:
        x = ToCheck[0][0]
        y = ToCheck[0][1]
        
        #check left
        if x - 1 > 0 and imgArray[y][x-1] == -1:
            level = heightNumber(arr[x-1][y], waterLevel)
            imgArray[y][x-1] = level
            if level != 0:
                ToCheck.append([x-1,y])

        #check right
        if x + 1 < len(arr) and imgArray[y][x+1] == -1:
            level = heightNumber(arr[x+1][y], waterLevel)
            imgArray[y][x+1] = level
            if level != 0:
                ToCheck.append([x+1,y])
            
            #check under
        if y - 1 > 0 and imgArray[y-1][x] == -1:
            level = heightNumber(arr[x][y-1], waterLevel)
            imgArray[y-1][x] = level
            if level != 0:
                ToCheck.append([x,y-1])
            
        #check above
        if y + 1 < len(arr[x]) and imgArray[y+1][x] == -1:
            level = heightNumber(arr[x][y+1], waterLevel)
            imgArray[y+1][x] = level
            if level != 0:
                ToCheck.append([x,y+1])
        
        ToCheck.remove(ToCheck[0])
    return imgArray


def makeImage(Array):
    # Make the array needed to convert it later to a image
    arr = np.zeros([len(Array),len(Array[0]), 4], dtype=np.uint8)
    i = 0
    # This will give the right values within the array
    while i < len(Array):
        j = 0
        while j < len(Array[i]):
            if Array[i][j] == 0 or Array[i][j] == -1:
                arr[i][j] = [0, 0, 0, 0]
            if Array[i][j] == 1:
                arr[i,j] = [255, 255, 0,100] # Yellow
            if Array[i][j] == 2:
                arr[i,j] =  [255, 165, 0,100] # Orange
            if Array[i][j] == 3:
                arr[i,j] = [255, 0, 0,100] # Red
            j = j+1
        i = i+1

    # Convert the array to image and save it
    image = Image.fromarray(arr)
    image.save('test.png')