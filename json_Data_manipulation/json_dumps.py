#json.dumps() method can convert a Python object from (LIST, TUPLES, Dictionary)  into a JSON string.
# NOTE = BUT NOT for SETS
import json

employee_data = {"name": "RAM", "age": 32, "city": "Bangalore", "role": "DevOps Engineer"}
#employee_data = { "RAM", 32 , "KRISH" }


print(type(employee_data))

json_data = json.dumps(employee_data, indent=4)
print(type(json_data))
print(json_data)