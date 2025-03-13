import json
from base.Api_base import ApiBase
from .data import *

class ready_api(ApiBase):

    def get_all_objects(self):
        apiurl = common_url
        response, status_code = self.get_method(url=apiurl)
        return response, status_code

    def add_objects(self):
        apiurl=common_url
        response, status_code = self.post_method(url=apiurl, headers = ad_object_headers, data = add_object_payload )
        return response, status_code


