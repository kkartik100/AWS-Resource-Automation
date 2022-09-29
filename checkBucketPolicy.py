import boto3

resource = boto3.client("s3")

print(resource.get_bucket_policy(Bucket="testbucketnilesh")["Policy"])

