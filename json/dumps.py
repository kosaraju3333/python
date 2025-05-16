import json

# Python dictionary
data_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Python List
data_list = ["Ram",35,"Test",True]

# Python tuple
data_tuple = ("Ram",35,"Test",True)


print(type(data_tuple)) #### This will give class 'dict'

# Serialize to JSON string
json_string = json.dumps(data_tuple)
print(type(json_string)) #### This will give class 'str'
print(json_string)
 