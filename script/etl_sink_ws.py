from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from etl_endpoints import ManageData, GetHelp

# initialize web service!
if __name__ == '__main__':
    # Flask setup
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    # add service's endpoints
    api.add_resource(ManageData, '/etl/<string:filename>')
    api.add_resource(GetHelp, '/help')

    # start things up on localhost:3514
    app.run(host='0.0.0.0', port=3514)  
