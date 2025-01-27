import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('microgreens')

def lambda_handler(event, context):
    try:
        batch_id = event['pathParameters']['id']
        response = table.delete_item(Key={'id': batch_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Batch deleted successfully'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
