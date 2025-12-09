class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speak(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a duck and I can swim")
    def speak(self):
        print("Woof Woof")

class Person:
    def speak(self):
        print("blah blah blah blah")
class Demo:
    def display(self,obj):
        obj.swim()
        obj.speak()
        print("Information displayed")

### Created duck1 object from Duck class and pass duck1 object to display function in Demo Class
duck1=Duck()
dog1=Dog()
p1=Person()

demo=Demo()
demo.display(duck1)
demo.display(dog1)
demo.display(p1)
