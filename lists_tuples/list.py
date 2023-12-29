# Creating Lists
servers_list = ["dev-server", "staging-server", "prod-server"]
number_list = [40, 5, 1, 30]

# Printing List
print(servers_list)

# Printing Particular element from list
print(servers_list[2])

# append element to list
servers_list.append("DevOps-server")
print(servers_list)

# remove element from list
servers_list.remove("DevOps-server")
print(servers_list)

# Find Length of list
servers_list_length = len(servers_list)
print("Length of server_list is:", servers_list_length )

# Slicing the list
servers_list_slice = servers_list[0:2]
print("servers list slice:"), servers_list_slice

# Sort the list
number_list.sort()
print(number_list)