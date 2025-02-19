from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Option
from selenium.webdriver.firefox.options import Options as Firefox_Option
from selenium.webdriver.edge.options import Options as Edge_Option


class WebdriverFactory:
    def __init__(self, browser, headless=False):
        self.browser = browser
        self.headless = headless

    def get_driver_instance(self):
        driver = None
        if self.browser.lower() == 'chrome':
            chrm_option = Chrome_Option()
            if self.headless:
                chrm_option.add_argument("--headless")
            driver = webdriver.Chrome(options=chrm_option)

        elif self.browser.lower() == 'firefox':
            frfox_option = Firefox_Option()
            if self.headless:
                frfox_option.add_argument("--headless")
            driver = webdriver.Firefox(options=frfox_option)

        elif self.browser.lower() == 'edge':
            edge_option = Edge_Option()
            if self.headless:
                edge_option.add_argument("--headless")
            driver = webdriver.Edge(options=edge_option)

        driver.maximize_window()
        return driver
