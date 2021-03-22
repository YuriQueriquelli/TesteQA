from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Inventory:
    def __init__(self, webdriver):
        #self.produto = (By.LINK_TEXT)
        self.cart = (By.ID,'shopping_cart_container')
        self.tipo = (By.CLASS_NAME, 'product_sort_container')
        self.checkout = (By.LINK_TEXT, 'CHECKOUT')
        self.webdriver = webdriver
    
    def filtrar(self, tipo):
        self.webdriver.find_element(*self.tipo).send_keys(tipo)

    def procurar(self, nome_produto):
        #self.webdriver.find_element(*self.produto, nome_produto).click()
        self.webdriver.find_element_by_link_text(nome_produto).click()
        self.webdriver.find_element_by_xpath('//*[@id="inventory_item_container"]/div/div/div/button').click()
        self.webdriver.back()

    def fechar_pedido(self):
        #self.webdriver.find_element_by_id('shopping_cart_container').click()
        self.webdriver.find_element(*self.cart).click()
        self.webdriver.find_element(*self.checkout).click()