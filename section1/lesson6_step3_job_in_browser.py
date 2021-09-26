from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.set_page_load_timeout(2)
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "#submit_button")
    button.click()
finally:
    browser.quit()
