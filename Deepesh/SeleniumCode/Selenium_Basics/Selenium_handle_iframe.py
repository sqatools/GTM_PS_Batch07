
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

# get iframe element
iframe_element = driver.find_element(By.XPATH, "//iframe[@name='globalSqa']")

# switch to the iframe
driver.switch_to.frame(iframe_element)

# click on element inside the iframe
driver.find_element(By.ID, "mobile_menu_toggler").click()

time.sleep(5)

page_heading1 = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1").text
print(page_heading1)

# switch out of the iframe content
driver.switch_to.default_content()

# Find the page heading
page_heading2 = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1").text
print(page_heading2)

# click on new tab button
driver.find_element(By.XPATH, "//li[text()='Open New Tab']").click()

# switch to new iframe
# iframe2 = driver.find_element(By.XPATH, "")
click_here_element = driver.find_element(By.XPATH, "//a[text()='Click Here']")

# take screenshot of element
click_here_element.screenshot("click_here_element.png")

# take screenshot of active page.
driver.save_screenshot("iframe_testing_page.png")

click_here_element.click()


time.sleep(5)

driver.close()



