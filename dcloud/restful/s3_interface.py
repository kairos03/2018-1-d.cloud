import boto3
import json

S3 = boto3.client('s3')
BUCKET = '2018-dcloud'


def list_path(bucket, user, path):

    files = []
    # get list
    objects = S3.list_objects(Bucket=bucket, Prefix='{}/{}'.format(user, path), Delimiter='/')

    # get sub directorys
    common_prefixes = objects.get('CommonPrefixes')
    if common_prefixes:
        for obj in common_prefixes:
            files.append({'type':'diretory', 'name':obj.get('Prefix').split('/')[-2]})

    # get files
    contents = objects.get('Contents')
    if contents:
        for obj in contents:
            file = obj.get('Key').split('/')[-1]
            if file != '':
                files.append({'type':'file', 'name':file})

    return {'files':files}

def delete_path(bucket, user, path):
    return S3.delete_object(Bucket=bucket, Key='{}/{}'.format(user, path))
