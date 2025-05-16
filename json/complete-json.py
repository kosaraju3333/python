import json

# Sample Python dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# 1. Save the dictionary to a file
with open("person.json", "w") as file:
    json.dump(person, file)
print("Data saved to person.json")

# 2. Read the JSON data from the file
with open("person.json", "r") as file:
    data = json.load(file)
print("Data loaded from file:", data)

# 3. Convert Python object to JSON string
json_string = json.dumps(data)
print("JSON string:", json_string)

# 4. Convert JSON string back to Python object
python_obj = json.loads(json_string)
print("Python object:", python_obj)
