import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#.context_click()
#action.double_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).click().perform()


