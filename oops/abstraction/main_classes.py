from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        Vehicle.__init__(self,n)
        self.color=color
    def start(self):
        print("Start with kick")
        print(f"This Bike color is {self.color}")

class Scooty(Vehicle):
    def __init__(self,n):
        Vehicle.__init__(self,n)
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self,n,gears):
        super().__init__(n)
        self.gears=gears
    def start(self):
        print("Start With Key")
    def display(self):
        print(f"This car has {self.gears} Gears")

# V=Car(4)
# V.start()

# V.Vehicle(4)