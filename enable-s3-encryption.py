#!/usr/bin/env python3

import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(description='Check all S3 buckets in the AWS account and enables default encryption with AES256')
parser.add_argument('aws_account_name', type=str, help='Named AWS user account')

args = parser.parse_args()

session = boto3.session.Session(profile_name=args.aws_account_name)
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
