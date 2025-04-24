from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I got navigate to the home page')
def step_impl(context):
    service = Service(
        "C://Users//nimalkumar.j//PycharmProjects//BehaveBDDHybrideFrameWorkWithPOM//driver//chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo")


@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()


@then(u'valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()


@then(u'Proper Message should be displayed in Search result')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search "
                                                  "criteria.')]").text.__eq__(expected_text)
    context.driver.quit()


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@when(u'I dont enter anything into the Search box filed')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
