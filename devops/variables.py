print("***** Creating Variables and getting id's of variable *****")
month="May"
date=18
print(id(month))
print(id(date))

counter = 100
miles = 100.0
name = "RK"

print(id(counter), counter)
print(id(miles), miles)
print(id(name), name)

print("***** Getting Type of variable *****")
print(type(counter), counter)
print(type(miles), miles)
print(type(name), name)


## Type casting
print("***** Variable Type Casting *****")
x = str(10)
y = int(10)
z = float(10)

print("X = ", x)
print("Y = ", y)
print("Z = ", z)

# del counter
# print(counter)


#### Pythin variable are multi assign

a = 10
b =10
c = 10

print(id(a), id(b), id(c))

### Python Variable Naming convention
counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000

print (counter)
print (_count)
print (name1)
print (name2)
print (Age)
print (zara_salary)

#### Pythin local variable
def sum(a,b):
    sum = a + b
    return sum
print(sum(5,4))


#### Python Global Variable
e = 100
f = 200
def priv_sum():
    priv_sum = e + f
    return priv_sum
print(priv_sum())


###
count = 5
def update():
    global count
    count = count + 1
    print(count)
update()

