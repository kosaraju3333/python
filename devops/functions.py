############################## Default arguments ####################################
## Example 1:
def show_info(name,city="Bangalore"):
    print("Name: ", name)
    print("City: ", city)

show_info("Ram")
show_info("RK","Hyderabad")
## Example: 2
def fcn(nums, numericlist=[]):
    numericlist.append(nums + 1)
    print(numericlist)
# function calls
fcn(66)
fcn(68)
fcn(70)

################################## Keyword Arguments ######################################
## Example 1:
print("########## Keyword Arguments #############")
def printinfo(name, age):
    print("Name: ", name)
    print("Age:", age)

printinfo(name="Abc",age=23)

## Example 2:
def greet(name,dept):
    print(f"Welcome to {dept}, {name}")
greet(name="KRK",dept="ECE")

### pass only Keyword Arguments to functions
## neted put "*" infront of argument you mentined in function argument.
## in below example dept is key work argument because we mentioned * in from of dept argument
# so, it has to be keyword argument only
def greet(name,*,dept):
    print(f"Welcome to {dept}, {name}")
greet("KRK",dept="ECE")

####################################### Positional Arguments ###############################
print("########## Positional Arguments #############")
def student_info(name, dept, age):
    print("Name: ", name)
    print("Dept: ", dept)
    print("Age: ", age)

student_info("RKR", "CSE", 23)
student_info("CSE", 23, "RKR")

### pass only positional Arguments to functions
## in below example we mentioned * in arguments so, it has to be positional argument only, no key works argument
def student_info(name, dept, age,/):
    print("Name: ", name)
    print("Dept: ", dept)
    print("Age: ", age)

student_info("RKR", "CSE", 23)

######################## Arbitrary Arguments (*args) ######################
print (f"################### Arbitrary Arguments (*args) ###################")
### Example 1:
def sum_of_nums(*args):
    sum = 0
    for i  in  args:
        sum = sum + i
    return sum
print(sum_of_nums(1,2,3,4,5,6,7,8,9))

### Example 2:
def example(num, *args):
    second_arg = max(args)
    sum_max = num  + second_arg
    return sum_max
print(example(100,1,2,3,4,5,6,7,8,9))

########################## Arbitrary Keyword arguments #####################
print(f"########################## Arbitrary Keyword arguments #####################")
def sports_person_info(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

sports_person_info(Name="Sachin", Age=45, Batting="yes", Bowling="Yes")
sports_person_info(Name="Virat", Age=35, Batting="Yes", Bowling="NO")


####
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)