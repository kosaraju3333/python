name="Ramakrishna"
cricketer_names=["Virat","Rohit","KL","Gill"]
numbers=[3,5,2,-10,-4,9,3]
# for i in cricketer_names:
#     print(i)

### Finding the square of the items in the list
square_list=[]
for number in numbers:
    square = number ** 2
    square_list.append(square)
print(f"We did square of each item from this list: {numbers} ")
print(f"The list of squares is: {square_list}")