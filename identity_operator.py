from operator import is_not

a=5
b=5.0

print(id(a))
print(id(b))

print(a is  b)
print(id(a) == id(b))

######
a = 5
b = 6
print(id(a))
print(a)
print(id(b))
print(b)
a = 8
print(id(a))

print(a is a)
print(a)