import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('microgreens')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        new_batch = {
            "id": str(uuid.uuid4()),
            "name": data['name'],
            "seed_type": data['seed_type'],
            "planting_date": data['planting_date'],
            "growth_stage": "Germination",
            "watering_schedule": data['watering_schedule'],
            "harvest_date": data['harvest_date'],
            "condition": "active",
            "notes": data.get('notes', "")
        }
        table.put_item(Item=new_batch)
        return {
            'statusCode': 201,
            'body': json.dumps(new_batch),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
