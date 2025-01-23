"""
Selenium Locators :

    # ID = "id"
    XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# class name : Locator
sub_heading = driver.find_element(By.CLASS_NAME, "post-title.entry-title")
print(sub_heading.text)

# Tagname : Locator
header = driver.find_element(By.TAG_NAME, "h1")
print(header)
print(header.text)

# ID :  Locator
driver.find_element(By.ID, "oneway").click()
driver.find_element(By.ID, "roundtrip").click()

# Name : Locator
driver.find_element(By.NAME, "fromcity").send_keys("Mumbai")
driver.find_element(By.NAME, "destcity").send_keys("Kolkata")
time.sleep(5)

# LINK Text : Locator
driver.find_element(By.LINK_TEXT, "Pytest Framework").click()
time.sleep(5)

# Partial Link Text : Locator
driver.find_element(By.PARTIAL_LINK_TEXT, "API").click()
time.sleep(5)

driver.close()
