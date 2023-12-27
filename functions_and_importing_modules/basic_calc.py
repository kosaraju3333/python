### This a Basic calc fro ADD, SUB and MUL

# Taking Input from the users
num1 = int(input('Please enter the num1 value:'))
num2 = int(input('Please enter the num2 value:'))

def add(num1, num2):
    ADD = num1 + num2
    return ADD

def sub(num1, num2):
    SUB = num1 - num2
    return SUB

def mul(num1, num2):
    MUL = num1 * num2
    return MUL

Addition = add(num1, num2)
print("Addition of num1 and num2 is:", Addition)

Subtraction = sub(num1, num2)
print("Subtraction of num1 and num2 is:", Subtraction)

Multiplication = mul(num1, num2)
print("Multiplication of num1 and num2 is:", Multiplication)
