import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.facebook.com/")

driver.find_element(By.CSS_SELECTOR, "#email").send_keys("testuser@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._6luy._9npi").send_keys("P@sswordpassword")
# click to login button
#driver.find_element(By.CSS_SELECTOR, "button[data-testid='royal-login-button']").click()

# click to open registration with partial attribute CSS selector
driver.find_element(By.CSS_SELECTOR, "a[data-testid^='open-registration']").click()

time.sleep(5)
driver.close()

