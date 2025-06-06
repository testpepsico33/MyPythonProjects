import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4) #global wait time 4 sec defined

driver.get("https://rahulshettyacademy.com/angularpractice/")

#//a[contains(@href,'shop')] , a[href*='shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products =driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successMessage=driver.find_element(By.CLASS_NAME,"alert").text
print(successMessage)

assert "Success! Thank you!" in successMessage
driver.close()