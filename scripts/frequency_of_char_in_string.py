#### Find the frequency of a char in a string

name = "Ramakrishna"
count = {}

for char in name.lower():
    if char in count:
        count[char] = count[char] +1
    else:
        count[char] = 1
print(count)


