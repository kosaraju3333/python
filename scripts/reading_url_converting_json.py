import requests

git_url = "https://api.github.com/orgs/spontansolutions/repos"

# Getting the url response using request.get() method, out of response is in JSON format
# get the response code like 200, 505, 403 (eg: "<Response [200]>") use below command 
response = requests.get(git_url)

# If you want to print the output of the url use below command 
print(response.text)

# Converting the above response JSON output to list of dictionaries
repo_lists = response.json()

repos_name_list = []

# Iterating the list of dictionaries
def spontan_repos_list():
    for repos in repo_lists:
        repo_name = repos["name"]
        repos_name_list.append(repo_name)
    return repos_name_list

spontan_repos_list()
print(repos_name_list)

# Checking data_type of repo_lists
print("type of repo_lists:", type(repo_lists))

# Checking Length 
print(len(repo_lists))

# Printing the name from list of dictionaries
print(repo_lists[0]["name"])
print(repo_lists[1]["name"])
print(repo_lists[2]["name"])
print(repo_lists[3]["name"])