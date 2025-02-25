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
