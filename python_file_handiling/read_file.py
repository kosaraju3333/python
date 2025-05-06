######## Reading a File Using read() Method
file = open("test.txt","r")
content = file.read()
print(content)
file.close()

####### Reading a File Using readline() Method
file = open("test.txt","r")
line = file.readline()
print(line)
file.close()


######## Reading a File Using readlines() Method
file = open("test.txt","r")
lines_list = file.readlines()
print(lines_list)
for line in lines_list:
    print(line,end='')
file.close()

######## Using with statement ########
with open("test.txt","r") as file:
    content =  file.read()
    print(content)

with open("test.txt","r") as file:
    line = file.readline()
    while line:
        print(line,end="")
        line = file.readline()
print()

with open("test.txt","r") as file:
    lines_list = file.readlines()
    for line in lines_list:
        print(line,end="")