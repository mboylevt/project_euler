import base64
import json

import requests
api_url = 'https://api.shapeways.com'
# Authenticate and get a bearer token

auth_url = '/oauth2/token'
client_id = 'ENPbso1i8tyUWX2tmMhHK5pm8pcHN9cauV96CVALkaIQUa3qQr'
client_secret = 'j7aEPlq83n9UtU0t3u1dg6Gk1Bw1CwU4TsTosKTjTSwl3GVQ0y'

auth_post_data = {
    'grant_type': 'client_credentials'
}

response = requests.post(url=api_url+auth_url, data=auth_post_data, auth=(client_id, client_secret))
access_token = response.json()['access_token']
print("Access token: " + access_token)

#Hit a pubic URL
materials_url = '/materials/v1'
headers = {
    'Authorization': 'Bearer ' + access_token
}
response = requests.get(url=api_url+materials_url, headers=headers)
print(response.json()['materials'])

# Hit a private URL
models_url = '/models/v1'
response = requests.get(url=api_url+models_url+'?page=1', headers=headers)
print(response.json()['models'])

# Upload a model
models_url = '/models/v1'
headers = {
    'Authorization': 'Bearer ' + access_token

}
with open('cube.stl', 'rb') as model_file:
    model_file_data = model_file.read()

model_upload_post_data = {
    'fileName': 'cube.stl',
    'file': base64.b64encode(model_file_data).decode('utf-8'),
    'description': 'Someone call a doctor, because this cube is SIIIICK.',
    'hasRightsToModel': 1,
    'acceptTermsAndConditions': 1
}

response = requests.post(url=api_url+models_url, headers=headers, data=json.dumps(model_upload_post_data))
print("******")
print(json.dumps(response.json(), indent=4, sort_keys=True))

# Order a model
model_id = 7892229
order_url = '/orders/v1'
# access_token = "YOUR ACCESS TOKEN HERE"
payment_verificaion_id = "MATT-DOC-TEST"

headers = {
    'Authorization': 'Bearer ' + access_token
}

items = [{
        'materialId': 6,
        'modelId': model_id,
        'quantity': 1
}]


order_data = {
    'items': items,
    'firstName': 'my',
    'lastName': 'dude',
    'country': 'US',
    'state': 'NY',
    'city': 'New York',
    'address1': '419 Park Ave South',
    'address2': '9th Floor',
    'zipCode': '10016',
    'phoneNumber': '1234567890',
    'paymentVerificationId': payment_verificaion_id,
    'paymentMethod': 'credit_card',
    'shippingOption': 'Cheapest'
}

response = requests.post(url=api_url+order_url, headers=headers, data=json.dumps(order_data))
print(json.dumps(response.json(), indent=4, sort_keys=True))