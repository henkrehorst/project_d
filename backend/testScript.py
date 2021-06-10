import filterCoords as fc
import algo
import squareMaker as sm
import requests
import json

# square = sm.makeSquare(52610.5,427702.5,52685.5,427284.5)

# l1 = fc.Point(square["left1"]["x"], square["left1"]["y"])
# l2 = fc.Point(square["left2"]["x"], square["left2"]["y"])
# r1 = fc.Point(square["right1"]["x"], square["right1"]["y"])
# r2 = fc.Point(square["right2"]["x"], square["right2"]["y"])

# startingPoints = (fc.Point(52610.5, 427702.5), fc.Point(52685.5, 427284.5))

# qF = fc.QuadrilateralFilter(l1, l2, r1, r2)
# tp = fc.RunFilterOutput2DArray('goeree.xyz', './', l1.x, l1.y, l2.x, l2.y, r1.x, r1.y, r2.x, r2.y, startingPoints)

# print("starting algo")
# imgArr = algo.algorithm(tp[0], 4, tp[1][0])

# algo.makeImage(imgArr)

# base = "http://127.0.0.1:5000/algorithm/gdal3.xyz/52610.5_427702.5-52685.5_427284.5"

dic = {
    "punt_a" : {
        "x": 52610.5,
        "y": 427702.5
    },
    "punt_b" : {
        "x": 52685.5,
        "y": 427284.5
    },
    "waterlevel" : 4,
    "breedte" : 100,
    "locatie" : "goeree",
    "locatieId" : 1
}

data = json.dumps(dic)

base = "http://127.0.0.1:5000/algorithm"
res = requests.post(base, json=data)
print(res)