from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/find_link_text"
text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link_search = browser.find_element(By.LINK_TEXT, text_link)
    link_search.click()

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[name='first_name']")
    input_first_name.send_keys("Zhannur")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "[name='last_name']")
    input_last_name.send_keys("Akhmetkhanov")
    input_city = browser.find_element(By.CSS_SELECTOR, ".city")
    input_city.send_keys("Nur-Sultan")
    input_country = browser.find_element(By.CSS_SELECTOR, "#country")
    input_country.send_keys("Astana")
    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()