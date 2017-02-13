from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.maximize_window()

driver.get('http://mail.163.com/')
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('mabo_39353')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('mabo13077199848')
driver.find_element_by_id('un-login').click()
driver.find_element_by_id('dologin').click()
'''
driver.find_element_by_name('password').send_keys(Keys.ENTER)
这句话按道理应该是可以执行的，但是没有作用
'''
#driver.find_elements_by_class_name('forgetpwd j-redirect').click()
#driver.find_element_by_name('changepage').click()