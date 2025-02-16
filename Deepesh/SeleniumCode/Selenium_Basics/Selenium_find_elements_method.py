import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# get current url
print("current url :", driver.current_url)

elements_list = driver.find_elements(By.XPATH, "//a[contains(@href, '')]")

for element in elements_list:
    print(element)
    link = element.get_attribute("href")
    print(link)
    with open("all_links.txt", "a") as file:
        if link is not None:
            file.write(f"{link}\n")

driver.close()
