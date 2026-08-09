import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactMessages')

def lambda_handler(event, context):

    if event.get("httpMethod") == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "API is working"})
        }

    body = json.loads(event['body'])


    item = {
        "id": str(uuid.uuid4()),
        "firstName": body.get("firstName"),
        "lastName": body.get("lastName"),
        "email": body.get("email"),
        "message": body.get("message"),
        "createdAt": datetime.now().isoformat()
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps({
            "message": "Data saved successfully"
        })
    }