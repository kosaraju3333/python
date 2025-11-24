class InstructorInfo:
    def __init__(self,name,address):
        self.ins_name = name
        self.ins_address = address
        ### Default Attribuite
        self.followers = 0
        # print(self.ins_name)
        # print(self.ins_address)
        # print("Welcome to Class and object in python")

instructor_1=InstructorInfo("ram","Bangalore")
print(instructor_1.ins_name)
print(instructor_1.followers)

instructor_2=InstructorInfo("Krishna","Hyderabad")
print(instructor_2.ins_name)
print(instructor_2.ins_address)

instructor_3=InstructorInfo("RK","Kerala")
print(instructor_3.ins_name)
print(instructor_3.ins_address)

instructor_4=InstructorInfo("KRK","Chennai")
print(instructor_4.ins_name)
print(instructor_4.ins_address)