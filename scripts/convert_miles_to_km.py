####### Convert miles to KM's #######

def convert_miles_to_km(miles):
    km = 1.6 * miles
    return km

def main():
    miles = int(input("Enter the number of miles you have walked: "))
    x = type(miles)
    print(x)
    km_you_walked = convert_miles_to_km(miles)
    print("you have walked: ",km_you_walked,"km's")



if __name__ == "__main__":
    main()
