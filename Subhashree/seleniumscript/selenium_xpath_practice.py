
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://navi-ref-oi-api.westeurope.cloudapp.azure.com/IdentityManager/page.axd?")

driver.find_element(By.XPATH,"//div[@id='F0_ctl00_Main_Main_ControlRef1_ContainerTemplate1_R0_Container21']//input").send_keys("TestU")
driver.find_element(By.XPATH,"//div[@id='F0_ctl00_Main_Main_ControlRef1_ContainerTemplate1_R0_Container22']//input").send_keys("Svdg@2295!!-")
driver.find_element(By.XPATH,"//span[@id='F0_ctl00_Main_Main_ControlRef1_Label1']//preceding-sibling::button").click()


driver.find_element(By.XPATH,"//span[@id='F0_ctl00_ControlRef8_ControlRef15_ControlRef15_ControlRef8b_Main_Main_ControlRef3_ControlRef3_ControlRef7_Container7_ContainerTemplate4_R1_Label6']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='F0_ctl00_ControlRef8_ControlRef15_ControlRef15_ControlRef8b_Main_Main_R0_ObjectSwitchContainer1_Tab1_ctl00_T0_ctl00_Container18_ControlRef15_ControlRef1_ControlRef1_Container3']//h1").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[@class='imx-dropdown-toggle']//i").click()
time.sleep(5)

driver.find_element(By.XPATH,f"//ul[@class='imx-dropdown-menu']//li[contains(text(),'Log Out')]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//span[@id='Popup0_Popup0_ControlRef2_Container6_Container7']//button").click()
time.sleep(10)