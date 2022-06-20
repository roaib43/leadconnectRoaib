from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
cwd = os.getcwd()
print(cwd, " >>")
with open('../config/config.json',  'r') as json_data_file:
    config_data_json = json_data_file.read()

config_data = json.loads(config_data_json)
def buildDriver():
    print(config_data)
    desired_caps = config_data['capabilities']
    driver = webdriver.Remote(config_data['appium_path'], desired_caps)
    return driver

def appLogin(driver):
    loginScreen = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    emailElement = ''
    passwordElement = ''
    for element in loginScreen:
        if element.get_attribute('text') == 'Email':
            emailElement = element
        elif element.get_attribute('text') == 'Password':
            passwordElement = element

    if emailElement == '' or passwordElement == '':
        assert False
    else:
        emailElement.click()
        emailElement.set_text(config_data['credentials']['username'])
        passwordElement.click()
        passwordElement.set_text(config_data['credentials']['password'])
        loginButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sign In")
        loginButton.click()
        WebDriverWait(driver, 40).until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.Button[@content-desc=\"Open navigation menu\"]")))
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation menu").is_displayed()
        WebDriverWait(driver, 50).until(EC.presence_of_element_located(
            (By.XPATH, '//android.view.View[@content-desc="Tab 1 of 5"]')))

def navigateToHome(driver):
    home = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 1 of 5")
    home.click()

def expectToBeOnHome(driver):
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Recent Activities").is_displayed()
