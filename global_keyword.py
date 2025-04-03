#### First one ####
a=100
def display():
    global a
    a=a+1
    print(a)
display()


###########

def display():
    a = 20
    def show():
        global a
        a = 30
    print(f"Value of a Before calling show() function is {a}")
    show()
    print(f"Value of a after calling show() function is {a}")
display()
print(a)