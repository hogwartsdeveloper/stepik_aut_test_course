from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button_troll = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_troll.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calc(int(x_el)))

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_submit.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    browser.switch_to.window(first_window)
finally:
    time.sleep(5)
    browser.quit()