name=input("Enter your name to find the number of characters it has: ")
### Converted string to int; BY default input() function takes input as string
# by adding int() to input() it converted as int data_type.
age=int(input("Enter your age: "))
name_length=len(name)
### converted int to string
print("your name has " + str(name_length) + " characters")
print("your age is " + str(age))
### Converting string to int


### add TWO numbers by taking 2 inputs from USERs

number_1=input("Enter number 1 value: ")
number_2=input("Enter number 2 value: ")

sum=int(number_1)+int(number_2)
print(sum)