# DOM Structure query learning


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

def hover_to_element():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

    menu_option = driver.find_element(By.XPATH, "//div[@class='menu-custom-main-menu-container']//a[text()='Tester’s Hub']")
    action = ActionChains(driver)
    action.move_to_element(menu_option)
    action.perform()
    time.sleep(5)

    demo_testing = driver.find_element(By.XPATH, "//span[text()='Demo Testing Site']//parent::a")
    action.move_to_element(demo_testing)
    action.perform()
    time.sleep(5)

    alert_box = driver.find_element(By.XPATH, "//span[text()='AlertBox']//parent::a")
    action.click(alert_box)
    action.perform()


#hover_to_element()

def drag_and_drop_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    # switch to the iframe
    iframe_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_element)

    # get image locator
    image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    # get trash locator
    trash_element = driver.find_element(By.ID, "trash")

    action = ActionChains(driver)
    # dran and drop image from one location to another.
    action.drag_and_drop(image_element, trash_element)
    action.perform()
    time.sleep(5)

    images_list = ['High Tatras 2', 'High Tatras 3', 'High Tatras 4']
    for image in images_list:
        image1 = driver.find_element(By.XPATH, f"//h5[text()='{image}']//parent::li")
        # get trash locator
        trash1 = driver.find_element(By.ID, "trash")
        action.drag_and_drop(image1, trash1)
        action.perform()
        time.sleep(2)

    time.sleep(5)


#drag_and_drop_operation()

def scroll_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    element_Alert_Box = driver.find_element(By.XPATH, "//a[text()='AlertBox']//parent::li")

    action = ActionChains(driver)
    action.scroll_to_element(element_Alert_Box )
    action.click()
    action.perform()

    time.sleep(5)


scroll_to_element()
