from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n

    @abstractmethod
    def start(self):
        pass
    ### Normal Method
    def display(self):
        print("Hi I am calling from Vehicle Class")

# v=Vehicle(2)