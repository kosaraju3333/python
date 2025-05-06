###################################################### Reading #########################################################

# ###### Reads the entire file #######

# #we are using the read() method to read the whole file into a single string −

# #### First Open a file #####
# file = open("welcome.txt","r")
# ### read() function reads the entire file content
# content = file.read()
# print(content)



####  we are using the readline() method to read one line at a time, making it memory efficient for reading large files line by line
# ####### Reads one line ata time #####
# #### First Open the file #####
# file = open("welcome.txt","r")
# line = file.readline()
# ### This prints only first line only
# print(line,end='')


###### Loop the lines in file ######
### Open the file ####
# file = open("welcome.txt","r")
# line = file.readline()
# while line:
#     print(line,end='')
#     line = file.readline()


### Now, we are using the readlines() method to read the entire file and splits it into a list where each element is a line
#### Open the file #####
# file = open("welcome.txt","r")
# lines = file.readlines()
# print(lines)
# #### Iterating the list form above lines  list
# for i in lines:
#     print(i,end='')

################################################### WRITING ############################################################
#### we are using the write() method to write the string passed to it to the file.
#### Writing to a file ######
# file = open("welcome.txt","w")
# new_content = file.write("test12345")
# print(new_content)

######## OR #########
# with open("welcome.txt","w") as file:
#     file.write("Hello, World..!!!\nWelcome to Python....")
#     print("Content is added successfully")


###### we are using the writelines() method to take a list of strings and writes each string to the file. It is useful for writing multiple lines at once

# lines = ["First line\n", "Second Line\n", "Third Line\n"]
# with open("welcome.txt","w") as file:
#     file.writelines(lines)
#     print("Content is added successfully")


################################################# CLOSING ##############################################################
file = open("welcome.txt","w")
file.write("This is an example....!!!!")
file.close()
print("File closed successfully!!")


#### "with" statement file close automatically ######
with open("welcome.txt","w") as file:
    file.write("In with, file will close automatically...!!!!")
    print("File closed successfully!! in WITH")



try:
   file = open("welcome.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")