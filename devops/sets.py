my_set = {1,2,3,4,5,5,4,3,2,1}
print(my_set)

my_set.add(100)
my_set.add(300)

print(my_set)

for i in my_set:
    print(i)

my_set.remove(5)
print(my_set)

if 100 in my_set:
    print(f"100 is present")
else:
    print(f"100 is not present")

my_set1 = {1,2,3,4,5,5,4,3,2,1}

print(my_set1.clear())
my_set1.add(1234)
print(my_set1)

### Python program to find common elements in two lists with the help of set operations −
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]

set1 = set(l1)
set2 = set(l2)

common = set1.intersection(set2)
print(list(common))

#### Python program to check if a set is a subset of another −
s1={1,2,3,4,5}
s2={4,5}
if s2.issubset(s1):
    print(f"Yes set2:{s2} is sub set of set1:{s1}")
else:
    print(f"NO set2:{s2} is not sub set of set1:{s1}")

### Python program to obtain a list of unique elements in a list −
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
print(type(T1))
print(set(T1))