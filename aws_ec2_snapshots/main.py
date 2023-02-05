import boto3

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

