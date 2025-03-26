import math
#### Find a prime number
n=int(input("Enter the number to check weather its prime or not?:\n"))

### First Approach

def prime_checker_1(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number):
        if number%i == 0:
            is_prime=False
    if is_prime==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")

### Second Approach
def prime_checker_2(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,math.ceil(number/2)+1):
        if number%i == 0:
            is_prime=False
    if is_prime==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")

prime_checker_1(n)
prime_checker_2(n)