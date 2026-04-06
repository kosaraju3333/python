import requests

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}

# x = requests.get(url)

# #print the response text (the content of the requested file):

# print(x.json())


git_url = "https://api.github.com/orgs/spontansolutions/repos"

respons=requests.get(git_url)

# print(respons)
print(respons.headers)

# repo_list = respons.json()
# print(repo_list)