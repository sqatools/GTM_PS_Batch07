import pytest
from api_modules.ready_to_userapi.ready_to_useapi_class import ReadToUserAPI

class TestReadToUseAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj = ReadToUserAPI()

    def test_get_all_objects(self):
        response, status_code = self.api_obj.get_all_object_details()
        assert len(response) == 13
        assert status_code == 200

    def test_get_specific_object_details(self):
        response, status_code = self.api_obj.get_specific_object_details()
        assert response['name'] == 'Samsung Galaxy Z Fold2'
        assert status_code == 200

    def test_add_object_operation(self):
        response, status_code = self.api_obj.create_new_entry()
        assert response['name'] == "Apple MacBook Pro 160"
        assert status_code == 200

    def test_get_users_details_api_auth(self):
        response, status_code= self.api_obj.get_users_details_with_auth()
        assert status_code == 200
