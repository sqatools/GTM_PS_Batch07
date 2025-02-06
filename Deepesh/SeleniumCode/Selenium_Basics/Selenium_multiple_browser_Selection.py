import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options as Chrome_Option
from selenium.webdriver.firefox.options import Options as Firefox_Option
from selenium.webdriver.edge.options import Options as Edge_Option

browser = 'chrome'
driver = None
headless = False
if browser.lower() == 'firefox':
    ff_option = Firefox_Option()
    if headless:
        ff_option.add_argument('--headless')
    driver = webdriver.Firefox(options=ff_option)

elif browser.lower() == 'edge':
    edge_option = Edge_Option()
    if headless:
        edge_option.add_argument('--headless')

    driver = webdriver.Edge(options=edge_option)

elif browser.lower() == 'chrome':
    chr_option = Chrome_Option()
    if headless:
        chr_option.add_argument('--headless')
    prefs = {
        # set download path of downloaded files.
        "download.default_directory": r"E:\Filesdata\batch07",
        "download.prompt_for_download": False,

    }
    chr_option.add_experimental_option("prefs", prefs)
    chr_option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chr_option)

driver.maximize_window()
driver.implicitly_wait(10)


def drop_selection_values():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    drop_down_element = driver.find_element(By.ID, "admorepass")
    select_obj = Select(drop_down_element)
    select_obj.select_by_visible_text("Add 1 more passenger (100%)")
    driver.save_screenshot("screenshot1.png")
    print("Number of passenger selection is completed")
    time.sleep(5)

    country_dd = driver.find_element(By.ID, "billing_country")
    select_obj2 = Select(country_dd)
    select_obj2.select_by_visible_text("India")
    driver.save_screenshot("screenshot2.png")
    print("Billing country selection is completed")

    time.sleep(5)


def download_file():
    driver.get("https://www.python.org/downloads/")
    download_btn = driver.find_element(By.XPATH, "//div[@class='download-os-windows']//p[@class='download-buttons']/a")
    download_btn.click()
    time.sleep(30)

download_file()

driver.close()
