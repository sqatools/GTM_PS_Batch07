import time

import pytest
from modules.goibibo_go_flight.flight_booking_page import FlightBooking
from modules.goibibo_go_flight.goibibo_go_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoibiboGoFlight:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = FlightBooking(self.driver)


    def test_seach_a_flight(self):
        self.fb.open_flight_booking_page(goibibo_url)
        self.fb.close_login_popup()
        self.fb.select_from_city(from_city_name)
        self.fb.select_to_city(to_city_name)
        self.fb.select_departure_date(depart_date)
        time.sleep(10)
