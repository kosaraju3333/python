def fun1(a,b):
    c = a + b
    print(f"Function1 print : {c}")

output1 = fun1(3,7)
print(f"Function1: {output1}")

def fun2(a,b):
    c = a + b
    return c

output2 = fun2(3,5)
print(f"Function2: {output2}")


def fun3(x):
    z=x+1
    return z
output3 = fun3(output2)
print(f"Function3: {output3}")