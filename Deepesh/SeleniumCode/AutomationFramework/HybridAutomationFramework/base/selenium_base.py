import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utilities.utils_tools import Utils


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = logging.getLogger(__name__)
        self.util = Utils()

    def get_element(self,
                    locator,
                    wait_condition=ec.presence_of_element_located):
        try:
            self.log.info(f"looking for element: {locator}")
            element = self.wait.until(wait_condition(locator))
            # element = self.wait.until(ec.presence_of_element_located((By.XPATH "value")))
            return element
        except Exception as e:
            self.log.info(f"Exception: {e}")
            file_name = f"{self.util.get_time_stamp_name()}_element.png"
            filepath = os.path.join(self.util.get_image_file_path(), file_name)
            self.log.info(f"image path: {filepath}")
            self.driver.save_screenshot(filepath)
            raise

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

    def switch_to_iframe(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        self.driver.switch_to.frame(element)

    def switch_to_default_page(self):
        self.driver.switch_to.default_content()
