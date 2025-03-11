name='Krishna'
age =34
height = 1.6

### we can print or access the variables in different ways like below but f string is more easy and faster and error free as well

## With commas
print("My Name is " ,name,"I am ",age, "years old." " My height is " ,height, "meters.")
## With type_casting
print("My Name is " + name + " I am " + str(age) + " years old. " + "My height is " + str(height) + " meters")

## With f string
## f string is more easy and faster way to formate the string  and error free as well
print(f"My Name is {name}. I am {age} years old. My height is {height} meters")
## we can use expressions as well
print(f"My Name is {name}. I am {age*2} years old. My height is {height} meters")
