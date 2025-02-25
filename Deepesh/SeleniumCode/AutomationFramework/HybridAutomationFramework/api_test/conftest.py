"""
for parallel test execution we have to use pytest-xdist
pip install pytest-xdist
# command to execute the parallel test cases
python -m pytest -v -n 3 .\tests\dummy_page\
n = Number of test cases.

"""

import pytest
from selenium import webdriver
from base.webdriver_factory import WebdriverFactory
from modules.goibibo_go_flight.goibibo_go_test_data import *
from utilities.utils_tools import Utils
from modules.dummy_website.dummy_page_test_data import *



def pytest_configure(config):
    util = Utils()
    time_stamp_name = util.get_time_stamp_name()
    log_filename = f"{time_stamp_name}_execution.log"
    logfile_path = f"logs/{log_filename}"
    config.option.log_file = logfile_path
