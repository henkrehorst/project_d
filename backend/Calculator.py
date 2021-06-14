import makeImg
import blobService
import db
from os import popen

def Calculation(data, name, imgId):
    #Make image
    imgName = name.replace(" ","")
    imgName = imgName.replace('/', '')
    imgName = imgName.replace(':', '')
    
    cornerpoints = makeImg.Image(data, imgName)

    #upload image to blob storage
    link = blobService.Upload(imgName)
    #ToDo: remove image after uploading
    rmLine = 'rm ' + imgName + '.png'
    popen(rmLine)
    #Update database
    a = db.updateAlgo(link, str(cornerpoints[0][0]) + ","+str(cornerpoints[0][1]), str(cornerpoints[1][0]) + ","+str(cornerpoints[1][1]), imgId)
    print(a)
