import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.facebook.com/")

driver.find_element(By.CSS_SELECTOR, '#email').send_keys("test@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[type^='sub']").click()

time.sleep(5)