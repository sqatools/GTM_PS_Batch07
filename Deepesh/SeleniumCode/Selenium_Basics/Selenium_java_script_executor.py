# DOM Structure query learning
# https://www.w3schools.com/jsref/prop_node_innertext.asp

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

from_city = driver.execute_script("return document.getElementById('fromcity');")
from_city.send_keys("Mumbai")

dest_city = driver.execute_script("return document.getElementById('destcity');")
dest_city.send_keys("Kolkata")

website_title = driver.execute_script("return document.title;")
print(website_title)

website_URL = driver.execute_script("return document.URL;")
print(website_URL)

link = driver.execute_script("return document.links.item(4).href;")
print(link)

driver.execute_script(f"window.open('{link}');")

time.sleep(10)

driver.close()

