import time

import pytest
from modules.dummy_website.dummy_page import DummyWebsitePage
from modules.dummy_website.dummy_page_test_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dwp = DummyWebsitePage(self.driver)

    @pytest.mark.smoke
    def test_enter_passenger_details(self):
        self.driver.get(dummy_website_url)
        self.dwp.enter_first_name(pass_first_name)
        self.dwp.enter_last_name(pass_last_name)
        self.dwp.enter_date_of_birth(pass_dob)
        self.dwp.select_add_more_passenger(more_pass_option)
        time.sleep(5)

    @pytest.mark.sanity
    def test_enter_travel_details(self):
        self.dwp.select_one_way_radio_button()
        self.dwp.enter_from_city_name(from_city)
        self.dwp.enter_dest_city_name(dest_city)
        self.dwp.enter_departure_date(depart_date)
        self.dwp.enter_return_date(return_date)
        self.dwp.enter_visa_date(visa_date)
        self.dwp.select_whatapp_receive_option()
        time.sleep(5)




