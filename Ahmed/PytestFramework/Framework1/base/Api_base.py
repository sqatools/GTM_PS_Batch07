import requests


class ApiBase:
    def get_method(self, url, headers=None, payload = None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload = None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json(), response.status_code

    def pull_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("PULL", url, headers=headers, data=payload)
        return response.json(), response.status_code

    def patch_method(self, url,headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        return response.json(), response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response.json(), response.status_code
