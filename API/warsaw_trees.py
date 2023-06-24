import requests
from requests.exceptions import HTTPError

WARSAW_TREE_DOMAIN = 'https://api.um.warszawa.pl/api/'
TREE_RESOURCE_ID = "ed6217dd-c8d0-4f7b-8bed-3b7eb81a95ba"
DEFAULT_LIMIT_VALUE = 250


def get_tree_list(limit=DEFAULT_LIMIT_VALUE):
    try:
        api_url = f"{WARSAW_TREE_DOMAIN}action/datastore_search"
        query_params = {"resource_id": TREE_RESOURCE_ID, "limit": limit}

        response = requests.get(api_url, params=query_params)
        response.raise_for_status()

        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
