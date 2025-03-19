### FizzBuzz program
stop_number=int(input("Enter the stop number for a range function: "))
numbers=range(1,stop_number)

for number in numbers:
    # if number%3 != 0 and number%5 != 0:
    #     print(number)
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)