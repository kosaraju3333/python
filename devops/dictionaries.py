capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}

d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}

print(d1)
print(d2)

### Creating Dictionary
sports_players = {
    "player_1":{
        "Name":"Sachin",
        "Age": 50
    },
    "player_2": {
        "Name":"Virat",
        "Age": 37
    }
}
print(sports_players)

student_info = dict(name="Alice", age=21, major="Computer Science")
print(student_info)

### accessing Dictionary
player_1_name = sports_players["player_1"]["Name"]
player_1_age = sports_players["player_1"]["Age"]

print(player_1_name)
print(player_1_age)

### Modifying Dictionary Items
sports_players["player_1"]["Age"]=55
sports_players["player_2"]["Age"]=40

print(sports_players)

### Adding More info
sports_players["player_1"]["Bowling"]="Yes"
sports_players["player_2"]["Bowling"]="No"

print(sports_players)

## Removing info

del sports_players["player_1"]["Bowling"]
del sports_players["player_2"]["Bowling"]

print(sports_players)

### Iteration through Dictionary
## Listing through  keys
for key in sports_players:
    print(f"Key:{sports_players[key]}")

## Listing through  keys
for value in sports_players.values():
    print(value)

## Listing through key-value pairs

for key, value in sports_players.items():
    print(f"key: {key}, value: {value}")

#### Dictionaries methods:
print(sports_players.items())

print(sports_players.keys())

print(sports_players.values())

print(sports_players.get(key))


#### Python program to create a new dictionary by extracting the keys from a given dictionary.

d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2 = {}

for k in keys:
    d2[k]=d1[k]
print(d2)

### Python program to convert a dictionary to list of (k,v) tuples.

d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
L1 = list(d1.items())
print(type(L1))
print(L1)

### Python program to remove keys with same values in a dictionary.

d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
values =  list(d1.values())
d2={}
print(values)
uvalues = []

for uval in values:
    if values.count(uval)==1:
        uvalues.append(uval)

for k,v in d1.items():
    if v in uvalues:
        d = {k:v}
        d2.update(d)
print(d2)