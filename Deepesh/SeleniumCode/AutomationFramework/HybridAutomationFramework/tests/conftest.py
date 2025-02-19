import pytest
from selenium import webdriver
from base.webdriver_factory import WebdriverFactory
from modules.goibibo_go_flight.goibibo_go_test_data import *
from utilities.utils_tools import Utils


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default=None, help='browser to launch')
    parser.addoption("--headless", action='store', default=None, help='GUI execution option')

@pytest.fixture(scope='class')
def launch_goibibo_website(request, pytestconfig):
    browser = pytestconfig.getoption('browser')
    headless = pytestconfig.getoption('headless')
    if browser and headless:
        wd = WebdriverFactory(browser, headless)
    else:
        wd = WebdriverFactory('chrome')
    driver = wd.get_driver_instance()
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()

#command to execute with dynamic option
# python -m pytest -v .\tests\goibibo_go_flight\ --browser=edge --headless=True

def pytest_configure(config):
    util = Utils()
    time_stamp_name = util.get_time_stamp_name()
    log_filename = f"{time_stamp_name}_execution.log"
    logfile_path = f"logs/{log_filename}"
    config.option.log_file = logfile_path
