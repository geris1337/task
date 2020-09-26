from selenium import webdriver
from selenium.webdriver.support.color import Color
import time

def highlight(element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    style = element.get_attribute('style')
    apply_style("background: yellow;")
    time.sleep(2)
    apply_style(style)

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/challenging_dom")
highlight(driver.find_element_by_xpath("//tr[3]/td[count(//table/thead/tr/th[.='Diceret']/preceding-sibling::th)+1]"))
highlight(driver.find_element_by_xpath("//td[text()='Apeirian7']/following-sibling::td[last()]/a[text()='delete']"))
highlight(driver.find_element_by_xpath("//td[text()='Apeirian2']/following-sibling::td[last()]/a[text()='edit']"))
highlight(driver.find_element_by_xpath("//td[text()='Definiebas7']"))
highlight(driver.find_element_by_xpath("//td[text()='Iuvaret7']"))

element = driver.find_element_by_xpath("//a[@class='button success']")
color = Color.from_string(element.value_of_css_property('background-color'))

if color.hex == "#5da423":
    element.click()