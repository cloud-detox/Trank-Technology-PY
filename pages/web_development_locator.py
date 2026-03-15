import time
from selenium.webdriver.common.by import By


class web_development_locator:

    def __init__(self, driver):
        self.driver = driver


    # -------- WEB DEVELOPMENT -------- #

    def web_development_section(self):

        links = [
            '//a[@href="https://www.tranktechnologies.com/web-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/cms-website-development-company-in-india"]',
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[7]',
            '//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"]'
        ]

        for link in links:
            self.driver.find_element(By.XPATH, link).click()
            self.driver.back()

        # open dropdown
        self.driver.find_element(By.XPATH, '(//i[@aria-hidden="true"])[3]').click()

        self.driver.find_element(
            By.XPATH,
            '//a[contains(@href,"website-development-company-in-delhi-ncr")]'
        ).click()

        windows = self.driver.window_handles

        if len(windows) > 1:
            self.driver.switch_to.window(windows[1])
            print(self.driver.title)
            self.driver.close()
            self.driver.switch_to.window(windows[0])


    # -------- APP DEVELOPMENT -------- #

    def app_development_section(self):

        links = [
            '//a[@href="https://www.tranktechnologies.com/app-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company-in-india"]'
        ]

        for link in links:
            self.driver.find_element(By.XPATH, link).click()
            self.driver.back()

        # dropdown open
        self.driver.find_element(By.XPATH, '(//i[@aria-hidden="true"])[4]').click()

        delhi_links = [
            '//a[@href="https://www.tranktechnologies.com/android-app-development-company-in-delhi-ncr"]',
            '//a[@href="https://www.tranktechnologies.com/app-development-company-in-delhi-ncr"]'
        ]

        for link in delhi_links:

            self.driver.find_element(By.XPATH, link).click()

            windows = self.driver.window_handles

            if len(windows) > 1:
                self.driver.switch_to.window(windows[1])
                print(self.driver.title)
                self.driver.close()
                self.driver.switch_to.window(windows[0])


    # -------- GRAPHIC DESIGN -------- #

    def graphic_section(self):

        links = [
            '//a[@href="https://www.tranktechnologies.com/graphic-design-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/logo-design-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/banner-design-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/packaging-design-company-in-india"]',
            '//a[@href="https://www.tranktechnologies.com/business-cards-design-company-in-india"]'
        ]

        for link in links:
            self.driver.find_element(By.XPATH, link).click()
            print(self.driver.title)
            self.driver.back()


    # -------- UI / UX -------- #

    def ux_ui_section(self):

        links = [
            '//a[@href="https://www.tranktechnologies.com/ui-ux-design-company-in-india"]',
            '//a[text()="UI UX Design"]',
            '//a[text()="Responsive Web Design"]',
            '//a[text()="Brand Identity Design"]'
        ]

        for link in links:

            self.driver.find_element(By.XPATH, link).click()
            print(self.driver.title)
            self.driver.back()
