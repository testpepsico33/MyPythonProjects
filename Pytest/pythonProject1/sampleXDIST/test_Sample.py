import time

from selenium import webdriver


def test_Omayo():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_Selenium_143():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.selenium143.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_Tutorial_ninja():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    driver.quit()

def test_Selenium_By_Arun():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium-by-arun.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_Compendium_Dev():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://compendiumdev.co.uk/")
    time.sleep(5)
    driver.quit()

def test_Jquery_Ui():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/")
    time.sleep(5)
    driver.quit()