###  This Program will select the random user from the list to pay the bill

import random
print("This Program will select the person from the poll to pay the bill...\nso please enter the names...!")
names=input("Enter the names with comma separator: ")
print(f"You have enter these names: {names}")

# Converting to array
names_list=names.split(",")

# Find the length of list
length_names_list=len(names_list)


# Using Randon function to get the random number we use this as a array index number
random_choice=random.randint(0,length_names_list-1)

# Pulling or Taking the item from the array by using above random number as index of an array
bill_person=names_list[random_choice]

print(f"{bill_person} will pay the bill")

#### Below Code is by using random choice function #####
#### This is very simple one #######
# bill_pay_person=random.choice(names_list)
# print(f"{bill_pay_person} will pay the bill")





