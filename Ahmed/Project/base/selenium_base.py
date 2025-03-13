from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_element(self, locator, wait_condition = ec.presence_of_element_located):
        element = self.wait.until(wait_condition(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def send_text(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def switch_iframe(self, locator):
        element = self.get_element(locator)
        self.driver.switch_to.frame(element)

    def switch_default(self):
        self.driver.switch_to.default_content()


    def scroll_page(self, locator):
        element_target = self.get_element(locator)
        action = ActionChains(self.driver)
        action.scroll_to_element(element_target)
        action.click()
        action.perform()

    def read_json_data(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
            json_data = json.loads(data)
            return json_data



        
