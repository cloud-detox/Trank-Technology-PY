import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class aboutus_locator:

    def __init__(self, driver):
        self.driver = driver
        self.a = ActionChains(self.driver)

        self.about =(By.XPATH, '//a[@href="https://www.tranktechnologies.com/about"][1]')


    def about_click(self):
        element = self.driver.find_element(*self.about)
        element.click()
        self.driver.execute_script("window.scrollTo(0,1000)")
        # time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,3734)")
        # time.sleep(2)
        self.driver.back()
        # time.sleep(2)

