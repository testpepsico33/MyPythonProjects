import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count =len(results)
assert count>0

for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
promoCode="rahulshettyacademy"
driver.find_element(By.XPATH,"//input[@type='text']").send_keys(promoCode)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(10)
promoInfo=driver.find_element(By.CLASS_NAME,"promoInfo").text
print(promoInfo)

