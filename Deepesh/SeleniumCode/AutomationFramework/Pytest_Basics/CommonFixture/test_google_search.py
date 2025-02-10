import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    def test_search_on_google(self):
        self.crm_driver.get("https://www.google.co.in")
        self.crm_driver.find_element(By.NAME, "q").send_keys("Python Automation")
        self.crm_driver.find_element(By.NAME, "btnK").click()
        time.sleep(10)


