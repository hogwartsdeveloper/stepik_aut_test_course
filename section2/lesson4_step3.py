from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.implicitly_wait(5)
    button_verify = browser.find_element(By.ID, "verify")
    button_verify.click()
    message = browser.find_element(By.ID, "verify_message").text
    message_success = "Verification was successful!"
    assert message == message_success, "message don't"
finally:
    browser.quit()