import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#Open web url
driver=webdriver.Chrome()
Actions = ActionChains(driver)
def test_navigate():
    driver.get("https://www.tranktechnologies.com/")
    driver.maximize_window()
    time.sleep(3)
test_navigate()

def test_explore():
    driver.find_element(By.XPATH,"//div[@class='cm-home-slide slick-slide slick-current slick-active']//a[@class='cm-slider-btn cm-prim-bg'][normalize-space()='Explore More']").click()
    time.sleep(3)
    f1=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Name']")
    f1.send_keys("Dharmendra Dadlani")
    f2=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Mail']")
    f2.send_keys("tests@tests.com")
    time.sleep(2)
    f3=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Company']")
    f3.send_keys("Catylex")
    time.sleep(2)
    driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//select[@name='service']").click()
    time.sleep(2)
    f4=driver.find_element(By.XPATH,'//*[@id="get_in_touch_banner"]/div[4]/select/option[3]')
    f4.click()
    time.sleep(2)
    f5=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@placeholder='Your Phone']")
    f5.send_keys("9925450491")
    time.sleep(2)
    f6=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//textarea[@placeholder='Message']")
    f6.send_keys("This is tests message")
    time.sleep(2)
    f7=driver.find_element(By.XPATH,"//form[@id='get_in_touch_banner']//input[@name='getintouch']")
    f7.click()
    time.sleep(3)
    print('successfully submitted form of home page')

test_explore()

# Home page redirected to links facebook, Instagram etc
def test_facebook():
    driver.find_element(By.XPATH,'//a[@href="https://www.facebook.com/TrankTechnologies"]').click()
    time.sleep(2)

test_navigate()
test_facebook()
wd=driver.current_window_handle
wd1=driver.window_handles
print(wd)
print(wd1)

driver.switch_to.window(wd1[1])
time.sleep(2)
f1=driver.find_element(By.XPATH,'(//input[@name="email"])[2]')
f1.send_keys('d.dadlani4@gmail.com')
time.sleep(5)
# driver.switch_to.window(wd1[0])
# driver.find_element(By.XPATH,"//img[@alt='LinkedIn']").click()
# driver.switch_to.window(wd1[1])
#
#
print("successfully redirected to facebook page")






# Vertical Tab
# #Create action class object and move to drop down
test_navigate()
def test_vertical():
    # Actions = ActionChains(driver)
    wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
    Actions.move_to_element(wb).perform()
    time.sleep(3)
test_vertical()
# #Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//strong[normalize-space()='eCommerce Development']")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Stock Trading']").click()
time.sleep(3)

print("successfully  Redirected to Stock Trading")

# Retail and eCommerce
# //strong[normalize-space()='Retail and Ecommerce']
test_vertical()
# # Actions = ActionChains(driver)
# # wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
# # Actions.move_to_element(wb).perform()
# # time.sleep(3)
#
#Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//strong[normalize-space()='Retail and Ecommerce']")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@id='retailEcommerce']//li[1]//a[1]").click()
time.sleep(3)

print("successfully  Redirected to eCommerce Website Development")

#
# Healthcare
# Actions = ActionChains(driver)
# wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
# Actions.move_to_element(wb).perform()
# time.sleep(3)
test_vertical()
#Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//strong[normalize-space()='Healthcare']")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Diet &')]").click()
time.sleep(3)

print("successfully  Redirected Healthcare-  Diet & Nutrition ")

# Fintech
# Actions = ActionChains(driver)
# wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
# Actions.move_to_element(wb).perform()
# time.sleep(3)
test_vertical()
#Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//li[@data-id='fintech']//a")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Crypto']").click()
time.sleep(3)

print("successfully  Redirected to Fintech - Crypto")


# Custom Apps
#
# Actions = ActionChains(driver)
# wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[1]/a")
# Actions.move_to_element(wb).perform()
# time.sleep(3)
test_vertical()
#Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//li[@data-id='customApp']")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='HRM Development']").click()
time.sleep(3)
print("successfully  Redirected to Custom Apps - HRM Development ")



# Technology Tab
#Create action class object and move to drop down
# Actions = ActionChains(driver)
# wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[2]/a")
# Actions.move_to_element(wb).perform()
# time.sleep(3)
# //li[@class='drop_down show_dropdown']//a[@href='#'][normalize-space()='Technologies']

# /html/body/header/div[2]/ul/li[2]/a
def test_Tech():
    wb=driver.find_element(By.XPATH,"/html/body/header/div[2]/ul/li[2]/a")
    Actions.move_to_element(wb).perform()
    time.sleep(3)

test_Tech()
# #Click on drop down value and perform action
st=driver.find_element(By.XPATH,"//strong[normalize-space()='eCommerce Development']")
Actions.move_to_element(st).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='Magento Development']").click()
time.sleep(3)

print("successfully  Redirected to Technology and Magento Development")

test_Tech()
st=driver.find_element(By.XPATH,"//strong[normalize-space()='Mobile App Development']")
Actions.move_to_element(st).perform()
time.sleep(3)

print("Mobile App Development")

driver.find_element(By.XPATH,"//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]").click()
time.sleep(3)

print("successfully  Redirected to Flutter Mobile App")
# Artificial Intelligence
test_Tech()
st=driver.find_element(By.XPATH,"//strong[normalize-space()='Artificial Intelligence']")
st.click()
time.sleep(3)
print("successfully  Redirected to Artificial Intelligence")

# Open About Us Link
def test_aboutus():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='About us']").click()
    time.sleep(3)
    print("successfully  Redirected to About Us Page")

test_aboutus()

# Redirect to Blog

def test_Blog():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']").click()
    time.sleep(3)
    print("successfully  Redirected to Blog Page")

test_Blog()
driver.find_element(By.XPATH,"//a[@href='/blog/category/app-development/']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='/blog/category/web-development/']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='/blog/category/software-development/']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='/blog/category/digital-marketing/']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='/blog/category/email-marketing/']").click()
time.sleep(3)


driver.find_element(By.XPATH,"//a[@href='/blog/category/artificial-intelligence/']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@href='/blog/category/ui-ux-design/']").click()
time.sleep(3)

print("successfully  completed Blog links")

# Redirect to Contact Us Page
def test_contactus():
    driver.find_element(By.XPATH,"//ul[@class='cm-flex-type-2']//a[normalize-space()='Contact us']").click()
    time.sleep(3)
    print("successfully  Redirected to Contact Us Page")

test_contactus()
driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Name']").send_keys("Dharmendra Dadlani")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='email_contact']").send_keys("tests@tests.com")
time.sleep(3)
driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Enter OTP']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Enter OTP']").send_keys('1234')
time.sleep(3)
driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Company']").send_keys("Google")
time.sleep(3)

wb=driver.find_element(By.XPATH,"//div[@class='cm-form-field']//select[@name='service']")
Actions.move_to_element(wb).perform()
time.sleep(3)

# drop down

driver.find_element(By.XPATH,'(//select[@name="service"])[2]').click()
time.sleep(2)

#Click on drop down value and perform action
st=driver.find_element(By.XPATH,'//form[@id="contact_form"]/div[5]/select/option[2]')
st.click()
time.sleep(5)


(driver.find_element(By.XPATH,"//form[@id='contact_form']//input[@placeholder='Your Phone']").send_keys('9097627467'))
driver.find_element(By.XPATH,"//form[@id='contact_form']//textarea[@placeholder='Message']").send_keys('This is tests message')
time.sleep(2)

driver.find_element(By.XPATH,'//input[@name="contact"]').click()
time.sleep(3)

print("successfully submitted values")

test_navigate()


