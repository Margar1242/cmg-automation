import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from action_wrapper.browser_actions import BrowserActions
from constants.locators.mobile_game_page_locators import MobileGamePageLocators
from pages.base_page import BasePage


class MobileGamePage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '0-shoot-to-slide'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, MobileGamePageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'play_button': MobileGamePageLocators.PLAY_BUTTON,
            'timer': MobileGamePageLocators.TIMER,
            'continue_button': MobileGamePageLocators.CONTINUE_BUTTON,
            'sorry_message': MobileGamePageLocators.SORRY_MESSAGE,
            'show_more_button': MobileGamePageLocators.SHOW_MORE_BUTTON,
            'show_less_button': MobileGamePageLocators.SHOW_LESS_BUTTON,
            'game_content': MobileGamePageLocators.GAME_CONTENT,
            'more_text': MobileGamePageLocators.MORE_TEXT
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on play button for Mobile Game Page")
    def click_on_play_button(self):
        ElementActions.click_on_element(self.driver, MobileGamePageLocators.PLAY_BUTTON)

    @allure.step("Click on continue button for Mobile Game Page")
    def click_on_continue_button(self):
        ElementActions.click_on_element(self.driver, MobileGamePageLocators.CONTINUE_BUTTON)

    @allure.step("Get not supported game for Mobile Game Page")
    def get_not_supported_game_page(self):
        self.get(f'{self.main_url()}/0-mini-metro-london')

    @allure.step("Get 'Sorry...' message for Mobile Game Page")
    def get_message(self):
        return ElementActions.get_text(self.driver, MobileGamePageLocators.SORRY_MESSAGE)

    @allure.step("Click on 'Show More' button for Mobile Game Page")
    def click_on_show_more_button(self):
        ElementActions.click_on_element(self.driver, MobileGamePageLocators.SHOW_MORE_BUTTON)

    @allure.step("Click on 'Show More' button for Mobile Game Page")
    def switch_to_game_iframe(self):
        BrowserActions.switch_to_iframe(self.driver, MobileGamePageLocators.IFRAME)
