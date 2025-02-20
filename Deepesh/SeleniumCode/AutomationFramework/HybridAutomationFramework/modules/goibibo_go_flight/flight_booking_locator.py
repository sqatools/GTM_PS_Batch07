from selenium.webdriver.common.by import By

from_city_label_locator = (By.XPATH, "//span[text()='From']//following-sibling::p")
from_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
to_city_input_field = (By.XPATH, "//span[text()='To']//following-sibling::input")
first_option_in_suggestion_list = (By.XPATH, "//ul[@id='autoSuggest-list']/li[1]//p[1]")
close_icon_login_popup = (By.XPATH, "//span[@class='logSprite icClose']")
departure_date_calender = (By.XPATH, "//span[text()='Departure']//parent::div")
traveller_section = (By.XPATH, "//span[contains(text(),'Travellers')]//parent::div")
adults_plus_icon = (By.XPATH, "//p[text()='Adults']//parent::div//span[3]")
children_plus_icon = (By.XPATH, "//p[text()='Children']//parent::div//span[3]")
infants_plus_icon = (By.XPATH, "//p[text()='Infants']//parent::div//span[3]")
done_button = (By.XPATH, "//a[text()='Done']")
search_flight_button = (By.XPATH, "//span[text()='SEARCH FLIGHTS']")

webpush_iframe_id = (By.ID, "webpush-onsite")
will_do_later_option = (By.ID, "deny")


