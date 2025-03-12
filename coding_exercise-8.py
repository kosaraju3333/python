### This is used to check whether given year is leap year or Not
print("This is used to check whether given year is leap year or Not")
year = int(input("Enter the year to find whether the year is leap year or NOT: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is Leap Year")
        else:
            print(f"{year} is NOT a Leap year")
    else:
        print(f"{year} is a LEAP year")
else:
    print(f"{year} is NOT a Leap year")
