import json


def lambda_handler(event, context):
    first_name = event["queryStringParameters"]['first_name']
    last_name = event["queryStringParameters"]['last_name']

    app_response = {}

    app_response['message'] = f'The details are {first_name} and {last_name}'
    app_response['profession'] = 'cricket'
    app_response['age'] = 40

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)

    return responseObject
