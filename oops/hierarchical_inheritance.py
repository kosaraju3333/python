class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print(f"name: {self.name}, age: {self.age}")

    def eat(self):
        print("I can Eat")

class Male(Human):
    def __init__(self,name,age,location):
        Human.__init__(self,name,age)
        self.location=location

    def show_details_m(self):
        Human.show_details(self)
        print(f"Current_location:{self.location}")

    def sleep(self):
        print("I can sleep whole day")

class Female(Human):
    def __init__(self,name,age,can_dance):
        super().__init__(name,age)
        # Human.__init__(self,name,age)
        self.can_dance=can_dance

    def work(self):
        print("I can code")

    def show_details_f(self):
        Human.show_details(self)
        print(f"Knowing_Dance={self.can_dance}")

female_1=Female("Leela", 34, True)
female_1.show_details_f()

female_2=Female("SR", 24, True)
female_2.show_details_f()


male_1=Male("Ram",35,"Bangalore")
male_1.show_details_m()

male_2=Male("Krish",25,"Hyderabad")
male_2.show_details_m()
# female_1.eat()
# print(female_1.age)
# female_1.show_details()
# print(f"Can Leela Dance?: {female_1.can_dance}")
