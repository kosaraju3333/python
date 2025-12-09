class A:
    def display(self):
        print("Display Form A Class")

class B(A):
    def display(self):
        print("Display From Class B")
class C:
    def show(self):
        print("Hi From Class C")
class D(B,C):
    def display(self):
        print("Display From Class D")

d1=D()
d1.display()