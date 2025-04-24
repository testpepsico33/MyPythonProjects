import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"input[minlength='2']").send_keys("Nirmal")
driver.find_element(By.NAME, "email").send_keys("cjnirmalkumar@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123abc")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text

#static dropdown
#select() class is used to point out the locator
dropdown =Select((driver.find_element(By.ID,"exampleFormControlSelect1")))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
dropdown.deselect_by_value()
print(message)
assert "Success" in message

time.sleep(5)