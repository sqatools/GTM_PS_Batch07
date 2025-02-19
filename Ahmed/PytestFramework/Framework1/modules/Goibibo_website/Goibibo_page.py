import time
from base.selenium_base import SeleniumBase
from .Goibibo_locator import *


class Goibibowebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def popup_closing (self):
        self.click_element(Login_close)
        self.click_element(discount_ad)

    def iframe_closing(self):
        self.switch_iframe(iframe_element)
        self.click_element(notification_deny)
        self.switch_default()

    def enter_from_city(self, from_city):
        self.click_element(from_btn)
        self.send_text(from_city_loc,from_city)
        from_city_select = (By.XPATH, f'// span[contains(text(), "{from_city}")]')
        self.click_element(from_city_select)

    def enter_to_city(self, to_city):
        self.send_text(to_city_loc, to_city)
        to_city_select = (By.XPATH, f'// span[contains(text(), "{to_city}")]')
        self.click_element(to_city_select)


    def enter_dep_date(self, depart_date):
        self.click_element(departure)
        try:
            self.click_element(depart_date_loc)
        except Exception as e:
            self.click_element(next_month)
            self.click_element(depart_date_loc)


    def enter_ret_date(self, return_date):
        self.click_element(return_cell)
        self.click_element(return_cal)
        try:
            self.click_element(return_date_loc)
        except Exception as e:
            self.click_element(next_month)
            self.click_element(return_date_loc)

    def select_travellers(self):
        self.click_element(Travellers)

    def select_Adults(self):
        for i in range(1,no_of_adults):
            self.click_element(Adult_count)
        time.sleep(1)

    def select_Child(self):
        for i in range(no_of_child):
            self.click_element(Child_count)
        time.sleep(1)

    def select_Infant(self):
        for i in range(no_of_infant):
            self.click_element(Infant_count)
        time.sleep(1)

    def select_class(self):
        class_info = (By.XPATH, f'//*[contains(@class, "sc-12foipm-45 caZeZT")]//li[text()="{class_select}"]')
        self.click_element(class_info)

    def select_done(self):
        self.click_element(done_btn)


    def search_flight(self):
        self.click_element(search_flight)


