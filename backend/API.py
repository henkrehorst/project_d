from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from threading import Thread
import datetime
import json

import db
from Calculator import Calculation

app = Flask(__name__)
api = Api(app)


class data(Resource):
    def get(self):
        line = db.getData()
        dic = {
            line[0][0]: {
                "id": line[0][0],
                "location": line[0][1],
                "upperright": line[0][2],
                "lowerleft": line[0][3],
                "centercoordinate": line[0][4],
                "link": line[0][5]},
            line[1][0]: {
                "id": line[1][0],
                "location": line[1][1],
                "upperright": line[1][2],
                "lowerleft": line[1][3],
                "centercoordinate": line[1][4],
                "link": line[1][5]}
        }

        return jsonify(dic)


class History(Resource):
    def get(self, duneId):
        data = db.getHistory(duneId)

        returnData = []

        for line in data:
            dic = {
                "Id": line[0],
                "Name": line[1],
                "Link": line[2],
                "TopCoordinate": line[3],
                "BottomCoordinate": line[4],
                "DuneLocation": line[5]
            }
            returnData.append(dic)
        return returnData


class Image(Resource):
    def get(self, imgId):
        data = db.getOneCal(imgId)

        dic = {
            "Id": data[0][0],
            "Name": data[0][1],
            "Link": data[0][2],
            "TopCoordinate": data[0][3],
            "BottomCoordinate": data[0][4],
            "DuneLocation": data[0][5]
        }

        return jsonify(dic)


class Algorithm(Resource):
    def post(self):
        data = request.get_json()

        dt = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        name = str(data["locatie"]) + " " + dt

        imgId = db.insertAlgo(data['locatieId'], name)

        thread = Thread(target=Calculation, args=(data, name, imgId))

        thread.daemon = True
        thread.start()

        return jsonify({'imageid': imgId})


@app.after_request
def disableCors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


api.add_resource(data, "/data")
api.add_resource(History, "/history/<int:duneId>")
api.add_resource(Image, "/image/<int:imgId>")
api.add_resource(Algorithm, "/algorithm")

if __name__ == "__main__":
    app.run(debug=True)
