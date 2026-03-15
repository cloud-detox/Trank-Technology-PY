import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class get_quote_locator:

    def __init__(self, driver):
        self.driver = driver

        # Button
        self.free_quote = (By.XPATH, '(//a[text()="Get a Free Quote"])[1]')

        # Form fields
        self.name = (By.XPATH, '//input[@placeholder="Your Name"]')
        self.email = (By.XPATH, '(//input[@name="email"])[1]')
        self.otp = (By.XPATH, '//input[@name="otp"]')
        self.company = (By.XPATH, '//input[@name="company"]')
        self.service = (By.XPATH, '//select[@name="service"]')
        self.phone = (By.XPATH, '//input[@name="phone"]')
        self.message = (By.XPATH, '//textarea[@name="message"]')
        self.submit = (By.XPATH, '//input[@name="getintouch"]')
    def fill_quote_form(self):
            # Open form
        self.driver.find_element(*self.free_quote).click()
        # time.sleep(2)

            # Fill details
        self.driver.find_element(*self.name).send_keys("tester01")
        # time.sleep(1)

        self.driver.find_element(*self.email).send_keys("test123@gmail.com")
        # time.sleep(1)

        self.driver.find_element(*self.otp).send_keys("123456")
        # time.sleep(1)

        self.driver.find_element(*self.company).send_keys("TCS")
        # time.sleep(1)

            # Dropdown handling
        dropdown = Select(self.driver.find_element(*self.service))
        dropdown.select_by_visible_text("App Development")
        # time.sleep(1)

        self.driver.find_element(*self.phone).send_keys("1234555")
        # time.sleep(1)

        self.driver.find_element(*self.message).send_keys("Hi I want to know about python fee structure")
        # time.sleep(1)

        self.driver.find_element(*self.submit).click()
        # time.sleep(2)