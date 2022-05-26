import boto3
import json

dynamodb_client = boto3.resource('dynamodb')

def createCustomer(event, context):
    table = dynamodb_client.Table('customerTable')
    resp = table.put_item(
        Item = {
            'customerId': '1',
            'Role': 'bc'
        }
    )
    print(resp)
    return {
        'statusCode': 200,
        'body': json.dumps('Put item successfully!')
    }