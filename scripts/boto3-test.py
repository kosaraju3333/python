import boto3
import requests
from datetime import datetime, timezone

# Create EC2 client
ec2 = boto3.client('ec2')

response = ec2.describe_instances()

print(response)

