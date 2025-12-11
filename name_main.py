# print("HI.....")
# print(__name__)

def display(name):
    return name

def do_something():
    print("This function is doing something")

if __name__=="__main__":
    print("This is name_main.py")
    name=input("Enter your Name: ")
    print(display(name))
    do_something()