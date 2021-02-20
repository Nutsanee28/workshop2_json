import json

python_dict = {"name": "Nud&Pat", "age": 21, "city": "Chachoengsao"}

json_string = json.dumps(python_dict)

print(json_string)