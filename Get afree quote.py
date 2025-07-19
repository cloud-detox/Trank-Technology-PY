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

driver.find_element(By.XPATH,"//a[@class='scroll']").click()
form=driver.find_element(By.XPATH,'//form[@id="get_in_touch"]')
a.move_to_element(form).perform()
driver.find_element(By.XPATH,"//div[@class='cm-form-field']//input[@placeholder='Your Name']").send_keys("Sonu")
driver.find_element(By.XPATH,"//input[@id='email_career']").send_keys("test@gmail.com")
driver.find_element(By.XPATH,"//button[@id='send_career_otp']").click()
alert=driver.switch_to.alert
alert.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Enter OTP']").send_keys("789456")
driver.find_element(By.XPATH,"//div[@class='cm-form-field']//input[@placeholder='Your Company']").send_keys("TIC")
driver.find_element(By.XPATH,'//form[@id="get_in_touch"]/div[5]/select/option[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='cm-form-field']//input[@placeholder='Your Phone']").send_keys("9419290589")
driver.find_element(By.XPATH,"//div[@class='cm-form-field']//textarea[@placeholder='Message']").send_keys("Automating testing practice")
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="recaptcha-checkbox-border"]').click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='cm-form-submit cm-prim-bg cm-white-col cm-uppercase']").click()
time.sleep(3)
