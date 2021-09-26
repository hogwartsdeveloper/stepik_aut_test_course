import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    bag = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_el = bag.get_attribute("valuex")
    print(x_el)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calc(int(x_el)))
    checkbox_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_robot.click()

    radio_robot = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_robot.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_submit.click()
finally:
    time.sleep(5)
    browser.quit()

