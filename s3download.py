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

# Path of the file in S3
object_key = "file/location/someFile.txt"

# save the file in the current directory.
local_file_path = "./someFile.txt"

# Download the object from S3
s3.download_file(bucket_name, object_key, local_file_path)

print(f"Object '{object_key}' downloaded to '{local_file_path}'")
