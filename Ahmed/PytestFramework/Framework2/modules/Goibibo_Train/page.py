from selenium.webdriver.common.by import By
from .locator import *
from base.selenium_base import SeleniumBase

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

