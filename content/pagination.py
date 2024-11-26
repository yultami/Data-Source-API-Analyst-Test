import requests


def get_all_pages(url, headers):
    all_data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            all_data.extend(response.json()['items'])
            url = response.links.get('next', {}).get('url')
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")
    return all_data
