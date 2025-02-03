import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# open URL in the browser
driver.get("https://www.goibibo.com/")

# set initial wait for web elements
driver.implicitly_wait(10)
driver.maximize_window() # maximize local browser window

driver.find_element(By.CSS_SELECTOR,"span[role ='presentation']").click()



time.sleep(10)
driver.close()
