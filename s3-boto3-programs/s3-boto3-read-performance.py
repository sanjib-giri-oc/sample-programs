import boto3
import json
import time
import os

with open('configuration.json', 'r') as fr:
    configuration = json.loads(fr.read())

s3 = boto3.resource('s3',
                    endpoint_url=configuration['endpoint_url'],
                    aws_access_key_id=configuration['access_key'],
                    aws_secret_access_key=configuration['secret_key'])

repetation = 50
total_time = 0

for i in range(repetation+1):

    start_time = time.time()
    s3.Bucket(configuration['bucket_name']).download_file("uploaded_sample_file{}.txt".format(i),"downloaded_sample_file{}.txt".format(i))
    end_time = time.time()

    elapsed_time =  end_time  - start_time
    total_time = total_time + elapsed_time

print("Average download/read time: ", total_time / repetation)

