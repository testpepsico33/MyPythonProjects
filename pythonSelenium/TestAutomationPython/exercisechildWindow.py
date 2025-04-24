import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

windowsOpened =driver.window_handles
childWindow=driver.switch_to.window(windowsOpened[1])
print(childWindow)
grabtext=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(grabtext)
parentWindow=driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(grabtext)
driver.find_element(By.ID,"password").send_keys("feewfe")
driver.find_element(By.ID,"signInBtn").click()
time.sleep(5)