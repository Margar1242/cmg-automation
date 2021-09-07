import allure
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from random import choice
import requests

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.game_page_locators import GamePageLocators
from pages.base_page import BasePage
from constants.game_page_constants import GAMES_DATA_URL, GAME_NODE_JSON_URL


class GamePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '0-powerline-io'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, GamePageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'timer': GamePageLocators.TIMER,
            'playlists_button': GamePageLocators.PLAYLISTS_BUTTON,
            'continue_button': GamePageLocators.CONTINUE_BUTTON,
            'progress_bar': GamePageLocators.PROGRESS_BAR,
            'full_screen_button': GamePageLocators.FULL_SCREEN_BUTTON,
            'also_like_section': GamePageLocators.ALSO_LIKE_SECTION,
            'also_like_section_games': GamePageLocators.ALSO_LIKE_SECTION_GAMES,
            'right_arrow': GamePageLocators.RIGHT_ARROW,
            'left_arrow': GamePageLocators.LEFT_ARROW,
            'like_button': GamePageLocators.LIKE_BUTTON,
            'game_name_title': GamePageLocators.GAME_NAME_TITLE,
            'dislike_button': GamePageLocators.DISLIKE_BUTTON,
            'game_iframe': GamePageLocators.GAME_IFRAME,
            'instructions': GamePageLocators.INSTRUCTIONS,
            'skip_all_ad_button': GamePageLocators.SKIP_ALL_AD_BUTTON,
            'top_picks_section': GamePageLocators.TOP_PICKS_SECTION,
            'gear_promo': GamePageLocators.GEAR_PROMO,
            'go_ad_free_promo': GamePageLocators.GO_AD_FREE_PROMO,
            'profile_promo': GamePageLocators.PROFILE_PROMO,
            'az_games_section': GamePageLocators.AZ_GAMES_SECTION,
            'aiming_games': GamePageLocators.AIMING_GAMES,
            'az_game_list': GamePageLocators.AZ_GAME_LIST,
            'leaderboard': GamePageLocators.LEADERBOARD,
            'like_this_game': GamePageLocators.LIKE_THIS_GAME,
            'game_loading_text': GamePageLocators.GAME_LOADING_TEXT,
            'rating_module': GamePageLocators.RATING_MODULE,
            'rating': GamePageLocators.RATING,
            'rating_value': GamePageLocators.RATING_VALUE,
            'votes_count': GamePageLocators.VOTES_COUNT,
            'game_urls': GamePageLocators.GAME_URLS,
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get timer seconds for Game Page")
    def get_timer_seconds(self, element):
        if element.is_displayed():
            text = element.text
            if text.isdigit():
                return int(text)

    @allure.step("Click continue button for Game Page")
    def click_continue_button(self):
        if ElementFinder.get_element_existence(self.driver, GamePageLocators.CONTINUE_BUTTON):
            ElementActions.click_on_element(self.driver, GamePageLocators.CONTINUE_BUTTON)

    @allure.step("Get playlists button for Game Page")
    def click_playlists_button(self):
        url = ElementActions.get_attribute(self.driver, GamePageLocators.PLAYLISTS_BUTTON, 'href')
        self.get(url)

    @allure.step("Click 'You'll Also Like...' section right arrow for Game Page")
    def click_also_like_section_right_arrow(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.RIGHT_ARROW)
        sleep(2)

    @allure.step("Click 'You'll Also Like...' section left arrow for Game Page")
    def click_also_like_section_left_arrow(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.LEFT_ARROW)
        sleep(2)

    @staticmethod
    def get_expected_visible_after_right_arrow_click_games(games, visible_games_count):
        if visible_games_count > len(games[visible_games_count:]):
            diff = visible_games_count - len(games[visible_games_count:]) - 1
            visible_games_after_arrow_click = games[-diff:] + games[:diff]
        else:
            visible_games_after_arrow_click = games[visible_games_count:visible_games_count * 2]
        return [game.get_attribute('href') for game in visible_games_after_arrow_click if game.is_displayed()]

    @staticmethod
    def get_expected_visible_after_left_arrow_click_games(games, visible_games_count):
        return [game.get_attribute('href') for game in games[:visible_games_count] if game.is_displayed()]

    @allure.step("Get 'You'll Also Like...' section games for Game Page")
    def get_also_like_section_game_list(self):
        elements = ElementFinder.find_element_from_element(self.also_like_section_games, 'li a', multiple=True)
        visible_elements = [game for game in elements if game.is_displayed()]
        return elements, len(visible_elements)

    @allure.step("Get 'You'll Also Like...' section random visible game for Game Page")
    def get_also_like_section_random_game_url(self):
        elements = ElementFinder.find_element_from_element(self.also_like_section_games, 'a', multiple=True)
        chosen_element = choice([url for url in elements if url.is_displayed()])
        return ElementActions.get_attribute_from_element(chosen_element, 'href'), chosen_element

    @allure.step("Click 'You'll Also Like...' section chosen random visible game for Game Page")
    def click_also_like_section_random_game(self, element):
        url = ElementActions.get_attribute_from_element(element, 'href')
        self.get(url)

    @allure.step("Get 'You'll Also Like...' section visible games for Game Page")
    def get_also_like_section_visible_games(self):
        elements = ElementFinder.find_element_from_element(self.also_like_section_games, 'a', multiple=True)
        visible_games = [game for game in elements if game.is_displayed()]
        return visible_games

    @staticmethod
    def get_elements_by_css_selector(element, css_selector):
        return ElementFinder.find_element_from_element(element, css_selector, multiple=True)

    @allure.step("Get Instruction' section text for Game Page")
    def get_instructions_text(self):
        return ElementFinder.find_element_from_element(self.instructions, '.desktop > p').text

    @allure.step("Get 'Instruction' section title for Game Page")
    def get_instructions_title(self):
        return ElementFinder.find_element_from_element(self.instructions, 'h2').text.replace('\t', '').\
            replace('\n', '').strip()

    @allure.step("Get 'Top Picks' section title for Game Page")
    def get_top_picks_title(self):
        return ElementFinder.find_element_from_element(self.top_picks_section, 'h2:first-child > span').text

    @allure.step("Get 'Top Picks' section for Game Page")
    def get_top_picks_section_visible_games(self):
        elements = ElementFinder.find_element_from_element(self.top_picks_section, 'div.views-field', multiple=True)
        visible_games = [game for game in elements if game.is_displayed()]
        return visible_games

    @allure.step("Get 'AZ Games' section link for Game Page")
    def get_az_games_link(self):
        element = ElementFinder.find_element_from_element(self.az_game_list, 'a')
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Get 'Aiming Games' title for Game Page")
    def get_aiming_games_title(self):
        return ElementActions.get_text(self.driver, GamePageLocators.AIMING_GAMES)

    @allure.step("Get 'AZ Games' section games for Game Page")
    def get_az_games_list(self):
        elements = ElementFinder.find_element_from_element(self.az_game_list, '.node-game a', multiple=True)
        game_list = [game for game in elements if game.is_displayed()]
        return game_list

    @allure.step("Click like button for Game Page")
    def click_like_button(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.LIKE_BUTTON)

    @allure.step("Get like button color for Game Page")
    def get_like_button_color(self):
        return ElementActions.get_attribute(self.driver, GamePageLocators.LIKE_BUTTON, 'src')

    @allure.step("Get 'Like This Section?' for Game Page")
    def get_like_this_game_text(self):
        return ElementActions.get_text(self.driver, GamePageLocators.LIKE_THIS_GAME).lower()

    @allure.step("Get games and game nodes info for Game Page")
    def get_games_data_and_nodes(self):
        games = requests.get(url=GAMES_DATA_URL).json()
        nodes = requests.get(url=GAME_NODE_JSON_URL).json()

        games_data = {game['title']: game['id'] for game in games}
        nodes_data = {node['nid']: node['likes'] for node in nodes}
        return games_data, nodes_data

    @allure.step("Click on '{1}' filter for All Games Page")
    def click_on_filter(self, filter_):
        element = getattr(GamePageLocators, filter_.upper())
        url = ElementActions.get_attribute(self.driver, element, 'href')
        self.get(url)

    @allure.step("Get all games for Game Page")
    def get_games_url(self):
        games = {}
        elements = ElementFinder.find_element_from_element(self.game_urls, ' .views-row > span:nth-child(1) > a',
                                                           multiple=True)
        for element in elements:
            game_name = element.text
            url = ElementActions.get_attribute_from_element(element, 'href')
            games[game_name] = url
        return games

    @allure.step("Get 'Thanks for voting!' message for Game Page")
    def get_like_message(self):
        return ElementActions.get_text(self.driver, GamePageLocators.LIKE_MESSAGE).replace('\t', ''). \
            replace('\n', '').strip().lower()
