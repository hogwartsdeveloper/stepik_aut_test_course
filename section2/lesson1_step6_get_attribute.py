from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
    people_checked = radiobutton.get_attribute("checked")

    assert people_checked is not None, "People radio is not selected by default"
    time.sleep(11)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn_disabled = button.get_attribute("disabled")
    assert btn_disabled is not None, "Button not disabled"
finally:
    browser.quit()

