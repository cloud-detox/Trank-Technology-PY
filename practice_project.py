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


def Hover_Technology ():
    Technology = driver.find_element(By.XPATH, '(//a[@href="#"])[5]')
    Action.move_to_element(Technology).perform()
    time.sleep(2)
Hover_Technology()

def hover_ecomdev():
    ecom = driver.find_element(By.XPATH, '//li[@data-id="ecomm"]')
    Action.move_to_element(ecom).perform()
    time.sleep(2)
hover_ecomdev()

def eCommerce_xpaths():
    E1 = '(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]'
    E2 = '(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]'
    E3 = '(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]'
    E4 = '(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]'
    E5 = '(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]'
    E6 = '(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]'
    E7 = '(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]'
    E8 = '(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]'
    E9 = '(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]'
    E10 = '(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]'
    E11 = '(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]'
    E12 = '(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]'
    E13 = '(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]'
    E14 = '(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]'
    E15 = '(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]'
    E16 = '(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]'
    E17 = '(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]'

    List1 = [E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17]

    for xpaths in List1:
        driver.find_element(By.XPATH, xpaths).click()
        time.sleep(2)
        driver.back()
        Hover_Technology()
        hover_ecomdev()
        time.sleep(2)
eCommerce_xpaths()