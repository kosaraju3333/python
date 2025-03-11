height=int(input("Enter your height : "))

if height >=3:
    print("you can ride a bike")
    age=int(input("Enter your age: "))
    if age < 12:
        print("Please pay 150 Rupees")
    elif age <= 18:
        print("Please pay 250 rupees")
    else:
        print("Please pay 500 rupees")
else:
    print("Your are not eligible to ride a bike\nBye..Bye...!")
