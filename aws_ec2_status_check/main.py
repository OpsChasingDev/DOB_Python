import boto3

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

# returns state of all ec2 instances
instances = aws_client.describe_instances()
for reservation in instances["Reservations"]:
    server = reservation["Instances"]
    for s in server:
        print(f"Instance {s['InstanceId']} is {s['State']['Name']}")
