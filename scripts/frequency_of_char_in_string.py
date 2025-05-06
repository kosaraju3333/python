#### Find the frequency of a char in a string

name = "Ramakrishna"
cont = {}

for char in name.lower():
    if char in cont:
        cont[char] = cont[char] +1
    else:
        cont[char] = 1
print(cont)


print('Hello', 'World')
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist)




mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])