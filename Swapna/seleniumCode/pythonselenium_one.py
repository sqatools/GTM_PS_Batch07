import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)


# locator by tagname

herder =driver.find_element(By.TAG_NAME, "h1")
print(herder.text)

# locator by id
driver.find_element(By.ID,"firstname").send_keys("test")


#locator by name
driver.find_element(By.NAME,"fromcity").send_keys("Pune")

# class name : Locator
heading = driver.find_element(By.CLASS_NAME, "post-title.entry-title")
print(heading.text)

## LINK Text : Locator
driver.find_element(By.LINK_TEXT,"Python Selenium").click()


#partial link :locator
driver.find_element(By.PARTIAL_LINK_TEXT,"Pytest").click()

time.sleep(5)
driver.close



