"""
# install selenium using below command
pip install selenium
# Run pip install selenium command in the terminal

# Check selenium version in python library list
pip list # run this command to get list of installed packaged


"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# open URL in the browser
driver.get("https://www.google.co.in")

# set initial wait for web elements
driver.implicitly_wait(10)
driver.maximize_window() # maximize local browser window

driver.find_element(By.NAME, "q").send_keys("Python Seleniumaman.py")
driver.find_element(By.NAME, "btnK").click()

time.sleep(10)
driver.close()
