import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver


class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_google_search(self):
        self.driver.get("http:google.com")
        assert self.driver.title == 'Gogle'
