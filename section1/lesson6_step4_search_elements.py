from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_page_load_timeout(2)

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[name='first_name']")
    input_first_name.send_keys("Zhannur")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "[name='last_name']")
    input_last_name.send_keys("Akhmetkhanov")
    input_city = browser.find_element(By.CSS_SELECTOR, ".city")
    input_city.send_keys("Nur-Sultan")
    input_country = browser.find_element(By.CSS_SELECTOR, "#country")
    input_country.send_keys("Astana")
    button_submit = browser.find_element(By.CSS_SELECTOR, "#submit_button")
    button_submit.click()
finally:
    time.sleep(5)
    browser.quit()