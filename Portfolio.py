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

def Portfolio():
    port=driver.find_element(By.XPATH,"//a[normalize-space()='Portfolio']")
    a.move_to_element(port).perform()
    port.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
Portfolio()