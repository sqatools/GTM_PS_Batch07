import time
import pytest
from modules.Goibibo_Train.page import train_booking
from modules.Goibibo_Train.data import *


@pytest.mark.usefixtures("get_driver")
class Testtrainbooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.tb = train_booking(self.driver)

    def test_GoibiboTrainBooking(self):
        self.tb.website(goibibo_url)
        time.sleep(5)
        self.tb.remove_popup()
        time.sleep(5)
        self.tb.select_train()
        self.tb.select_source()
        self.tb.select_dest()
        self.tb.select_date()
        time.sleep(5)
        self.tb.search_train()
        time.sleep(5)
