import boto3

eks_client = boto3.client('eks')

clusters = eks_client.list_clusters()['clusters']

for clust in clusters:
    cluster_response = eks_client.describe_cluster(
        name=clust
    )
    cluster_info = cluster_response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']
    print(f"Status: {cluster_status} | Endpoint: {cluster_endpoint} | Version: {cluster_version}")
    