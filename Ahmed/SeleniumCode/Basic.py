import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
'''
# open URL in the browser
driver.get("https://www.google.co.in")

# set initial wait for web elements
driver.implicitly_wait(10)
driver.maximize_window() # maximize local browser window

driver.find_element(By.NAME, "q").send_keys("python")
driver.find_element(By.NAME, "btnK").click()

time.sleep(10)
driver.close()
'''

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.XPATH,"//input[contains(@value, 'radio_123')]").click()
driver.find_element(By.XPATH,"//input[contains(@value, 'radio_345')]").click()
driver.find_element(By.ID,"firstname").send_keys("Ahmed")
driver.find_element(By.NAME,"birthday").send_keys("07-10-1991")
driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,"female").click()
driver.find_element(By.ID,"oneway").click()
driver.find_element(By.ID,"roundtrip").click()
driver.find_element(By.ID,'fromcity').send_keys("Chennai")
driver.find_element(By.ID,'destcity').send_keys("Bengaluru")
driver.find_element(By.ID, 'departdate').send_keys("01-02-2025")
driver.find_element(By.ID, 'returndate').send_keys("10-02-2025")
driver.find_element(By.ID, 'visadate').send_keys("05-02-2025")
driver.find_element(By.ID,"eamil").click()
driver.find_element(By.ID,"whatsapp").click()
driver.find_element(By.ID, 'billing_name').send_keys("Ahmed")
driver.find_element(By.ID, 'billing_phone').send_keys("1234567890")
driver.find_element(By.ID, 'billing_email').send_keys("ahmed@gmail.com")
driver.find_element(By.ID, 'billing_address').send_keys("1st Street")
driver.find_element(By.ID, 'billing_country').send_keys("India")
driver.find_element(By.ID, 'postcode').send_keys("600002")
driver.find_element(By.ID, 'Prefecture').send_keys("Chennai")
driver.find_element(By.ID, 'street_address1').send_keys("1st Cross")
driver.find_element(By.ID, 'street_address2').send_keys("1st Main Road")
driver.find_element(By.CLASS_NAME, 'contact-form-name').send_keys("Ahmed")
driver.find_element(By.CLASS_NAME, 'contact-form-email').send_keys("ahmed@gmail.com")
driver.find_element(By.CLASS_NAME, 'contact-form-email-message').send_keys("Hello")
driver.find_element(By.CLASS_NAME, 'contact-form-button.contact-form-button-submit').click()
driver.find_element(By.NAME, 'q').send_keys("Automation")
driver.find_element(By.CLASS_NAME, 'gsc-search-button').click()
time.sleep(10)