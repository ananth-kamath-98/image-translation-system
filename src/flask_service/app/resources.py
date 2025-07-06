import boto3
import os

_session = boto3.Session(region_name=os.getenv('REGION_NAME', 'us-east-1'))

dynamodb = _session.resource('dynamodb')
