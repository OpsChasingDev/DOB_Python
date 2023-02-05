# got some hard coded stuff in here - caution

import boto3
from operator import itemgetter

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

instance_id = "i-05d9202e693a8893f"

# get volumes for prod ec2 instance
volumes = aws_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

ec2_volume = volumes['Volumes'][0]

# get latest snapshot for desired volume
snapshots = aws_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [ec2_volume['VolumeId']]
        }
    ]
)
latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

# create the new volume from the snapshot
new_volume = aws_client.create_volume(
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="us-east-1d",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)

# loop to verify the new volume is ready to be attached
while True:
    vol = aws_resource.Volume(new_volume['VolumeId'])
    print(vol.state)
    # attach newly created volume to ec2 instance when volume is ready
    if vol.state == 'available':
        aws_resource.Instance(instance_id).attach_volume(
            VolumeId=new_volume['VolumeId'],
            # the device has the last character manually modified because we cannot attach the new volume on the same device already added to the ec2 instance
            Device='/dev/xvdb'
        )
        break