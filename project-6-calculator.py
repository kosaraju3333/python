### Calculator program
import os
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operators={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    number1=float(input("Enter the First Number: "))
    for symbol in operators:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an Operation: ")
        number2=float(input("Enter the next number: "))
        calculator_function=operators[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue=input(f"Enter 'y' to continue calculate with {output} or 'n to start new calculation or 'x to exit: ").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag=False
            os.system('clear')
            calculator()
        else:
            continue_flag=False
            print("Bye")

calculator()





#
#     operation=input("Pick an Operation: ")
#     next_number=int(input("Enter the next number: "))
#
#     if operators[operation] == "add":
#         add_output=add(first_number,next_number)
#         print(f"{first_number} {operation} {next_number} = {add_output}")
#         should_continue=input(f"Enter 'y' to continue calculate with or 'n to start new calculation or 'x to exit: ").lower()
#
#
#     elif operators[operation] == "sub":
#         sub_output=sub(first_number,next_number)
#         print(f"{first_number} {operation} {next_number} = {sub_output}")
#
#     elif operators[operation] == "mul":
#         mul_output=mul(first_number,next_number)
#         print(f"{first_number} {operation} {next_number} = {mul_output}")
#
#     elif operators[operation] == "div":
#         div_output=div(first_number,next_number)
#         print(f"{first_number} {operation} {next_number} = {div_output}")
#
# new()
# continue_new_exit=input(f"Enter 'y' to continue calculate with or 'n to start new calculation or 'x to exit: ").lower()
# if continue_new_exit == 'y':
#
# elif continue_new_exit == 'n':
#     os.system('clear')
#     new()
#
# elif continue_new_exit == 'x':
#     exit()




# x=operators["+"]
# print(x)