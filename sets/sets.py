# Creating Set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding to set
my_set.add(6)
# Removing from set
my_set.remove(3)

print(my_set)


#Set Operations
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6}

Union_set = set1.union(set2) # add two sets
print("Union set: ", Union_set)

intersection_set = set1.intersection(set2)
print("intersection set: ", intersection_set)

difference_set = set1.difference(set2)
print("difference set: ", difference_set)


#Subset and Superset:
is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2

print(is_subset)
print(is_superset)