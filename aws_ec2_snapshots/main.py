import boto3

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

volumes = aws_client.describe_volumes()

for volume in volumes['Volumes']:
    snapshot = aws_client.create_snapshot(
        VolumeId=volume['VolumeId']
    )
    print(snapshot)