import os
### Current working directory
print(os.getcwd())

### List files in Current Working directory
### This will give in a list
print(os.listdir("/Users/ramakrishnakosaraju/spontansolutions/python"))
# list_dir = os.listdir("/Users/ramakrishnakosaraju/spontansolutions/python")
# for list in list_dir:
#     print(list)

### Creating directory
# os.mkdir("/Users/ramakrishnakosaraju/spontansolutions/python/test123456789.py",777)

# ### Create nested directories
# os.makedirs("test123/test345")

# ### remove a file
# os.remove("../error1.log")

# ### remove empty directory
# os.rmdir("../../test123456789.py")

# ## Rename file or folder
# os.rename("../app.log", "app-error.log")

## Join paths
print(os.path.join("test", "test.log"))

### Check if file exists
if os.path.exists("../lists.py"):
    print("file exists")
else:
    print("file not exists")

## Check if path is file or directory
print(os.path.isfile("../lists.py"))
print(os.path.isdir("../lists.py"))

### Read environment variable
print(os.getenv("USER"))
print(os.getenv("HOME"))

## Get ENV with default Variables
print(os.getenv("USER1", "KRK"))

## Set ENV
os.environ["app_name"]="Bank-app"
print(os.getenv("app_name"))

## get OS Name
print(os.name)

print(os.walk())