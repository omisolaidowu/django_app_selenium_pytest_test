from selenium.webdriver.common.by import By
from dataclasses import dataclass


class formLocator:
    username = "username-fill" #class
    password = "password-fill" #class
    loginSubmit = "Login" #name
    published = "id_published" #id
    title = "my-title" #class
    content = "content-field" #class
    description = "-content-description" #class
    blogSubmit = "submit" #IDs


locate = formLocator()



@dataclass
class Webactions():
    driver: object

    def getWeb(self, URL):
        self.driver.get(URL)
        
    def getTitle(self):
        return self.driver.title

    def current_url(self):
        return self.driver.current_url

    def fill_username(self, username):
        self.driver.find_element(By.CLASS_NAME, locate.username).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(By.CLASS_NAME, locate.password).send_keys(password)
    
    def submit_login(self):
        self.driver.find_element(By.NAME, locate.loginSubmit).click()
    
    def published_yes(self):
        self.driver.find_element(By.ID, locate.published).click()

    def enter_title(self, title):
        self.driver.find_element(By.CLASS_NAME, locate.title).send_keys(title)

    def write_content(self, content):
        self.driver.find_element(By.CLASS_NAME, locate.content).send_keys(content)

    def enter_description(self, description):
        self.driver.find_element(By.CLASS_NAME, locate.description).send_keys(description)

    def submit_post(self):
        self.driver.find_element(By.ID, locate.blogSubmit).click()