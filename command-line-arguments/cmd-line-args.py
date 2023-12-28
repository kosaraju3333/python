## This Program is example for Command line arguments.

# For Command Line arguments, we need sys package thats why we are importing SYS package 
import sys

def add(num1, num2):
    ADD = num1 + num2
    return ADD

def sub(num1, num2):
    SUB = num1 - num2
    return SUB

def mul(num1, num2):
    MUL = num1 * num2
    return MUL

# Assignment of Command Line Arguments to variables.
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    Addition = add(num1, num2)
    print("Addition value is:", Addition)

if operation == "sub":
    Subtraction = sub(num1, num2)
    print("Subtraction value is:", Subtraction)

if operation == "mul":
    Multiplication = mul(num1, num2)
    print("Multiplication value is:", Multiplication)

