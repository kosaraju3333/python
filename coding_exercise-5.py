# Find out how amy days, weeks, months we have left, if we live until 90 years old

print("This program is used to calculate how any days, weeks, months you have left, if you live until 90 years old ")
print("So, Please Provide your details")
name = input("Enter your Name: ")
current_age = int(input("Enter your current age: "))
max_age = 90

years_left = max_age - current_age

days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

print(f"Hi {name}\nyou have {days_left} days, {weeks_left} weeks and {months_left} months left.")