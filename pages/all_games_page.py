import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.all_games_page_locators import AllGamesPageLocators
from pages.base_page import BasePage


class AllGamesPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '1-complete-game-list'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, AllGamesPageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'ac': AllGamesPageLocators.AC,
            'dg': AllGamesPageLocators.DG,
            'hm': AllGamesPageLocators.HM,
            'nr': AllGamesPageLocators.NR,
            'sz': AllGamesPageLocators.SZ,
            'game_urls': AllGamesPageLocators.GAME_URLS,
            'offered_games': AllGamesPageLocators.OFFERED_GAMES,
            'flash_robot_image': AllGamesPageLocators.FLASH_ROBOT_IMAGE,
            'related_games': AllGamesPageLocators.RELATED_GAMES

        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on '{1}' filter for All Games Page")
    def click_on_filter(self, filter_):
        element = getattr(AllGamesPageLocators, filter_.upper())
        url = ElementActions.get_attribute(self.driver, element, 'href')
        self.get(url)

    @allure.step("Get all games for All Games Page")
    def get_games_url(self):
        games = {}
        elements = ElementFinder.find_element_from_element(self.game_urls, ' .views-row > span:nth-child(1) > a',
                                                           multiple=True)
        for element in elements:
            game_name = element.text
            url = ElementActions.get_attribute_from_element(element, 'href')
            games[game_name] = url
        return games

    @allure.step("Click on view all games button All Games Page")
    def click_on_view_all_games_button(self):
        url = ElementActions.get_attribute(self.driver, AllGamesPageLocators.VIEW_ALL_GAMES_BUTTON, 'href')
        self.get(url)

    @allure.step("Get robot image for All Games Page")
    def get_flash_robot_image(self):
        return ElementActions.get_attribute_from_element(self.flash_robot_image, 'src')

    @allure.step("Get offered games from flush game for All Games Page")
    def get_offered_games(self):
        elements = ElementFinder.find_element_from_element(self.offered_games, '.game-item a', multiple=True)
        return [ElementActions.get_attribute_from_element(element, 'href') for element in elements]

    @allure.step("Get game name for All Games Page")
    def get_game_title(self):
        return ElementActions.get_text(self.driver, AllGamesPageLocators.GAME_TITLE).lower().replace('\t', ''). \
            replace('\n', '').strip()
