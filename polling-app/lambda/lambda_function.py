# Code from https://github.com/cloudacode/serverless-sample/polling-app
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
        eventBody = json.loads(event["body"])
        candidate = ""
        # print(eventBody)

        if ("candidate" in eventBody):
            candidate = eventBody["candidate"];
            # Log a message to CloudWatch
            print("VOTE {}".format(candidate))
            response['body'] = 'Success'
        else:
            print("No candidates selected")
        return response

    # Not a POST Method, return a message
    else:
        response['body'] = 'Try POST HTTP Method'
        return response
