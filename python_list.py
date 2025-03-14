numbers=[10, 5, -34, 55, -100, 78, -43, 68, 67665]
names=["ram", "lakshman", "hanuman"]
mix_list=[1, "Ram", True, 10.45]
print("Simple Print")
print(numbers)
print(names)
print(mix_list)

print()
print("Calling individual item from list")
print(numbers[4])
print(names[2])
print(mix_list[1])

print()
print("Slicing")
print(numbers[2:])
print(names[:2])
print(mix_list[-1])

print()
print("step in slicing")
print(numbers[0:7:2])

print()
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print("append to list")
numbers.append(-200)
print(numbers)
print("inset at specific index")
numbers.insert(4,183)
print(numbers)
print("Add multiple objects to list at once at end of the list")
numbers.extend([555, 666,777])
print(numbers)
print("update the list at specific item")
numbers[4]=264
print(numbers)
print("Update the list at multiple items")
numbers[2:6]=[111, 222, 333, 111]
print(numbers)
print("remove")
numbers.remove(111)
print(numbers)
print("pop")
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
print(numbers.count(-200))


print(names)
names.reverse()
print(names)

