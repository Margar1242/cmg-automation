import os
import allure
from random import choice
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from action_wrapper.browser_actions import BrowserActions
from constants.runner_constants import PLATFORM, Platforms
from constants.locators.premium_signup_page_locators import PremiumSignupPageLocator
from constants.premium_signup_constants import (VALID_CARD_NUMBERS,
                                                VALID_MM_YY_NUMBER,
                                                VALID_ZIP_CODE,
                                                INVALID_ZIP_CODE,
                                                INVALID_CARD_NUMBER)
from helpers.helpers import generate_random_string
from pages.base_page import BasePage


class PremiumSignupPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = 'signup'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, PremiumSignupPageLocator.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'email_field': PremiumSignupPageLocator.EMAIL_FIELD,
            'payment_title': PremiumSignupPageLocator.PAYMENT_TITLE,
            'month_membership_text': PremiumSignupPageLocator.MONTH_MEMBERSHIP_TEXT,
            'cc_number_field': PremiumSignupPageLocator.CC_NUMBER_FIELD,
            'cc_number_input': PremiumSignupPageLocator.CC_NUMBER_INPUT,
            'zip_field': PremiumSignupPageLocator.ZIP_FIELD,
            'zip_input': PremiumSignupPageLocator.ZIP_CODE_INPUT,
            'premium_button': PremiumSignupPageLocator.GET_PREMIUM_BUTTON,
            'checkbox_container': PremiumSignupPageLocator.TERMS_OF_USE_CHECKBOX,
            'email_error': PremiumSignupPageLocator.EMAIL_ERROR,
            'cc_error': PremiumSignupPageLocator.CC_NUMBER_ERROR,
            'zip_error': PremiumSignupPageLocator.ZIP_CODE_ERROR,
            'terms_error': PremiumSignupPageLocator.TERMS_ERROR

        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Enter username, password and nickname for Premium Signup Page")
    def enter_username_password_nickname(self):
        for _ in range(3):
            try:
                username = generate_random_string()
                password = f'Test1234'
                nickname = generate_random_string()
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.LOGIN_ID, username)
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.PASSWORD, password)
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.CONFIRM_PASSWORD, password)
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.NICKNAME, nickname)
                ElementActions.click_on_element(self.driver, PremiumSignupPageLocator.SIGNUP_BUTTON)
                WaitActions.wait_until_element_is_visible(self.driver, PremiumSignupPageLocator.PAYMENT_TITLE,
                                                          time_out=13)
                break
            except TimeoutException:
                self.driver.refresh()

    @allure.step("Get 'Enable your Premium Avatar, Theme, Nickname & more' text for Premium Signup Page")
    def get_title_text(self):
        return ElementActions.get_text(self.driver, PremiumSignupPageLocator.TITLE).replace('\n', '') \
            .replace('\t', '').strip().lower()

    @allure.step("Get 'PAYMENT' title text for Premium Signup Page")
    def get_payment_title_text(self):
        return ElementActions.get_text(self.driver, PremiumSignupPageLocator.PAYMENT_TITLE).replace('\n', '') \
            .replace('\t', '').strip().lower()

    @allure.step("Get '$5.99/month membership. Cancel Anytime' text for Premium Signup Page")
    def get_month_membership_text(self):
        part_1 = self.month_membership_text.text.replace('\n', '').replace('\t', '')
        return part_1[:part_1.find(' Switch')].lower().strip()

    @allure.step("Get 'Terms of Use' text for Premium Signup Page")
    def get_terms_of_use_text(self):
        return ElementActions.get_text(self.driver, PremiumSignupPageLocator.TERMS_TEXT).replace('\n', '') \
            .replace('\t', '').strip().lower()

    @allure.step("Get 'Terms of Use' checkbox for Premium Signup Page")
    def get_terms_of_use_checkbox(self):
        container = self.checkbox_container
        element = ElementFinder.find_element_from_element(container, 'input')
        return ElementActions.get_attribute_from_element(element, 'type')

    @allure.step("Get 'Terms of Use' link for Premium Signup Page")
    def get_terms_of_use_link(self):
        return ElementActions.get_attribute(self.driver, PremiumSignupPageLocator.TERMS_OF_USE_BUTTON, 'href')

    @allure.step("Click on 'Get Premium' button for Premium Signup Page")
    def click_on_premium_button(self):
        ElementActions.click_on_element(self.driver, PremiumSignupPageLocator.GET_PREMIUM_BUTTON)

    @allure.step("Enter incorrect email for Premium Signup Page")
    def enter_incorrect_email(self):
        ElementActions.put_text(self.driver, PremiumSignupPageLocator.EMAIL_FIELD, generate_random_string())
        self.click_on_premium_button()

    @allure.step("Enter correct email for Premium Signup Page")
    def enter_correct_email(self):
        self.email_field.clear()
        ElementActions.put_text(self.driver, PremiumSignupPageLocator.EMAIL_FIELD, f'{generate_random_string()}'
                                                                                   f'@gmail.com')

    @allure.step("Enter incorrect card number for Premium Signup Page")
    def enter_incorrect_card_number(self):
        BrowserActions.switch_to_iframe(self.driver, PremiumSignupPageLocator.CC_NUMBER_IFRAME)
        if os.environ[PLATFORM] == Platforms.ANDROID.value:
            for num in INVALID_CARD_NUMBER:
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.CC_NUMBER_INPUT, num)
        else:
            ElementActions.put_text(self.driver, PremiumSignupPageLocator.CC_NUMBER_INPUT, INVALID_CARD_NUMBER)
        self.driver.switch_to.default_content()

    @allure.step("Enter valid card number for Premium Signup Page")
    def enter_valid_card_number(self):
        BrowserActions.switch_to_iframe(self.driver, PremiumSignupPageLocator.CC_NUMBER_IFRAME)
        self.cc_number_input.clear()
        card_number = choice(VALID_CARD_NUMBERS)
        if os.environ[PLATFORM] == Platforms.ANDROID.value:
            for num in card_number:
                ElementActions.put_text(self.driver, PremiumSignupPageLocator.CC_NUMBER_INPUT, num)
        else:
            ElementActions.put_text(self.driver, PremiumSignupPageLocator.CC_NUMBER_INPUT, card_number)
        self.driver.switch_to.default_content()

        BrowserActions.switch_to_iframe(self.driver, PremiumSignupPageLocator.CARD_MM_YY_IFRAME)
        ElementActions.put_text(self.driver, PremiumSignupPageLocator.CARD_MM_YY_INPUT, VALID_MM_YY_NUMBER)
        self.driver.switch_to.default_content()

    @allure.step("Enter incorrect zip code for Premium Signup Page")
    def enter_incorrect_zip_code(self):
        self.enter_valid_card_number()
        BrowserActions.switch_to_iframe(self.driver, PremiumSignupPageLocator.ZIP_CODE_IFRAME)
        self.zip_input.clear()
        ElementActions.put_text(self.driver, PremiumSignupPageLocator.ZIP_CODE_INPUT, INVALID_ZIP_CODE)
        self.driver.switch_to.default_content()

    @allure.step("Enter valid zip code for Premium Signup Page")
    def enter_valid_zip(self):
        BrowserActions.switch_to_iframe(self.driver, PremiumSignupPageLocator.ZIP_CODE_IFRAME)
        self.zip_input.clear()
        ElementActions.put_text(self.driver, PremiumSignupPageLocator.ZIP_CODE_INPUT, VALID_ZIP_CODE)
        self.driver.switch_to.default_content()

    @allure.step("Click on 'Terms of Use' button for Premium Signup Page")
    def click_on_terms_button(self):
        url = ElementActions.get_attribute(self.driver, PremiumSignupPageLocator.TERMS_OF_USE_BUTTON, 'href')
        self.get(url)

    @allure.step("Enter valid zip code for Premium Signup Page")
    def enter_valid_params(self):
        self.enter_valid_card_number()
        self.enter_valid_zip()
        self.enter_correct_email()
        self.click_on_terms_checkbox()
        self.click_on_premium_button()
        if not self.is_mobile:
            WaitActions.wait_until_element_is_visible(self.driver, PremiumSignupPageLocator.CATEGORIES)
        else:
            WaitActions.wait_until_element_is_visible(self.driver, PremiumSignupPageLocator.HUD)

    @allure.step("Click on 'Terms of Use' checkbox for Premium Signup Page")
    def click_on_terms_checkbox(self):
        ElementActions.click_on_element(self.driver, PremiumSignupPageLocator.ACCEPT_TERMS_BUTTON)

    @allure.step("Get success registration text for Premium Signup Page")
    def get_success_registration_text(self):
        text = ElementActions.get_text(self.driver, PremiumSignupPageLocator.SUCCESS_TEXT).replace('\t', '') \
            .replace('\n', '').strip().upper()
        if 'SHOW PROFILE' in text:
            text = text[:text.index('SHOW')]
        return text
