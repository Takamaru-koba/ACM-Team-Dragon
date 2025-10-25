import os
from dotenv import load_dotenv
import boto3

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

# Create an S3 client
s3 = boto3.client(
    service_name="s3", 
    aws_access_key_id=access_key_id, 
    aws_secret_access_key=secret_access_key,
    region_name="us-east-1"
)

# List all objects in the bucket
response = s3.list_objects(Bucket=bucket_name)

# Print the object details
print("Objects in the bucket:")
for obj in response.get("Contents", []):
    print(f"- {obj['Key']} (Last modified: {obj['LastModified']})")
