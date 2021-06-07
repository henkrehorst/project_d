from filterCoords import RunFilterOutput2DArray
from squareMaker import makeSquare
import random
from PIL import Image
import numpy as np

def MakeArray():
    y = random.randint(100,200)
    heightArray = [[0 for x in range(40)] for y in range(400)]

    i = 0
    while i < len(heightArray):
        j = 0
        while j < len(heightArray[i]):
            heightArray[i][j] = random.randint(0,10)
            j = j+1
        i = i+1
    return heightArray

def Algorithm(Array, waterHeight):
    # This will be the array that will become the image
    imgArray = [[0 for x in range(len(Array[0]))] for y in range(len(Array))]

    # This list is for checking the next set of notes
    ToCheck = []

    # This will give us the first row to check
    i = 0
    while i < len(Array[0]):
        if Array[0][i] < waterHeight:
            ToCheck.append(i)
            imgArray[0][i] = 1
        i = i+1

    # Check the other lines then the first one
    j = 0
    while j < len(Array):
        
        i = 0
        nextArr = []
        while i < len(ToCheck):
            
            left = ToCheck[i] - 1

            # Check to left of the node that is lower
            if left > 0:
                if left not in ToCheck:
                    if Array[j][left] < waterHeight:
                        ToCheck.append(left)
                        imgArray[j][left] = waterHeight - Array[j][left]
            
            # Check to the right of the node that is lower
            right = ToCheck[i] + 1
            if right < len(Array[j]):
                if right not in ToCheck:
                    if Array[j][right] < waterHeight:
                        ToCheck.append(right)
                        imgArray[j][right] = waterHeight - Array[j][right]
            
            # Check the next node
            above = j+1
            if above < len(Array):
                if Array[above][ToCheck[i]] < waterHeight:
                    nextArr.append(ToCheck[i])
                    imgArray[above][ToCheck[i]] = waterHeight - Array[above][ToCheck[i]]

            i = i+1
        j = j+1
        ToCheck = nextArr

    return imgArray

def makeImage(Array, checkHeigth):
    # Make the array needed to convert it later to a image
    arr = np.zeros([len(Array),len(Array[0]), 4], dtype=np.uint8)
    i = 0
    check = checkHeigth / 3
    # This will give the right values within the array
    while i < len(Array):
        j = 0
        while j < len(Array[i]):
            if Array[i][j] == 0:
                arr[i][j] = [57, 255, 20,100]
            if Array[i][j] > 0 and Array[i][j] < check:
                arr[i,j] = [255, 255, 0,100] # Yellow
            if Array[i][j] >= check and Array[i][j] < (check * 2):
                arr[i,j] =  [255, 165, 0,100] # Orange
            if Array[i][j] >= (check * 2):
                arr[i,j] = [255, 0, 0,100] # Red
            j = j+1
        i = i+1

    # Convert the array to image and save it
    image = Image.fromarray(arr)
    image.save('test.png')

checkHeigth = 8
# Make a dummy array
heightArray = MakeArray()
# Call the algorithm. Give an 2d array and the waterheight
arr = Algorithm(heightArray, checkHeigth)
# Create the image based on array made by the algorithm
makeImage(arr, checkHeigth)
