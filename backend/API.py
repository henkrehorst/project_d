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


class thread(Resource):
    def post(self, duration):
        thread = Thread(target=threaded_task, args=(duration,))
        thread.daemon = True
        thread.start()
        return jsonify({'thread_name': str(thread.name),
                        'started': True})

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

