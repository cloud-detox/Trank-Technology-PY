from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MerkenPage(BasePage):

    # Stable locators
    CANON_SYSTEEMCAMERA = (
        By.XPATH,
        "//a[contains(@href,'canon-systeemcamera')]"
    )

    CANON_PRODUCT = (
        By.XPATH,
        "//p[contains(text(),'Canon EOS R6')]"
    )

    ADD_TO_CART = (
        By.XPATH,
        "//button[.//span[contains(text(),'In winkelwagen')]]"
    )

    def canon(self):
        # Accept cookies if shown
        self.accept_cookies_if_present()

        # ✅ Direct navigation (NO hover)
        self.driver.get("https://www.kamera-express.nl/merken/canon")

        # Wait for page load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # ---- Open system cameras ----
        system_camera = self.wait.until(
            EC.presence_of_element_located(self.CANON_SYSTEEMCAMERA)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            system_camera
        )
        self.driver.execute_script("arguments[0].click();", system_camera)

        # ---- Open product ----
        product = self.wait.until(
            EC.presence_of_element_located(self.CANON_PRODUCT)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )
        self.driver.execute_script("arguments[0].click();", product)

        # ---- Add to cart (MOST IMPORTANT FIX) ----
        add_to_cart = self.wait.until(
            EC.presence_of_element_located(self.ADD_TO_CART)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_to_cart
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart)
