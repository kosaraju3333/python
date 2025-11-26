class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name

    def show_details(self):
        print(f"University Name: {self.uni_name}")

class Course(University):
    def __init__(self,uni_name,course_name):
        University.__init__(self,uni_name)
        self.course_name=course_name

    def show_details(self):
        University.show_details(self)
        print(f"Course Name: {self.course_name}")

class Branch(University):
    def __init__(self,uni_name,branch_name):
        University.__init__(self,uni_name)
        self.branch_name=branch_name

    def show_details(self):
        super().show_details()
        # University.show_details(self)
        print(f"Branch Name: {self.branch_name}")

class Student(Course,Branch):
    def __init__(self,s_name,uni_name,course_name,branch_name):
        University.__init__(self,uni_name)
        Course.__init__(self, uni_name, course_name)
        Branch.__init__(self,uni_name,branch_name)
        self.s_name=s_name

    def show_details(self):
        print(f"Student Name: {self.s_name}")
        Course.show_details(self)
        print(f"Branch name: {self.branch_name}")

class Faculty(Branch):
    def __init__(self,f_name,uni_name,branch_name):
        Branch.__init__(self,uni_name,branch_name)
        self.f_name=f_name

    def show_details(self):
        print(f"Faculty_Name: {self.f_name}")
        Branch.show_details(self)



print("####################### Student Details #######################")
student_1=Student("Ram", "JNTU-K", "Engineering", "ECE")
student_1.show_details()

print("####################### faculty Details #######################")

faculty_1=Faculty("Srinu", "IIT", "CSE")
faculty_1.show_details()