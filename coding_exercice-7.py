### This program will calculate the BMI
print("This Program is used to calculate your BMI\nPlease provide your details")

name = input("Enter your Name: ")
weight = float(input("Enter your weight in KG's: "))
height = float(input("Enter your height in meters: "))

bmi = round(weight/(height ** 2),2)

if bmi < 18.5:
    print(f"Your BMI Score: {bmi}")
    print("You are Underweight")
elif bmi < 24.9:
    print(f"Your BMI Score: {bmi}")
    print("You are in Normal Range")
elif bmi < 29.9:
    print(f"Your BMI Score: {bmi}")
    print("You are Overweight(Pre-obese")
elif bmi < 34.9:
    print(f"Your BMI Score: {bmi}")
    print("You are Obese")
else:
    print(f"Your BMI Score: {bmi}")
    print("You are Clinically Obese")
