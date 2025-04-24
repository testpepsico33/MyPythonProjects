import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_Options=webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")

driver =webdriver.Chrome(options=chrome_Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)