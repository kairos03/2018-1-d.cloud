import boto3
import json
from dcloud import aws_conf

S3 = boto3.client(
    's3',
    aws_access_key_id=aws_conf.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=aws_conf.AWS_SECRET_ACCESS_KEY)
BUCKET = '2018-dcloud'


def list_path(bucket, user, path):

    files = []
    # get list
    objects = S3.list_objects(Bucket=bucket, Prefix='{}/{}'.format(user, path), Delimiter='/')

    # get sub directorys
    common_prefixes = objects.get('CommonPrefixes')
    if common_prefixes:
        for obj in common_prefixes:
            files.append({'type':'directory', 'name':obj.get('Prefix').split('/')[-2]})

    # get files
    contents = objects.get('Contents')
    if contents:
        for obj in contents:
            file = obj.get('Key').split('/')[-1]
            if file != '':
                files.append({'type':'file', 'name':file})

    return {'files':files}

def upload_file(bucket, user, local_path, key):
    return S3.upload_file(local_path, bucket, user+"/"+key)

def download_file(bucket, user, local_path, key):
    return S3.download_file(bucket, user+"/"+key, local_path)

def delete_path(bucket, user, path):
    return S3.delete_object(Bucket=bucket, Key=user+"/"+path)

def make_directory(bucket, user, path):
    return S3.put_object(Bucket=BUCKET, Key=user+"/"+path)

#
def move_file(bucket, user, old_path, new_path):
    S3.copy_object(Bucket=bucket, CopySource=bucket+"/"+user+"/"+old_path, Key=user+"/"+new_path)
    S3.delete_object(Bucket=bucket, Key=user+"/"+old_path)
    return

def copy_file(bucket, user, old_path, new_path):
    S3.copy_object(Bucket=bucket, CopySource=bucket+"/"+user+"/"+old_path, Key=user+"/"+new_path)
    return
