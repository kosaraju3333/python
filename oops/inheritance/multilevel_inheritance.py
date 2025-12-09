class Human:
    can_breath=True
    def __init__(self,heart_beat):
        self.nose=1
        self.eyes=2
        self.heart_beat=heart_beat

    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can Work")

class Male(Human):
    def __init__(self,name):
        self.name=name

    def sleep(self):
        print("I can sleep whole day")

class Boy(Male):
    def __init__(self,heat_beat,name,can_dance):
        Human.__init__(self, heat_beat)
        Male.__init__(self,name)
        self.know_dancing=can_dance

    def work(self):
        ### Access Home class method in Boy class method.
        Human.work(self)
        print("I can Code")

    def display(self):
        print(f"I am {self.name}, I have {self.eyes} eyes, my heart beat count is: {self.heart_beat}, I can breath: {self.can_breath}")
        Human.work(self)
        print("I can Code")
        Human.eat(self)
        Male.sleep(self)
        print(f"can you dance?: {self.know_dancing}")

# class Programmer(Boy):
#     def work(self):
#         Boy.work(self)
#         print("I can write programs")

boy_1=Boy(75,"RK", True)
boy_1.eat()
boy_1.work()
print(f"Can you dance?: {boy_1.know_dancing}")
print(boy_1.heart_beat)

boy_2=Boy(name="KRK",heat_beat=70, can_dance=False)
boy_2.display()

# program_1=Programmer(75)
# print(program_1.heart_beat)
# program_1.work()
