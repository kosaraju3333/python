## This Program is example for Environment Variables.

# To access environment variables we nedd OS package, we have imported os here
import os


# To Run shell command in python
os.system('echo "Listing all github public repos"')

# Lets say for example if we want to access github and list all public repos we need github USERNAME 
# Here i'm using GITHUB_USERNAME as environment varaiable  
github_username = os.getenv("GITHUB_USERNAME")
print("Your git hub username is:", github_username)

