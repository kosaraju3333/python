import requests

url = "https://api.github.com/repos/hashicorp/terraform/pulls"

response = requests.get(url)

print(response)

pull_requests = response.json()
print(pull_requests)
