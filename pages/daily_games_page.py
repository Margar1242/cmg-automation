import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.daily_games_page_locators import DailyGamesPageLocators
from pages.base_page import BasePage


class DailyGamesPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '1-daily-games'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, DailyGamesPageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'subcategory_block': DailyGamesPageLocators.SUBCATEGORY_BLOCK
        }
        return ElementFinder.find_element(self.driver, mapper[item])

    def get_game_link_and_name(self):
        games = {}
        for i in range(1, 9):
            key = ElementFinder.find_element_from_element(self.subcategory_block,
                                                          f'.game-item:nth-child({i}) .game-link-wrapper h3').text
            value_element = ElementFinder.find_element_from_element(self.subcategory_block,
                                                                    f'.game-item:nth-child({i}) .game-link-wrapper a')
            value = ElementActions.get_attribute_from_element(value_element, 'href')
            games[key] = value
        return games

    @allure.step("Click on daily games category game for Daily Games Page")
    def click_on_game(self, url):
        self.get(url)
