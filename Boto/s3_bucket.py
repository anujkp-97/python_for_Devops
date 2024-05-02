import boto3

client = boto3.client('s3')

response = client.create_bucket(
    
    Bucket='anuj-radhaswamiji-boto3-123',
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}

    
)
# response = client.delete_bucket(
#     Bucket='anuj-radhaswamiji-boto3-123',
#     ExpectedBucketOwner='964852290492'
    
# )


# s3 = boto3.client('s3')
# s3.create_bucket(Bucket='anuj-radhaswamiji-234',
#     CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
