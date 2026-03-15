import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class contactus_locator:

    def __init__(self, driver):
        self.driver = driver

        # Contact link
        self.contact_option = (By.XPATH, '(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        # Form fields
        self.name = (By.XPATH, '(//input[@placeholder="Your Name"])[2]')
        self.email = (By.XPATH, '//input[@placeholder="Your Email"]')
        self.send_otp = (By.XPATH, '//button[@id="send_otp"]')
        self.otp = (By.XPATH, '(//input[@placeholder="Enter OTP"])[2]')
        self.company = (By.XPATH, '(//input[@name="company"])[2]')
        self.service = (By.XPATH, '(//select[@name="service"])[2]')
        self.phone = (By.XPATH, '(//input[@name="phone"])[2]')
        self.message = (By.XPATH, '(//textarea[@placeholder="Message"])[2]')
        self.submit = (By.XPATH, '(//input[@type="submit"])[2]')

    def fill_contact_form(self):

        # Open Contact Page
        self.driver.find_element(*self.contact_option).click()
        # time.sleep(2)

        # Fill form
        self.driver.find_element(*self.name).send_keys("Mamta Bhatt")
        # time.sleep(1)

        self.driver.find_element(*self.email).send_keys("test@gmail.com")
        # time.sleep(1)

        # click send otp
        self.driver.find_element(*self.send_otp).click()

        # wait for alert and accept
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        # time.sleep(4)

        self.driver.find_element(*self.otp).send_keys("123456")
        # time.sleep(1)
        # # Handle alert
        try:

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

        except:
            print("No alert present")

        # time.sleep(2)

        self.driver.find_element(*self.company).send_keys("Tata Consultancy Services")
        # time.sleep(1)

        service = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.service) )
        # Dropdown
        dropdown = Select(self.driver.find_element(*self.service))
        dropdown.select_by_visible_text("App Development")
        # time.sleep(1)

        self.driver.find_element(*self.phone).send_keys("0123456789")
        # time.sleep(1)

        self.driver.find_element(*self.message).send_keys("I want to inquiry about the ongoing courses")
        # time.sleep(1)

        self.driver.find_element(*self.submit).click()
        # time.sleep(3)

        self.driver.back()
        # time.sleep(2)