from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

sleep(1)

driver.find_element(By.XPATH, "//a[@class='nav_a' and @href='/gp/help/customer/display.html?ie=UTF8&nodeId=508510&ref_=footer_gw_m_b_he']").click()

sleep(1)

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")

search.clear()

search.send_keys('cancel order')

sleep(1)

# click search
driver.find_element(By.CLASS_NAME, 'a-button-input').click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']").text

sleep(1)
