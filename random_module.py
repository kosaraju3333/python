import random

## Both a and b are included
a=random.randint(1,6)
print(a)

## Only a is included not b
b=random.randrange(1,6)
print(b)

## Get Float
c=random.random()
print(c)

d=random.uniform(23,1)
print(d)

### Chose random number from list
l=[12, -5, 34, 0, -3090]
print(l)
a=random.choice(l)
print(a)

### Shuffel the list
l=[12, -5, 34, 0, -3090]
print(l)
random.shuffle(l)
print(l)
