from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactScreenChecks:

    def expectToBeOnContactsPage(self, driver):
        self.driver = driver
        WebDriverWait(driver, 80).until(EC.presence_of_element_located(
            (By.XPATH, "//android.view.View[@content-desc=\"All contacts\"]")))
        contactScreen = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="All contacts")
        if contactScreen.get_attribute('content-desc') != 'All contacts':
            assert False

    def expectToBeOnCreateContact(self, driver):
        self.driver = driver
        WebDriverWait(driver, 40).until(EC.presence_of_element_located(
            (By.XPATH, "//android.view.View[@content-desc=\"Add contact\"]")))
        contactScreen = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add contact")
        if contactScreen.get_attribute('content-desc') != 'Add contact':
            assert False

    def expectGivenContactInList(self, driver, fname, lname=None, phone=None, role='Lead'):
        self.driver = driver
        firstChar = fname[0].upper()
        contact_accessibilityid = firstChar + '\n' + fname.capitalize() + '\n' + 'No contact details' + '\n' + role
        if lname is not None:
            contact_accessibilityid = firstChar + '\n' + fname.capitalize() + ' ' + lname.capitalize() + '\n' + 'No contact details' + '\n' + role
        if phone is not None:
            contact_accessibilityid = firstChar + '\n' + fname.capitalize() + '\n' + phone + '\n' + role
        if phone and lname is not None:
            contact_accessibilityid = firstChar + '\n' + fname.capitalize() + ' ' + lname.capitalize() + '\n' + phone + '\n' + role
        WebDriverWait(driver, 380).until(EC.presence_of_element_located(
            (By.XPATH, '//android.view.View[@content-desc=\"' + contact_accessibilityid + '\"]')))
        contactsList = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=contact_accessibilityid)
        if contactsList.get_attribute('content-desc') == contact_accessibilityid:
            return contact_accessibilityid
        else:
            assert False

    def expectGivenContactPageOpened(self, driver, fname, lname=None):
        self.driver = driver
        if lname != None:
            contact_accessibilityid = fname.capitalize() + ' ' + lname.capitalize()
        else:
            contact_accessibilityid = fname.capitalize()
        WebDriverWait(driver, 40).until(EC.presence_of_element_located(
            (By.XPATH, '//android.view.View[@content-desc="' + contact_accessibilityid + '"]')))
        contactInfo = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=contact_accessibilityid)
        if contactInfo.get_attribute('content-desc') != contact_accessibilityid:
            assert False

    def expectRequiredFieldErrorMessage(self, driver):
        self.driver = driver
        WebDriverWait(driver, 40).until(EC.presence_of_element_located(
            (By.XPATH, '//android.view.View[@content-desc="First name is required."]')))
        errorMessage = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='First name is required.')
        if errorMessage.get_attribute('content-desc') != 'First name is required.' and errorMessage.get_attribute('displayed') is not True:
            assert False

    def expectDNDEnabled(self, driver, dndenabled):
        self.driver = driver
        dndState = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Switch")
        if dndState.get_attribute('checked') != dndenabled:
            assert False

    def checkContactinfoPhone(self, driver, fname, phone):
        self.driver = driver
        fname = fname.capitalize()
        contactdata = []
        contactinfo = driver.find_elements(by=AppiumBy.XPATH, value='//*[contains(@content-desc,\'' + fname + '\')]')
        for ele in contactinfo:
            if ele.get_attribute('content-desc').__contains__('DND'):
                contactdata = ele.get_attribute('content-desc').replace(" ", "").replace("\n", "")
                if not contactdata.__contains__(phone):
                    assert False
