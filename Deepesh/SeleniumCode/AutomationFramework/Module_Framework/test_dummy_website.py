import time

import pytest
from dummy_page import DummyWebsitePage

@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBooking:
    def test_dummy_booking(self):
        self.obj = DummyWebsitePage(self.driver)
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.obj.enter_first_name(first_name='Rahul')
        self.obj.enter_last_name(last_name='Gupta123')
        time.sleep(5)

