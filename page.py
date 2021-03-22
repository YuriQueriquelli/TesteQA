from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Ecommerce:
    def __init__(self, webdriver):
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.button = (By.ID, 'login-button')
        self.webdriver = webdriver

    def login(self, user_name, password):
        self.webdriver.find_element(*self.user_name).send_keys(user_name)
        self.webdriver.find_element(*self.password).send_keys(password)
        self.webdriver.find_element(*self.button).click()



