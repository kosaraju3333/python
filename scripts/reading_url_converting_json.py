import requests

git_url = "https://api.github.com/orgs/spontansolutions/repos"

# Getting the url response using request.get() method, out of response is in JSON format
response = requests.get(git_url)

# Converting the above response JSON output to list of dictionaries
repo_lists = response.json()

# Checking data_type of repo_lists
print("type of repo_lists:", type(repo_lists))

# Checking Length 
print(len(repo_lists))

# Printing the name from list of dictionaries
print(repo_lists[0]["name"])
print(repo_lists[1]["name"])
print(repo_lists[2]["name"])
print(repo_lists[3]["name"])

# Iterating the list of dictionaries
for repos in repo_lists:
    repo_name = repos["name"]
    print("sponata_repos:", repo_name)

# iterate the list
list = [1, 2, 3, 4]
for l in list:
    print(l)

