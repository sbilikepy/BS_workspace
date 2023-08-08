import api_access.secret
from api_access.secret import apikey, secret
import requests
import base64
import json

def main():
    api_key = apikey # /api_access/secret.py
    api_secret = secret # /api_access/secret.py

    # Encode API key and secret in base64
    credentials = f"{api_key}:{api_secret}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    # URL and payload for token request
    token_url = "https://api.idealista.com/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "scope": "read"
    }

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    # Send POST request to obtain token
    response = requests.post(token_url, data=payload, headers=headers)

    # Handle response
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data["access_token"]
        print("Access Token:", access_token)
    else:
        print("Error:", response.status_code, response.text)
        return

    search_url = 'https://api.idealista.com/3.5/es/search'

    search_params = {
        'country': 'es',
        'operation': 'sale',
        'propertyType': 'homes',
    }

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Send POST request for search
    response = requests.post(search_url, json=search_params, headers=headers)

    # Handle response
    if response.status_code == 200:
        data = response.json()
        element_list = data.get('elementList', [])
        print(element_list)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    main()
