### Program to find maximum number from a set of numbers

numbers=input("Enter the numbers with space separator: ").split()
print(numbers)
max_number=0
length_array=0

### Finding the length of array
for l in numbers:
    length_array=length_array+1
print(f"length of array is: {length_array}")

### Convert list of strings to int
for i in range(0,length_array):
    ## Converted list of string to list of int
    numbers[i]=int(numbers[i])
    if numbers[i] > max_number:
        max_number=numbers[i]
print(f"Max number is : {max_number}")




