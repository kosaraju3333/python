class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

p1=Person("Ram",45)
p2=Person("krish",42)

if p1 > p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")


# if p1.age > p2.age:
#     print(f"{p1.name} will pay the bill")
# else:
#     print(f"{p2.name} will pay the bill")