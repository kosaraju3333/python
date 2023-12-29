# Creating tuple
aws_admin_names = ("RAM", "KRISH", "RAMKI")

#tuple append, remove will not work because TUPLE is a IMMUTUBLE

#Length of tuple
print("Length:", len(aws_admin_names))

# Print first element from tuple
first_element = aws_admin_names[0]
print("First-element:", first_element)

# Concatenating Tuples
new_aws_admin_names = aws_admin_names + ('NEEL' , 'sunil')
print("NEW admin list:", new_aws_admin_names)

# Checking for an Element
is_present = 'RAM' in aws_admin_names
print("is present:", is_present)