set1={"Ram","Shyam","Virat"}
set2={"Virat","Rohit","KL"}
set3={"Raina","MSD","Ram"}

## Disjoint
## Moduel
print(set1.isdisjoint(set2))
print(set2.isdisjoint({"Ram","Krish"}))

## Subset
## set 1 is subset of set2 if every element of set1 is in set2
#Module
print(set1.issubset(set2))
print(set2.issubset(["Virat","King","SKY","Rohit","Hardik","KL"]))
## Operation
print(set1 <= set2)

## Superset
## set 1 is superset of set2 if set1 contains every element of set2.
print(set1.issuperset(set2))
print(set1.issuperset({"Ram","Shyam","Virat"}))
## Operation
print(set1 >= set2)

## Del
## Clear will delete the set items only not sets.
## Delete the set as well
del set2
