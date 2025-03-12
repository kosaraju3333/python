### This Program is used for Order the Pizza
print("Welcome to Pizza Shop")
name = input("Enter Your Name: ")
pizza_size = input("Enter the Pizza Size Small(S) or Medium(M) or Large(L): ")
pizza_bill = 0
if pizza_size == "small" or pizza_size == "s" or pizza_size == 'SMALL' or pizza_size == 'S':
    pizza_bill = pizza_bill + 100
    print("Small Pizza price is 100 Rupees")

elif pizza_size == "medium" or pizza_size == "m" or pizza_size == "MEDIUM" or pizza_size == 'M':
    pizza_bill = pizza_bill + 200
    print("Medium Pizza price is 200 Rupees")

elif pizza_size == "large" or pizza_size == "l" or pizza_size == "LARGE" or pizza_size == 'L':
    pizza_bill = pizza_bill + 300
    print("Large Pizza price is 300 Rupees")

else:
    print("Wrong Input")
    print("Please Enter S or M or L or SMALL or small or MEDIUM or medium or LARGE or large  as input")
    exit(1)

add_pepperoni = input("Do you want pepperoni add-on-Type 'YES' or 'NO'?: ")
if add_pepperoni == 'YES' or add_pepperoni == 'yes':
    if pizza_size == 'small' or pizza_size == 's':
        pizza_bill = pizza_bill + 30
    else:
        pizza_bill = pizza_bill + 50

extra_cheese = input("Do you want extra cheese add-on as well-Type 'YES' or 'NO'?: ")
if extra_cheese == 'YES' or extra_cheese == 'yes':
    pizza_bill = pizza_bill + 20

print(f"Your total bill: {pizza_bill} Rupees")



