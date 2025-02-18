from base.selenium_base import SeleniumBase
from .Goibibo_locator import *


class Goibibowebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def popup_closing (self):
        self.click_element(self, Login_close)
        self.click_element(self, discount_ad)

    def iframe_closing(self):
        self.click_element(self, notification_deny)

    def enter_from_city(self, from_city):
        self.click_element(from_btn)
        self.send_text(from_city_loc,from_city_name)

    def enter_to_city(self, to_city):
        self.send_text(to_city_loc, to_city_name)

    def enter_dep_date(self):
        self.click_element(departure)
        self.click_element(depart_date_loc)

    def enter_ret_date(self):
        self.click_element(return_cell)
        self.click_element(return_date_loc)

    def select_travellers(self):
        self.click_element(Travellers)
        self.click_element(Adult_count)
        self.click_element(Adult_count)
        self.click_element(Child_count)
        self.click_element(Infant_count)
        self.click_element(class_info)
        self.click_element(done_btn)

    def search_flight(self):
        self.click_element(search_flight)


