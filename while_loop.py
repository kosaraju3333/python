# count=10
# while count > 5:
#     print(count)
#     count = count -1
#     if count == 7:
#         break
# else:
#     print("in while else")
# print("Out From Loop")
# count=1

# while True:
#     print(count)
#     count=count+1
#     if count == 50:
#         break

total=0
number=int(input("Enter a number  0 to quite: "))
while number != 0:
    total=total+number
    number = int(input("Enter the 0 to quite: "))
print(f"total is {total}")
