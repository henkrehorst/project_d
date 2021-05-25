from flask import Flask
from flask_restful import Api, Resource
from subprocess import Popen

from squareMaker import makeSquare
from filterCoords import RunFilter

app = Flask(__name__)
api = Api(app)

class Conversion(Resource):
    def get(self, filename):
        Process = Popen('conversion.sh %s' % (filename,), shell=True)

class Algorithm(Resource):
    def get(self,filename,coordinates):
        XCoordinate1 = float(coordinates.split('-')[0].split('_')[0])
        YCoordinate1 = float(coordinates.split('-')[0].split('_')[1])
        XCoordinate2 = float(coordinates.split('-')[1].split('_')[0])
        YCoordinate2 = float(coordinates.split('-')[1].split('_')[1])

        square = makeSquare(XCoordinate1,YCoordinate1,XCoordinate2,YCoordinate2)

        newfilename = RunFilter(filename, square["left1"]["x"],square["left1"]["y"],square["right1"]["x"],square["right1"]["y"],square["right2"]["x"],square["right2"]["y"],square["left2"]["x"],square["left2"]["y"])

        return {"Filename": newfilename}

api.add_resource(Algorithm, "/algorithm/<string:filename>/<string:coordinates>")

if __name__ == "__main__":
    app.run(debug=True)

