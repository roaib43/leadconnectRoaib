from helpers.helper import *
from helpers.contactNavigator import *
from helpers.contactScreenChecks import *
import pytest

@pytest.mark.usefixtures("ui_locators")
class TestContact:
    driver = None

    @classmethod
    def setup(self):
        self.driver = buildDriver()
        appLogin(self.driver)
        # Creating Navigation and ScreenCheck Objects
        self.contactNavigation = ContactNavigator()
        self.contactScreenCheck = ContactScreenChecks()


    @classmethod
    def teardown(self):
        self.driver.quit()

    def test_createcontact(self, ui_locators):
        '''
        this script will check the complete happy path for contact creation flow, Script Flow as follow
        Login to app > Go to Contacts > Create Contact > Fill in required Fields + lname + phone > Save Contact
        > Check if contact Saved
        '''

        # Performing App navigation and Asserting ScreenChecks
        self.contactNavigation.navigateToContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)
        self.contactNavigation.clickCreateContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnCreateContact(driver=self.driver)

        #fill is contact form
        self.contactNavigation.fillContactFormFields(driver=self.driver, fname='roaibtesting', lname='test', phone='1234567890', locators=ui_locators)
        self.contactNavigation.savecontactform(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)

        #Check if contact saved and open that contact
        contactelementID = self.contactScreenCheck.expectGivenContactInList(driver=self.driver, fname='roaibtesting', lname='test', phone='+911234567890')
        self.contactNavigation.clickGivenContactInList(driver=self.driver, contactelement=contactelementID)
        self.contactScreenCheck.expectGivenContactPageOpened(driver=self.driver, fname='roaibtesting', lname='test')

        #Check DND status
        self.contactScreenCheck.expectDNDEnabled(driver=self.driver, dndenabled='false')


    def test_createcontactwithoutrequiredparameter(self, ui_locators):
        '''
        this script will check if the form thorws error when the required fields are not filled, Script Flow as follow
        Login to app > Go to Contacts > Create Contact > Fill in lastname (ignore require filed) > Save Contact
        > Check if error is thrown
        '''

        # Performing App navigation and Asserting ScreenChecks
        self.contactNavigation.navigateToContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)
        self.contactNavigation.clickCreateContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnCreateContact(driver=self.driver)

        # fill contact form with only last name and save
        self.contactNavigation.fillContactFormFields(driver=self.driver, lname='roaibtesting', locators=ui_locators)
        self.contactNavigation.savecontactform(driver=self.driver, locators=ui_locators)

        #Contact form should not be saved and check for error message
        self.contactScreenCheck.expectRequiredFieldErrorMessage(driver=self.driver)

    def test_createcontactwithoutNumber(self, ui_locators):
        '''
        this script will check contact creation flow without phone number,
        Script Flow as follow
        Login to app > Go to Contacts > Create Contact > Fill in required Fields + last name > Save Contact
        > Check if contact Saved
        '''

        # Performing App navigation and Asserting ScreenChecks
        self.contactNavigation.navigateToContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)
        self.contactNavigation.clickCreateContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnCreateContact(driver=self.driver)

        # fill contact form with only last name and save
        self.contactNavigation.fillContactFormFields(driver=self.driver, fname='roaibcontact', locators=ui_locators)
        self.contactNavigation.savecontactform(driver=self.driver, locators=ui_locators)

        # Check if contact saved and open that contact
        contactelementID = self.contactScreenCheck.expectGivenContactInList(driver=self.driver,  fname='roaibcontact')
        self.contactNavigation.clickGivenContactInList(driver=self.driver, contactelement=contactelementID)
        self.contactScreenCheck.expectGivenContactPageOpened(driver=self.driver,  fname='roaibcontact')

        # Check DND status
        self.contactScreenCheck.checkContactinfoPhone(driver=self.driver, fname='roaibcontact', phone='Nophonenumber')

    def test_checkcancelbutton(self, ui_locators):
        '''
        this script will check if the cancel button works as expected from ContactPage,
        Script Flow as follow
        Login to app > Go to Contacts > Create Contact > Click Cancel > Check if contacts page is displayed
        '''

        # Performing App navigation and Asserting ScreenChecks
        self.contactNavigation.navigateToContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)
        self.contactNavigation.clickCreateContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnCreateContact(driver=self.driver)

        #Click cancel on contactform
        self.contactNavigation.cancelcontactform(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)

    def test_createcontactwithDND(self, ui_locators):
        '''
        this script will check if the dnd option works on contact page and checks if dnd is enabled for the contact,
        Script Flow as follow
        Login to app > Go to Contacts > Create Contact > Fill in the required filed and enabled dnd > Save Contact
        > Open contact > check Dnd status
        '''

        # Performing App navigation and Asserting ScreenChecks
        self.contactNavigation.navigateToContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnContactsPage(driver=self.driver)
        self.contactNavigation.clickCreateContact(driver=self.driver, locators=ui_locators)
        self.contactScreenCheck.expectToBeOnCreateContact(driver=self.driver)

        # fill contact form with dnd enabled
        self.contactNavigation.fillContactFormFields(driver=self.driver, fname='roaibtesting', dnd=True, locators=ui_locators)
        self.contactNavigation.savecontactform(driver=self.driver, locators=ui_locators)

        # Check if contact saved and open that contact
        contactelementID = self.contactScreenCheck.expectGivenContactInList(driver=self.driver,  fname='roaibtesting')
        self.contactNavigation.clickGivenContactInList(driver=self.driver, contactelement=contactelementID)
        self.contactScreenCheck.expectGivenContactPageOpened(driver=self.driver,  fname='roaibtesting')

        # Check DND status
        self.contactScreenCheck.expectDNDEnabled(driver=self.driver, dndenabled='true')
