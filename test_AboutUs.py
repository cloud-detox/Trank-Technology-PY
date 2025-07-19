import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
driver.get("https://www.tranktechnologies.com/")
driver.maximize_window()
time.sleep(2)
a=ActionChains(driver)

@pytest.mark.smoke
def test_About_Us():
    about=driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='About us']")
    a.move_to_element(about).perform()
    about.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
# test_About_Us()