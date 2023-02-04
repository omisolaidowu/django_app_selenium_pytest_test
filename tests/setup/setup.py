from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv('.env')


LT_GRID_USERNAME = os.getenv("LT_GRID_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")


desired_caps = {
		'LT:Options' : {
			"user" : LT_GRID_USERNAME,
			"accessKey" : LT_ACCESS_KEY,
			"build" : "Django Functional Testing",
			"name" : "Django Test",
			"platformName" : "Windows 11",
            "tunnel": True

		},
		"browserName" : "Chrome",
		"browserVersion" : "104.0",
        
	}


class Settings: 
       
    def __init__(self) -> None:
        self.grid_url = "https://{}:{}@hub.lambdatest.com/wd/hub".format(
            LT_GRID_USERNAME, LT_ACCESS_KEY
            )
        self.desired_caps = desired_caps
        self.driver = webdriver.Remote(command_executor=self.grid_url, desired_capabilities= self.desired_caps)
        
    def setup(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        try:
            if (self.driver != None):
                print("Cleaning the test environment")
                self.driver.quit()
        except  AssertionError as e:
            print(e)
            self.driver.quit()
