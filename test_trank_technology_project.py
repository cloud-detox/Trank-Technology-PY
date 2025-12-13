# Whenever we put test that all method collect pytest bydefault and execute it.
# pytest is framewok - if in other files we put test then that also run
# to run pytest we dont need to call method - thats why we commented out
# to run methods we need pytest
# for report generate we need install first pytest html for that first use this command = pip install pytest-html
# for report generate use this = pytest --html=report.html
# thats why we define method to organize the project and in the report we able to see which module run , passed and failed
# capital T in test is not recognized by pytest . only small t is recongized
# If we use pytest then we dont need to call method thats why we here commented out all methods
# when file not able to generate report or not recongized then we can use this command = pytest test_trank_technology_project.py --html=report.html

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.tranktechnologies.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)

# Vertical
def test_vertical():
    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a = ActionChains(driver)
    a.move_to_element(vertical).perform()
    time.sleep(2)
# test_vertical()

def test_trading():
    a = ActionChains(driver)

    trading = driver.find_element(By.XPATH,"//strong[text()='Trading']")
    a.move_to_element(trading).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//a[text()='Stock Trading'])[1]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Algo Trading']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Paper Trading']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Custom')]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//a[text()='CFD Trading'])[1]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//a[text()='Web Portal Trading'])[1]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Trading App')]").click()
    driver.back()
    time.sleep(2)
    print("Done Execution for vertical trading")
# test_trading()

def test_RetailAndEcommerce():
    a = ActionChains(driver)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    # click on Retail And Ecommerce
    driver.find_element(By.XPATH,"//strong[text()='Retail and Ecommerce']").click()
    time.sleep(2)

    # Perform Retail validations
    vertical = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    Retail = driver.find_element(By.XPATH,"//strong[text()='Retail and Ecommerce']")
    a.move_to_element(Retail).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@id='retailEcommerce']//li[1]//a[1]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    Retail = driver.find_element(By.XPATH,"//strong[text()='Retail and Ecommerce']")
    a.move_to_element(Retail).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='eCommerce App Development']").click()
    driver.back()
    time.sleep(2)
    print("Done Eexecution for Vertical Retail and Ecommerce")
# test_RetailAndEcommerce()

def test_healthcare():
    a = ActionChains(driver)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    # click on healthcare
    driver.find_element(By.XPATH, "//strong[text()='Healthcare']").click()
    time.sleep(2)
    # perform healthcare validations
    vertical = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    healthcare = driver.find_element(By.XPATH,"//strong[text()='Healthcare']")
    a.move_to_element(healthcare).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Diet &')]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    healthcare = driver.find_element(By.XPATH,"//strong[text()='Healthcare']")
    a.move_to_element(healthcare).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//a[text()='Health tracking App'])[1]").click()
    driver.back()
    time.sleep(2)
    print("Done execution for vertical healthcare")
# test_healthcare()

def test_fintech():
    a = ActionChains(driver)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    # click on fintech
    driver.find_element(By.XPATH, "//strong[text()='Fintech']").click()
    time.sleep(2)
    # perform fintech validations
    vertical = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    Fintech = driver.find_element(By.XPATH,"//strong[text()='Fintech']")
    a.move_to_element(Fintech).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Pos Software')]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    Fintech = driver.find_element(By.XPATH,"//strong[text()='Fintech']")
    a.move_to_element(Fintech).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"(//a[text()='Crypto'])[1]").click()
    driver.back()
    time.sleep(2)
    print("Done execution for Fintech")
# test_fintech()

def test_customApp():
    a = ActionChains(driver)

    # click on logo of trank&technologies
    driver.find_element(By.XPATH,'//img[@alt="Trank Technologies"]').click()
    time.sleep(2)

    # perform custom app validations
    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Desktop App')]").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='CRM Development']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='HRM Development']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='ERP App Development']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Travel']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='E-Learning']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Dating App Development']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Real Estate']").click()
    driver.back()
    time.sleep(2)

    vertical = driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
    a.move_to_element(vertical).perform()
    time.sleep(2)
    customApp = driver.find_element(By.XPATH,"//strong[text()='Custom App']")
    a.move_to_element(customApp).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='CRM Development USA']").click()
    driver.back()
    time.sleep(2)
    print("Done execution for vertical custom app")
# test_customApp()

# Technology
def test_technology():
    a = ActionChains(driver)
    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
# test_technology()

def test_eCommerceDevelopment():
    a = ActionChains(driver)

    # click on eCommerce Development
    driver.find_element(By.XPATH,"//strong[text()='eCommerce Development']").click()
    time.sleep(2)
    # perform eCommerce Development validations
    Technology = driver.find_element(By.XPATH, "//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Magento Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Opencart Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Codeigniter Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='WordPress Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Big Commerce']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Shopify Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='CS-Cart Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Node JS Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Nop')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Woo Commerce']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Laravel Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Prestashop Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Drupal Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Wix Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Joomla Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='React JS Development']").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Express JS Development']").click()
    driver.back()
    time.sleep(2)
    print("Done execution for technologies eCommerce development")
# test_eCommerceDevelopment()

def test_MobileAppDevelopment():
    a = ActionChains(driver)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    # click on Mobile App Development
    driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']").click()
    time.sleep(2)
    # perform mobile app development validations
    Technology = driver.find_element(By.XPATH, "//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'React Native Mobile')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Enterprise Mobile App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Xamarin Mobile App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Kotlin Mobile App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Ionic App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Swift App')]").click()
    driver.back()
    time.sleep(2)

    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    Mobile_App_Development = driver.find_element(By.XPATH,"//strong[text()='Mobile App Development']")
    a.move_to_element(Mobile_App_Development).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Appointment Booking')]").click()
    driver.back()
    time.sleep(2)
    print("Done execution for Technologies Mobile App Development")
# test_MobileAppDevelopment()

def test_Ai():
    a = ActionChains(driver)
    Technology = driver.find_element(By.XPATH,"//a[text()='Technologies']")
    a.move_to_element(Technology).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//strong[text()='Artificial Intelligence']").click()
    time.sleep(2)
    print("Done execution for Technologies AI")
# test_Ai()

def test_AboutUs():
    # click on logo of trank&technologies
    driver.find_element(By.XPATH, '//img[@alt="Trank Technologies"]').click()
    time.sleep(2)
    # perform about us validations
    driver.find_element(By.XPATH,"//a[text()='About us']").click()
    time.sleep(2)
    print("Done execution for About Us")
# test_AboutUs()

def test_blog():
    # click on logo of trank&technologies
    driver.find_element(By.XPATH, '//img[@alt="Trank Technologies"]').click()
    time.sleep(2)
    # perform blog validations
    driver.find_element(By.XPATH,"//a[text()='Blog']").click()
    time.sleep(2)
    print("Done execution for Blog")
# test_blog()

def test_ContactUs():
    # click on logo of trank&technologies
    driver.find_element(By.XPATH, '//img[@alt="Trank Technologies Logo"]').click()
    time.sleep(2)
    # perform contact us validations
    driver.find_element(By.XPATH,"//a[text()='Contact us']").click()
    time.sleep(2)
    print("Done execution for Contact Us")
# test_ContactUs()

def test_Portfolio():
    # click on logo of trank&technologies
    driver.find_element(By.XPATH, '//img[@alt="Trank Technologies"]').click()
    time.sleep(2)
    # perform portfolio validations
    driver.find_element(By.XPATH,"//a[text()='Portfolio']").click()
    time.sleep(2)
    print("Done execution for Portfolio")
# test_Portfolio()