from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@type ='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(@type,'submit')]").click()

#text method
#//tagname[text()='attribute']

#contains method
#//tagname[contains(@attribute, "attribute value")]
driver.close()
