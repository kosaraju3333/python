

### Function to find Leap year
def find_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
                # print(f"{year} is Leap Year")
            else:
                return "Not Leap"
                # print(f"{year} is NOT a Leap year")
        else:
            return  "Leap"
            # print(f"{year} is a LEAP year")
    else:
        return "Not Leap"
        # print(f"{year} is NOT a Leap year")

calendar = {
    "january" : 31,
    "february": 28,
    "march"   : 31,
    "april"   : 30,
    "may"     : 31,
    "june"    : 30,
    "july"    : 31,
    "august"  : 30,
    "september" : 31,
    "october"   : 30,
    "november"  : 31,
    "december"  : 30
}
year_input=int(input("Enter the Year:\n"))
month_input=input("Enter the Month in full like january , february and etc... not lik jan , feb ...:\n").lower()
leap_year_feb=29

if find_leap_year(year_input) != "Leap":
    days_in_month=calendar[month_input]
    print(f"{year_input} is 'Not a Leap Year' ")
    print(f"In Year {year_input} {month_input} has {days_in_month} Days")
else:
    print(f"{year_input} is a 'Leap Year' ")
    if month_input == "february":
        print(f"In Year {year_input} {month_input} has {leap_year_feb} Days")
    else:
        leap_yesr_days_in_month=calendar[month_input]
        print(f"In Year {year_input} {month_input} has {leap_yesr_days_in_month} Days")
# elif find_leap_year(year_input) == "Leap":
#     print(f"In Year {year_input} {month_input} has {leap_year_feb} Days")



