from utilities.utils_tools import Utils
from modules.dummy_website.dummy_page_test_data import *


def pytest_configure(config):
    util = Utils()
    time_stamp_name = util.get_time_stamp_name()
    log_filename = f"{time_stamp_name}_execution.log"
    logfile_path = f"logs/{log_filename}"
    config.option.log_file = logfile_path
