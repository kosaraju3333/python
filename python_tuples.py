tuple1=("Ram",23,-45,6.4,-100,"Krish")

print((tuple1[-2 ]))

## This is not tuple it will give int type
tuple2=(34)
print(type(tuple2))

### This is tuple it will give tuple type
tuple3=(34,)
print(type(tuple3))

tuple4=(23,-45,455,23)

### tuple slicing
print(tuple1[1:])
print(tuple1[:5])
print(tuple1[0:5:2])
print(tuple1[::2])

### Length of tuple
print(len(tuple1))

### Nested of Tuples
tuple5=(tuple1,tuple4)
print(tuple5)
print(tuple5[0])
print(len(tuple5))

### Concatenate Tuples
tuple6 = tuple1 + tuple3 + tuple4
print(tuple6)
print(len(tuple6))

### Min and Max in tuples
## Note : Min and Max are not work on mixed tuples(combination of string, float, int, Boolen)
print("Min and Max of tuple")
print(tuple4)
print(min(tuple4))
print(max(tuple4))

### Count function in
print(tuple6.count(23))

## Find the index of particular item in tuple
#Note: it will not give 2nd occurance of item index
print(tuple6.index("Krish"))

### Convert List to Tuple
list1=[2,5,3,7,-100,"Ram",45.98]
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

####
tuple7=(10,)*7
print(tuple7)