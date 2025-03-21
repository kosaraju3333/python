### Password Generator
import random
import string
from traceback import print_tb

print("Welcome to Password Generator!")
letters_input=int(input("How Many 'LETTERS' would you like to have in your password?\n"))
numbers_input=int(input("How Many 'NUMBERS' would you like to have in your password?\n"))
symbols_input=int(input("How Many 'SYMBOLS' would you like to have in your password?\n"))

letters_string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers_array=[0,1,2,3,4,5,6,7,8,9]
symbols_string="!,@,#,$,%,^,&,*,(,),_,-,+,=,|"

# letter_pass=[]
# number_pass=[]
# symbol_pass=[]
password=[]

for i in range(letters_input):
    letter=random.choice(letters_string)
    password.append(letter)
    # letter_pass=letter_pass+letter
# print(letter_pass)

for i in range(numbers_input):
    number=random.choice(numbers_array)
    password.append(number)
    # number_pass=number_pass+str(number)
# print(number_pass)

for i in range(symbols_input):
    symbol=random.choice(symbols_string)
    password.append(symbol)
    # symbol_pass=symbol_pass+symbol
# print(symbol_pass)

# password=letter_pass + number_pass + symbol_pass
print(password)
random.shuffle(password)

final_password=''
for i in password:
    final_password=final_password+str(i)
print(f"Your Password is: {final_password}")

