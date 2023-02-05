import boto3
from operator import itemgetter

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

instance_id = "i-05d9202e693a8893f"

volumes = aws_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

ec2_volume = volumes['Volumes'][0]
print(ec2_volume)