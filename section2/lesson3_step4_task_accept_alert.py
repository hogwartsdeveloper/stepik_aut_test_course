from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    x = int(x)
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button_go = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_go.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calc(x_el))

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_submit.click()

    alert_result = browser.switch_to.alert
    alert_text = alert_result.text
    print(alert_text)
    alert_result.accept()
finally:
    browser.quit()