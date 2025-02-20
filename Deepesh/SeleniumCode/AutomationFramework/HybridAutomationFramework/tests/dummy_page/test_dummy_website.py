import time

import pytest
from modules.dummy_website.dummy_page import DummyWebsitePage
from modules.dummy_website.dummy_page_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dwp = DummyWebsitePage(self.driver)

    # @pytest.fixture(scope='class', autouse=True)
    # def launch_dummy_url(self):
    #     self.driver.get(dummy_website_url)

    @pytest.mark.smoke
    def test_enter_passenger_details(self):
        self.dwp.enter_first_name(pass_first_name)
        self.dwp.enter_last_name(pass_last_name)

    def test_enter_dob_details(self):
        self.dwp.enter_date_of_birth(pass_dob)
        self.dwp.select_add_more_passenger(more_pass_option)

    @pytest.mark.sanity
    def test_enter_travel_details(self):
        self.dwp.select_one_way_radio_button()
        self.dwp.enter_from_city_name(from_city)
        self.dwp.enter_dest_city_name(dest_city)

    def test_enter_travel_date(self):
        self.dwp.enter_departure_date(depart_date)
        self.dwp.enter_return_date(return_date)

    def test_enter_visa_date(self):
        self.dwp.enter_visa_date(visa_date)
        self.dwp.select_whatapp_receive_option()
        time.sleep(5)

    def test_enter_billing_name(self):
        self.dwp.enter_billing_name(billing_name)

    def test_enter_billing_phone(self):
        self.dwp.enter_billing_phone(billing_phone)

    def test_enter_billing_email(self):
        self.dwp.enter_billing_email(billing_email)

    def test_enter_billing_address(self):
        self.dwp.enter_billing_address(billing_address)

    def test_select_billing_country(self):
        self.dwp.select_billing_country(billing_country)
