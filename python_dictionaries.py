##  Declare the dictionary
phone_no={
     "Ram": 123,
    'shyam':456,
    'Mohan': 789
}
print(phone_no)
#### add the item in dictionary
phone_no['Mohan12']=123
print(phone_no)
#
# ###
# phone_no['shyam']={'work_no': 111, 'home_no': 222}
# print(phone_no)
# print(phone_no['shyam']['home_no'])
#
# ## Delete item from dic
# #
# # del phone_no['Mohan']
# # print(phone_no)

## POP or delete particular item, and it will return only deleted key VALUE only not both key and value
# print(phone_no.pop('Mohan'))
# print(phone_no)

## Pop or delete last item, and it will return key value
# print(phone_no.popitem())
# print(phone_no)

# phone_no.clear()
# print(phone_no)

## Access only keys
print(phone_no.keys())

## Access Only Keys
print(phone_no.values())

### Access or Print dic items
print(phone_no.items())

### Create new dict from existing dict
phone_no2=phone_no.copy()
print(phone_no2)

### Length of Dic
print(len(phone_no))








### Another way to declare the dictionary
#
# phone_no=dict({
#      "Ram": 123,
#     'shyam':456,
#     'Mohan': 789
# })
#
# print(phone_no)

#### Update the item in dictionary
