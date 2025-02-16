import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    def test_search_on_google(self):
        self.crm_driver.get("https://www.google.co.in")
        self.crm_driver.find_element(By.NAME, "q").send_keys("Python Automation")
        self.crm_driver.find_element(By.NAME, "btnK").click()
        time.sleep(5)


    def test_dummy_website(self):
        self.crm_driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.crm_driver.find_element(By.XPATH, "(//input[@name='firstname'])[1]").send_keys("Rahul")
        self.crm_driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("Gupta")
        self.crm_driver.find_element(By.ID, "birthday").send_keys("02/11/2025")
        self.crm_driver.find_element(By.ID, "male").click()
        self.crm_driver.find_element(By.ID, "female").click()
        dd_element =  self.crm_driver.find_element(By.ID, "admorepass")
        ss = Select(dd_element)
        ss.select_by_visible_text("Add 3 more passenger (200%)")
        self.crm_driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.crm_driver.find_element(By.ID, "destcity").send_keys("Delhi")
        time.sleep(5)
