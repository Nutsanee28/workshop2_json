import json

json_string = '{"name":"Nud&Pat","age":21,"city":"Chachoengsao" }'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])