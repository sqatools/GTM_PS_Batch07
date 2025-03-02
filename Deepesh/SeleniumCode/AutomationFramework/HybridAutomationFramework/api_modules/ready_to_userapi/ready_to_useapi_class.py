from base.api_base import APIBase
from .ready_to_useapi_data import *
import json

class ReadToUserAPI(APIBase):

    def get_all_object_details(self):
        api_url = common_url
        response, status_code = self.get_method(url=api_url)
        return response, status_code

    def get_specific_object_details(self, obj_id=5):
        api_url = f"{common_url}/{obj_id}"
        response, status_code = self.get_method(url=api_url)
        return response, status_code

    def create_new_entry(self):
        payload = json.dumps(add_object_payload)
        response, status_code = self.post_method(url=common_url, payload=payload, headers=ad_object_headers)
        return response, status_code

    def get_users_details_with_auth(self):
        response, st_code = self.get_method(url=users_url, headers=users_headers)
        return response, st_code


