from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x_e = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_e.text)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(calc(x))

    button_submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    button_submit.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    browser.quit()