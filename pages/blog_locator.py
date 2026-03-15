import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class blog_locator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.a = ActionChains(self.driver)

        self.blog = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        # blog page clicks
        self.App_Dev=(By.XPATH,'//a[@href="/blog/category/app-development/"]')
        self.Web_Dev=(By.XPATH,'//a[@href="/blog/category/web-development/"]')
        self.Software=(By.XPATH,'//a[@href="/blog/category/software-development/"]')
        self.Digital=(By.XPATH,'//a[@href="/blog/category/digital-marketing/"]')
        self.email=(By.XPATH,'//a[@href="/blog/category/email-marketing/"]')
        self.AI=(By.XPATH,'//a[@href="/blog/category/artificial-intelligence/"]')
        self.UI_Design=(By.XPATH,'//a[@href="/blog/category/ui-ux-design/"]')

        # search option
        self.search=(By.XPATH, '//span[text()="Search"]')
        self.search_key=(By.XPATH, '//input[@name="s"]')
        self.submit=(By.XPATH, '//button[@type="submit"]')


    def blog_options_click(self):

        # Open blog page once
        self.driver.find_element(*self.blog).click()

        blog_clicks = [
            self.App_Dev, self.Web_Dev, self.Software,
            self.Digital, self.email, self.AI, self.UI_Design
        ]

        for locator in blog_clicks:

            self.driver.find_element(*locator).click()
            print(self.driver.title)

            self.driver.back()

        # Search functionality
        self.driver.find_element(*self.search).click()

        self.driver.find_element(*self.search_key).send_keys("Selenium with python")

        self.driver.find_element(*self.submit).click()
