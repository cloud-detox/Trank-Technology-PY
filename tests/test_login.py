import pytest
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestLogin:
    driver: WebDriver
    wait: WebDriverWait

    def test_login(self):
        lp = LoginPage(self.driver, self.wait)
        lp.login("sunilrathodn999@gmail.com", "Naik@2025")
