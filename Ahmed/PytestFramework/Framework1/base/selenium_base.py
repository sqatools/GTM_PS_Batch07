import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By



class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = logging.getLogger(__name__)

    def get_element(self,
                    locator,
                    wait_condition=ec.presence_of_element_located):
        self.log.info(f"looking for element: {locator}")
        element = self.wait.until(wait_condition(locator))
        # element = self.wait.until(ec.presence_of_element_located((By.XPATH "value")))
        return element

    def click_element(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        self.log.info(f"clicking on element: {locator}")
        element.click()

    def send_text(self, locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        self.log.info(f"sending text: {value},  on element: {locator}")
        element.send_keys(value)

    def get_text(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        return element.text

    def select_dropdown_value(self, locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        self.log.info(f"selecting value: {value},  on element: {locator}")
        select_elem = Select(element)
        select_elem.select_by_visible_text(value)

    def switch_iframe(self, locator):
        self.driver.switch_to.frame(locator)

    def switch_default(self):
        self.driver.switch_to.default()