import requests
import json
from socket import timeout
import logging
from pprint import pprint

def list_category(url):
    category_list = set()
    if(url!="null"):
        url_response = requests.get(url)
        data = url_response.json()
        for i in data["entries"]:
            category = i["Category"]
            category_list.add(category)
        print(category_list)
        print("length of the set:", len(category_list), type(category_list))
    else:
        print("Error Loading the URL")

def links_status(url):
    list_link = []
    if(url!="null"):
        url_response = requests.get(url)
        data = url_response.json()
        for link in data["entries"]:
            links = link["Link"]
            print(links)
            try:
                data2 = requests.get(links,timeout=10)
                if (data2.status_code==200):
                    list_link.append(links)
                    print(list_link)
                else:
                    print("status code is not 200")
            except requests.exceptions.Timeout:
                logging.error("timeout")
        print(list_link)
    else:
        print("Error Loading the URL")


list_category("https://api.publicapis.org/entries")
links_status("https://api.publicapis.org/entries")

