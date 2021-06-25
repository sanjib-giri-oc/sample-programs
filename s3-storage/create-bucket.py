import boto3
import json

with open('configuration.json', 'r') as fr:
    configuration = json.loads(fr.read())

s3 = boto3.resource('s3',
                    endpoint_url=configuration['endpoint_url'],
                    aws_access_key_id=configuration['access_key'],
                    aws_secret_access_key=configuration['secret_key'])

bucket_name = "my-bucket"

s3.create_bucket(Bucket=bucket_name)
