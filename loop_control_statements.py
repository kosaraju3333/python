# number=int(input("Enter the  number range between 1 to 50: "))
# count=0
# while count < number:
#     print(count)
#     count=count+1
#     if count == 17:
#         break
from itertools import count

# number=int(input("Enter the  number range between 1 to 50: "))
# count=1
# while count <= number:
#     print(count)
#     count=count+1
#     if count == 3:
#         print("Hi Krish")
#         continue
#     print("Hi Ram")




# for i in range(1,7):
#     if i == 5:
#         continue
#     else:
#         print(i)


count=1
while count <= 10:
    count = count + 1
    if count == 5:
        continue
    print(count)