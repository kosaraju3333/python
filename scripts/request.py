import requests
from pprint import pprint

response = requests.get("https://api.github.com").json()

# print(type(response))
pprint(response)

# data=response.json()
# print(data)