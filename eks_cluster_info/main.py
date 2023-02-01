import boto3

eks_client = boto3.client('eks')

clusters = eks_client.list_clusters()['clusters']

for clust in clusters:
    cluster_response = eks_client.describe_cluster(
        name=clust
    )
    cluster_status = cluster_response['cluster']['status']
    print(cluster_status)
    