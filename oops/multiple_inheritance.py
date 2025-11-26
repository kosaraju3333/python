class Human:
    def __init__(self,heart_beat):
        print("Calling from Human __init__")
        self.num_eyes=2
        self.num_nose=1
        self.heart_beat=heart_beat

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        print("Calling from Male __init__")
        self.name=name

    def drive(self):
        print("I can drive")
    def work(self):
        print("I can Code")

class Boy(Human,Male):
    ## initialises the __init__ constructor for attribute
    def __init__(self,name,heart_beat,language):
        ## calling parent/super class __init__ constructor to access parent class attributes
        Human.__init__(self,heart_beat)
        Male.__init__(self,name)
        self.language=language


    def work(self):
        print("I can test")

    def sleep(self):
        print("I can Sleep")

    def display(self):
        print(f"I am {self.name}, My heart beat count is {self.heart_beat}, I have {self.num_eyes} eyes. I know {self.language} programming")
    def language(self):
        print(f"I know {self.language()} language")

### Used Positional Arguments for boy_1####
boy_1=Boy("RK", 72, "Python")
boy_1.display()

### Used Keyword Arguments for boy_2 ###
boy_2=Boy(language="Java", name="KRK", heart_beat=75)
boy_2.display()

### access the particular method from class
Male.work(boy_1)

### Method Order
print(Boy.mro())

# boy_1.work()
# boy_1.drive()
# boy_1.eat()
# Boy_1.
