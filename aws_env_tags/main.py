import boto3

aws_client_paris = boto3.client("ec2", region_name="eu-west-3")
aws_resource_paris = boto3.resource("ec2", region_name="eu-west-3")

aws_client_germany = boto3.client("ec2", region_name="eu-central-1")
aws_resource_germany = boto3.resource("ec2", region_name="eu-central-1")

ids_paris = []
ids_germany = []

# set tags for Paris region instances
reservations_paris = aws_client_paris.describe_instances()["Reservations"]
for instance in reservations_paris:
    instances = instance["Instances"]
    for instance in instances:
        ids_paris.append(instance["InstanceId"])

aws_resource_paris.create_tags(
    Resources=ids_paris,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'production'
        },
    ]
)

# set tags for Germany region instances
reservations_germany = aws_client_germany.describe_instances()["Reservations"]
for instance in reservations_germany:
    instances = instance["Instances"]
    for instance in instances:
        ids_germany.append(instance["InstanceId"])

aws_resource_germany.create_tags(
    Resources=ids_germany,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'development'
        },
    ]
)