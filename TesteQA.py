from selenium import webdriver

driver = webdriver.Chrome()

link = 'https://www.saucedemo.com/'
driver.get(link)

#login page
inputUser = driver.find_element_by_id('user-name')
inputUser.send_keys('standard_user')

inputPassword = driver.find_element_by_id('password')
inputPassword.send_keys('secret_sauce')

buttonLogin = driver.find_element_by_id('login-button')
buttonLogin.click()

#low to high
options = driver.find_element_by_xpath('//*[@id="inventory_filter_container"]/select')
options.send_keys('Price (low to high)')

#Itens page
first_item = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/div[1]/div[3]/button')
first_item.click()

second_item = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/div[4]/div[3]/button')
second_item.click()

shoppingCart = driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a')
shoppingCart.click()

#Shopping cart
checkoutButton = driver.find_element_by_xpath('//*[@id="cart_contents_container"]/div/div[2]/a[2]')
checkoutButton.click()

#Checkout page
firstName = driver.find_element_by_xpath('//*[@id="first-name"]')
firstName.send_keys('TESTE')

lastName = driver.find_element_by_xpath('//*[@id="last-name"]')
lastName.send_keys('1231231')

postalCode = driver.find_element_by_xpath('//*[@id="postal-code"]')
postalCode.send_keys('22222-123')

buttonContinue = driver.find_element_by_xpath('//*[@id="checkout_info_container"]/div/form/div[2]/input')
buttonContinue.click()

#last page
finish_bt = driver.find_element_by_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')
finish_bt.click()