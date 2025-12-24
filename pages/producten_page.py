from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductenPage(BasePage):

    SONY_A7 = (By.XPATH, "//p[contains(text(),'Sony A7 IV body')]")
    ADD_TO_CART = (By.XPATH, "//button[@class='full-width sf-button']")

    def open_cameras(self):
        self.accept_cookies_if_present()

        # Direct navigation (no hover)
        self.driver.get("https://www.kamera-express.nl/camera/systeemcamera")

        self.click(self.SONY_A7)
        self.click(self.ADD_TO_CART)
