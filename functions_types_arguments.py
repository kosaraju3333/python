### Positional Arguments
def greet(name,dept):
    print(f"Hi {name}")
    print(f"are you from {dept}?")
greet("RAM","CSE")

### Keywords Arguments
def greet(name,dept):
    print(f"Hi {name}")
    print(f"are you from {dept}?")
greet(name="RAM",dept="CSE")

### Default arguments
def greet(name,subject,dept="ECE"):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"are you from {dept}")
greet("RAM",subject="Python",dept="CSE")

### Arbitrary Arguments
## add numbers:
## Note: singe * means it only allows or accept Arbitrary positional arguments.
def add(*numbers):
    sum=0
    for number in numbers:
        sum = sum + number
    print(f"Total sum is: {sum}")
add(3,7,5,3,4,5,6,5,4,3,5)



