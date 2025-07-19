import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()

def test_Navigateurl():
    driver.get("https://www.tranktechnologies.com/")
    driver.maximize_window()
    time.sleep(2)
# Navigateurl()

def test_Vertical():
    vertical = driver.find_element(By.XPATH, '(//a[@href="#"])[2]')
    actions = ActionChains(driver)
    actions.move_to_element(vertical).perform()
    time.sleep(2)
# Vertical()
def test_StockTrending():
    driver.find_element(By.XPATH,
                        "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Stock Trading']").click()
    time.sleep(2)
# StockTrending()
def test_Back():
    driver.back()
# Back()
time.sleep(2)
def test_Paper_Trading():
    test_Vertical()
    driver.find_element(By.XPATH,"//a[contains(text(),'Paper Trading')]").click()
    time.sleep(2)
    test_Back()
    time.sleep(2)
# Paper_Trading()
def test_CFD():
    test_Vertical()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CFD Trading']").click()
    time.sleep(2)
    test_Back()
    time.sleep(2)
# CFD()
def test_Development():
    test_Vertical()
    driver.find_element(By.XPATH,"//a[contains(text(),'Trading App')]").click()
    test_Back()
    time.sleep(2)
# Development()
def test_Algo_Trading():
    test_Vertical()
    driver.find_element(By.XPATH,"//a[contains(text(),'Algo Trading')]").click()
    test_Back()
    time.sleep(2)
# Algo_Trading()
def test_Custom_Trading():
    test_Vertical()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Custom')]").click()
    test_Back()
    time.sleep(2)
# Custom_Trading()
def test_Web_Trading():
    test_Vertical()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Web Portal Trading']").click()
    test_Back()
    time.sleep(2)
# Web_Trading()
def test_Retail_Ecommerce():
    test_Vertical()
    re=driver.find_element(By.XPATH,'//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/retailandecomm-mob.png"]')
    actions = ActionChains(driver)
    actions.move_to_element(re).perform()
    time.sleep(2)
# Retail_Ecommerce()
def test_Ecommerce_Website_Dev():
    test_Vertical()
    driver.find_element(By.XPATH,"//div[@id='retailEcommerce']//li[1]//a[1]").click()
    driver.back()
    time.sleep(2)
# Ecommerce_Website_Dev()
def test_Ecommerce_App_Dev():
    test_Vertical()
    test_Retail_Ecommerce()
    driver.find_element(By.XPATH,"//a[contains(text(),'eCommerce App Development')]").click()
    driver.back()
    time.sleep(2)
# Ecommerce_App_Dev()
def test_healthcare():
    test_Vertical()
    hc=driver.find_element(By.XPATH,'//li[@data-id="healthcare"]')
    actions=ActionChains(driver)
    actions.move_to_element(hc).perform()
    time.sleep(2)
# healthcare()
def test_diet_nutrition():
    test_Vertical()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Diet &')]").click()
    driver.back()
    time.sleep(2)
# diet_nutrition()
def test_health_tracking_app():
    test_Vertical()
    test_healthcare()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Health tracking App']").click()
    driver.back()
    time.sleep(2)
# health_tracking_app()

def test_fintech():
    test_Vertical()
    fn=driver.find_element(By.XPATH,'//li[@data-id="fintech"]')
    actions=ActionChains(driver)
    actions.move_to_element(fn).perform()
    time.sleep(2)
# fintech()
def test_pos_website_development():
    test_Vertical()
    test_fintech()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Pos Software')]").click()
    driver.back()
    time.sleep(2)
# pos_website_development()
def test_crypto():
    test_Vertical()
    test_fintech()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Crypto']").click()
    driver.back()
    time.sleep(2)
# crypto()