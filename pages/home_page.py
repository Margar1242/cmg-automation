import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from time import sleep
from constants.locators.home_page_locators import HomePageLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def is_loaded(self):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.STRATEGY)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'strategy': HomePageLocator.STRATEGY,
            'skill': HomePageLocator.SKILL,
            'numbers': HomePageLocator.NUMBERS,
            'logic': HomePageLocator.LOGIC,
            'trivia': HomePageLocator.TRIVIA,
            'more': HomePageLocator.MORE,
            'playlists': HomePageLocator.PLAYLISTS,
            'random': HomePageLocator.RANDOM,
            'daily_games': HomePageLocator.DAILY_GAMES,
            'top_ten_games_section': HomePageLocator.TOP_TEN_GAMES_SECTION,
            'also_like_section': HomePageLocator.ALSO_LIKE_SECTION,
        }
        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get category link for Home Page")
    def get_category_link(self, element):
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Click on category in Home Page")
    def click_on_category(self, element, random=False):
        url = element.get_attribute('href')
        element.click()
        if not random:
            WaitActions.wait_until_url_contains(self.driver, url)

    @allure.step("Wait until url contain for Home Page")
    def wait_until_url_contain(self, url):
        WaitActions.wait_until_url_contains(self.driver, url)

    @allure.step("Wait until also like section is visible for Home Page")
    def get_also_like_section(self):
        WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.ALSO_LIKE_SECTION)

    @allure.step("Get top ten games for Home Page")
    def get_top_ten_game_links(self):
        elements = ElementFinder.find_elements_by_css_selector(self.top_ten_games_section,
                                                               '.game-item .game-link-wrapper a')[:10]
        game_links = []
        for element in elements:
            game_links.append(ElementActions.get_attribute_from_element(element, 'href'))
        return game_links

    @allure.step("Click on MORE dropdown category for Home Page")
    def click_on_more_category(self, category):
        element = ElementFinder.find_element_by_css_selector(self.more, f'.expandable-wrapper .menu .{category}')
        url = ElementActions.get_attribute_from_element(element, 'href')
        element.click()
        WaitActions.wait_until_url_contains(self.driver, url)
        sleep(1)
