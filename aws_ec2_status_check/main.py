import boto3
import schedule

aws_client = boto3.client("ec2", region_name="us-east-1")
aws_resource = boto3.resource("ec2", region_name="us-east-1")

# return health check of all ec2 instances
def instance_status_check():
    statuses = aws_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses["InstanceStatuses"]:
        instance_status = status["InstanceStatus"]["Status"]
        system_status = status["SystemStatus"]["Status"]
        state = status["InstanceState"]["Name"]
        print(f"Instance: {status['InstanceId']} | Status: {instance_status} | System: {system_status} | State: {state}") 

schedule.every(5).seconds.do(instance_status_check)

while True:
    schedule.run_pending()