"""
Needed to create a json file to be saved locally to grab the
"""

import json


class JsonWorker:

    def __init__(self, save_loc: str):
        self.save_location = save_loc

    def write_json(self, content: dict):
        json_dict = json.dumps(content, indent=4)
        with open(self.save_location, 'w') as file:
            file.write(json_dict)

    @staticmethod
    def read_json(json_loc):
        with open(json_loc, "r") as json_file:
            json_elements = json.load(json_file)
        return json_elements
