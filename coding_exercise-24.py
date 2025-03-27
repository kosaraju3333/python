student_data=[
    {
        "Name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
    },
    {
        "Name": "Mohan",
        "roll_no": 20,
        "age": 22,
        "course": "Java"
    }
]

def add_new_student(**student_info):
    new_student={}
    for key,value in student_info.items():
        new_student[key]=value
    student_data.append(new_student)

print(student_data)
add_new_student(Name="Shyam",roll_no=22,age=18,course="C++",location="Bangalore")
print(student_data)

## Another way
def add_new_student_1(name,roll_no,age,course):
    new_student_1={}
    new_student_1["Name"]=name
    new_student_1["roll_no"]=roll_no
    new_student_1["age"]=age
    new_student_1["course"]=course
    print(new_student_1)
    #student_data.append(new_student_1)
    student_data.append(new_student_1)

print(student_data)
add_new_student_1("Shyam",22,18,"C++")
print(student_data)