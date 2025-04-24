import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browserSortedVeggies=[]
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElements= driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)
originalBrowserListSorted = browserSortedVeggies
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserListSorted

print(originalBrowserListSorted)
print(browserSortedVeggies)
