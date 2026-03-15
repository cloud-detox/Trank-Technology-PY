import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
class technology_locator:

    def __init__(self,driver):
       self.driver = driver
       self.a = ActionChains(self.driver)

    # Main menu
       self.tech=(By.XPATH,'(//a[text()="Technologies"])[1]')
       self.ecomm_dev=(By.XPATH,'//li[@data-id="ecomm"]')

    # ecommerce sub menus:
       self.mag = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
       self.code = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
       self.Big_Co = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
       self.cs_cart = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
       self.Nop_Co = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
       self.Lara = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
       self.Drupa = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
       self.Joomla = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
       self.Express_JS = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
       self.Opencart = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
       self.WordPress = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
       self.Shopify = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
       self.Node_JS = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
       self.Woo_Co = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
       self.Presta = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
       self.Wix = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
       self.React_JS =(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

       self.mobile_app=(By.XPATH,'//li[@data-id="mobileApp"]')

        # mobile apps sub menus:
       self.react_n=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
       self.Xamar_M=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
       self.Flutter=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
       self.Swift=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
       self.Enter_Mob=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
       self.Kotlin=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
       self.Ionic=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
       self.Appoint=(By.XPATH,'(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

       self.artificial = (By.XPATH,'(//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"])[1]')


    def technology_mousehover(self):
        element=self.driver.find_element(* self.tech)
        self.a.move_to_element(element).perform()


    def ecommerce_mousehover(self):
        element=self.driver.find_element(*self.ecomm_dev)
        self.a.move_to_element(element).perform()

    def ecommerce_submenus_click(self):
        self.ecom_lst = [self.mag,self.code,self.Big_Co,self.cs_cart,self.Nop_Co,
                         self.Lara,self.Drupa,self.Joomla,self.Express_JS,self.Opencart,
                         self.WordPress,self.Shopify, self.Node_JS,self.Woo_Co,self.Presta,self.Wix,self.React_JS
                         ]
        for locator in self.ecom_lst :
            # time.sleep(2)
            self.technology_mousehover()
            # time.sleep(2)
            self.ecommerce_mousehover()
            # time.sleep(2)
            self.driver.find_element(*locator).click()
            # time.sleep(2)
            self.driver.back()
            # time.sleep(3)

    def mobile_mousehover(self):
        element= self.driver.find_element(* self.mobile_app)
        self.a.move_to_element(element).perform()


    def mobile_submenus_click(self):
        self.mobile_lst =[self.react_n,self.Xamar_M,self.Flutter,self.Swift,self.Enter_Mob,
                      self.Kotlin,self.Ionic,self.Appoint
                         ]
        for locator in self.mobile_lst:
           # time.sleep(2)
           self.technology_mousehover()
           # time.sleep(2)
           self.mobile_mousehover()
           # time.sleep(2)
           self.driver.find_element(*locator).click()
           # time.sleep(2)
           self.driver.back()
           # time.sleep(3)

    def artificial_mousehover(self):
        element=self.driver.find_element(*self.artificial)
        self.a.move_to_element(element).perform()
    def artificial_submenus_click(self):
        self.artificial_lst =[self]
        for locator in self.artificial_lst:
           # time.sleep(2)
           self.technology_mousehover()
           # time.sleep(2)
           self.artificial_mousehover()
           # time.sleep(2)
           self.driver.find_element(*self.artificial).click()
           time.sleep(2)
           self.driver.back()
