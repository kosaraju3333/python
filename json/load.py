import json

with open("data123.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))