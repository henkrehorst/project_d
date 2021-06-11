from flask import Flask, request
from flask_restful import Api, Resource
from subprocess import Popen
from threading import Thread
import datetime
import json

import db
from Calculator import Calculation

app = Flask(__name__)
api = Api(app)


class data(Resource):
    def post(self, duration):
        dbData = db.getData()
        dic = {
            "loc1": {
            "id": line[0][0]
            "location": line[0][1]
            "upperright": line[0][2]
            "lowerleft": line[0][3]
            "centercoordinate": line[0][4]
            "link": line[0][5]},
            "loc2": {
            "id": line[1][0]
            "location": line[1][1]
            "upperright": line[1][2]
            "lowerleft": line[1][3]
            "centercoordinate": line[1][4]
            "link": line[1][5]}
            }
        

        return jsonify(dic)

class Algorithm(Resource):
    def post(self):
        data = json.loads(request.get_json())

        dt = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        name = str(data["locatie"]) + " " + dt

        imgId = db.insertAlgo(data['locatieId'], name)

        thread = Thread(target=Calculation, args=(data,name,imgId))
        
        thread.daemon = True
        thread.start()

        return imgId
        
        

api.add_resource(Algorithm, "/algorithm")
api.add_resource(thread, "/thread/<int:duration>")

if __name__ == "__main__":
    app.run(debug=True)

