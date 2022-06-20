# leadconnectRoaib
# leadconnectRoaib 

This is the complete source code for running the testscripts via Appium

Project Structure:
 - app (directory):
    - Contains the app to be tested
 - config (directory):
    - config.json - this file contains most the configs for the project such as desiredCapabilities for Appiun, Appium server Path, App Credentials.
    - locators.json - this file contains most of the UI Locators for navigation, so that is easy to maintain
 - helpers (directory):
    - This folder contains multiple python files that are used for creating builder, app login, navigating in app, checking for validations etc
 - testCases (directory): 
    - This folder contains all the test scripts
 - conftest.py (file):
    - Provides all the required data during script execution
 - requirements.txt:
    - Contains all the dependencies

Running Scripts: 

- Update the complete path of the app to be installed under config/config.json in capabilities 
 ![image](https://user-images.githubusercontent.com/26030123/174588960-c1856d17-9499-48d3-a055-df16541d58ab.png)

