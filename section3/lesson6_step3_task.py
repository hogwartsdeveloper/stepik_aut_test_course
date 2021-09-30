import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestParametrize:

    @pytest.mark.parametrize("number", [6895, 6896, 6897, 6898, 6899, 6903, 6904, 6905])
    def test_check_feedback(self, browser, number):
        browser.get(f"https://stepik.org/lesson/23{number}/step/1")

        input_answer = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[contains(@id, 'ember')]"))
        )
        answer = math.log(int(time.time()))
        input_answer.send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()

        feedback = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//pre[contains(@class, 'smart-hint')]"))
        ).text

        assert feedback == "Correct!", \
            f"Wrong feedback, got {feedback}, instead of 'Correct!'"


