# Code from https://github.com/cloudacode/serverless-sample/s3-uploader
import logging
import base64
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

# Allow all CORS and Headers
response  = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*'
    },
    'body': ''
}

def lambda_handler(event, context):

    httpMethod = event["httpMethod"]

    # Check the HTTP Method
    if httpMethod == "POST":
        file_name = event['headers']['filename']
        file_content = base64.b64decode(event['body'])

        BUCKET_NAME = os.environ['BUCKET_NAME']

        # Upload the file to S3 bucket
        try:
            s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
            logger.info('S3 Response: {}'.format(s3_response))
            response['body'] = file_name + ' file has been uploaded'

            return response

        except Exception as e:
            raise IOError(e)
    # Not a POST Method, return a message
    else:
        response['body'] = 'Try POST HTTP Method'
        return response
