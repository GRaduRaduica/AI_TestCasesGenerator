"""
needed to create a json file to be saved locally to grab the
"""

import json

class Json_Worker():

    def __init__(self, save_loc: str, dict_data: dict):
        self.save_location = save_loc
        self.content_json = dict_data

    def write_json(self):
        json_dict = json.dumps(self.content_json, indent=4)
        with open(self.save_location, 'w') as file:
            file.write(json_dict)

    @staticmethod
    def read_json(json_loc):
        with open(json_loc, "r") as json_file:
            json_elements = json.load(json_file)
        return json_elements
