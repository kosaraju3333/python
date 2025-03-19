### Program to calculate average height from a list of heights

heights=input("Enter the heights in '''CM''' with comma(,) separator: ").split(",")
print(heights)

array_length=0
sum_heights=0

for height in heights:
    array_length = array_length + 1
    sum_heights = sum_heights + float(height)
else:
    average_height = round(sum_heights/array_length)
    print(f"Average height is: {average_height}")




