import allure
from selenium.webdriver.remote.webdriver import WebDriver
from random import choice

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from action_wrapper.browser_actions import BrowserActions
from constants.locators.big_screen_locators import BigScreenLocators
from constants.big_screen_constants import *
from helpers.helpers import generate_random_email
from pages.base_page import BasePage
from time import sleep


class BigScreenPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '0-connection'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.LOADING_TEXT)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'big_screen_button': BigScreenLocators.BIG_SCREEN_BUTTON,
            'container': BigScreenLocators.BIG_SCREEN_PROGRESS_BAR_CONTAINER,
            'progress_bar': BigScreenLocators.PROGRESS_BAR,
            'popup_text': BigScreenLocators.BIG_SCREEN_POPUP_TEXT,
            'big_screen_popup': BigScreenLocators.BIG_SCREEN_POPUP,
            'X': BigScreenLocators.X,
            'sponsored_video_button': BigScreenLocators.SPONSORED_VIDEO_BUTTON,
            'premium_access_button': BigScreenLocators.PREMIUM_ACCESS_BUTTON,
            'return_to_regular_mode': BigScreenLocators.RETURN_TO_REGULAR_MODE,
            'popup': BigScreenLocators.POPUP,
            'play_big_screen_now_button': BigScreenLocators.PLAY_BIG_SCREEN_NOW_BUTTON,
        }
        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on continue button for Big Screen Page")
    def click_on_continue_button(self):
        if ElementFinder.get_element_existence(self.driver, BigScreenLocators.CONTINUE_BUTTON, timeout=25):
            ElementActions.click_on_element(self.driver, BigScreenLocators.CONTINUE_BUTTON)
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.BIG_SCREEN_BUTTON)

    @allure.step("Get big screen and progress bar for Big Screen Page")
    def get_container_elements(self):
        elements = ElementFinder.find_element_from_element(self.container, '.col-sm-6', multiple=True)
        progress_bar = ElementFinder.find_element_from_element(elements[0], '.game-xp-progress')
        big_screen = ElementFinder.find_element_from_element(elements[1], '.requestfullscreen')
        return progress_bar, big_screen

    @allure.step("Get big screen popup text for Big Screen Page")
    def get_big_screen_popup_text(self):
        return ElementActions.get_text(self.driver, BigScreenLocators.BIG_SCREEN_POPUP_TEXT).replace('\n', ''). \
            replace('\t', '').strip()

    @allure.step("Get big screen popup 'or' text for Big Screen Page")
    def get_popup_or_text(self):
        return ElementActions.get_text(self.driver, BigScreenLocators.OR_TEXT).replace('\n', ''). \
            replace('\t', '').strip().upper()

    @allure.step("Click on big screen button for Big Screen Page")
    def click_on_big_screen_button(self):
        ElementActions.click_on_element(self.driver, BigScreenLocators.BIG_SCREEN_BUTTON)
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.BIG_SCREEN_POPUP)

    @allure.step("Click on 'Pay For Premium Access' button for Big Screen Page")
    def click_on_pay_for_premium_access_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.PREMIUM_ACCESS_BUTTON)
        ElementActions.click_on_element(self.driver, BigScreenLocators.PREMIUM_ACCESS_BUTTON)

    @allure.step("Get premium access text for Big Screen Page")
    def get_premium_access_text(self):
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.BIG_SCREEN_IFRAME)
        text = ElementActions.get_text(self.driver, BigScreenLocators.NOT_AVAILABLE_TEXT).replace('\n', ''). \
            replace('\t', '').strip().upper()
        self.driver.switch_to.default_content()
        return text

    @allure.step("Click on X button for Big Screen Page")
    def click_on_x_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.POPUP)
        ElementActions.click_on_element(self.driver, BigScreenLocators.X)

    @allure.step("Get big screen popup for Big Screen Page")
    def get_popup_big_screen_popup(self):
        return ElementFinder.get_element_existence(self.driver, BigScreenLocators.POPUP, 5)

    @allure.step("Click on 'return to regular mode' button for Big Screen Page")
    def click_on_regular_mode_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.POPUP)
        ElementActions.click_on_element(self.driver, BigScreenLocators.RETURN_TO_REGULAR_MODE)

    @allure.step("Click on 'View Sponsored Video' button for Big Screen Page")
    def click_sponsored_video_button(self):
        ElementActions.click_on_element(self.driver, BigScreenLocators.SPONSORED_VIDEO_BUTTON)

    @allure.step("Click on 'Play Big Screen' button for Big Screen Page")
    def click_play_big_screen_now_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.PLAY_BIG_SCREEN_NOW_BUTTON,
                                                  time_out=30)
        ElementActions.click_on_element(self.driver, BigScreenLocators.PLAY_BIG_SCREEN_NOW_BUTTON)

    @allure.step("Get 'Full Screen Window' for Big Screen Page")
    def get_full_screen_window(self):
        return ElementFinder.get_element_existence(self.driver, BigScreenLocators.FULL_SCREEN_WINDOW, timeout=10)

    @allure.step("Click on 'Exit Big Screen' button for Big Screen Page")
    def click_on_exit_big_screen_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.EXIT_BIG_SCREEN)
        ElementActions.click_on_element(self.driver, BigScreenLocators.EXIT_BIG_SCREEN)
        sleep(5)

    @allure.step("Enter premium username and password for Big Screen Page")
    def enter_premium_username_password(self):
        ElementActions.click_on_element(self.driver, BigScreenLocators.LOGIN)
        ElementActions.put_text(self.driver, BigScreenLocators.USERNAME, USERNAME)
        ElementActions.put_text(self.driver, BigScreenLocators.PASSWORD, PASSWORD)
        ElementActions.click_on_element(self.driver, BigScreenLocators.LOGIN_BUTTON)

    @allure.step("Click on 'Logout' button for Big Screen Page")
    def click_on_logout_button(self):
        ElementActions.click_on_element(self.driver, BigScreenLocators.LOGOUT)
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.LOGIN)

    @allure.step("Click on 'Exit Big Screen' button for Big Screen Page")
    def click_on_exit_big_screen_button(self):
        ElementActions.click_on_element(self.driver, BigScreenLocators.EXIT_BIG_SCREEN)

    @allure.step("Fill premium membership fields for Big Screen Page")
    def fill_premium_membership_fields(self):
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.BIG_SCREEN_IFRAME)
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.CC_NUMBER_IFRAME)
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.CC_NUMBER_IFRAME)

        card_number = choice(CARD_NUMBERS)
        ElementActions.put_text(self.driver, BigScreenLocators.CC_NUMBER_INPUT, card_number)
        self.driver.switch_to.default_content()
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.BIG_SCREEN_IFRAME)

        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.CARD_MM_YY_IFRAME)
        ElementActions.put_text(self.driver, BigScreenLocators.CARD_MM_YY_INPUT, MM_YY_NUMBER)
        self.driver.switch_to.default_content()
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.BIG_SCREEN_IFRAME)

        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.ZIP_CODE_IFRAME)
        ElementActions.put_text(self.driver, BigScreenLocators.ZIP_CODE_INPUT, ZIP_CODE)
        self.driver.switch_to.default_content()
        BrowserActions.switch_to_iframe(self.driver, BigScreenLocators.BIG_SCREEN_IFRAME)

        email = generate_random_email()
        ElementActions.put_text(self.driver, BigScreenLocators.EMAIL_INPUT, email)

        password = 'Test123!'
        ElementActions.put_text(self.driver, BigScreenLocators.PASSWORD_INPUT, password)
        ElementActions.click_on_element(self.driver, BigScreenLocators.ACCEPT_TERMS_BUTTON)

        ElementActions.click_on_element(self.driver, BigScreenLocators.PREMIUM_BUTTON)
        WaitActions.wait_until_element_is_visible(self.driver, BigScreenLocators.SUCCESS_PAGE_ELEMENT)

    @allure.step("Get premium access message for Big Screen Page")
    def get_premium_access_message(self):
        return ElementActions.get_text(self.driver, BigScreenLocators.SUCCESS_TEXT).replace('\t', '') \
            .replace('\n', '').strip().upper()
