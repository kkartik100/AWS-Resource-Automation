import boto3

resource=boto3.client("s3")
resource.upload_file(
    Filename="upload.png",
    Bucket="testbucket01",
    Key="uploadtest.png")