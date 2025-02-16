
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

driver.find_element(By.LINK_TEXT, "Black Box Testing").click()
windows = driver.window_handles
print(windows)
# switch to new window
driver.switch_to.window(windows[1])
time.sleep(5)
bb_testing_heading = driver.find_element(By.XPATH, "//h3[contains(text(),'Black Box Testing')]")
assert bb_testing_heading

# close new tab after verification
#driver.close()
time.sleep(5)

# switch back to original window
driver.switch_to.window(windows[0])

driver.find_element(By.LINK_TEXT, "White Box Testing").click()
time.sleep(5)


driver.close()



