# a=range(0,15,2)
# ###Here
# # i=0, j=15, k=2
# ### formula = i + i+k + i+2k + i+3k ....j-1
# for i in a:
#     print(i)
#
# b = range(10,0,-1)
# for i in b:
#     print(i)
#
# c = range(-1,-10,-2)
# for i in c:
#     print(i)

### Program to find the total sum of numbers from 1 to 100
numbers=range(1,101)
total_sum=0
for number in numbers:
    total_sum=total_sum + number
print(f"Total sum of range(0,101) is: {total_sum}")