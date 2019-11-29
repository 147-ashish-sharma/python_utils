import boto3
import uuid
from botocore.exceptions import ClientError
bucket_prefix = "mytest"
s3_connection = boto3.resource('s3')
# s3_client = boto3.client('s3')
def create_bucket_name(prefix):
    return ''.join([prefix, str(uuid.uuid4())])
def my_create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': current_region})
    print(bucket_response)
try:
    my_create_bucket(bucket_prefix, s3_connection)
except ClientError as e:
    logging.error(e)
