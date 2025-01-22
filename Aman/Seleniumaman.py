import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# open URL in the browser
driver.get("https://www.google.co.in")

# set initial wait for web elements
driver.implicitly_wait(10)
driver.maximize_window() # maximize local browser window

driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()

time.sleep(10)
driver.close()
