### Function with single return value
def add(a,b):
    c = a+b
    print(c)
add(5,4)

### Function with return statement and with return value.
def add(a,b):
    c = a+b
    return c

result = add(7,4)
print(result)

### Function with return statement without return value.
def add(a,b):
    c = a+b
    return
result = add(4,4)
print(result)


