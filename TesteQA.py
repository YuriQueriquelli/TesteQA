from selenium import webdriver
from time import sleep
from selenium.webdriver import Chrome
from page import Ecommerce
from products import Inventory
from checkout import CheckOut

driver = webdriver.Chrome()

link = 'https://www.saucedemo.com/'
driver.get(link)

login = Ecommerce(driver)
produtos = Inventory(driver)
checkout = CheckOut(driver)

#logar
login.login("standard_user", "secret_sauce")

#filtrar
produtos.filtrar('Price (low to high)')

#selecionar produtos
produtos.procurar('Sauce Labs Onesie')
produtos.procurar('Test.allTheThings() T-Shirt (Red)')

#fechar pedido
produtos.fechar_pedido()
checkout.preencher('Teste', 'QA', '12345678')
