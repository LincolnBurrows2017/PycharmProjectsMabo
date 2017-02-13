
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
#driver=webdriver.PhantomJS()
driver.set_window_size(20,40)
driver.set_window_size(1100,700)

driver.get('http://qzone.qq.com')

driver.switch_to_frame("login_frame")

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('1607108966')
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('Mabo18664212590')
driver.implicitly_wait(5)
#time.sleep(30)
driver.find_element_by_id('p').send_keys(Keys.RETURN)
#driver.find_element_by_id('login_button').click()
#driver.find_element_by_xpath('//*[@id="loginform"]/div[4]/a').click()
print(driver.get_cookies())

#driver.quit()
'''
from selenium import webdriver
import time

# 设置Phantonjs路径
driver = webdriver.PhantomJS()
driver.maximize_window()
login_url = 'https://h5.qzone.qq.com/mqzone/index'

driver.get('https://h5.qzone.qq.com/mqzone/index')
time.sleep(3)

# 点击“继续打开触屏版”
driver.execute_script("var q=document.getElementById('guideSkip');q.click()")
driver.implicitly_wait(3)

# 填写登录信息
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('1607108966')
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('Mabo18664212590')

# 登录
driver.execute_script("var login=document.getElementById('go');login.click();")
driver.implicitly_wait(3)

# 获取Cookie
cookie = driver.get_cookies()
'''