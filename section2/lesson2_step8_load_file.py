from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "../esp/author.txt")
file_path_real = os.path.realpath(file_path)

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_first_name = browser.find_element(By.NAME, "firstname")
    input_last_name = browser.find_element(By.NAME, "lastname")
    input_email = browser.find_element(By.NAME, "email")
    input_upload_file = browser.find_element(By.ID, "file")
    button = browser.find_element(By.CLASS_NAME, "btn")

    input_first_name.send_keys("Aleksey")
    input_last_name.send_keys("Sherbakov")
    input_email.send_keys("idiv@mail.com")
    input_upload_file.send_keys(file_path_real)
    button.click()
finally:
    time.sleep(7)
    browser.quit()