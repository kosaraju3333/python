class Person:
    def __init__(self,name,age,location,role):
        self.name=name
        self.age=age
        self.location=location
        self.your_role=role


    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}, Role: {self.your_role}")

class Student(Person):
    def __init__(self,name,age,collage_name,branch_name,location,role):
        Person.__init__(self,name,age,location,role)
        self.s_collage_name=collage_name
        self.s_branch_name=branch_name

    def student_details(self):
        Person.show_details(self)
        print(f"Collage_Name: {self.s_collage_name}")
        print(f"Branch_Name: {self.s_branch_name}")

class Faculty(Person):
    def __init__(self,name,age,collage_name,sub_teach,location,role):
        Person.__init__(self,name,age,location,role)
        self.f_collage_name=collage_name
        self.f_sub_teach=sub_teach

    def faculty_details(self):
        Person.show_details(self)
        print(f"Collage_Name: {self.f_collage_name}")
        print(f"Subject Teaches: {self.f_sub_teach}")


student_1=Student("Ram",23,"Sasi", "ECE", "AP" , "Student")
student_1.student_details()


faculty_1=Faculty("RK", 45, "SRKR", "Python", "Hyderabad", "Faculty")
faculty_1.faculty_details()
