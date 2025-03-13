import pytest
from modules.Ready_API.page import ready_api

class Test_ready_to_API:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ap = ready_api()

    def test_get_every_objects(self):
        response, status_code = self.ap.get_all_objects()
        assert len(response) == 13
        assert status_code == 200


