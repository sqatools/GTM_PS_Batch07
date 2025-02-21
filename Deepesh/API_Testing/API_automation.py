
import requests
from pprint import pprint
def get_method_response():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.text)

get_method_response()
