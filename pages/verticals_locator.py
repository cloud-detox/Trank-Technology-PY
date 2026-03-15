import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
class verticals_locator:

    def __init__(self,driver):
       self.driver = driver
       self.a = ActionChains(self.driver)
    # Main menu
       self.Verticals=(By.XPATH,'(//a[@href="#"])[2]')
       self.Trading = (By.XPATH,'//li[@data-id="trading"]')

     # Trading sub menus.
       self.Stock = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]')
       self.Paper = (By.XPATH,'//a[text()="Paper Trading"]')
       self.CFD = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
       self.Trading_app =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
       self.Algo = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
       self.Custom =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
       self.WebPortal =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')


       self.Retail_commerce =(By.XPATH,'//li[@data-id="retailEcommerce"]')

     #Retail sub menus:
       self.eComm = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]')
       self.eComm_App =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')


       self.Healthcare=(By.XPATH,'//li[@data-id="healthcare"]')

     # Healthcare sub menus:
       self.Diet_Nut=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
       self.Health_t=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

       self.fintech=(By.XPATH,'//li[@data-id="fintech"]')

     # fintech sub menus
       self.Pos = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
       self.Crypto =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')

       self.custom_app=(By.XPATH,'//li[@data-id="customApp"]')

    #Cutom apps submenus:
       self.Desktop=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
       self.HRM=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
       self.Travel=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
       self.Dating=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
       self.CRM=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
       self.usa_crm=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
       self.ERP=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
       self.E_learn=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
       self.Real_E=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')
    #
    def vertical_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.Verticals)
        self.a.move_to_element(element).perform()

    def trading_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.Trading)
        self.a.move_to_element(element).perform()

    def retail_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.Retail_commerce)
        self.a.move_to_element(element).perform()

    def health_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.Healthcare)
        self.a.move_to_element(element).perform()

    def fintech_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.fintech)
        self.a.move_to_element(element).perform()

    def custom_app_mousehover(self):
        # self.a = ActionChains(self.driver)
        element=self.driver.find_element(*self.custom_app)
        self.a.move_to_element(element).perform()

    def trading_submenus_click(self):

        self.trading_lst = [self.Stock,self.Paper,self.CFD, self.Trading_app,self.Algo,self.WebPortal]
        for locator in self.trading_lst:
          # time.sleep(2)
          self.vertical_mousehover()
          # time.sleep(2)
          self.trading_mousehover()
          # time.sleep(2)
          self.driver.find_element(*locator).click()
          # time.sleep(2)
          self.driver.back()
          # time.sleep(3)
          # driver()

    def retail_submenus_click(self):
        self.retail_lst=[self.eComm,self.eComm_App]
        for locator in self.retail_lst:
            # time.sleep(2)
            self.vertical_mousehover()
            # time.sleep(2)
            self.retail_mousehover()
            # time.sleep(2)
            self.driver.find_element(*locator).click()
            # time.sleep(2)
            self.driver.back()
            # time.sleep(3)

    def healthcare_submenus_click(self):
        self.health_lst=[ self.Diet_Nut,self.Health_t]
        for locator in self.health_lst:
            # time.sleep(2)
            self.vertical_mousehover()
            # time.sleep(2)
            self.health_mousehover()
            # time.sleep(2)
            self.driver.find_element(*locator).click()
            # time.sleep(2)
            self.driver.back()
            # time.sleep(3)

    def fintech_submenus_click(self):
        self.fintech_lst = [self.Pos,self.Crypto]
        for locator in self.fintech_lst:
            # time.sleep(2)
            self.vertical_mousehover()
            # time.sleep(2)
            self.fintech_mousehover()
            # time.sleep(2)
            self.driver.find_element(*locator).click()
            # time.sleep(2)
            self.driver.back()
            # time.sleep(3)

    def custom_submenus_click(self):
        self.custom_lst = [self.Desktop,self.HRM,self.Travel,self.Dating,self.CRM,self.usa_crm,self.ERP,self.E_learn,self.Real_E]
        for locator in self.custom_lst:
            # time.sleep(2)
            self.vertical_mousehover()
            # time.sleep(2)
            self.custom_app_mousehover()
            # time.sleep(2)
            self.driver.find_element(*locator).click()
            # time.sleep(2)
            self.driver.back()
            # time.sleep(3)