from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Testing(Resource):
    def get(self):
        return "Hello World!"

api.add_resource(Testing, "/testing")

if __name__ == "__main__":
    app.run(debug=True)