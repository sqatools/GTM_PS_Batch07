import time
import os
import pytest
from modules.goibibo_go_flight.flight_booking_page import FlightBooking
from modules.goibibo_go_flight.goibibo_go_test_data import *
from utilities.utils_tools import Utils



@pytest.mark.usefixtures("get_driver")
class TestGoibiboGoFlight:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fb = FlightBooking(self.driver)
        self.ut = Utils()
        cur_loc = os.getcwd()
        self.json_data = self.ut.read_json_file(f"{cur_loc}//modules//goibibo_go_flight//goibibo_test_data.json")



    def test_seach_a_flight(self):
        self.fb.open_flight_booking_page(goibibo_url)
        self.fb.close_login_popup()
        self.fb.select_from_city(from_city_name)
        self.fb.select_to_city(to_city_name)
        self.fb.select_departure_date(self.json_data['depart_date'])
        self.fb.click_traveller_section()
        self.fb.select_no_adults(self.json_data['No_of_adult'])
        self.fb.select_no_children(self.json_data['No_Of_child'])
        self.fb.select_no_infants(self.json_data['No_of_infant'])
        self.fb.select_travel_class(self.json_data['travel_class'])
        time.sleep(10)
        self.fb.click_done_button()
        self.fb.click_search_button()
        time.sleep(10)
