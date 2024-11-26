import requests


def get_repositories(query, key):
    headers = {
        'Authorization': f'Bearer {key}'
    }
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc'
    }
    response = requests.get('https://api.github.com/search/repositories', headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch repositories: {response.status_code}")
