## json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
## It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
import json

person_data = """{  
    "Name": "Jennifer Smith",  
    "Contact Number": 7867567898,  
    "Email": "jen123@gmail.com",  
    "Hobbies":["Reading", "Sketching", "Horse Riding"]  
    }"""

# student_data = '''
#     {
#         "students": [
#             {
#                 "id": 1,
#                 "name": Ram"
#                 "age": 30,
#                 "full-time": True
#             },
#             {
#                 "id": 2,
#                 "name": Krish"
#                 "age": 33,
#                 "full-time": False
#             }
#         ]
#     }
# '''

data = json.loads(person_data)
data["test"] = True
new_person_data = json.dumps(data, indent=4)
print(new_person_data)