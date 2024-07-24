from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
class Health(Resource):
    def get(self):
        return {'status': 'healthy'}

api.add_resource(HelloWorld, '/')

api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')