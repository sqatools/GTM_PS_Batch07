import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def greeting():
    print(" \n--Welcome to class session----")
    yield
    print(" \n---Thank You, Please visit again----")


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.crm_driver = driver
    yield
    driver.close()
