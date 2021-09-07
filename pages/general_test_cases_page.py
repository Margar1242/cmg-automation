import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.general_test_case_locators import GeneralTestCaseLocators
from pages.base_page import BasePage


class GeneralTestCasePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = '0-connection'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, GeneralTestCaseLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'ad_container': GeneralTestCaseLocators.AD_CONTAINER
        }
        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on play button for General Test Cases Page")
    def click_on_play_button(self):
        query = "document.getElementsByClassName('icon-circle')[0].click()"
        self.driver.execute_script(query)
