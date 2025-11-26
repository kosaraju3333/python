class Human:
    def __init__(self,heart_beat):
        self.num_eyes=2
        self.num_nose=1
        self.heart_beat=heart_beat


    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")
    
class Male(Human):
    ## Calling or using parent class Attributes
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name

    def drive(self):
        print(f"Name: {self.name}")
        print("I can Drive")
    
    ## Method Override // Overriding the parent class method functionality
    def work(self):
        print("I can Code")

    def display(self):
        print(f"Hi I am {self.name} and my heart beat count is {self.heart_beat}")

class Female(Human):
    def drive(self):
        print("I can not Drive")

    ## access Method from parent or super Class and add or append some more functionality to the method
    def eat(self):
        super().eat()

        print("I can cook too..!!")

male_1=Male("Ram",72)
male_1.eat()
male_1.work()
male_1.drive()
print(male_1.num_eyes)
male_1.display()

female_1=Female(63)
female_1.eat()
female_1.work()
female_1.drive()
print(male_1.num_eyes)