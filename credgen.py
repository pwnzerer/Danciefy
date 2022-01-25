import requests
import base64
import json
import datetime

def generatecreds():
    
    clientId = "fe975f2082b44c62abd69a45ebd8b834"
    clientSecret = "a4bdd6d162d4419980fb1feae5393978"
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': clientId,
        'client_secret': clientSecret,
    })

    auth_response_data = auth_response.json()

    print(auth_response_data)

    access_token = auth_response_data['access_token']

    return access_token


# message = f"{clientId}:{clientSecret}"
# messageBytes = message.encode('ascii')
# base64Bytes = base64.b64encode(messageBytes)
# base64Message = base64Bytes.decode('ascii')

# url = 'https//accounts.spotify.com/api/token'
# method = "POST"
# headers = {"Authorizatio":f"Basic {base64Message}"}
# data = {'grant_type': 'client_credentials'}

# r = requests.post(url, headers=headers, data=data)

# print(json.dumps(r.json(), indent=2))
