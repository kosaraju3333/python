import random

tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)

### Accessing Tuples
print(tup1[0])
print(tup4[1:3])

# Following action is not valid for tuples
# tup1[0] = 100;

tup5 = tup1 + tup2
print(tup5)

print(tup1)
del tup1

print(f"Length of tuple1 is : {len(tup2)}")
print(f"Max value in a tuple2 is: {max(tup2)}")
print(f"Min value in a tule2 is: {min(tup2)}")

string="This is a string"
print(tuple(string))
print(type(tuple(string)))

#### Python program to find unique numbers in a given tuple
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()
for i in T1:
    if i not in T2:
        T2 = T2 + (i,)
print ("original tuple:", T1)
print ("Unique numbers:", T2)


### Python program to find sum of all numbers in a tuple −
T1 = (1, 9, 1, 6, 3, 4)
sum = 0
for i in range(len(T1)):
    sum = sum + T1[i]
print(sum)

total = 0
for i in T1:
    total = total + i
print(total)

#### Python program to create a tuple of 5 random integers −
Tuple1 = ()
for i in range(5):
    x = random.randint(1,100)
    Tuple1 = Tuple1 + (x,)
print(Tuple1)