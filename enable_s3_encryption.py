#!/usr/bin/env python3

import boto3
from botocore.exceptions import ClientError

session = boto3.session.Session(profile_name='AWS_PROFILE_NAME')
s3 = session.client(service_name='s3')

enc_config = {
  'Rules': [
    {
      'ApplyServerSideEncryptionByDefault': {
        'SSEAlgorithm': 'AES256'
      }
    },
  ]
}

for bucket in s3.list_buckets()['Buckets']:
  try:
    enc_algorithm = s3.get_bucket_encryption(Bucket=bucket['Name'])['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
    print('Bucket %s has default server-side encryption enabled with %s' % (bucket['Name'],enc_algorithm))
  except ClientError as e:
    if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
      print('Bucket: %s does not have default server-side encryption enabled' % bucket['Name'])
      try:
        s3.put_bucket_encryption(Bucket=bucket['Name'],ServerSideEncryptionConfiguration=enc_config)
        print('Enabled encryption on bucket: %s' % bucket['Name'])
      except ClientError as e:
        print(e.response['Error']['Code'])
    else:
      print(e.response['Error']['Code'])
