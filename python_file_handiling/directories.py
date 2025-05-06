import os
import shutil
from time import process_time

######## check whether the given directory path exists using the os.path.exists() function −
directory_path = "/Users/ramakrishnakosaraju/spontansolutions"
if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' is exists")
else:
    print(f"The directory '{directory_path}' does not exists")


####### creating a new directory using the os.makedirs() function −
new_dirs = "/Users/ramakrishnakosaraju/spontansolutions/python/test123/test456/test789"
# os.makedirs(new_dirs)
try:
    os.makedirs(new_dirs)
    print(f"Directory '{new_dirs}' created successfully.")

except FileExistsError as e:
    print(f"Error: Failed to create directory '{new_dirs}'. {e}")

####### creating a new directory using the os.mkdir() function −
new_dir_path = "/Users/ramakrishnakosaraju/spontansolutions/python/new_dir_txt"
try:
    os.mkdir("/Users/ramakrishnakosaraju/spontansolutions/python/new_dir_txt")
except OSError as e:
    print(f"Directory {new_dir_path} already exists. {e} ")


##### Get Current Working Directory #####
print(os.getcwd())

## List Files and Directories ######
dir_path = "/Users/ramakrishnakosaraju/spontansolutions/python"
try:
    content = os.listdir(dir_path)
    print(f"Contents of '{dir_path}':")
    for item in content:
        print(item)
except NotADirectoryError as e:
    print(f"Error: Failed to list contents it is NOT a directory '{dir_path}'. {e}")

### Changing the Current Working Directory
new_dir = "/Users/ramakrishnakosaraju/spontansolutions/shell_script"
try:
    os.chdir(new_dir)
    print(f"Changed to new dir {new_dir}")
    print(f"Now Listing all files in {new_dir} directory")
    files = os.listdir(new_dir)
    # files = os.system("ls -l")
    print(files)
    for file in files:
        if os.path.isfile(file):
            print(f"{file} is a file")
        else:
            print(f"{file} is not a file")
except OSError as error:
    print(f"Not changed to new dir {new_dir}. {error}")


###### delete an empty directory in Python
dir_name = ["/Users/ramakrishnakosaraju/spontansolutions/python/new_dir_txt", "/Users/ramakrishnakosaraju/spontansolutions/python/test123"]
try:
    for directory in dir_name:
        os.rmdir(directory)
        print(f"removed/deleted {dir_name} directory")
except OSError as e:
    print(f"Directory {dir_name} not deleted--: {e}")

###### delete a NON-empty directory in Python
dir_name = ["/Users/ramakrishnakosaraju/spontansolutions/python/test123"]
try:
    for directory in dir_name:
        shutil.rmtree(directory)
        print(f"removed/deleted {dir_name} which is NON-EMPTY directory")
except OSError as e:
    print(f"Non-empty - Directory {dir_name} not deleted--: {e}")