class Student:
    def __init__(self,name,roll_num,age):
        self.name=name      #Public instance Variable or Public Attribute
        self._roll_num=roll_num  #Protected instance Variable or Protected Attribute
        self.__age=age    #Private instance Variable or Private Attribute

    def get_age(self):
        return self.__age

    def set_age(self,age_number):
        if age_number>35:
            print("Invalid age given..Age should be less than 35")
        else:
            self.__age=age_number
            print(f"Set age is: {self.__age}")

    ### Private Method ####
    def __display(self):    #Private instance Method or Private Method
        print(f"Hi myself {self.name}, age {self.__age} with roll number {self._roll_num} from Student class")

    ### Public Method ####
    def displayPrivateData(self):
        self.__display()

s1=Student("Ram",462,35)
print(s1.get_age())
s1.set_age(44)
