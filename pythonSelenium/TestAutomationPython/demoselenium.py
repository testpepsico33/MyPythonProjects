import time

from selenium import webdriver
from selenium.webdriver.chrome.service import service
#service()
driver_Edge = webdriver.Edge()
driver_Edge.get("https://rahulshettyacademy.com/")
driver_Edge.maximize_window()
print(driver_Edge.title)
print(driver_Edge.current_url)

time.sleep(5)

driver_Chrome = webdriver.Chrome()
driver_Chrome.get("https://rahulshettyacademy.com/")
driver_Chrome.maximize_window()
print(driver_Chrome.title)
print(driver_Chrome.current_url)

