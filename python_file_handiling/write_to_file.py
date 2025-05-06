#### Open a file and write test , if file is not present it will create
file = open("test.txt","w")
file.write("Hello World...!!!")
print("Open file and written text successfully!!!...")

### Open a file in append mode and add the text to it...

file = open("test.txt","a")
file.write("\nWelcome to python file handling")
file.close()
print("Open file and appended  text successfully!!!...")


#### Writing to a File Using write() Method
with open("test.txt","w") as file:
    file.write("Hello World...!!!\n")
    file.write("Welcome to python file handling!!..12345\n")
print("File opened and written successfully!!")


##### Writing to a File Using writelines() Method

lines = ["Hello World...!!!\n", "Welcome to python file handling...!!!\n"]
with open("test.txt","w") as file:
    file.writelines(lines)
print("File opened and written successfully!!!...")
