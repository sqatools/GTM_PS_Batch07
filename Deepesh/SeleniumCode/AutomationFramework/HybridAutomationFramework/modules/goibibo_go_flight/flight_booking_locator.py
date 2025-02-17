from selenium.webdriver.common.by import By

from_city_label_locator = (By.XPATH, "//span[text()='From']//following-sibling::p")
from_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
to_city_input_field = (By.XPATH, "//span[text()='To']//following-sibling::input")
first_option_in_suggestion_list = (By.XPATH, "//ul[@id='autoSuggest-list']/li[1]//p[1]")
close_icon_login_popup = (By.XPATH, "//span[@class='logSprite icClose']")
departure_date_calender = (By.XPATH, "//span[text()='Departure']//parent::div[@role='presentation']")

