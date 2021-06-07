import os

import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page = ''
        self.exceptions = {
            'not_displayed': '{} is not displayed',
            'object_comparing': 'Expected {} and current {} {} are different',
            'is_not': '{} is not {}',
        }

    @staticmethod
    def main_url() -> str:
        return os.environ.get('URL')

    def correct_url(self) -> str:
        return f"{os.environ.get('URL')}/{self.page}"

    def current_url(self) -> str:
        return self.driver.current_url

    def load(self):
        with allure.step(f"Load the '{self.page}' page."):
            self.driver.get(self.correct_url())

    def is_loaded(self):
        if not self.at_page():
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def get(self):
        try:
            if not self.at_page():
                self.load()
            self.is_loaded()
        except RuntimeError:
            self.load()
            self.is_loaded()
        return self

    def at_page(self) -> bool:
        return self.current_url() == self.correct_url()
