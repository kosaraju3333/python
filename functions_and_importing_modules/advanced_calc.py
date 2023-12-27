# Importing basic_calc.py as a module in this program
import basic_calc

# Importing num1 and num2 variables from basic_calc module
from basic_calc import num1, num2

# Here calling the whole imported module
basic_calc

def div(num1, num2):
    DIV = num1 / num2
    return DIV

def reminder(num1, num2):
    REMINDER = num1 % num2
    return REMINDER

def absolute_value(num1):
    ABSOLUTE_VALUE = abs(num1)
    return ABSOLUTE_VALUE

Division = div(num1, num2)
print("Division of num1 and num2 is:", Division)

Reminder = reminder(num1, num2)
print("Reminder of num1 and num2 is:", Reminder)

Absolute_value = absolute_value(num1)
print("Absolute_value of num1 and num2 is:", Absolute_value)

# Here calling the only add() function from basic_calc module this is to know how to call saperate functions from module. 
#using_add_function = basic_calc.add(num1, num2)
#print("Imported add function from basic_calc for practice:", using_add_function)