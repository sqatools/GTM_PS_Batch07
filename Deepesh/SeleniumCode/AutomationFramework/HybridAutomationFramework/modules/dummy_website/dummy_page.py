from base.selenium_base import SeleniumBase
from .dummy_page_locator import *


class DummyWebsitePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.send_text(first_name_element, first_name)

    def enter_last_name(self, last_name):
        self.send_text(last_name_element, last_name)

    def enter_date_of_birth(self, dob):
        self.send_text(dob_element, dob)

    def select_add_more_passenger(self, value):
        self.select_dropdown_value(select_num_of_pass_dd, value)

    def select_one_way_radio_button(self):
        self.click_element(one_way_radio_btn)

    def enter_from_city_name(self, from_city):
        self.send_text(from_city_field, from_city)

    def enter_dest_city_name(self, dest_city):
        self.send_text(dest_city_field, dest_city)

    def enter_departure_date(self,depart_date):
        self.send_text(depart_date_calender, depart_date)

    def enter_return_date(self,return_date):
        self.send_text(return_date_calender, return_date)

    def enter_visa_date(self, visa_date):
        self.send_text(visa_date_calender, visa_date)

    def select_whatapp_receive_option(self):
        self.click_element(whats_app_radio)

