import boto3

resource = boto3.client("s3")

objects = resource.list_objects(Bucket = "03b86200652a-nutanix-cluster-hibernate")['Contents']

print(objects[0])

# for object in objects:
#     print(object) 