## Open File and read the file
file = open("test.py")
print(file.read())

# Create a File
file = open("new_text.txt", "x")

# Write to file

file = open("new_text_1.txt", "w")
file.write("This file is created using python scripting")
#file.write("This file is created using python scripting" + "\n")
file.close

## Read a File

file = open("new_text_1.txt", "r")
print(file.read())
file.close

## Append a File

file = open("new_text_1.txt", "a")
file.write("\n" + "appended the text uisng python script")
file.close