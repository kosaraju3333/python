a = int(input('Enter a Value:' ))
b = int(input('Enter b Value:' ))

def sum(a,b):
    SUM = a + b
    return SUM

def difference(a,b):
    DIFFERENCE = a - b
    return DIFFERENCE

def product(a,b):
    PRODUCT = a * b
    return PRODUCT

def quotient(a,b):
    QUOTIENT = a / b
    return QUOTIENT

print("SUM of a and b is:", sum(a,b))
print("DIFFERENCE of a and b is:", difference(a,b))
print("PRODUCT of a and b is:", product(a,b))
print("QUOTIENT of a and b is:", quotient(a,b))
    