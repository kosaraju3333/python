### Multiple return value in a single function
import statistics
def mean_median_mode(list1):
    ## It will return  in tuple
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)
    ## If we want to return in array
    #return [statistics.mean(list1), statistics.median(list1), statistics.mode(list1)]

# print(mean_median_mode([543,3,56,2,3,4,678,9]))
result=mean_median_mode([543,3,56,2,3,4,678,9])
print(result)

#### With single return statement the function can return multiple values
def mean_median_mode(list1):
    ## It will return  in tuple
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)
    ## If we want to return in array
    #return [statistics.mean(list1), statistics.median(list1), statistics.mode(list1)]

# print(mean_median_mode([543,3,56,2,3,4,678,9]))
a,b,c=mean_median_mode([543,3,56,2,3,4,678,9])
print(f"Mean is {a}\nMedian is {b},\nMode is {c}")

### Multiple return statements in a single function #####
def add(x,y):
    if x == 0 and y == 0:
        return "You have entered zero for both variables"
    else:
        return x + y

var1=int(input("Enter value for var1:\n"))
var2=int(input("Enter value for var2:\n"))

add_result=add(var1,var2)
print(add_result)



