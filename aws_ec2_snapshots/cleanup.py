import boto3
from operator import itemgetter

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

snapshots = aws_client.describe_snapshots(
    OwnerIds=[
        'self'
    ]
)

# sort the list of dictionaries by the StartTime key
# uses itemgetter function from operator module
timestamp = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
print('######_SORTED_#####')
for now_sorted in timestamp:
    print(now_sorted['StartTime'])
print('######_UNSORTED_#####')
for snapshot in snapshots['Snapshots']:
    print(snapshot['StartTime'])