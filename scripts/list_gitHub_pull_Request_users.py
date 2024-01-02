import requests

git_hub_pull_url = "https://api.github.com/repos/hashicorp/terraform/pulls"

response = requests.get(git_hub_pull_url)
user_details = response.json()
print(user_details[2]["user"]["login"])