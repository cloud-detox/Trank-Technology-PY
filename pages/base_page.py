from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    ACCEPT_COOKIES = (By.XPATH, '//button[@class="is--regular"]')

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def accept_cookies_if_present(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.ACCEPT_COOKIES)
            ).click()
        except:
            pass

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()
