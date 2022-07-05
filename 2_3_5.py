import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time


link='https://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    s = Service('c:\chromedriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(link)
    time.sleep(3)
    button1 = browser.find_element(By.CSS_SELECTOR, ".container button").click()
    time.sleep(3)
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    select_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    xx = select_x.text
    y = calc(xx)
    print(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR,".container button").click()


finally:
    time.sleep(500)
    browser.quit()
