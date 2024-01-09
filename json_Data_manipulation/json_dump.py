# Python program to write JSON to a file

import json

employee_data = {"name": "RAM", "age": 32, "city": "Bangalore", "role": "DevOps Engineer"}


with open("employee_data.json", "w") as file:
    json.dump(employee_data, file)