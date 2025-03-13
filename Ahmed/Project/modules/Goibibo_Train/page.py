import json
from base.selenium_base import SeleniumBase
from .locator import *

class train_booking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def website(self, url):
        self.driver.get(url)

    def remove_popup(self):
        self.click_element(Login_panel)
        self.click_element(save_ad)
        self.switch_iframe(iframe_id)
        self.click_element(deny_btn)
        self.switch_default()

    def select_train(self):
        self.click_element(Train_select)

    def select_source(self):
        self.click_element(source_select)
        self.send_text(source_station, source_city)
        self.click_element(source_stn_select)

    def select_dest(self):
        self.click_element(dest_select)
        self.send_text(dest_station,dest_city)
        self.click_element(dest_stn_select)

    def select_date(self):
        self.click_element(journey_date)

    def search_train(self):
        self.click_element(search_train)

    def sort_trains(self):
        self.click_element(sort_dropdown)
        self.click_element(sort_select)

    def scroll_to_element(self, locator):
        self.scroll_page(locator)
    def confirm_train(self):
        self.click_element(trainclass_select)

    def irctc_login(self):
        self.click_element(irctc_username)
        self.send_text(irctc_username, username)
        self.click_element(validate_irctc)

    def add_traveller(self):
        self.click_element(add_passenger)


    def read_json_file(self, file_name):
        with open(file_name) as file:
            data = file.read()
            return json.loads(data)

    def cancellation_refund(self):
        self.click_element(refund_cancel)

    def contact_details(self):
        self.send_text(contact_number, phone)
        self.send_text(contact_mail, email)

    def additional_preference(self):
        self.click_element(add_preference)
        self.click_element(auto_upgrade)
        self.click_element(book_only)
        self.scroll_to_element(page_bottom)
        self.click_element(book_choice)
        self.click_element(same_coach)

    def proceed(self):
        self.click_element(payment_button)













