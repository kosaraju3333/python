
name = input("Enter your Name: ")
height = float(input("Enter your Height: "))

if height > 3:
    print("You can Ride on Rollo Coaster")
    age = int(input("Enter Your age: "))
    if age < 12:
        ticket_price = 150
        print("Ticket price is 150 Rupees")
    elif age <= 18:
        ticket_price = 250
        print("Ticket price is 250 Rupees")
    else:
        ticket_price = 500
        print("Ticket 500 Rupees")

    photo = input("If you want photo, need to pay 50 rupees extera on ticket price-So, Do you want to take photo?- please type  'YES' or 'NO' : ")
    if photo == 'YES' or photo == 'yes':
        total_price = ticket_price + 50
        print(f"Your final price is  {total_price} Rupees")
    else:
        print(f"Your final price is  {ticket_price} Rupees")

    print("Thank You....! Enjoy the ride...!")

else:
    print("You can not ride on rollo coaster ")
    print("We are sorry....! see you soon...! ")
