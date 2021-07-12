import os

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from constants.general_constants import TYPE, Types


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page = ''
        self.is_mobile = os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}
        self.exceptions = {
            'not_displayed': '{} is not displayed',
            'object_comparing': 'Expected "{}" and current "{}" {} are different',
            'is_not': '{} is not {}',
        }

    @staticmethod
    def main_url() -> str:
        return os.environ.get('URL')

    def correct_url(self) -> str:
        return f"{os.environ.get('URL')}/{self.page}"

    def current_url(self) -> str:
        return self.driver.current_url

    def load(self, url=None):
        url = url if url else self.correct_url()
        page = url if url else self.page
        with allure.step(f"Load the '{page}' page."):
            self.driver.get(url)

    def is_loaded(self, url=None):
        page = url if url else self.page
        if not self.at_page(url):
            raise RuntimeError(f"The {page} page is not loaded properly")

    def get(self, url=None):
        try:
            if not self.at_page(url):
                self.load(url)
            self.is_loaded(url)
        except RuntimeError:
            self.load(url)
            self.is_loaded(url)
        return self

    def at_page(self, url=None) -> bool:
        return self.current_url() == url if url else self.current_url() == self.correct_url()
