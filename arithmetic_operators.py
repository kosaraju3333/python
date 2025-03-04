#print(5 + 2 * (3 - 1) + 10 / 5)

## Calculate BMI (Body Mass Index)

print("This tool helps to find your BMI")
print("To calculate your BMI we need your 'Weight' and 'Height' so please provide those details.")

name=input("Enter your Name: ")
weight=float(input("Enter your Weight in KG's: "))
height= float(input("Enter your Height in Meters: "))

BMI=weight/(height ** 2)

print("Hi " + name + " your BMI is: " + str(BMI))