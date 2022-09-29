import boto3

client = boto3.client("ec2")

vpcs = client.describe_vpcs( )

no_vpcs = vpcs['Vpcs']

print(len(no_vpcs))

for vpc in no_vpcs:
    print(vpc['VpcId'])