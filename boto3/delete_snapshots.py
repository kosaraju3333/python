import boto3
from pprint import pprint

## Open AWS Console
aws_console = boto3.Session(profile_name='boto3-user')

## Open ec2 Console
ec2_console_client = aws_console.client(service_name='ec2', region_name='us-east-1')

## empty_list
list_snapshots = []
## ec2_snapshot client method to list all available snapshots
snapshots_list = ec2_console_client.describe_snapshots(
     OwnerIds=[
        'self',
    ]
    #  SnapshotIds=[
    #     'snap-0fb9c051bb7d1a6d0'
    # ]
)['Snapshots']
for value in snapshots_list:
     snapshot_id = value['SnapshotId']
    #  print('snapshot ids: ', value['SnapshotId'])
     list_snapshots.append(snapshot_id)

print(list_snapshots)