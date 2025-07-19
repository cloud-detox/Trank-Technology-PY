from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver= webdriver.Chrome()
driver.get("https://www.tranktechnologies.com/")
driver.maximize_window()
time.sleep(2)
a=ActionChains(driver)

def Ecommerce():
    t=driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[3]')
    a.move_to_element(t).perform()
    eco=driver.find_element(By.XPATH,"//strong[normalize-space()='eCommerce Development']")
    a.move_to_element(eco).perform()

def Magneto():
    Ecommerce()
    driver.find_element(By.XPATH,"//a[normalize-space()='Magento Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Opencart():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Opencart Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Codeigniter():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Codeigniter Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Wordpress():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='WordPress Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Bigcommerce():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Big Commerce']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Shopify():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Shopify Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def CScart():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CS-Cart Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Nodejs():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Node JS Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Nop():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Nop')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Woo():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Woo Commerce']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Laravel():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Laravel Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Prestashop():
    Ecommerce()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Prestashop Development']").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

Magneto()
Opencart()
Codeigniter()
Wordpress()
Bigcommerce()
Shopify()
CScart()
Nodejs()
Nop()
Woo()
Laravel()
Prestashop()

def MobileApp_Development():
    M = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[3]')
    a.move_to_element(M).perform()
    mobile = driver.find_element(By.XPATH, "//strong[normalize-space()='Mobile App Development']")
    a.move_to_element(mobile).perform()

def React_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//a[contains(text(),'React Native Mobile')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Enterprise_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//a[contains(text(),'Enterprise Mobile App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Xamari_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Xamarin Mobile App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Kotlin_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Kotlin Mobile App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Flutter_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Ionic_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Ionic App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Swift_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Swift App')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def Appointment_App():
    MobileApp_Development()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Appointment Booking')]").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

React_App()
Enterprise_App()
Xamari_App()
Kotlin_App()
Flutter_App()
Ionic_App()
Swift_App()
Appointment_App()

def AI():
    M = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[3]')
    a.move_to_element(M).perform()
    art=driver.find_element(By.XPATH,"//strong[normalize-space()='Artificial Intelligence']")
    a.move_to_element(art).perform()
    art.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
AI()




