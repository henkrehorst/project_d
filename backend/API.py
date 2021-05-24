from flask import Flask
from flask_restful import Api, Resource
from squareMaker import makeSquare

app = Flask(__name__)
api = Api(app)

class Algorithm(Resource):
    def get(self,filename,coordinates):
        XCoordinate1 = float(coordinates.split('-')[0].split('_')[0])
        YCoordinate1 = float(coordinates.split('-')[0].split('_')[1])
        XCoordinate2 = float(coordinates.split('-')[1].split('_')[0])
        YCoordinate2 = float(coordinates.split('-')[1].split('_')[1])

        return {"Filename": filename, "Square": makeSquare(XCoordinate1,YCoordinate1,XCoordinate2,YCoordinate2)}

api.add_resource(Algorithm, "/algorithm")

if __name__ == "__main__":
    app.run(debug=True)

