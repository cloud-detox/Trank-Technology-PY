from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.tranktechnologies.com/")
    driver.maximize_window()
    time.sleep(2)
    a = ActionChains(driver)

    def Blog():
        blog = driver.find_element(By.XPATH, "//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']")
        a.move_to_element(blog).perform()
        blog.click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

    Blog()


chrome()


def firefox():
    driver1 = webdriver.Firefox()
    driver1.get("https://www.tranktechnologies.com/")
    driver1.maximize_window()
    time.sleep(2)
    a = ActionChains(driver1)

    def Blog():
        blog = driver1.find_element(By.XPATH, "//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']")
        a.move_to_element(blog).perform()
        blog.click()
        time.sleep(2)
        driver1.back()
        time.sleep(2)
        driver1.quit()

    Blog()
firefox()
def edge():
    driver2 = webdriver.Edge()
    driver2.get("https://www.tranktechnologies.com/")
    driver2.maximize_window()
    time.sleep(2)
    a = ActionChains(driver2)

    def log():
        log = driver2.find_element(By.XPATH, "//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']")
        a.move_to_element(log).perform()
        log.click()
        time.sleep(2)
        driver2.back()
        time.sleep(2)
        driver2.quit()

    log()


edge()
