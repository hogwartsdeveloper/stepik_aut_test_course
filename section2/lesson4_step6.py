from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.ID, "button")
    button.click()
finally:
    browser.quit()