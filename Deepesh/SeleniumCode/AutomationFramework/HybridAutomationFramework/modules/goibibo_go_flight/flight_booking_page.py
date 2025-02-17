from selenium.webdriver.common.by import By
from base.selenium_base import SeleniumBase
from .flight_booking_locator import *


class FlightBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_flight_booking_page(self, url):
        self.driver.get(url)

    def select_from_city(self, from_city_name):
        self.click_element(from_city_label_locator)
        self.send_text(from_city_input_field, from_city_name)
        element = self.get_element(first_option_in_suggestion_list)
        elem_text = element.text
        updated_text = elem_text.replace("\n", "")
        self.log.info(f"suggestion list text: {updated_text}")
        if updated_text == from_city_name:
            element.click()

    def select_to_city(self, to_city_name):
        self.click_element(from_city_label_locator)
        self.send_text(to_city_input_field, to_city_name)
        element = self.get_element(first_option_in_suggestion_list)
        elem_text = element.text
        updated_text = elem_text.replace("\n", "")
        self.log.info(f"suggestion list text: {updated_text}")
        if updated_text == to_city_name:
            element.click()

    def close_login_popup(self):
        self.click_element(close_icon_login_popup)


    def select_departure_date(self, depart_date):
        self.click_element(departure_date_calender)
        depart_date_locator = (By.XPATH, f"//div[contains(@aria-label,'{depart_date}')]")
        self.click_element(depart_date_locator)

