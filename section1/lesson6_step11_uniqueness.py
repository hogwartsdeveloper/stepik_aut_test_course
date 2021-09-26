from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, ".first[required='']")
    input_first_name.send_keys("Zhannur")

    input_last_name = browser.find_element(By.CSS_SELECTOR, ".second[required='']")
    input_last_name.send_keys("Akhmetkhanov")

    input_email = browser.find_element(By.CSS_SELECTOR, ".third[required='']")
    input_email.send_keys("email@samgau.com")

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()

