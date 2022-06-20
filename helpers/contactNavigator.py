from appium.webdriver.common.appiumby import AppiumBy

from time import sleep
class ContactNavigator:

    def __init__(self):
        self.driver = None

    def navigateToContact(self, driver, locators):
        self.driver = driver
        # driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tab 5 of 5").click()
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locators['contact_tab']).click()

    def clickCreateContact(self, driver, locators):
        self.driver = driver
        # driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button").click()
        driver.find_element(by=AppiumBy.XPATH,value=locators['create_contact']).click()

    def fillContactFormFields(self, driver, locators, fname=None, lname=None, phone=None, email=None, tags=None, dob=None,
                              contactsource=None, contenttype=None, dnd=False):
        self.driver = driver
        textWidgets = driver.find_elements(by=AppiumBy.CLASS_NAME, value=locators['contact_textWidgets'])
        if fname != None:
            for element in textWidgets:
                if element.get_attribute('text').__contains__('First name'):
                    element.click()
                    element.set_text(fname)
                    # driver.hide_keyboard()
                    break
        if lname != None:
            for element in textWidgets:
                if element.get_attribute('text') == 'Last name':
                    element.click()
                    element.set_text(lname)
                    # driver.hide_keyboard()
                    break
        if phone != None:
            for element in textWidgets:
                if element.get_attribute('text') == 'Phone':
                    element.click()
                    element.set_text(phone)
                    # driver.hide_keyboard()
                    break
        if dnd:
            if driver.is_keyboard_shown():
                driver.hide_keyboard()
            dndButton = driver.find_element(by=AppiumBy.CLASS_NAME, value=locators['dnd_button'])
            dndButton.click()

    def savecontactform(self,driver,locators):
        self.driver = driver
        # driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        driver.find_element(by=AppiumBy.XPATH,value=locators['save_contact']).click()

    def cancelcontactform(self, driver,locators):
        self.driver = driver
        # driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()
        driver.find_element(by=AppiumBy.XPATH,value=locators['cancel_contact']).click()

    def clickGivenContactInList(self, driver, contactelement):
        self.driver = driver
        contact = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=contactelement)
        contact.click()

    def clickOnBack(self, driver, locators):
        self.driver = driver
        backButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=locators['contact_back_button'])
        backButton.click()
