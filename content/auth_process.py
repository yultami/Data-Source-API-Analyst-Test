import requests


def authenticate(key):
    headers = {
        'Authorization': f'Bearer {key}'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Authentication failed: {response.status_code}")
