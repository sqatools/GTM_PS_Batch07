import time
import pytest
import os
from modules.Goibibo_Train.page import train_booking
from modules.Goibibo_Train.data import *
from modules.Goibibo_Train.locator import *


@pytest.mark.usefixtures("get_driver")
class Testtrainbooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.tb = train_booking(self.driver)
        cur_loc = os.getcwd()
        self.pass_data = self.tb.read_json_file(f"{cur_loc}//modules//Goibibo_Train//passenger_data.json")

    def test_launch_GoibiboTrain(self):
        self.tb.website(goibibo_url)
        time.sleep(5)

    def test_removepopups(self):
        self.tb.remove_popup()
        time.sleep(5)

    def test_searchtrain(self):
        self.tb.select_train()
        self.tb.select_source()
        self.tb.select_dest()
        self.tb.select_date()
        time.sleep(5)
        self.tb.search_train()
        time.sleep(5)

    def test_selecttrain(self):
        self.tb.sort_trains()
        time.sleep(5)
        self.tb.scroll_to_element(trainclass_select)
        self.tb.confirm_train()
        time.sleep(5)

    def test_booktrain(self):
        self.tb.irctc_login()
        time.sleep(5)

    def test_addpassenger(self):
        self.tb.add_traveller()
        n = len(self.pass_data)
        for i in range (n):
            self.tb.send_text(passenger_name,self.pass_data[i]['Name'])
            self.tb.send_text(passenger_age,self.pass_data[i]['Age'])
            Gender = self.pass_data[i]['Gender']
            gender_select = (By.XPATH, f"//input[contains(@id, '{Gender}')]//parent::span")
            self.tb.click_element(gender_select)
            self.tb.click_element(berth_preference)
            Berth = self.pass_data[i]['Berth']
            berth_selection = (By.XPATH, f"//p[text()='{Berth}']//parent::li")
            self.tb.click_element(berth_selection)
            self.tb.click_element(save_passenger)
            time.sleep(5)
            if i < n-1:
                self.tb.scroll_to_element(add_another_passenger)
                self.tb.click_element(add_another_passenger)



    def test_refund_option(self):
        self.tb.scroll_to_element(page_bottom)
        self.tb.cancellation_refund()

    def test_passenger_contact(self):
        self.tb.contact_details()
        self.tb.scroll_to_element(page_bottom)


    def test_additional_pref(self):
        self.tb.additional_preference()

    def test_proceed_payment(self):
        self.tb.proceed()
        time.sleep(5)






