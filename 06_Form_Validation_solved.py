
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
name = driver.find_element_by_xpath("//input[@id='name']")  
name.send_keys('vid')
driver.find_element_by_xpath("//input[@name='email']").send_keys('vidzierlien@qxf2.com')

phone = driver.find_element_by_id('phone')
phone.send_keys('9999999999')
 dropdown_element = driver.find_element_by_xpath("//button[@data-toggle='dropdown']")
dropdown_element.click()

driver.find_element_by_xpath("//a[text()='Male]").click()

time.sleep(1)
driver.close()   
