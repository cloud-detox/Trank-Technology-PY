import time
from selenium.webdriver.common.by import By

class social_locator:

    def __init__(self, driver):
        self.driver = driver


        self.facebook=(By.XPATH, '//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkdin=(By.XPATH, '//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.instagram=(By.XPATH, '//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pinterest=(By.XPATH, '//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter=(By.XPATH, '//a[@href="https://twitter.com/tranktechno"]')
        self.youtube=(By.XPATH,'//img[@alt="Youtube"]')
        self.quora=(By.XPATH, '//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')

    def close_chat_popup(self):
        try:
            time.sleep(2)

            # Switch to tawk iframe if present
            frames = self.driver.find_elements(By.XPATH, "//iframe[contains(@src,'tawk')]")
            if len(frames) > 0:
                self.driver.switch_to.frame(frames[0])
                time.sleep(1)

                close_btn = self.driver.find_elements(By.XPATH, "//i[contains(@class,'tawk-icon-x')]")
                if len(close_btn) > 0:
                    close_btn[0].click()
                    time.sleep(1)

                self.driver.switch_to.default_content()
        except:
            self.driver.switch_to.default_content()

    def social_links(self):

            self.social_lists = [
                self.facebook,
                self.linkdin,
                self.instagram,
                self.pinterest,
                self.twitter,
                self.youtube
            ]

            for social in self.social_lists:
                # Close popup before clicking
                self.close_chat_popup()

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # time.sleep(2)

                element = self.driver.find_element(*social)

                # Scroll element into view
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                # time.sleep(1)

                # JS click to avoid interception
                self.driver.execute_script("arguments[0].click();", element)
                # time.sleep(3)

                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[1])

                print("New Tab Title:", self.driver.title)

                self.driver.close()
                self.driver.switch_to.window(windows[0])
                # time.sleep(2)

            #  Handle Quora separately (same pattern)

            self.close_chat_popup()

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)

            element = self.driver.find_element(*self.quora)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # time.sleep(1)
            self.driver.execute_script("arguments[0].click();", element)
            # time.sleep(3)

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])

            print("Quora Title:", self.driver.title)

            self.driver.close()
            self.driver.switch_to.window(windows[0])

    # def social_links(self):
    #
    #     self.social_lists=[self.facebook,self.linkdin,self.instagram,self.twitter,self.youtube]
    #
    #     for social in self.social_lists:
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(2)
    #         self.driver.find_element(*social).click()
    #         time.sleep(2)
    #         print(self.driver.title)
    #         windows = self.driver.window_handles
    #         self.driver.switch_to.window(windows[1])
    #         print(self.driver.title)
    #         self.driver.close()
    #         self.driver.switch_to.window(windows[0])
    #
    #
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    #     self.close_btn =self.driver.find_elements(By.XPATH,'(//i[@class="tawk-icon tawk-icon-x"])[1]')
    #     self.close_btn[0].click()
    #     time.sleep(2)
    #     self.driver.find_element(self.quora).click()
    #     print(driver.title)
    #     windows = driver.window_handles
    #     self.driver.switch_to.window(windows[1])
    #     print(driver.title)
    #     driver.close()
    #
    #
    #

