import os

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.login_page_locators import LogInPageLocators
from pages.base_page import BasePage


class LogInPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = 'login'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, LogInPageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'login_button': LogInPageLocators.LOGIN_BUTTON,
            'login_title': LogInPageLocators.LOGIN_TITLE,
            'username': LogInPageLocators.USERNAME,
            'password': LogInPageLocators.PASSWORD,
            'submit_button': LogInPageLocators.SUBMIT_BUTTON,
            'forgot_password': LogInPageLocators.FORGOT_PASSWORD,
            'user_signup': LogInPageLocators.USER_SIGNUP
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get Your Login ID or Nickname placeholder on Login Page")
    def get_login_placeholder(self):
        return ElementActions.get_attribute(self.driver, LogInPageLocators.USERNAME, "placeholder")

    @allure.step("Get Password placeholder on Login Page")
    def get_password_placeholder(self):
        return ElementActions.get_attribute(self.driver, LogInPageLocators.PASSWORD, "placeholder")

    @allure.step("Get Sign Up button link on Login Page")
    def get_signup_link(self):
        element = ElementFinder.find_element_from_element(self.user_signup, 'p > strong > a')
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Get Forgot password link on Login Page")
    def get_forgot_password_link(self):
        return ElementActions.get_attribute(self.driver, LogInPageLocators.FORGOT_PASSWORD, "href")

    @allure.step("Get LOG IN title on Login Page")
    def get_log_in_text(self):
        return ElementActions.get_text(self.driver, LogInPageLocators.LOGIN_TITLE).strip().upper()

    @allure.step("Get user signup text on Login Page")
    def get_user_signup_text(self):
        return ElementActions.get_text(self.driver, LogInPageLocators.USER_SIGNUP).replace('\n', '').replace('\t', '')

    @allure.step("Enter incorrect username and password on Login Page")
    def enter_incorrect_username_and_password(self):
        ElementActions.put_text(self.driver, LogInPageLocators.USERNAME, "11abcde")
        ElementActions.put_text(self.driver, LogInPageLocators.PASSWORD, "1a1bcde")

    @allure.step("Click on Log In button on Login Page")
    def click_on_login_button(self, need_wait=False):
        ElementActions.click_on_element(self.driver, LogInPageLocators.SUBMIT_BUTTON)
        if need_wait:
            WaitActions.wait_until_element_is_visible(self.driver, LogInPageLocators.GAME_IMAGE)

    @allure.step("Get incorrect login or password error message on Login Page")
    def get_alert(self):
        text = ElementActions.get_text(self.driver, LogInPageLocators.ERR_MESSAGE)
        text = " ".join(text.strip().replace('\n', '').replace('\t', '').split())[:-1].strip()
        return text

    @allure.step("Enter valid username and password on Login Page")
    def enter_valid_username_and_password(self):
        self.username.clear()
        ElementActions.put_text(self.driver, LogInPageLocators.USERNAME, "testrafik")
        ElementActions.put_text(self.driver, LogInPageLocators.PASSWORD, "testrafik")

    @allure.step("Click on forgot password button on Login Page")
    def click_on_forgot_password_link(self):
        url = ElementActions.get_attribute(self.driver, LogInPageLocators.FORGOT_PASSWORD, 'href')
        self.get(url)

    @allure.step("Click on sign up button on Login Page")
    def click_on_signup_link(self):
        url = ElementActions.get_attribute(self.driver, LogInPageLocators.SIGNUP_LINK, 'href')
        self.get(url)
