from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InspiratiePage(BasePage):

    # More stable locator (text-based)
    LANDSCAPE = (
        By.XPATH,
        "//a[contains(@href,'landschapsfotografie')]"
    )

    def natuurfotografie(self):
        self.accept_cookies_if_present()

        # Direct navigation
        self.driver.get("https://www.kamera-express.nl/inspiratie")

        # Wait for page to load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Wait until landscape card exists in DOM
        element = self.wait.until(
            EC.presence_of_element_located(self.LANDSCAPE)
        )

        # Scroll element into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        # JS click (bypasses overlay / animation issues)
        self.driver.execute_script("arguments[0].click();", element)
