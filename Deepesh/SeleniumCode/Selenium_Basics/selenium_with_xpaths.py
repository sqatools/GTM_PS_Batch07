 import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.goibibo.com/")

driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()
driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::p").click()


source_city = "Mumbai, India"
from_city_input = driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input")
from_city_input.send_keys(source_city)

drop_down_value = driver.find_element(By.XPATH, f"//span[text()='{source_city}']//parent::p")
drop_down_value.click()

time.sleep(5)
dest_city = "Pune, India"
dest_city_input = driver.find_element(By.XPATH, "//span[text()='To']//following-sibling::input")
dest_city_input.send_keys(dest_city)

drop_down_value2 = driver.find_element(By.XPATH, f"//span[text()='{dest_city}']//parent::p")
drop_down_value2.click()

time.sleep(5)

depart_date = "Feb 12 2025"
driver.find_element(By.XPATH, "//span[text()='Departure']//parent::div").click()
driver.find_element(By.XPATH, f"//div[contains(@aria-label,'{depart_date}')]").click()

time.sleep(5)

driver.close()


