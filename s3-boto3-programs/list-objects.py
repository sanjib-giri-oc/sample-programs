import boto3
import json

with open('configuration.json', 'r') as fr:
    configuration = json.loads(fr.read())

s3 = boto3.resource('s3',
                    endpoint_url=configuration['endpoint_url'],
                    aws_access_key_id=configuration['access_key'],
                    aws_secret_access_key=configuration['secret_key'])

my_bucket = s3.Bucket(configuration['bucket_name'])

#for my_bucket_object in my_bucket.objects.all():
#    print(my_bucket_object)

i = 0
for my_bucket_object in my_bucket.objects.all():
    i += 1
    print("obj{}:".format(i), my_bucket_object.key)
