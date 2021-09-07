import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.home_page_locators import HomePageLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.HEADER_LOCATOR)
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
            'top_ad': HomePageLocator.TOP_AD,
            'right_ad_1': HomePageLocator.RIGHT_AD_1,
            'right_ad_2': HomePageLocator.RIGHT_AD_2,
            'right_ad_3': HomePageLocator.RIGHT_AD_3,
            'right_ad_4': HomePageLocator.RIGHT_AD_4,
            'right_ad_5': HomePageLocator.RIGHT_AD_5,
            'mobile_ad_1': HomePageLocator.MOBILE_AD_1,
            'mobile_ad_2': HomePageLocator.MOBILE_AD_2,
            'mobile_ad_3': HomePageLocator.MOBILE_AD_3,

        }
        return ElementFinder.find_element(self.driver, mapper[item], timeout=60)

    @allure.step("Get category link for Home Page")
    def get_category_link(self, element):
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Click on category in Home Page")
    def click_on_category(self, locator_name):
        if self.is_mobile:
            self.click_on_toggle()
        if locator_name == "RANDOM":
            ElementActions.click_on_element(self.driver, getattr(HomePageLocator, locator_name))
        else:
            url = ElementActions.get_attribute(self.driver, getattr(HomePageLocator, locator_name), 'href')
            self.get(url)

    @allure.step("Wait until also like section is visible for Home Page")
    def get_also_like_section(self):
        WaitActions.wait_until_element_is_visible(self.driver, HomePageLocator.ALSO_LIKE_SECTION)

    @allure.step("Get top ten games for Home Page")
    def get_top_ten_game_links(self):
        elements = ElementFinder.find_element_from_element(self.top_ten_games_section,
                                                           '.game-item .game-link-wrapper a', multiple=True)[:10]
        game_links = []
        for element in elements:
            game_links.append(ElementActions.get_attribute_from_element(element, 'href'))
        return game_links

    @allure.step("Click on MORE dropdown category for Home Page")
    def click_on_more_category(self, category):
        if self.is_mobile:
            self.click_on_toggle()
            ElementActions.click_on_element(self.driver, HomePageLocator.MORE)
        element = ElementFinder.find_element_from_element(self.more, f'.expandable-wrapper .menu .{category}')
        url = ElementActions.get_attribute_from_element(element, 'href')
        self.get(url)

    @allure.step("Click on toggle in Home Page")
    def click_on_toggle(self):
        ElementActions.click_on_element(self.driver, HomePageLocator.TOGGLE)
