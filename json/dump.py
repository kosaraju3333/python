import json

json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"}}'

# Read and deserialize from file
with open("data123.json","w") as file:
    json.dump(json_string, file)