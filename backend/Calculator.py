import makeImg
import blobService
import db

def Calculation(data, name, imgId):
    #Make image
    imgName = name.replace(" ","")
    imgName = imgName.replace('/', '')
    imgName = imgName.replace(':', '')
    
    cornerpoints = makeImg.Image(data, imgName)

    #upload image to blob storage
    link = blobService.Upload(imgName)

    #Update database
    a = db.updateAlgo(link, str(cornerpoints[0]), str(cornerpoints[1]), data["locatieId"])
    print(a)
