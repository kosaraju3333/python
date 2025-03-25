def add(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    print(f"Sum is: {sum}")

add(4,3,4,5,6)
add(4,5)
add(2)


### Pass Arbitrary positional arguments and keyword arguments

def add(*numbers,name):
    sum = 0
    for number in numbers:
        sum = sum + number
    print(f"Hi {name}\nSum is : {sum}")

add(3,6,2,3,45,6,name="Ram")


### Pass Normal argument first and AP_argument next
def add(name,*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    print(f"Hi {name}\nSum is: {sum}")
add("ram",4,5)
