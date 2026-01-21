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
# def ver ():
#     vertical = driver.find_element(By.XPATH, '(//a[@href="#"])[2]')
#     Action.move_to_element(vertical).perform()
#     time.sleep(2)
#
# ver()
# def trading ():
#     trading = driver.find_element(By.XPATH, '//li[@data-id="trading"]') #Hover to VERTICAL>>Trading
#     Action.move_to_element(trading).perform()
#     time.sleep(1)
#
# trading()
#
# def Retailandcom():
#     retandcom = driver.find_element(By.XPATH, '//li[@data-id="retailEcommerce"]')
#     Action.move_to_element(retandcom).perform()
#     time.sleep(1)
#
# def Healthcare():
#     Health = driver.find_element(By.XPATH, '//li[@data-id="healthcare"]')
#     Action.move_to_element(Health).perform()
#     time.sleep(1)
#
# def Fintech():
#     Fintech = driver.find_element(By.XPATH, '//li[@data-id="fintech"]')
#     Action.move_to_element(Fintech).perform()
#     time.sleep(1)
#
# def Custoapp():
#     customapp = driver.find_element(By.XPATH, '//li[@data-id="customApp"]')
#     Action.move_to_element(customapp).perform()
#     time.sleep(1)
#
def Hover_Technology ():
    Technology = driver.find_element(By.XPATH, '(//a[@href="#"])[5]')
    Action.move_to_element(Technology).perform()
    time.sleep(2)
Hover_Technology()

def hover_ecomdev():
    ecom = driver.find_element(By.XPATH, '//li[@data-id="ecomm"]')
    Action.move_to_element(ecom).perform()
    time.sleep(2)
Hover_Technology()
hover_ecomdev()

#
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]').click() #Clicked on Vertical>>Trading>>Stock Trading
# time.sleep(1)
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]').click()
# time.sleep(1)   #Clicked on Paper Trading
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]').click()
# time.sleep(1) #Clicked on CFD Trading
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]').click()
# time.sleep(1) #Clicked on Trading App Development Company in Massachusetts
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]').click()
# time.sleep(2) #Clicked on Algo trading
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]').click()
# time.sleep(2) #Clicked on custom trading
# driver.back()
#
# ver()
# trading()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]').click()
# time.sleep(2) #Clicked on web portal trading
# driver.back()
#
# ver()
# Retailandcom()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]').click()
# time.sleep(2)   #Clicked on Retail&Comm >> Ecom website development
# driver.back()
#
# ver()
# Retailandcom()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]').click()
# time.sleep(2)   #Clicked on Retail&Comm >> Ecom app development
# driver.back()
#
# ver()
# Healthcare()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]').click()
# time.sleep(2)   #Clicked on Healtcare >> Diet & Nutrition
# driver.back()
#
# ver()
# Healthcare()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]').click()
# time.sleep(2)   #Clicked on Healtcare >> Health tracking app
# driver.back()
#
# ver()
# Fintech()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Fintech >> POS software dev
# driver.back()
#
# ver()
# Fintech()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]').click()
# time.sleep(2)   #Clicked on Fintech >> Crypto
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> Desktopapp Development
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> HRM Development
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> Travel
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> Dating app
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> CRM Development USA
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> CRM Development
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> ERP APP Development
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> E Learning
# driver.back()
#
# ver()
# Custoapp()
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]').click()
# time.sleep(2)   #Clicked on Customeapp >> Real State
# driver.back()
#
# driver.find_element(By.XPATH, '//a[text()="UI UX Design Cost: Budgeting & Key Factors"]').click()
# time.sleep(2) #Click on homepage > UI UX Design Cost: Budgeting & Key Factors(bottom of the page)
# driver.back()
#
# driver.find_element(By.XPATH, '//a[text()="10 Ways to Drive Organic Traffic to an eCommerce Website"]').click()
# time.sleep(2) #Click on homepage > 10 Ways to Drive Organic Traffic to an eCommerce Website(bottom of the page)
# driver.back()
#
# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/blog/"])[3]').click()
# time.sleep(2) #on main home page click button >> View all
# driver.back()
# time.sleep(2)

