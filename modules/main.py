import my_module as m
from my_module import calculator,a,area_of_square
from my_module import *
a , b=7,9
print(a)
print(b)

print("#####################")
print(m.a)
print(m.area_of_square(3))
print(m.calculator(5,6))
print()
print("#################################")
print()
print(a)
print(area_of_square(6))
print(calculator(4,6))
