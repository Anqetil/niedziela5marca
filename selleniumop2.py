from selenium import webdriver
from selleniumopp1 import LoginPage
import time
from selenium1 import make_screenshot

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
time.sleep(0.5)
page.enter_username('standard_user')
time.sleep(0.5)
page.enter_password('secret_sauce')
time.sleep(0.5)
page.click_login()
time.sleep(0.5)

assert driver.current_url == 'https://www.saucedemo.com/inventory.html'


make_screenshot(driver)
page.the_snapshot()
driver.quit()