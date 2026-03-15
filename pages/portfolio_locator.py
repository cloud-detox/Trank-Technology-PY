import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class portfolio_locator:

    def __init__(self,driver):
        self.driver = driver

        self.portfolio =(By.XPATH,'//a[@href="https://www.tranktechnologies.com/portfolio"]')


    def portfolio_click(self):
        element = self.driver.find_element(*self.portfolio)
        element.click()
        # time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")
        # time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,3734)")
        # time.sleep(2)
        self.driver.back()
        # time.sleep(2)
