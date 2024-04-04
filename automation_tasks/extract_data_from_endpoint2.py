import requests
import json
from pprint import pprint

def people_craft(url):
    ISS_craft_people = []
    Tiangong_craft_people = []
    if(url != 'null'):
        url_response = requests.get(url)
        data = url_response.json()
        for person in data["people"]:
            if person['craft']=="ISS":
                ISS_craft_people.append(person['name'])
            else:
                Tiangong_craft_people.append(person["name"])
        print("Total number of persons in ISS" + str(len(ISS_craft_people)))
        print("Total number of persons in Tiangong" + str(len(Tiangong_craft_people)))

    else:
        print("Error Loading the URL")

#people_craft("gjfgdjhga")
people_craft("http://api.open-notify.org/astros.json")
