from os import path
import json

def get_json_from_file(file_name):
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "../Conf", file_name + ".json"))
    with open(filepath) as file:
        return json.load(file)


class Configurator:
    def __init__(self):
        self.ships = get_json_from_file("ships")
        
