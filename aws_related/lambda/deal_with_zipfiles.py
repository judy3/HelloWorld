import json
import urllib.parse
import boto3

import os
import zipfile
import time

##This script is used to unzip a zipfile from one s3 bucket and upload all unziped files to another bucket. Please note to set up the lambda excute time and memory enough. 
##Some the libs I imported might not included in the aws, so zip the files together and uploade to lambda. 
##zips commands here:
##zip -9 bundle.zip deal_with_zipfiles.py
##cd $VIRTUAL_ENV/lib/python3.6/site-packages
##zip -r9 ~/lambda/bundle.zip *
##cd $VIRTUAL_ENV/lib64/python3.6/site-packages
##zip -r9 ~/lambda/bundle.zip *

print('Loading function')
s3 = boto3.client('s3')
sns = boto3.client('sns')

def unzip(sourcezip, dest_dir):
    with zipfile.ZipFile(sourcezip) as zf:
        zf.extractall(dest_dir)
        
def upload_to_s3(local_name, bucket, key):
    z=zipfile.ZipFile(local_name,'r')
    for f in z.namelist():
        local_file="/tmp/files/{}".format(f)
        if os.path.isfile(local_file):
            print("uploading " + local_file)
            c_time=time.strftime("%Y%m%d")
            #s3_path="{}-{}/{}".format(key,c_time,f)
            s3_path="{}".format(f)
            s3.upload_file(local_file, bucket, s3_path,  ExtraArgs={'ACL':'public-read'})

def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    path = "/tmp/{}".format(key)
    print("the path is "+ path)
    s3.download_file(bucket,key, path)
    
    print("Downloaded a zip file:")
    os.system('ls /tmp/')
    print("extracting files from the zip file")
    unzip(path, '/tmp/files/')
    
    bucket2="demo-jy2"
    print("uploading to {} ...".format(bucket2))
    upload_to_s3(path, bucket2, key)
    
    response = sns.publish(
    TopicArn='arn:aws:sns:ap-southeast-1:accountnumberhere:topicnamehere',    
    Message='The files has been uploaded, please check the management console.'
    )
    print("Response: {}".format(response))
