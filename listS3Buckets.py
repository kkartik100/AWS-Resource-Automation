import boto3

resource = boto3.resource("s3")
bucket_list = list(resource.buckets.all())

# for bucket in bucket_list:
#     print(bucket)  

print(len(bucket_list))
 