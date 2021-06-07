import allure
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.global_header_navigation_locators import GlobalHeaderNavigationLocators
from pages.base_page import BasePage


class GlobalHeaderNavigationPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def is_loaded(self):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, GlobalHeaderNavigationLocators.LOGIN_BUTTON)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'login_form': GlobalHeaderNavigationLocators.LOGIN_FORM,
            'sign_up_form': GlobalHeaderNavigationLocators.SIGN_UP_FORM,
            'avatar': GlobalHeaderNavigationLocators.AVATAR,
            'username': GlobalHeaderNavigationLocators.USERNAME,
            'progress_bar': GlobalHeaderNavigationLocators.PROGRESS_BAR,
            'log_out': GlobalHeaderNavigationLocators.LOG_OUT,
            'ad_popup_button': GlobalHeaderNavigationLocators.CLOSE_AD_POPUP
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on login button for Home Page")
    def click_on_login_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.LOGIN_BUTTON)

    @allure.step("Click on sign up button for Home Page")
    def click_on_sign_up_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.SIGN_UP_BUTTON)

    @allure.step("Enter username and password for Home Page")
    def enter_username_and_password(self):
        ElementActions.put_text(self.driver, GlobalHeaderNavigationLocators.NICKNAME, 'testrafik')
        ElementActions.put_text(self.driver, GlobalHeaderNavigationLocators.PASSWORD, 'testrafik')
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.SUBMIT_BUTTON)

    @allure.step("Click on user profile button for Home Page")
    def click_on_user_profile_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.USER_PROFILE)

    @allure.step("Get profile link for Home Page")
    def get_user_profile_link(self):
        element = ElementFinder.find_element_by_css_selector(self.username, 'a:first-child')
        return ElementActions.get_attribute_from_element(element, 'href')

    @allure.step("Get user profile nickname for Home Page")
    def get_nickname(self):
        return ElementFinder.find_element_by_css_selector(self.username, 'a').text.lower()

    @allure.step("Close ad popup for Home Page")
    def close_ad_popup_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.CLOSE_AD_POPUP)

    @allure.step("Click on log out button for Home Page")
    def click_on_log_out_button(self):
        ElementActions.click_on_element(self.driver, GlobalHeaderNavigationLocators.LOG_OUT)
        WaitActions.wait_until_url_contains(self.driver, self.main_url())
        sleep(2)
