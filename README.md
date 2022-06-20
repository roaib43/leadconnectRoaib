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

Prerequisite
 - Python - version: 3.9.7
 - pip - version: 21.1.2
 - Make sure appium set is complete and it is working as expected 
 	Note: If the path for appium execution is different then please update the path in config.json file

**Step1 **: Clone the repo from gitHub (git clone https://github.com/roaib43/leadconnectRoaib.git)

**Step2** : in the project directory create a python3 virtual env 
	Command: python -m venv <path_to_virtualEvn>
	Eg: python -m venv leadConnectRoaibenv
 
 Python virual env folder named leadConnectRoaibenv should be created in the project directory 

**Step3**: Activate virtual env
	Command: 
		- on windows: we need to just need the activate.bat file via terminal
		
		<virtual_env>\Scripts\activate.bat
		Eg: leadConnectRoaibenv\Scripts\activate.bat (from project directory)

		- On Mac: 
		Command: <virtual_env>/bin/activate
  
**Step4**: Install requirements inside the virtual env 
	Command: from the Project directory (leadConnectRoaib)
		pip install -r requirements.txt
  
  ![pipinstall](https://user-images.githubusercontent.com/26030123/174589331-b595e2f3-1fa9-434c-b115-c737fd06f0ae.jpg)

**Step5**: After intallting requirements, navigate to test case folder to stat execution
	Commands: 
			- cd testCases
			- pytest --html=report.html  (report.html is the name of the html to be generated after execution)
   
   ![satrting execution](https://user-images.githubusercontent.com/26030123/174589403-a6634308-a1da-4077-9a2b-e4f74d1f0b49.jpg)
