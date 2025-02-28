from selenium.webdriver.common.by import By
from .data import *

Login_panel = (By.XPATH, "//*[contains(@class, 'logSprite icClose')]")
save_ad = (By.XPATH, "//*[contains(@class, 'sc-jlwm9r-1 ewETUe')]")
deny_btn = (By.ID,'deny')
iframe_id = (By.ID, "webpush-onsite")
Train_select = (By.XPATH, "//*[text()='Trains' and @class = 'sc-1f95z5i-4 drxYQA']")
source_select = (By.XPATH, "//*[contains(@class, 'styles_FswFldHeading__5ZTwg') and text() = 'From']")
source_station = (By.XPATH, "//*[contains(@class, 'styles_FswAutoCompLegend___EW1V')]//following-sibling::input")
source_stn_select = (By.XPATH, f"//p[contains(@class, 'styles_FswAutoCompItemDescTitle__cEIX6') and text()='{source_city}']")
dest_select = (By.XPATH, "//*[contains(@class, 'styles_FswFldTitle__0nABI') and contains(text() , 'Destination')]")
dest_station = (By.XPATH, "//*[contains(@class,'styles_FswAutoComp__xECf3')]//child::input")
dest_stn_select = (By.XPATH, f"//p[contains(@class, 'styles_FswAutoCompItemDescTitle__cEIX6') and text()='{dest_city}']")
journey_date = (By.XPATH, f"//p[contains(text(), '{mmyy}')]//parent::div//parent::div//p[text()='{dd}']")
search_train = (By.XPATH, "//span[text()='SEARCH TRAINS']")
