import allure
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from random import choice

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.game_page_locators import GamePageLocators
from pages.base_page import BasePage


class GamePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '0-cube-shot'

    def is_loaded(self):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, GamePageLocators.ALSO_LIKE_SECTION)
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
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get timer seconds for Game Page")
    def get_timer_seconds(self):
        return ElementActions.get_text(self.driver, GamePageLocators.TIMER)

    @allure.step("Click continue button for Game Page")
    def click_continue_button(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.CONTINUE_BUTTON)

    @allure.step("Get playlists button for Game Page")
    def click_playlists_button(self, url):
        ElementActions.click_on_element(self.driver, GamePageLocators.PLAYLISTS_BUTTON)
        WaitActions.wait_until_url_contains(self.driver, url)

    @allure.step("Click 'You'll Also Like...' section right arrow for Game Page")
    def click_also_like_section_right_arrow(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.RIGHT_ARROW)
        sleep(1)

    @allure.step("Click 'You'll Also Like...' section left arrow for Game Page")
    def click_also_like_section_left_arrow(self):
        ElementActions.click_on_element(self.driver, GamePageLocators.LEFT_ARROW)
        sleep(1)

    @staticmethod
    def get_expected_visible_after_right_arrow_click_games(games, visible_games_count):
        if visible_games_count > len(games[visible_games_count:]):
            diff = visible_games_count - len(games[visible_games_count:]) - 1
            visible_games_after_arrow_click = games[diff:] + games[visible_games_count - diff + 1]
        else:
            visible_games_after_arrow_click = games[visible_games_count:visible_games_count * 2]
        return [game.get_attribute('href') for game in visible_games_after_arrow_click if game.is_displayed()]

    @staticmethod
    def get_expected_visible_after_left_arrow_click_games(games, visible_games_count):
        if visible_games_count - len(games[visible_games_count:]) < 0:
            diff = visible_games_count - len(games[visible_games_count:])
            visible_games_after_arrow_click = games[:visible_games_count + diff] + games[diff:]
        else:
            visible_games_after_arrow_click = games[:visible_games_count]
        return [game.get_attribute('href') for game in visible_games_after_arrow_click if game.is_displayed()]

    @allure.step("Get 'You'll Also Like...' section games for Game Page")
    def get_also_like_section_game_list(self):
        elements = ElementFinder.find_elements_by_css_selector(self.also_like_section_games, 'li a')
        visible_elements = [game for game in elements if game.is_displayed()]
        return elements, len(visible_elements)

    @allure.step("Get 'You'll Also Like...' section random visible game for Game Page")
    def get_also_like_section_random_game_url(self):
        elements = ElementFinder.find_elements_by_css_selector(self.also_like_section_games, 'a')
        chosen_element = choice([url for url in elements if url.is_displayed()])
        return ElementActions.get_attribute_from_element(chosen_element, 'href'), chosen_element

    @allure.step("Click 'You'll Also Like...' section chosen random visible game for Game Page")
    def click_also_like_section_random_game(self, element, url):
        element.click()
        WaitActions.wait_until_url_contains(self.driver, url)

    @allure.step("Get 'You'll Also Like...' section visible games for Game Page")
    def get_also_like_section_visible_games(self):
        elements = ElementFinder.find_elements_by_css_selector(self.also_like_section_games, 'a')
        visible_games = [game for game in elements if game.is_displayed()]
        return visible_games

    @staticmethod
    def get_elements_by_css_selector(element, css_selector):
        return ElementFinder.find_elements_by_css_selector(element, css_selector)

    @allure.step("Get first game from 'You'll Also Like...' section for Game Page")
    def get_element_by_css_selector(self, element, css_selector):
        return ElementFinder.find_element_by_css_selector(element, css_selector)

    @allure.step("Get Instruction' section text for Game Page")
    def get_instructions_text(self):
        return ElementFinder.find_element_by_css_selector(self.instructions, '.desktop > p').text

    @allure.step("Get 'Instruction' section title for Game Page")
    def get_instructions_title(self):
        return ElementFinder.find_element_by_css_selector(self.instructions, 'h3:first-child').text

    @allure.step("Get 'Top Picks' section title for Game Page")
    def get_top_picks_title(self):
        return ElementFinder.find_element_by_css_selector(self.top_picks_section, 'h2:first-child > span').text

    @allure.step("Get 'Top Picks' section for Game Page")
    def get_top_picks_section_visible_games(self):
        elements = ElementFinder.find_elements_by_css_selector(self.top_picks_section, 'div.views-field')
        visible_games = [game for game in elements if game.is_displayed()]
        return visible_games

    @allure.step("Get 'AZ Games' section link for Game Page")
    def get_az_games_link(self):
        element = ElementFinder.find_element_by_css_selector(self.az_game_list, 'a')
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Get 'Aiming Games' title for Game Page")
    def get_aiming_games_title(self):
        return ElementActions.get_text(self.driver, GamePageLocators.AIMING_GAMES)

    @allure.step("Get 'AZ Games' section games for Game Page")
    def get_az_games_list(self):
        elements = ElementFinder.find_elements_by_css_selector(self.az_game_list, '.node-game a')
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
        return ElementActions.get_text(self.driver, GamePageLocators.LIKE_THIS_GAME)
