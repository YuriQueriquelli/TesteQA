from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CheckOut:
    def __init__(self, webdriver):
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.submit = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input')
        self.final = (By.LINK_TEXT, 'FINISH')
        self.webdriver = webdriver

    def preencher(self, first_name, last_name, postal_code):
        self.webdriver.find_element(*self.first_name).send_keys(first_name)
        self.webdriver.find_element(*self.last_name).send_keys(last_name)
        self.webdriver.find_element(*self.postal_code).send_keys(postal_code)
        self.webdriver.find_element(*self.submit).click()
        self.webdriver.find_element(*self.final).click()


        
