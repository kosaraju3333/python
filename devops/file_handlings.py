# ### Open files
# # Opening a file in read mode
# file = open("error.log", "r")
#
# # Opening a file in write mode
# file = open("error.log", "w")
#
# # Opening a file in append mode
# file = open("error.log", "a")
#
# # Opening a file in binary read mode
# file = open("error.log", "rb")

#### Open a file and write a data
file = open("error1.log", "w")
file.write("New File\nsecond line\nThird line\nfourth line")
file.close()

### Read a file
### Read lines function will read all list as a list
readfile = open("error.log", "r")
print("#### readlines()###")

print(readfile.readlines())

### Read the entire file
read_file = open("error.log", "r")
print("#### read()###")
print(read_file.read())

### Read the entire file line by line
read_line_by_line = open("error.log", "r")
print("#### readline()###")
print(read_line_by_line.readline())