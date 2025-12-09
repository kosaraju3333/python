class Student:
    def __init__(self,name,roll_num,age):
        self.name=name      #Public instance Variable or Public Attribute
        self._roll_num=roll_num  #Protected instance Variable or Protected Attribute
        self.__age=age    #Private instance Variable or Private Attribute

    ### Private Method ####
    def __display(self):    #Private instance Method or Private Method
        print(f"Hi myself {self.name}, age {self.__age} with roll number {self._roll_num} from Student class")

    ### Public Method ####
    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My roll number is {self._roll_num} calling from Branch class")

s1=Student("Ram",462, 35)
print(s1.name)
print(s1._roll_num)
s1.displayPrivateData()

### Name mangling
print(dir(s1))
print(s1._Student__age)
s1._Student__display()

b1=Branch("Krish",123, 25)
b1.name="RK"
b1.show()
print(b1.name)
print(b1._roll_num)