def person_info(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

person_info(name="Ram",age=30,dept="ECE")
person_info(name="Shyam",dept="CSE")


### Pass normal(positional), *args and **kwargs arguments  to function BUT follow the order First need to send positional, *args followed by **kwargs arguments.

def info(surname,*args,**kwargs):
    sum = 0
    for i in args:
        sum = sum + i
    for key,value in kwargs.items():
        print(key,value)
    print(f"Hi {surname}\nsum is: {sum}")


info("DP",5,43,4,56,7,8,9,name="Shyam",age=34,dept="IT")
info("VK",4,12,34,67,8,name="Ram",dept="CSE")

###### Multiply

def multiply(*numbers):
    mul=1
    for number in numbers:
        mul = mul * number
    print(f"Multiplication of the given numbers is: {mul}")

multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)
