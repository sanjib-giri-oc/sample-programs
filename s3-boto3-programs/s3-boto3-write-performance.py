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
    with open("sample_file{}.txt".format(i), "w") as f:
        f.write("This is sample file number {}".format(i))

    start_time = time.time()
    s3.Bucket(configuration['bucket_name']).upload_file("sample_file{}.txt".format(i),"uploaded_sample_file{}.txt".format(i))
    end_time = time.time()

    elapsed_time =  end_time  - start_time
    total_time = total_time + elapsed_time

    os.remove("sample_file{}.txt".format(i))

print("Average upload/write time: ", total_time / repetation)

