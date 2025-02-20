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

    def click_traveller_section(self):
        self.click_element(traveller_section)

    def select_no_adults(self, no_adults):
        for i in range(1, no_adults):
            self.click_element(adults_plus_icon)

    def select_no_children(self, no_children):
        for i in range(no_children):
            self.click_element(children_plus_icon)

    def select_no_infants(self, no_infants):
        for i in range(no_infants):
            self.click_element(infants_plus_icon)

    def select_travel_class(self, travel_class):
        travel_class_loc = (By.XPATH, f"//li[text()='{travel_class}']")
        self.click_element(travel_class_loc)

    def click_done_button(self):
        self.click_element(done_button)

    def click_search_button(self):
        self.click_element(search_flight_button)

    def deny_push_notification(self):
        self.switch_to_iframe(webpush_iframe_id)
        self.click_element(will_do_later_option)
        self.switch_to_default_page()
