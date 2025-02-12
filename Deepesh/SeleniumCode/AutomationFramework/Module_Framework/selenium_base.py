from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self,
                    locator,
                    wait_condition=ec.presence_of_element_located):
        element = self.wait.until(wait_condition(locator))
        # element = self.wait.until(ec.presence_of_element_located((By.XPATH "value")))
        return element

    def click_element(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        element.click()

    def send_text(self, locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        element.send_keys(value)

    def get_text(self, locator, **kwargs):
        element = self.get_element(locator, **kwargs)
        return element.text

    def select_dropdown_value(self, locator, value, **kwargs):
        element = self.get_element(locator, **kwargs)
        select_elem = Select(element)
        select_elem.select_by_visible_text(value)
