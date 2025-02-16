
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

drop_down_element = driver.find_element(By.ID, "admorepass")
select_obj = Select(drop_down_element)
#select_obj.select_by_value("3")
#select_obj.select_by_index(3)
select_obj.select_by_visible_text("Add 1 more passenger (100%)")


country_dd = driver.find_element(By.ID, "billing_country")
select_obj2 = Select(country_dd)
select_obj2.select_by_visible_text("India")

time.sleep(5)
driver.close()



