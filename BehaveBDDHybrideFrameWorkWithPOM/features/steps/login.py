from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given(u'I navigate to the login page')
def step_impl(context):
    service = Service(
        "C://Users//nimalkumar.j//PycharmProjects//BehaveBDDHybrideFrameWorkWithPOM//driver//chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter valid email address and valid password into the field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("chittujs@yahoo.com")
    context.driver.find_element(By.ID, "input-password").send_keys("76@Kumar")

@when(u'I click on Login Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()

@then(u'I should logged in')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[normalize-space()='Edit your account information']").is_displayed()
    context.driver.quit()

@when(u'I enter invalid email and valid password into the field')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "nirmalcjarav" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys("76@Kumar")

@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert (context.driver.find_element(By.XPATH, "(//div[@class='alert alert-danger alert-dismissible'])[1]").text
            .__contains__(expected_warning_message))

@when(u'I enter valid email and invalid password into the field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("chittujs@yahoo.com")
    context.driver.find_element(By.ID, "input-password").send_keys("76@Kumar112")

@when(u'I enter invalid email and invalid password into the field')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "nirmalcjarav" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys("76@Kumar12345")

@when(u'I dont enter anything into the email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
