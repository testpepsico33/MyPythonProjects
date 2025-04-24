import selenium
import pytest
from selenium.webdriver.chrome import webdriver
import time
import chromedriver_autoinstall
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="function")
def launchBrowser():

    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    global driver

    #chr_options=Options()
    #chr_options.add_experimental_option("detach", True)
    #global driver
    #driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)



def test_printUrl(launchBrowser):
    driver.get("https://www.redbus.in/")
    print(driver.current_url)


