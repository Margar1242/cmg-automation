import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.category_page_locators import CategoryPageLocators
from pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, CategoryPageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'strategy': CategoryPageLocators.STRATEGY,
            'skill': CategoryPageLocators.SKILL,
            'numbers': CategoryPageLocators.NUMBERS,
            'logic': CategoryPageLocators.LOGIC,
            'trivia': CategoryPageLocators.TRIVIA,
            'more': CategoryPageLocators.MORE,
            'playlists': CategoryPageLocators.PLAYLISTS,
            'random': CategoryPageLocators.RANDOM,
            'daily_games': CategoryPageLocators.DAILY_GAMES,
            'also_like_section': CategoryPageLocators.ALSO_LIKE_SECTION,
            'top_ad': CategoryPageLocators.TOP_AD,
            'right_ad_1': CategoryPageLocators.RIGHT_AD_1,
            'right_ad_2': CategoryPageLocators.RIGHT_AD_2,
            'right_ad_3': CategoryPageLocators.RIGHT_AD_3,
            'right_ad_4': CategoryPageLocators.RIGHT_AD_4,
            'right_ad_5': CategoryPageLocators.RIGHT_AD_5,
            'mobile_ad_1': CategoryPageLocators.MOBILE_AD_1,
            'mobile_ad_2': CategoryPageLocators.MOBILE_AD_2,
            'mobile_ad_3': CategoryPageLocators.MOBILE_AD_3,
        }

        return ElementFinder.find_element(self.driver, mapper[item], timeout=60)

    @allure.step("Get category link for Category Page")
    def get_category_link(self, element):
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Click on category in Category Page")
    def click_on_category(self, locator_name):
        if self.is_mobile:
            self.click_on_toggle()
        if locator_name == "RANDOM":
            ElementActions.click_on_element(self.driver, getattr(CategoryPageLocators, locator_name))
        else:
            url = ElementActions.get_attribute(self.driver, getattr(CategoryPageLocators, locator_name), 'href')
            self.get(url)

    @allure.step("Wait until also like section is visible for Category Page")
    def get_also_like_section(self):
        WaitActions.wait_until_element_is_visible(self.driver, CategoryPageLocators.ALSO_LIKE_SECTION)

    @allure.step("Click on MORE dropdown category for Category Page")
    def click_on_more_category(self, category):
        if self.is_mobile:
            self.click_on_toggle()
            ElementActions.click_on_element(self.driver, CategoryPageLocators.MORE)
        element = ElementFinder.find_element_from_element(self.more, f'.expandable-wrapper .menu .{category}')
        url = ElementActions.get_attribute_from_element(element, 'href')
        self.get(url)

    @allure.step("Click on toggle for Category Page")
    def click_on_toggle(self):
        ElementActions.click_on_element(self.driver, CategoryPageLocators.TOGGLE)
