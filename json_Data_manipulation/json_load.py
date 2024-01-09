## json.load() takes a file object and returns the json object. 
## It is used to read JSON encoded data from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts a file object.

import json

data = { 
    "name": "Satyam kumar", 
    "place": "patna", 
    "skills": [ 
        "Raspberry pi", 
        "Machine Learning", 
        "Web Development"
    ], 
    "email": "xyz@gmail.com", 
    "projects": [ 
        "Python Data Mining", 
        "Python Data Science"
    ] 
} 

## Creating a file 
with open("data_file.json", "w") as write:
    json.dump(data, write)

## Loading the file and reading and print content

with open("data_file.json", "r") as read_content:
    print(json.load(read_content)) 