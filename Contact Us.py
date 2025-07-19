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

def Contact():
    contact=driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Contact us']")
    a.move_to_element(contact).perform()
    contact.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
Contact()