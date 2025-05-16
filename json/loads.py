import json
# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"}}'
print(type(json_string))  #### This will give class 'str'


# Deserialize JSON string to Python object

python_object = json.loads(json_string)
print(type(python_object)) #### This will give class 'dict'
print(python_object)