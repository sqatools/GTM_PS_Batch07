"""
implicit wait :  implicit wait applies on all web elements on web page, it maximum time out if driver is not
                 able to find the element within given period of time. If we found the element
                 within 1 sec, then it move ahead and perform action.
explicit wait :  Explicit wait applies on specific element, we can also use different wait condition of
                 explicit wait to find the element.
fluent wait :  When we provide configurable polling frequency to explicit wait, the it is called fluent
               wait.
static wait : static sleep hard coded sleep, where script has to wait until given period of time,
              there is no relation between element finding and static wait
              .e.g time.sleep(10)
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


def check_implicit_wait():
    driver.implicitly_wait(15)
    t1 = time.time()
    try:
        driver.find_element(By.ID, "fromcity1").send_keys("Mumbai")
    except Exception as e:
        print(e)
    t2 = time.time()
    print("total time :", t2-t1)

#check_implicit_wait()

def check_for_explicit_wait():
    wait = WebDriverWait(driver, 10, poll_frequency=2)
    t1 = time.time()
    try:
        wait.until(ec.presence_of_element_located((By.ID, "destcity1"))).send_keys("Kolkata")
    except Exception as e:
        print(e)
    t2 = time.time()
    print("Total timeout :", t2-t1)

check_for_explicit_wait()



driver.close()
