
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


def alert_box():
    alert_btn = driver.find_element(By.ID, "btnShowMsg")
    alert_btn.click()
    time.sleep(2)
    alert = Alert(driver)
    print(alert.text)
    time.sleep(2)
    alert.accept()

#alert_box()

def confirm_box():
    confirm_btn = driver.find_element(By.ID, "button")
    confirm_btn.click()
    time.sleep(2)
    alert = Alert(driver)
    print(alert.text)

    time.sleep(2)
    alert.accept()
    UI_msg = driver.find_element(By.ID, "demo").text
    print(UI_msg)
    assert UI_msg == "You pressed OK!"

    confirm_btn = driver.find_element(By.ID, "button")
    confirm_btn.click()
    alert.dismiss()

    UI_msg_cancel = driver.find_element(By.ID, "demo").text
    print(UI_msg_cancel)
    assert UI_msg_cancel == "You pressed Cancel!"


#confirm_box()

def prompt_box():
    prompt_box = driver.find_element(By.ID, "promptbtn")
    prompt_box.click()
    time.sleep(3)
    alert_prompt = Alert(driver)
    new_value = "GTM"
    alert_prompt.send_keys(new_value)
    time.sleep(3)
    alert_prompt.accept()

    ui_msg = driver.find_element(By.ID, "prompt")
    expected_msg = f"Hello {new_value}! How are you today?"
    assert ui_msg == expected_msg
    time.sleep(5)

    prompt_box = driver.find_element(By.ID, "promptbtn")
    prompt_box.click()
    time.sleep(3)
    alert_prompt.dismiss()
    ui_msg = driver.find_element(By.ID, "prompt")
    expected_msg = f"User cancelled the prompt."
    assert ui_msg == expected_msg




prompt_box()
