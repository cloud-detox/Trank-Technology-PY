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
driver.get("https://uncodemy.com/")

driver.implicitly_wait(10)
Action = ActionChains(driver)
cate = driver.find_element(By.XPATH, '//span[@id="categoriesBtn"]') #Hover to categorie
Action.move_to_element(cate).perform()
fsd = driver.find_element(By.XPATH, '//menuitem[@label="settings"]') #Hover to fullstake dev
Action.move_to_element(fsd).perform()
driver.find_element(By.XPATH, '(//a[@href="/course/full-stack-with-nodejs-training-course-in-noida"])[1]').click() #CLick  to fullstake node.js
driver.back()
time.sleep(2)



