import random

list1 = ["Rohan", "Physics", 21, 95.4]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

print(list1)
print(list2[1:5])

### Update list
print(f"2nd index value is list is: {list2[2]}")
list2[2]=4000

print(f"new 2nd index value is: {list2[2]}")

### Delete value from list
print(f"2nd value from this list2 {list2} is delete")
del list2[2]
print(f"Now this is new update list2 {list2}")

### appending the lists
new_list =  list1 + list2
print(new_list)

print("Physics" in list1)

### append to list
list1.append(100)
print(list1)
list1.append(454545454545)
print(list1)

### Length of list
print(f"Length of list1 is : {len(list1)}")

### count of how many times obj occurs in list
print(list1.count(21))

### list reverse
list1.reverse()
print(list1)

list1.reverse()
print(list1)

### List insert
list1.insert(0,"Rohan123")
print(list1)

## List remove
list1.remove("Physics")
print(list1)

### Compare lists

list_1 = [1, 2, "DevOps", "AWS", "Java"]
list_2 = [4, 5, "Python", "AWS", "Java"]

common = []
un_common = []

for i in list_1:
    if i in list_2:
        common.append(i)
    else:
        un_common.append(i)

for j in list_2:
    if j not in list_1:
        un_common.append(j)
print(f"Common objects in 2 list {common}")
print(f"Un Common objects in two lists {un_common} ")

############
#Find uniqe number in  list
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []

for i in L1:
    if i in L2:
        continue
    else:
        L2.append(i)
print(L2)
L2.sort()
print(L2)

##########################
## Python program to find sum of all numbers in a list.

L1 = [1, 9, 1, 6, 3, 4]
sum = 0
for i in L1:
    sum = sum + i
print(f"Sum of all number in a list is : {sum}")

#############################
#Python program to create a list of 5 random integers.

random_list = []
for i in range(5):
    x =  random.randint(1,100)
    random_list.append(x)
print(random_list)

random_list1 = []
x = 0
while x < 5:
    num = random.randint(1,100)
    random_list1.append(num)
    x = x + 1
print(random_list1)

