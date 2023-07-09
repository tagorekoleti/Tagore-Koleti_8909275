# Importing required libraries
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(4)

login_un = driver.find_element("id", "username")
login_un.send_keys("student")
time.sleep(2)

login_pwd = driver.find_element("id", "password")
login_pwd.send_keys("Password123")
time.sleep(2)

submit_button = driver.find_element("xpath", "/html/body/div/div/section/section/div[1]/button")
submit_button.click()
time.sleep(3)

loggingOut = driver.find_element("xpath", "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
loggingOut.click()
time.sleep(3)

# Closing the webdriver
driver.close()
