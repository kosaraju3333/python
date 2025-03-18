# set1={"Ram","Shyam","Virat"}
# set2={"Virat","Rohit","KL"}
# set3={"Raina","MSD"}
# ## Set Union
# print(set1.union(set2,set3))
# #          (OR)
# ## using operator (|)
# print(set1 | set2 | set3)
# #eg:here we can not perform Union operation between set and tuple
# #print(set1 | set2 | set3 | ("Gill","Virat"))
# ## perform Union operation between set and tuple or List
# print(set1.union(set2,set3,("Gill","Virat")))
#
# print(set1.union(set2,set3,["Jaddu","Iyer","Axar"]))
#
# ## Update or Modify the set using union
# set1.update(set2)
# print(set1)
# #       Or
# set1.update(["Varun","Kuldeep","virat"])
# print(set1)
#
# ## Set Intersection
# ## Set Intersection between 2 sets with instersection function
# print(set1.intersection(set2))
#
# ## Set Intersection between 3 sets
# print(set1.intersection(set2,set3))
# ## Inter section with the help of operator
# print(set1 & set2)
# print(set1 & set2 & set3)
#
# ## Pass List, Tuples to intersection function
# print(set1.intersection(["Ram","Krish"],("Krish","Ramki","Ram")))
#
# ### Update or Modify the set with common items using intersection
# set1.intersection_update(set2)
# print(set1)
# ### pass List or Tuple
# set2.intersection_update(["Ram","Krish","Jenny","Virat","KL"])
# print(set2)

# set1={"Ram","Shyam","Virat"}
# set2={"Virat","Rohit","KL"}
# set3={"Raina","MSD","Ram"}

# ## Difference in sets with method/function
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.difference(set2,set3))
#
# ## Difference in sets with operations
# print(set1 - set2)
# print(set2 - set1)
# print(set1 - set2 - set3)
#
# ## Difference in sets passing List or Tuples
# print(set1.difference(["Smith","Warner","Maxi"]))
#
# ##Update or Modify the set using difference
# # set1.difference_update(set2)
# # print(set1)
# # set2.difference_update(set1)
# # print(set2)
# set1.difference_update(["Krish","Shyam","Virat"])
# print(set1)

set1={"Ram","Shyam","Virat"}
set2={"Virat","Rohit","KL"}
set3={"Raina","MSD","Ram"}
# ## Symmetric Difference with method, we can not perform on multiple sets like on set1, set2, set3
# print(set1.symmetric_difference(set2))
# ## Symmetric Difference with Operation, Here we can perform on Multiple sets like set1, set2, set3
# print(set1 ^ set2 ^ set3)
#
# ## Update or Modify the set using symmetric difference
#
# set1.symmetric_difference_update(set2)
# print(set1)
# set2.symmetric_difference_update(set3)
# print(set2)
# ### Passing Tuple or List or set
# set3.symmetric_difference_update({"MSD","YV"})
# print(set3)