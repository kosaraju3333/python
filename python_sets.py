set1={20,False,2,-100,0,56.12,"Ram","Krish",True,1,0}
## If you see the output you can see 0 and 1 because Tre and False are  considered as 0 and 1 as we know sets are allowed duplicates
print(set1)
print(len(set1))

## We can not access the Item based on index number in set.
#print(set1[3])

## Lets check the data type of sets
## This set2 type will give dict
## We can not create empty set with {} brackets.
set2={}
print(type(set1))
print(type(set2))

## Create Empty set
set3=set()
print(type(set3))

## add item to set
set1.add(99)
print(set1)

## Length of Set
print(len(set1))

## Remove Item
set1.remove(0)
print(set1)

### Discard is also same like remove but it won't give error if give nuber from out of set, It will print same set
set1.discard(4554)
print(set1)

## If we want to clear all the items from the set use clear function
# set1.clear()
# print(set1)

### Remove any random item from set use POP
print(set1.pop())
print(set1)

### add Tuple in set
set1.add(("RK",45,4.5))
print(set1)
