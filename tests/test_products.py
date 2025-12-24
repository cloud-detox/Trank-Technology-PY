import pytest
from pages.producten_page import ProductenPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestProducten:
    driver: WebDriver
    wait: WebDriverWait

    def test_fotocameras(self):
        pp = ProductenPage(self.driver, self.wait)
        pp.open_cameras()
