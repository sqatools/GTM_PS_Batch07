from base.api_base import APIBase
from .ready_to_useapi_data import *

class ReadToUserAPI(APIBase):

    def get_all_object_details(self):
        api_url = common_url
        response, status_code = self.get_method(url=api_url)
        return response, status_code
