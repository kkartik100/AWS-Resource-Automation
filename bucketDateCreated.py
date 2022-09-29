import boto3

resource = boto3.client("s3")

# name = resource.list_buckets()["Buckets"][0]["Name"]
# print(name)

# creation_date=resource.list_buckets()["Buckets"][0]["CreationDate"]
# print(creation_date)

for bucket in resource.list_buckets()['Buckets']:
    print(bucket['Name'])
    print(bucket['CreationDate'])
    print("\n")