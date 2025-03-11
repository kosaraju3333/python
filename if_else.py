height=float(input("Enter your height in CM: "))

height = round(height)
print(height)
print(type(height))
if height >= 100:
    print("Metro Token is required")
else:
    print("Metro Token is not required")
