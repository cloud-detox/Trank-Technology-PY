import time
from selenium.webdriver.support.ui import Select

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tranktechnologies.com/")

driver.implicitly_wait(5)
Action = ActionChains(driver)


def hover_technology():
    technology = driver.find_element(By.XPATH, '(//a[text()="Technologies"])[1]')
    Action.move_to_element(technology).perform()
    time.sleep(2)
hover_technology()

# def hover_Ecomdevelopment():
#     ecomdev = driver.find_element(By.XPATH, '//strong[text()="eCommerce Development"]')
#     Action.move_to_element(ecomdev).perform()
#     time.sleep(2)
# hover_Ecomdevelopment()
#
# xpaths = [
#     '(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]',
#     '(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]'
# ]
#
# for xpath in xpaths:
#     hover_technology()
#     time.sleep(1)
#     hover_Ecomdevelopment()
#     time.sleep(1)
#
#     driver.find_element(By.XPATH, xpath).click()
#     time.sleep(2)
#     driver.back()

# hover_technology()
# def hover_Mobileappdev():
#     Mobileappdev = driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company-in-india"])[1]')
#     Action.move_to_element(Mobileappdev).perform()
#     time.sleep(2)
#
#
# ListMAD = ['(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]' , '(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]']
# for xpath in ListMAD:
#     hover_technology()
#     time.sleep(1)
#     hover_Mobileappdev()
#     time.sleep(1)
#
#     driver.find_element(By.XPATH, xpath).click()
#     time.sleep(2)
#     driver.back()














