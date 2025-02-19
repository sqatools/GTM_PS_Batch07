import time
import pytest

from modules.Goibibo_website.Goibibo_page import Goibibowebsite
from modules.Goibibo_website.Goibibo_data import *

@pytest.mark.usefixtures("get_driver")
class Testticketbooking:

    #@pytest.fixture(autouse=True)
    def test_Goibibo_booking(self):
        self.obj = Goibibowebsite(self.driver)
        self.driver.get(url)
        time.sleep(5)
        self.obj.popup_closing()
        self.obj.iframe_closing()
        self.obj.enter_from_city(from_city)
        self.obj.enter_to_city(to_city)
        self.obj.enter_dep_date(depart_date)
        self.obj.enter_ret_date(return_date)
        self.obj.select_travellers()
        self.obj.select_Adults()
        self.obj.select_Child()
        self.obj.select_Infant()
        self.obj.select_class()
        self.obj.select_done()
        self.obj.search_flight()

