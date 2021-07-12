import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.mobile_specific_locators import MobileSpecificLocators
from pages.base_page import BasePage


class MobileSpecificPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, MobileSpecificLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'search_bar': MobileSpecificLocators.SEARCH_BAR,
            'az_games': MobileSpecificLocators.AZ_GAMES,
            'strategy': MobileSpecificLocators.STRATEGY,
            'numbers': MobileSpecificLocators.NUMBERS,
            'trivia': MobileSpecificLocators.TRIVIA,
            'skill': MobileSpecificLocators.SKILL,
            'logic': MobileSpecificLocators.LOGIC,
            'playlists': MobileSpecificLocators.PLAYLISTS,
            'daily_games': MobileSpecificLocators.DAILY_GAMES,
            'more': MobileSpecificLocators.MORE,
            'signup_button': MobileSpecificLocators.SIGNUP_BUTTON,
            'login_button': MobileSpecificLocators.LOGIN_BUTTON,
            'classic': MobileSpecificLocators.CLASSIC,
            'puzzles': MobileSpecificLocators.PUZZLES,
            'geography': MobileSpecificLocators.GEOGRAPHY,
            'word_games': MobileSpecificLocators.WORD_GAMES,
            'memory': MobileSpecificLocators.MEMORY,
            'science': MobileSpecificLocators.SCIENCE,
            'dropdown': MobileSpecificLocators.DROPDOWN,
            'dropdown_items': MobileSpecificLocators.DROPDOWN_ITEMS,
            'view_all_button': MobileSpecificLocators.VIEW_ALL_BUTTON,
            'my_games': MobileSpecificLocators.MY_GAMES
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on toggle for Mobile Specific Game Page")
    def click_on_toggle(self):
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.TOGGLE)

    @allure.step("Click on more button for Mobile Specific Game Page")
    def click_on_more_button(self):
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.MORE_BUTTON)

    @allure.step("Get 'More' button text for Mobile Specific Game Page")
    def get_more_button_text(self):
        return ElementActions.get_text(self.driver, MobileSpecificLocators.MORE_BUTTON)

    @allure.step("Get more section categories for Mobile Specific Game Page")
    def get_more_section_categories(self):
        return ElementFinder.find_element_from_element(self.more, 'ul li a', multiple=True)

    @allure.step("Click on login button for Mobile Specific Game Page")
    def click_on_login_button(self):
        self.click_on_toggle()
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.LOGIN_BUTTON)

    @allure.step("Enter username and password for Mobile Specific Game Page")
    def enter_username_and_password(self):
        ElementActions.put_text(self.driver, MobileSpecificLocators.USERNAME_INPUT, 'testrafik')
        ElementActions.put_text(self.driver, MobileSpecificLocators.PASSWORD, 'testrafik')
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.SUBMIT)
        WaitActions.wait_until_element_is_visible(self.driver, MobileSpecificLocators.HEADER_LOCATOR)

    @allure.step("Click on user profile button for Mobile Specific Game Page")
    def click_on_user_profile_button(self):
        self.click_on_toggle()
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.USER_PROFILE_BUTTON)

    @allure.step("Click on dropdown for Mobile Specific Game Page")
    def click_on_dropdown(self):
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.DROPDOWN)

    @allure.step("Get dropdown items for Mobile Specific Game Page")
    def get_dropdown_items(self):
        self.click_on_dropdown()
        items = {}
        filters = ElementFinder.find_element_from_element(self.dropdown_items, 'li', multiple=True)
        for item in filters:
            item_name = item.text
            items[item_name] = item
        return items

    @allure.step("Get profile games for Mobile Specific Game Page")
    def get_profile_games(self):
        games = {}
        items = ElementFinder.find_element_from_element(self.my_games, '.game-item h3 a', multiple=True)
        for item in items:
            games[item.text] = item
        return games

    @allure.step("Click on 'View All' button for Mobile Specific Game Page")
    def click_on_view_all_button(self):
        ElementActions.click_on_element(self.driver, MobileSpecificLocators.VIEW_ALL_BUTTON)
