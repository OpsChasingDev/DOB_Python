import boto3

aws_client_paris = boto3.client("ec2", region_name="eu-west-3")
aws_resource_paris = boto3.resource("ec2", region_name="eu-west-3")

ids_paris = []

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