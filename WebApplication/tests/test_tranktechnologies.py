import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#Open web url
driver=webdriver.Chrome()
Actions = ActionChains(driver)
# driver.implicitly_wait(10)
@pytest.mark.smoke
def test_navigate():
    driver.get("https://www.tranktechnologies.com/")
    driver.maximize_window()
    time.sleep(3)
@pytest.mark.smoke
def test_explore():
    driver.find_element(By.XPATH,"//div[@class='cm-home-slide slick-slide slick-current slick-active']//a[@class='cm-slider-btn cm-prim-bg'][normalize-space()='Explore More']").click()
    f1=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Name']")
    f1.send_keys("Dharmendra Dadlani")
    f2=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Mail']")
    f2.send_keys("tests@tests.com")
    f3=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Company']")
    f3.send_keys("Catylex")
    driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//select[@name='service']").click()
    f4=driver.find_element(By.XPATH,'//*[@id="get_in_touch_banner"]/div[4]/select/option[3]')
    f4.click()
    f5=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Phone']")
    f5.send_keys("9925450491")
    f6=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//textarea[@placeholder='Message']")
    f6.send_keys("This is tests message")
    f7=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@name='getintouch']")
    f7.click()
    print('successfully submitted form of home page')
    driver.back()
    driver.back()
    time.sleep(3)

@pytest.mark.smoke
# Home page redirected to links facebook, Instagram etc
def test_facebook():
    driver.find_element(By.XPATH,'//a[@href="https://www.facebook.com/TrankTechnologies"]').click()
    time.sleep(3)
@pytest.mark.smoke
def test_facebook_login():
    wd=driver.current_window_handle
    wd1=driver.window_handles
    # print(wd)
    # print(wd1)
    driver.switch_to.window(wd1[1])
    f1=driver.find_element(By.XPATH,'(//input[@name="email"])[2]')
    f1.send_keys('d.dadlani4@gmail.com')
    print("successfully redirected to facebook page")

    driver.close()
    driver.switch_to.window(wd1[0])  # prvious tab
    time.sleep(3)

# Vertical Tab
def test_vertical():
    wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    time.sleep(3)


# #Click on drop down value and perform action
def test_stockTrading():
    st=driver.find_element(By.XPATH,"//strong[normalize-space()='eCommerce Development']")
    Actions.move_to_element(st).perform()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Stock Trading']").click()
    print("successfully  Redirected to Stock Trading")
    time.sleep(3)

# Retail and eCommerce
#Click on drop down value and perform action
def test_retail_EC_WebDevelopment():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    st=driver.find_element(By.XPATH,"//strong[normalize-space()='Retail and Ecommerce']")
    Actions.move_to_element(st).perform()
    driver.find_element(By.XPATH,"//div[@id='retailEcommerce']//li[1]//a[1]").click()
    print("successfully  Redirected to eCommerce Website Development")
    time.sleep(3)

# Healthcare
#Click on drop down value and perform action
def test_Healthcare_DietNutrition():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    st=driver.find_element(By.XPATH,"//strong[normalize-space()='Healthcare']")
    Actions.move_to_element(st).perform()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Diet &')]").click()
    print("successfully  Redirected Healthcare-  Diet & Nutrition ")
    time.sleep(3)

# Fintech
#Click on drop down value and perform action
def test_Fintech_Crypto():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    st=driver.find_element(By.XPATH,"//li[@data-id='fintech']//a")
    Actions.move_to_element(st).perform()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Crypto']").click()
    print("successfully  Redirected to Fintech - Crypto")
    time.sleep(3)

# Custom Apps
#Click on drop down value and perform action
def test_CustomApp_HRM_Development():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    st=driver.find_element(By.XPATH,"//li[@data-id='customApp']")
    Actions.move_to_element(st).perform()
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='HRM Development']").click()
    print("successfully  Redirected to Custom Apps - HRM Development ")
    time.sleep(3)

# Technology Tab
#Create action class object and move to drop down

def test_Technology():
    wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[2]/a")
    Actions.move_to_element(wb).perform()

# #Click on drop down value and perform action
def test_EC_Dev_Magento_Development():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[2]/a")
    Actions.move_to_element(wb).perform()
    st=driver.find_element(By.XPATH,"//strong[normalize-space()='eCommerce Development']")
    Actions.move_to_element(st).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[normalize-space()='Magento Development']").click()
    print("successfully  Redirected to Technology and Magento Development")
    time.sleep(3)

def test_MB_APP_Dev_Flutter_MBApp():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[2]/a")
    Actions.move_to_element(wb).perform()

    st=driver.find_element(By.XPATH,"//strong[normalize-space()='Mobile App Development']")
    Actions.move_to_element(st).perform()
    print("Mobile App Development")
    time.sleep(1)
    driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]").click()
    time.sleep(3)
    print("successfully  Redirected to Flutter Mobile App")

# Artificial Intelligence
def test_AI_redirect():
    wb = driver.find_element(By.XPATH, "/html/body/header/div[2]/ul/li[2]/a")
    Actions.move_to_element(wb).perform()
    time.sleep(1)
    st=driver.find_element(By.XPATH,"//strong[normalize-space()='Artificial Intelligence']")
    st.click()
    time.sleep(1)
    print("successfully  Redirected to Artificial Intelligence")

# Open About Us Link
def test_aboutus():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='About us']").click()
    time.sleep(3)
    print("successfully  Redirected to About Us Page")

# Redirect to Blog
def test_Blog():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']").click()
    time.sleep(3)
    print("successfully  Redirected to Blog Page")

def test_Blog_AppDev():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/app-development/']").click()
    time.sleep(1)

def test_Blog_webDevelopment():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/web-development/']").click()
    time.sleep(1)

def test_Blog_SoftwareDevelopment():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/software-development/']").click()
    time.sleep(1)

def test_Blog_DigitalMarketing():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/digital-marketing/']").click()
    time.sleep(1)

def test_Blog_EmailMarketing():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/email-marketing/']").click()
    time.sleep(1)

def test_Blog_AI():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/artificial-intelligence/']").click()
    time.sleep(1)

def test_Blog_UI_UX_Design():
    driver.find_element(By.XPATH,"//a[@href='/blog/category/ui-ux-design/']").click()
    time.sleep(1)

print("successfully  completed Blog links")

# Redirect to Contact Us Page
def test_contactus():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Contact us']").click()
    time.sleep(1)
    print("successfully  Redirected to Contact Us Page")

def test_free_Consulation_Form():
    driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Name']").send_keys("Dharmendra Dadlani")
    driver.find_element(By.XPATH,"//input[@id='email_contact']").send_keys("tests@tests.com")
    driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Enter OTP']").click()
    driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Enter OTP']").send_keys('1234')
    driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Company']").send_keys("Google")
    wb=driver.find_element(By.XPATH,"//div[@class='cm-form-field']//select[@name='service']")
    Actions.move_to_element(wb).perform()
    driver.find_element(By.XPATH,'(//select[@name="service"])[2]').click()
    st=driver.find_element(By.XPATH,'//form[@id="contact_form"]/div[5]/select/option[2]')
    st.click()
    driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Phone']").send_keys('9097627467')
    driver.find_element(By.XPATH,"//form[@id='contact_form']//textarea[@placeholder='Message']").send_keys('This is tests message')
    time.sleep(1)
    driver.find_element(By.XPATH,'//input[@name="contact"]').click()
    print("successfully submitted values")
    time.sleep(1)
