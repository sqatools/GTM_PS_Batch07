import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(17)

driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal-email']").send_keys("Test@email.com")
driver.find_element(By.CSS_SELECTOR,"input[data-testid^='royal-p']").send_keys("Test")
driver.find_element(By.CSS_SELECTOR,'button[name ="login"]').click()

time.sleep(10)
driver.close()