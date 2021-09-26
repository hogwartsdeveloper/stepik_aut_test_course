from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_first_name = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input_first_name.send_keys("Zhannur")
    input_last_name = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input_last_name.send_keys("Akhmetkhanov")
    input_city = browser.find_element(By.XPATH, "//input[contains(@class, 'city')]")
    input_city.send_keys("Piter")
    input_country = browser.find_element(By.XPATH, "//input[@id='country']")
    input_country.send_keys("Russian")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
finally:
    time.sleep(5)
    browser.quit()