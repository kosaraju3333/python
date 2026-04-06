import boto3
from pprint import pprint
import json

s3_buckets_list = []

s3_client = boto3.client('s3')

response = s3_client.list_buckets()
# pprint(response)

for buckets in response["Buckets"]:
    # bucket_name=buckets["Name"]
    s3_buckets_list.append(buckets["Name"])
    # print(buckets["Name"])

print(s3_buckets_list)

# for bucket_name in s3_buckets_list:
#     response=s3_client.get_bucket_tagging(
#         Bucket=bucket_name
#         )
#     pprint(response)

response=s3_client.get_bucket_tagging(
        Bucket="portal-spontansolutions"
        )

pprint(response)