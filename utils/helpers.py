import json

def elements_to_json(elements):
    element_dict = [el.to_dict() for el in elements]
    return json.dumps(element_dict, indent=2)
