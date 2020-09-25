from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

timeout = 10
captcha_timeout = 1000
driver = webdriver.Chrome()
driver.get("https://www.tiketa.lt/EN/search")

# Registered method
# driver.find_element_by_xpath("//*[text()='Login']").click()
# driver.find_element_by_id("txtLoginName").send_keys("email")
# driver.find_element_by_id("txtLoginPsw").send_keys("password")
# driver.find_element_by_id("btnLogin").click()
# driver.refresh()

# Main
driver.find_element_by_xpath("//input[@placeholder='Search ...']").send_keys("Forum", Keys.TAB)
driver.find_element_by_id("cityCaption").click()
driver.find_element_by_xpath("//a[text()='Kaunas']").click()
driver.find_element_by_xpath("//input[@name='sf_DateFrom']").send_keys("2020-09-01")
driver.find_element_by_xpath("//input[@name='sf_DateTo']").send_keys("2021-12-31", Keys.TAB)
WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Search']"))).click()

# Workaround to avoid blank href click
element = WebDriverWait(driver,1000).until(lambda d: d.find_element_by_xpath("//*[text()='Intelligent Forum']"))
action1 = ActionChains(driver).move_to_element(element).click()
action1.perform()

WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'EN/Purchase')]"))).click()

# Comment line below when using a registered account
WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, "btnNoLogin"))).click()

# Google captcha might appear here

# Select price of 35EUR since 40EUR is unavailable
price = WebDriverWait(driver,captcha_timeout).until(lambda d: d.find_element_by_xpath("//*[@class='price' and contains(text(), '35,00')]"))
action2 = ActionChains(driver).move_to_element(price).click()
action2.perform()

sector = WebDriverWait(driver,timeout).until(lambda d: d.find_element_by_xpath("//*[@class='price' and contains(text(), 'Sėdimas')]"))
action3 = ActionChains(driver).move_to_element(sector).click()
action3.perform()
