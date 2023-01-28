import boto3

aws_client = boto3.client("ec2", region_name="eu-central-1")
aws_resource = boto3.resource("ec2")

new_vpc = aws_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)
new_vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'new-vpc'
        }
    ]
)

vpcs = aws_client.describe_vpcs()
vpcs = vpcs['Vpcs']

for vpc in vpcs:
    print(vpc["VpcId"])
    cidrs = (vpc["CidrBlockAssociationSet"])
    for cidr in cidrs:
        print(cidr["CidrBlockState"])