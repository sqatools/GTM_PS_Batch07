import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.NAME,"firstname").send_keys("Subhashree")
driver.find_element(By.NAME,"firstname").send_keys("RAMESH")
time.sleep(10)
driver.close()