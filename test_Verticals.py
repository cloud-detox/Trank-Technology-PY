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

def test_Verticals():

    def test_Trading():
        v=driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
        a.move_to_element(v).perform()
        trading=driver.find_element(By.XPATH,"//strong[normalize-space()='Trading']")
        a.move_to_element(trading).perform()

    def test_Stock_Trading():
        test_Trading()
        driver.find_element(By.XPATH,'(//a[@data-mm-id="1"])[1]').click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    # test_Stock_Trading()

    def test_Algo_Trading():
        test_Trading()
        driver.find_element(By.XPATH, "//a[contains(text(),'Algo Trading')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Paper_Trading():
        test_Trading()
        driver.find_element(By.XPATH, "//a[contains(text(),'Paper Trading')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Custom_Trading():
        test_Trading()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Custom')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_CFD_Trading():
        test_Trading()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CFD Trading']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Webportal_Trading():
        test_Trading()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Web Portal Trading']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Trading_App():
        test_Trading()
        driver.find_element(By.XPATH, "//a[contains(text(),'Trading App')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    # test_Algo_Trading()
    # test_Paper_Trading()
    # test_Custom_Trading()
    # test_CFD_Trading()
    # test_Webportal_Trading()
    # test_Trading_App()

    def test_Retail_Ecommerce():
        v = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
        a.move_to_element(v).perform()
        retail=driver.find_element(By.XPATH,"//strong[normalize-space()='Retail and Ecommerce']")
        a.move_to_element(retail).perform()

    def test_Ecommerce_Website():
        test_Retail_Ecommerce()
        driver.find_element(By.XPATH, "//div[@id='retailEcommerce']//li[1]//a[1]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Ecommerce_App():
        test_Retail_Ecommerce()
        driver.find_element(By.XPATH,"//a[contains(text(),'eCommerce App Development')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    # test_Ecommerce_Website()
    # test_Ecommerce_App()

    def test_Healthcare():
        v = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
        a.move_to_element(v).perform()
        health = driver.find_element(By.XPATH, "//strong[normalize-space()='Healthcare']")
        a.move_to_element(health).perform()

    def test_Diet_Nutrition():
        test_Healthcare()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Diet &')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Health_Tracking():
        test_Healthcare()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Health tracking App']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    # test_Diet_Nutrition()
    # test_Health_Tracking()

    def test_Fintech():
        v = driver.find_element(By.XPATH, '(//i[@class="fa fa-chevron-down"])[2]')
        a.move_to_element(v).perform()
        fin = driver.find_element(By.XPATH, "//strong[normalize-space()='Fintech']")
        a.move_to_element(fin).perform()

    def test_Pos_Software():
        test_Fintech()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Pos Software')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Crypto():
        test_Fintech()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Crypto']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
    # test_Pos_Software()
    # test_Crypto()

    def test_Custom_App():
        v=driver.find_element(By.XPATH,'(//i[@class="fa fa-chevron-down"])[2]')
        a.move_to_element(v).perform()
        Custom=driver.find_element(By.XPATH,"//strong[normalize-space()='Custom App']")
        a.move_to_element(Custom).perform()

    def test_Desktop_App():
        test_Custom_App()
        driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Desktop App')]").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)


    def test_CRM():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='CRM Development']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_HRM():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='HRM Development']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_ERP():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='ERP App Development']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Travel():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Travel']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_E_Learning():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='E-Learning']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Dating_App():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Dating App Development']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_Real_Estate():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Real Estate']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    def test_CRM_USA():
        test_Custom_App()
        driver.find_element(By.XPATH, "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='CRM Development USA']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

#     test_Desktop_App()
#     test_CRM()
#     test_HRM()
#     test_ERP()
#     test_Travel()
#     test_E_Learning()
#     test_Dating_App()
#     test_Real_Estate()
#     test_CRM_USA()
# test_Verticals()



