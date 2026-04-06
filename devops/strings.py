### Single line string
print("This is a String")

## Assigning String to variable
content = "This is a String"
print(content)

### Multi lines string ####
multi_lines = """"This a multi line sting,
we can write string in multiple lines. 
This is important."
"""
print(multi_lines)

##########  Strings are Array #######
string = "Strings are Array"
print(string[0:4])

#### Looping through a String
for i in string:
    print(i)

### Length of string

print(len(string))

#### Check string
text = "The best things in life are free!"
print("free" in text)

if "free" in text:
    print("Yes 'free' is present")

if "free" not in text:
    print("Yes 'free' is not present")
else:
    print("'free' is present")

##########  Strings are Array #######
string = "Strings are Array"
### slice from starting
print(string[:4])

### slice from Ending
print(string[3:])

### Negative indexing slicing
b = "Hello, World!"
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
print(b[-5:-2])

## Modify String
string = "Strings are Array"
## Upper()
print(string.upper())
## Lower()
print(string.lower())

### Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "
print(a.strip())

## Replacing string
## replace()
string = "Strings are Array"
print(string.replace("r","t"))

## Split String
## split()
print(string.split(" "))
print(type(string.split(" ")))


####### String Concatenation #######
a = "My name is"
b = "abcd"
Name = a + b
print(Name)

a = "My name is"
b = "abcd"
Name = a + " " + b
print(Name)

#### String Formate ####
### This will give error
# age = 35
# txt = "My name is abcd I am " + age
# print(txt)

## F string
age = 35
txt = f"My name is abcd I am + {age}"
print(txt)

## Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

txt = f"New price is: {50 * 30}"
print(txt)

#Escape Character
txt = "We are the ***so-called*** \\\n \"Vikings\" from the north."
print(txt)

###########
## Python program to find number of vowels in a given string.
mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count = 0
for x in mystr:
   if x.lower() in vowels:
        count = count + 1
print(f"Number of vowels in a given string is : {count}")

## Python program to drop all digits from a string.
mystr1 = 'He12llo, Py00th55on!'
digits = []
new_str = []
for num in range(10):
    digits.append(str(num))
print(digits)
for char in mystr1:
    if char not in digits:
        new_str.append(char)
newstr = ''.join(new_str)
print(newstr)
print(digits)

# digits1 = [str(x) for x in range(10)]
# print(digits1)





