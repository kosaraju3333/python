## Check whether given number is even or odd.

print("This program will check whether given number is even or odd")

number=int(input("Enter number: "))

if number % 2 == 0:
    print(f"The number {number} you entered is EVEN number")
else:
    print(f"The number {number} you entered is ODD number")