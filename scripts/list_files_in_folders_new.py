import os
import sys

## The split() method splits a string into a list.
folders = input("Enter the folders paths with spaces: ").split()
# #files = os.listdir("/Users/ramakrishnakosaraju/spontansolutions/scripts")
# files = os.listdir(sys.argv[1])

print(folders)

## First check if the given paths are exists are not
for folder in folders:
    isExist = os.path.exists(folder)
    if isExist == True:
        print(folder, " path is exists")
        ## Second we are checking the given path is Directory or not
        is_dir = os.path.isdir(folder)
        if is_dir == True:
            print(folder, "Is a DIRECTORY")
            files = os.listdir(folder)
            print(files)
        else:
            print(folder, "Is a NOT a DIRECTORY")
    else:
        print(folder, "path is not exist")

#print(isExist)
    #print(folder, "is exists")




######## Using Functions #######
def list_dir(dir_path):
    files = os.listdir(dir_path)
    return files

def main():
    dir_paths = input("Enter the folders paths with spaces: ").split()
    for dir_path in dir_paths:
        isExist = os.path.exists(dir_path)
        if isExist == True:
            print(dir_path, " path is exists")
            ## Second we are checking the given path is Directory or not
            is_dir = os.path.isdir(dir_path)
            if is_dir == True:
                print(dir_path, "Is a DIRECTORY")
                files_in_dir = list_dir(dir_path)
                print(files_in_dir)
            else:
                print(dir_path, "Is a NOT a DIRECTORY")
        else:
            print(dir_path, "path is not exist")

if __name__ == "__main__":
    main()  
