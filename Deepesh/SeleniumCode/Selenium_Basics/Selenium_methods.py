import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# get current url
print("current url :", driver.current_url)

# get website title
print("title :", driver.title)

# check element is displayed
male_radio = driver.find_element(By.ID, "male")
print("is_displayed : ", male_radio.is_displayed())

# check element is enabled
print("male radio button is_enabled :", male_radio.is_enabled())

# check element is selected before click
print("is selected before click :", male_radio.is_selected())

# check element is selected after click
male_radio.click()
print("is selected after click :", male_radio.is_selected())

# move back page
driver.find_element(By.LINK_TEXT, "Python 3 Tutorial").click()
time.sleep(5)
driver.back()
time.sleep(5)

# move forward to Python Tutorial Page
driver.forward()
time.sleep(5)

# refresh the page
driver.refresh()

time.sleep(5)

driver.close()



