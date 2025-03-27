student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}

student_graders={}

for key, value in student_marks.items():
    if value > 90:
        student_graders.update({key:"A+"})
    elif value > 80:
        student_graders.update({key:"A"})
    elif value > 70:
        student_graders.update({key:"B+"})
    elif value > 60:
        student_graders.update({key:"B"})
    elif value > 50:
        student_graders.update({key: "C"})
    elif value > 40:
        student_graders.update({key: "D"})
    else:
        student_graders.update({key:"F"})
print(student_graders)

### Another Way
for student in student_marks:
    marks=student_marks[student]
    if marks > 90:
        student_graders[student]="A+"
    elif marks > 80:
        student_graders[student]="A"
    elif marks >70:
        student_graders[student]="B+"
    elif marks > 60:
        student_graders[student]="B"
    elif marks > 50:
        student_graders[student]="C"
    elif marks > 40:
        student_graders[student]="D"
    else:
        student_graders[student]="F"

print(student_graders)