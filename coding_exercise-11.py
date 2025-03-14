### Toss Program
import random

print("This Program will give Head or Tail")
call=input("Call or Select 'HEAD or H' or 'Tail or T': ")
if random.randint(0,1):
    print("HEAD")
else:
    print("TAIL")
