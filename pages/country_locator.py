import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class country_locator:

    def __init__(self, driver):
        self.driver = driver
        self.country_dropdown = (By.XPATH, '//select[@id="countrySelector"]')

    def select_country(self):
        dropdown_element = self.driver.find_element(*self.country_dropdown)
        dropdown_element.click()
        # time.sleep(1)

        Select(dropdown_element).select_by_visible_text("India")
        # time.sleep(1)