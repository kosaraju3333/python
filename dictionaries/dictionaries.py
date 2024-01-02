
# Creating a Dictionarie
employee_info_dict = {"name": "RAM", "age": 32, "city": "Bangalore", "role": "DevOps Engineer"}
# Printing Dictionarie
print(employee_info_dict)

# Accessing Values
print(employee_info_dict["name"]) 
print(employee_info_dict["role"]) 

# Modifing Elements
employee_info_dict["age"] = 26
# Adding Elements
employee_info_dict["ID"] = "MIL117"

# Removing Element
del employee_info_dict["ID"]

# Printing Dictionarie
print(employee_info_dict)

# Checking Key Existance:
if "role" in employee_info_dict:
    print("Role key is present in dictionary")

# Iterating Through Keys and Values 

i = 0
for key, value in employee_info_dict.items():
    print("iteration: ", i)
    print(key, value)
    i += 1