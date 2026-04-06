import boto3
from pprint import pprint

s3_client = boto3.client("s3")

tagging = s3_client.put_bucket_tagging(
    Bucket='portal-spontansolutions',
    Tagging={
        'TagSet': [
            {
                'Key': 'Name',
                'Value': 'portal-app-bucket',
            },
            {
                'Key': 'Type',
                'Value': 'Production',
            },
            {
                'Key': 'Owner',
                'Value': 'DevOps-Team',
            },
            {
                'Key': 'Service',
                'Value': 'Portal-app',
            }
        ],
    },
)

pprint(tagging)