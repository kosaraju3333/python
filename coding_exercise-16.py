### Program to calculate sum of even numbers from 1 to 100, including 1 and 100

numbers=range(1,101)
sum_even_number=0
for number in numbers:
    if number%2==0:
        sum_even_number=sum_even_number+number
print(f"Total sum of even numbers from range 1 to 100 is: {sum_even_number}")