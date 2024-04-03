import json

## Open Json file
s3_file = open('s3_bucket_data.json')



## return JSON Object as a dictionary 
data = json.load(s3_file)

## Iterating through the json list
for i in data["Versions"]:
    print(i['StorageClass'])


# Closing file
s3_file.close()