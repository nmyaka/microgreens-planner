import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('microgreens')

def lambda_handler(event, context):
    try:
        # Capture the id from the path parameters
        batch_id = event['pathParameters']['id']
        
        # Capture the updated data from the request body (assumes JSON format)
        updated_data = json.loads(event['body'])
        
        # Update the item in DynamoDB with the provided id
        response = table.update_item(
            Key={'id': batch_id},
            UpdateExpression="set #name = :name, seed_type = :seed_type, planting_date = :planting_date, growth_stage = :growth_stage, watering_schedule = :watering_schedule, harvest_date = :harvest_date, notes = :notes",
            ExpressionAttributeNames={
                '#name': 'name'
            },
            ExpressionAttributeValues={
                ':name': updated_data['name'],
                ':seed_type': updated_data['seed_type'],
                ':planting_date': updated_data['planting_date'],
                ':growth_stage' : updated_data['growth_stage'], 
                ':watering_schedule' : updated_data['watering_schedule'], 
                ':harvest_date' : updated_data['harvest_date'], 
                ':notes' : updated_data['notes']
            },
            ReturnValues="UPDATED_NEW"
        )
        
        # Return success message with the updated data
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Batch updated successfully', 'updated': response['Attributes']}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
