### Program to calculate number of paint cans are required to paint a area in square Meters
import math

h=int(input("Enter the height of wall in meters:\n"))
w=int(input("Enter the width of wall in meters:\n"))


def paint_cans_cal(height,width,coverage=7):
    #area = height * width
    no_of_cans=math.ceil((height * width)/coverage)
    print(f"Number of paint cans required is:  {no_of_cans}")


paint_cans_cal(height=h,width=w)