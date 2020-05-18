import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# pytest -v pytest_mark_parametrize.py

arr = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
       "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
       "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
       ]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', arr)
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.get(link)
    good_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div.cost-info__text-segment span"), '1 point'))

    input = browser.find_element_by_css_selector("textarea")

    time.sleep(1)
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_css_selector(
        ".smart-hints__hint")
    welcome_text = welcome_text_elt.text

    assert "Correct!" == welcome_text
