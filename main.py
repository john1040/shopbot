from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
browser.get('https://fearofgod.com/')
# browser.implicitly_wait(1)

#login
login_path = '/html/body/div[1]/div[1]/header/div/div/nav[2]/ul/li[2]/a/span'
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, login_path))).click()
login = browser.find_element_by_xpath(login_path)
login.click()
#fill out info
email_path = '/html/body/div[1]/div[2]/main/div/section[1]/form/div[1]/input'
email = 'ilcf1u@gmail.com'
browser.find_element_by_xpath(email_path).send_keys(email)
pwd_path = '/html/body/div[1]/div[2]/main/div/section[1]/form/div[2]/input'
pwd = 'Gmguy2211@'
browser.find_element_by_xpath(pwd_path).send_keys(pwd)
signin_path = '/html/body/div[1]/div[2]/main/div/section[1]/form/div[3]/input'
signin = browser.find_element_by_xpath(signin_path)
signin.click()

browser.implicitly_wait(1)

# go to new releases
browser.get('https://fearofgod.com/collections/new-releases')
browser.implicitly_wait(2)

# click on the item we selected
item_path = '/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]'
item = browser.find_element_by_xpath(item_path)
item.click()

browser.implicitly_wait(1)

#add to cart
cart_path = '/html/body/div[1]/div[2]/main/form/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/button'
cart = browser.find_element_by_xpath(cart_path)
cart.click()

browser.implicitly_wait(3)

checkout_path = '/html/body/div[2]/div[1]/div[2]/div[2]/div/a[1]'
checkout = browser.find_element_by_xpath(checkout_path)
checkout.click()