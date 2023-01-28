import boto3

aws_client = boto3.client("ec2", region_name="eu-central-1")
vpcs = aws_client.describe_vpcs()
vpcs = vpcs['Vpcs']

for vpc in vpcs:
    print(vpc["VpcId"])
    cidrs = (vpc["CidrBlockAssociationSet"])
    for cidr in cidrs:
        print(cidr["CidrBlockState"])