# driver.find_element(By.XPATH, '(//a[@href="https://www.tranktechnologies.com/web-development-company-in-india"])[1]').click() #Click on Explore more
# time.sleep(2)
# driver.find_element(By.XPATH, '(//input[@placeholder="Your Name"])[2]').send_keys('kapil') #Enter name
# time.sleep(2)
# driver.find_element(By.XPATH, '(//input[@type="email"])[2]').send_keys('kpldixit@gmail.com')
# time.sleep(2)
# driver.find_element(By.XPATH, '(//input[@name="company"])[2]').send_keys('genpact') #Enter Company
# time.sleep(2)
# downdown = driver.find_element(By.XPATH, '(//select[@name="service"])[2]')
# new = Select(downdown)
# new.select_by_visible_text("Custom Web Portal Development")
# driver.find_element(By.XPATH, '(//input[@placeholder="Your Phone"])[2]').send_keys('3474337')
# driver.find_element(By.XPATH, '(//textarea[@name="message"])[2]').send_keys('Hello DND')
# time.sleep(1)
# driver.find_element(By.XPATH, '(//input[@value="Submit"])[2]').click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
#
# driver.find_element(By.XPATH, '//a[text()="Web Development"]').click() #CLick on web dev at bottom of the main page and fill the form
# time.sleep(5)
# driver.find_element(By.XPATH, '(//input[@type="text"])[8]').send_keys('kapil')
# time.sleep(1)
# driver.find_element(By.XPATH, '(//input[@name="email"])[3]').send_keys('kpldixit34@gmail.com')
# driver.find_element(By.XPATH, '(//input[@name="company"])[3]').send_keys('TTT')
# time.sleep(2)
# bottom = driver.find_element(By.XPATH, '(//select[@name="service"])[3]')
# bot = Select(bottom)
# bot.select_by_visible_text("eCommerce App Development")
# time.sleep(2)
# driver.find_element(By.XPATH, '(//input[@name="phone"])[3]').send_keys('9999999')
# driver.find_element(By.XPATH, '(//textarea[@name="message"])[3]').send_keys("Message")
# driver.find_element(By.XPATH, '(//input[@type="submit"])[3]').click()
# time.sleep(2)
# driver.back()
#
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[1]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[2]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[3]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[4]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[5]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[6]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[7]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[8]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[9]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[10]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[11]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[12]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[13]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[14]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[15]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[16]').click()
# driver.find_element(By.XPATH, '(//div[@class="cm-faq-header cm-flex-type-1"])[17]').click()
# time.sleep(2)
# driver.back()
# #
# driver.find_element(By.XPATH, '(//a[@href="#"])[10]').click() #Get In Touch >> Get a Free Quote
# time.sleep(1)  #About US page starts here
# driver.find_element(By.XPATH, '//input[@name="name"]').send_keys('Kapil') #form will open >> Enter name
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@type="email"]').send_keys('kpldixit34@gmail.com') #Enter emaail
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@name="otp"]').send_keys('2443') #Enter OTP
# time.sleep(2)
# driver.find_element(By.XPATH, '//input[@name="company"]').send_keys('RWS') #Enter Company
# drop = driver.find_element(By.XPATH, '//select[@name="service"]')
# ser = Select(drop)
# ser.select_by_visible_text("Others") #Select Others from drop down menu
# time.sleep(2)
# driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys('34754346') #Enter phone number
# time.sleep(1)
# driver.find_element(By.XPATH, '//textarea[@name="message"]').send_keys('Hello World') #Enter Message
# time.sleep(1)
# driver.find_element(By.XPATH, '(//input[@type="submit"])[1]').click() #Click ok SUBMIT button
# time.sleep(2)
# driver.back()
# time.sleep(2)

# def footer_links():
#     L1 = '//a[@href="https://www.tranktechnologies.com/web-development-company-in-india"]'
#     L2 = '//a[@href="https://www.tranktechnologies.com/cms-website-development-company-in-india"]'
#     L3 = '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[7]'
#     L4 ='//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"]'
#     L5 ='//a[@href="https://www.tranktechnologies.com/ui-ux-design-company-in-india"]'
#     L6 ='//a[@href="https://www.tranktechnologies.com/mobile-app-design-company-in-india"]'
#     L7 ='//a[@href="https://www.tranktechnologies.com/responsive-web-design-company-in-india"]'
#     L8 ='//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company-in-india"]'
#     L9 ='//a[@href="https://www.tranktechnologies.com/app-development-company-in-india"]'
#     L10 ='//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company-in-india"]'
#     L11 ='//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company-in-india"]'
#     L12 ='//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company-in-india"]'
#     L13 ='//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"]'
#     L14 ='//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company-in-india"]'
#     L15 ='//a[@href="https://www.tranktechnologies.com/graphic-design-company-in-india"]'
#     L16 ='//a[@href="https://www.tranktechnologies.com/logo-design-company-in-india"]'
#     L17 ='//a[@href="https://www.tranktechnologies.com/banner-design-company-in-india"]'
#     L18 ='//a[@href="https://www.tranktechnologies.com/packaging-design-company-in-india"]'
#     L19 ='//a[@href="https://www.tranktechnologies.com/business-cards-design-company-in-india"]'
#
#     F1 = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L4,L15,L16,L17,L18,L19]
#
#     for f in F1:
#         driver.find_element(By.XPATH, f).click()
#         time.sleep(2)
#         driver.back()
# footer_links()