import os
import json
from flask import request
from flask_restful import Resource

DATA_DIR = "dropin_data/"

def dropin_list():
    dropins = []

    for dropin in os.listdir(DATA_DIR):
        dropins.append(dropin)

    return dropins

class GetHelp(Resource):
    # same help setup as etl-service: list out available data
    def get(self):
        return {"data_files": dropin_list()}

class ManageData(Resource):
    # retrieve data that we've already stored
    def get(self, filename):
        
        data_path = f"{DATA_DIR}{filename}.json"

        # check for dropin
        if not os.path.isfile(data_path):
            return {"error": f"No data for {filename} found."}

        data_list = {}
        full_result = {}
        with open(data_path) as data_file:
            data_list = json.load(data_file)

        full_result["count"] = len(data_list)
        full_result["elements"] = data_list

        return full_result

    # etl-service is sending us some new data to store
    def post(self, filename):
        
        data_path = f"{DATA_DIR}{filename}.json"

        if request.json is None:
            return {"error": "Post request requires data of type application/json"}

        json_data = request.get_json()
        data_str = json.dumps(json_data, indent=4)

        # we will overwrite the file currently at this path;
        # we can always specify an "append" name from the etl-service side to create a unique name
        # we just probably don't want to endlessly accumulate queries
        with open(data_path, "w") as data_file:
            data_file.write(data_str)

        return {"message": f"Data saved to {data_path}"}
        