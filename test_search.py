import allure
import time
import time

from allure_commons.types import AttachmentType
from selenium import webdriver


class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome()


    def teardown(self):
        self.driver.quit()

#blocker critical normal minor trivial

    @allure.feature('Open Pages')
    @allure.story('Открываем страницу Google.com')
    @allure.severity('blocker')
    def test_google_search(self):
        self.driver.get("http:google.com")
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attacment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('Open Pages')
    @allure.story('Открываем страницу yandex.ru')
    @allure.severity('critical')
    def test_yandex_search(self):
        self.driver.get("http:yandex.ru")

        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Яндекс'

    @allure.feature('Open Pages')
    @allure.story('Открываем страницу Yahoo.com')
    @allure.severity('trivial')
    def test_yahoo_search(self):
        self.driver.get("http:yahoo.com")
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attacment_type=AttachmentType.PNG)
        assert self.driver.title == 'Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos'
