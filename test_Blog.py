import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
# @pytest.mark.smoke
def test_Navigateurl():
    driver.get("https://www.tranktechnologies.com/")
    driver.maximize_window()
    time.sleep(2)
# Navigateurl()
# @pytest.mark.smoke
def test_blog():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']").click()
    driver.back()
    time.sleep(2)
# blog()