from selenium.webdriver.common.by import By

first_name_element = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name_element = (By.XPATH, "(//input[@id='firstname'])[2]")
dob_element = (By.ID, "birthday")
select_num_of_pass_dd = (By.ID, "admorepass")

one_way_radio_btn = (By.ID, "oneway")
from_city_field = (By.ID, "fromcity")
dest_city_field = (By.ID, "destcity")
depart_date_calender = (By.ID, "departdate")
return_date_calender = (By.ID, "returndate")
visa_date_calender  = (By.ID, "visadate")
whats_app_radio = (By.ID, "whatsapp")


