from selenium_base import SeleniumBase
from dummy_page_locator import *


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
