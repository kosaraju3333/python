tuple1=(3,56,9,-11,56)
# for i in tuple1:
#     print(i)
#     if i == 9:
#         break
# else:
#     print("Loop successfully completed and we are in else block now!!!")

for i in tuple1:
    if i%6==0:
        print(i)
        break
    # else:
    #     print(f"{i} is not divisible by 6")
else:
    print(f"all items in tuple are not divisible by 6")