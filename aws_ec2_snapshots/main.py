import boto3
import schedule

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

def create_snapshot():
    volumes = aws_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )

    for volume in volumes['Volumes']:
        snapshot = aws_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(snapshot)

schedule.every(15).seconds.do(create_snapshot)

while True:
    schedule.run_pending()