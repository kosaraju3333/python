student_data={
    "Ram":{"roll_no":10, "age":20, "course":"Python"},
    "Mohan":{"roll_no":20, "age":22, "course":"Java"}
}

print(student_data)

## access the data individually
print(student_data["Mohan"])
print(student_data["Mohan"]["course"])

### Add item to nested dict
student_data["Mohan"]["Phone_number"]=123456
print(student_data["Mohan"])
print(student_data)

## Delete item from nested dict

del student_data["Mohan"]["Phone_number"]
print(student_data["Mohan"])
print(student_data)

### Nesting a list in dictionary

travel_data={
    "USA":["Texas","NewYork", "LA"],
    "INDIA":["AP","Karnataka","TN"]
}

print(travel_data)