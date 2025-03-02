import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

header = driver.find_element(By.TAG_NAME,"h1")
print(header.text)

driver.find_element(By.NAME,"firstname").send_keys("Subhashree")
driver.find_element(By.NAME,"firstname").send_keys("RAMESH")
time.sleep(10)

driver.find_element(By.LINK_TEXT, "Pytest Framework").click()
time.sleep(10)

driver.find_element(By.PARTIAL_LINK_TEXT, "API").click()
time.sleep(10)

driver.close()