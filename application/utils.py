import json

def read_json(json_filepath:str)->dict:
    with open(json_filepath) as secret:
        json_info=json.load(secret)
    return json_info