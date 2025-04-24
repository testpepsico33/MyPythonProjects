import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()
driver.implicitly_wait(2)

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
#Sum validation
prices=driver.find_elements(By.CSS_SELECTOR," tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum+int(price.text)
print(sum)
totalAmount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalAmount
promoCode="rahulshettyacademy"
driver.find_element(By.XPATH,"//input[@type='text']").send_keys(promoCode)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait =WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located(((By.CSS_SELECTOR,".promoInfo"))))
promoInfo=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(promoInfo)

discountAmount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmount > discountAmount


