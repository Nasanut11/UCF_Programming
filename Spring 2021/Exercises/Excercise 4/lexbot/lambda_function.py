import json

def lambda_handler(event, context):
    # TODO implement
    print(event["data"])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
