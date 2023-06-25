import os
import json


def find_path_to_file(name_file):
    full_path = os.path.abspath(__file__ + "/..")
    full_path = full_path.split("\\")
    del full_path[-1]
    full_path = "/".join(full_path)
    full_path = os.path.join(full_path, name_file)
    return full_path
    

def create_json(name_json, name_dict):
    with open(find_path_to_file(name_file=name_json), "w") as file:
        json.dump(name_dict, file, indent=4, ensure_ascii=True)
        
def read_json(name_json):
    with open(find_path_to_file(name_json), "r") as file:
        data = json.load(file)
        return data
