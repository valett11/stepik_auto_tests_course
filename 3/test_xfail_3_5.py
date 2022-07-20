import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

list = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']
@pytest.fixture(scope="function")

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('adr', list)
def test_guest_should_see_login_link(browser, adr):
    link = adr
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    cor = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert cor == "Correct!"
