my_list = [1, 2, 3, 4, 5]
print("my_list variable memory location:", id(my_list))

a = my_list
print("a variable memory location:", id(a))

b = [1, 2, 3, 4, 5]
print("b variable memory location:", id(b))

#Identity Operator
is_operator = a is my_list
is_not_operator = b is not my_list

# Menbership Operator
in_operator = 3 in a
not_in_oprtator = 8 not in a

print("is operator:", is_operator)
print("is not operator:", is_not_operator)

print("in operator:", in_operator)
print("not in operator:", not_in_oprtator)


