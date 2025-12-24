from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    ACCEPT_COOKIES = (By.XPATH, '//button[@class="is--regular"]')
    LOGIN_HOVER = (By.XPATH, '(//div[@class="login-button"])[2]')
    LOGIN_BUTTON = (By.XPATH, '(//button[@class="sf-button"])[2]')
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.ID, "btn_login")

    def login(self, email, password):
        self.click(self.ACCEPT_COOKIES)
        self.hover(self.LOGIN_HOVER)
        self.click(self.LOGIN_BUTTON)

        self.type(self.USERNAME, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
