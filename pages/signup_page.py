import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.color import Color
from random import choice, randint

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.signup_page_locators import SignupPageLocator
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = 'signup'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, SignupPageLocator.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'login_id': SignupPageLocator.LOGIN_ID,
            'password': SignupPageLocator.PASSWORD,
            'confirm_password': SignupPageLocator.CONFIRM_PASSWORD,
            'avatar_section': SignupPageLocator.AVATAR_SECTION,
            'themes': SignupPageLocator.THEMES,
            'star_icon': SignupPageLocator.STAR_ICON,
            'nickname_section': SignupPageLocator.NICKNAME_SECTION,
            'suggested_username': SignupPageLocator.SUGGESTED_USERNAME,
            'new_nickname_button': SignupPageLocator.NEW_NICKNAME_BUTTON,
            'create_custom_nickname': SignupPageLocator.CREATE_CUSTOM_NICKNAME,
            'signup_button': SignupPageLocator.SIGNUP_BUTTON,
            'premium_avatar_popup': SignupPageLocator.PREMIUM_AVATAR_POPUP
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get 'Create free account' section title for Signup Page")
    def get_free_account_title(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.CREATE_FREE_ACCOUNT_TITLE).replace("\n", "").replace("\t", "").strip()

    @allure.step("Get 'Create free account' section text for Signup Page")
    def get_free_account_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.WELCOME)

    @allure.step("Get 'Create free account' section text for Signup Page")
    def get_already_have_account_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.ALREADY_HAVE_ACCOUNT)

    @allure.step("Get 'Log In' button link for Signup Page")
    def get_login_button_link(self):
        return ElementActions.get_attribute(self.driver, SignupPageLocator.LOGIN_BUTTON, 'href')

    @allure.step("Get 'Your Login Info' title for Signup Page")
    def get_login_info_text(self):
        text = ElementActions.get_text(self.driver, SignupPageLocator.LOGIN_INFO).lower()
        text_part = text[text.index('your'):]
        return text_part.upper()

    @allure.step("Get 'Login ID' input description text for Signup Page")
    def get_login_id_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.LOGIN_ID_TEXT)

    @allure.step("Get nickname section text for Signup Page")
    def get_nickname_section_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.NICKNAME_TEXT)

    @allure.step("Get nickname section text for Signup Page")
    def get_custom_nickname_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.CREATE_CUSTOM_NICKNAME).upper()

    @allure.step("Get premium membership text for Signup Page")
    def get_premium_membership_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.CUSTOM_NICKNAME_TEXT).replace('\n', '').strip()

    @allure.step("Get 'premium membership text' star icon for Signup Page")
    def get_premium_membership_star(self, selector='#cmg-signup-custom-name-title'):
        return self.driver.execute_script(f"return window.getComputedStyle(document.querySelector"
                                          f"('{selector}'),':before').getPropertyValue"
                                          f"('background-image')")

    @allure.step("Click on random premium avatar for Signup Page")
    def click_on_random_premium_avatars(self):
        ElementActions.click_on_element(self.driver, SignupPageLocator.VIEW_ALL_BUTTON)
        premium_avatars = ElementFinder.find_element_from_element(self.avatar_section, '.premium-avatar-label',
                                                                  multiple=True)
        choice([ElementFinder.find_element_from_element(avatar, 'input') for avatar in premium_avatars if
                avatar.is_displayed()]).click()

    @allure.step("Get premium avatar popup text for Signup Page")
    def get_popup_text(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.PREMIUM_AVATAR_POPUP)

    @allure.step("Enter not valid user id or password for Signup Page")
    def enter_not_valid_params(self, incorrect_password=False):
        password = "123aaa"
        user_id = "aaaaa" if not incorrect_password else "testrafik111"
        self.login_id.clear()
        self.password.clear()
        self.confirm_password.clear()
        ElementActions.put_text(self.driver, SignupPageLocator.LOGIN_ID, user_id)
        ElementActions.put_text(self.driver, SignupPageLocator.PASSWORD, password)
        ElementActions.put_text(self.driver, SignupPageLocator.CONFIRM_PASSWORD, password if not incorrect_password
                                else password[:-1])
        ElementActions.click_on_element(self.driver, SignupPageLocator.SIGNUP_BUTTON)

    @allure.step("Get duplicate id error message for Signup Page")
    def get_duplicate_id_error_message(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.DUPLICATE_ID_ERROR_TEXT)

    @allure.step("Get not matched password and confirm password error message for Signup Page")
    def get_not_matched_password_error_message(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.NOT_MATCHED_PASSWORD)

    @allure.step("Enter user id and password for Signup Page")
    def enter_valid_params(self, username):
        user_id = f"tester{randint(10, 999)}test{randint(1000, 9999)}"
        password = 'qwertY123'
        ElementActions.put_text(self.driver, SignupPageLocator.LOGIN_ID, user_id)
        ElementActions.put_text(self.driver, SignupPageLocator.PASSWORD, password)
        ElementActions.put_text(self.driver, SignupPageLocator.CONFIRM_PASSWORD, password)
        ElementActions.click_on_element(self.driver, SignupPageLocator.SIGNUP_BUTTON)
        if not self.is_mobile:
            if ElementFinder.get_element_existence(self.driver, SignupPageLocator.CLOSE_POPUP, timeout=10):
                ElementActions.click_on_element(self.driver, SignupPageLocator.CLOSE_POPUP)
        WaitActions.wait_until_url_contains(self.driver, f'{self.main_url()}/profile/{username}')

    @allure.step("Get suggested username for Signup Page")
    def get_suggested_username(self):
        return ElementActions.get_text(self.driver, SignupPageLocator.SUGGESTED_USERNAME).lower()

    @allure.step("Logout for Signup Page")
    def logout(self):
        if self.is_mobile:
            self.click_on_toggle()
        ElementActions.click_on_element(self.driver, SignupPageLocator.LOGOUT)
        if self.is_mobile:
            WaitActions.wait_until_element_is_visible(self.driver, SignupPageLocator.MAIN_PAGE_GAMES)
        else:
            WaitActions.wait_until_element_is_visible(self.driver, SignupPageLocator.MAIN_PAGE_LOGIN_BUTTON)

    @allure.step("Get all avatars from avatars section for Signup Page")
    def get_all_images(self, section="avatar", pseudo="after"):
        selector = ".fieldset-wrapper .premium-avatar-label .field-content"
        all_image_selector = "label"
        element = self.avatar_section
        attribute = 'backgroundImage'
        if section == "theme":
            selector = "#themes .premium-theme"
            all_image_selector = "ul li"
            element = self.themes
            attribute = 'content'
        all_images = ElementFinder.find_element_from_element(element, all_image_selector, multiple=True)
        premium = self.driver.execute_script(f'return Array.from(document.querySelectorAll("{selector}")).map('
                                             f'elem=>window.getComputedStyle(elem,":{pseudo}").{attribute})')
        return all_images, premium

    @allure.step("Get premium images border for Signup Page")
    def get_premium_image_border(self, section='avatar'):
        selector = '.premium-avatar-label img'
        section_element = self.avatar_section
        if section == 'theme':
            selector = '.premium-theme'
            section_element = self.themes
        elements = ElementFinder.find_element_from_element(section_element, selector, multiple=True)
        avatar_info = {}
        for element in elements:
            if section == "avatar":
                image_name = ElementActions.get_attribute_from_element(element, 'alt')
            else:
                name_selector = ElementFinder.find_element_from_element(section_element, f'{selector} span')
                image_name = name_selector.text
            style = ElementActions.get_css_property_value_from_element(element=element, css_property='box-shadow')
            rgb = style[style.index('rgb'):style.rfind(')') + 1]
            color = Color.from_string(rgb).hex
            avatar_info[image_name] = color
        return avatar_info

    @allure.step("Click on toggle in Signup Page")
    def click_on_toggle(self):
        ElementActions.click_on_element(self.driver, SignupPageLocator.TOGGLE)

    @allure.step("Click on new nickname button in Signup Page")
    def click_new_nickname_button(self):
        while True:
            if ElementFinder.get_element_existence(self.driver, SignupPageLocator.ALERT_MESSAGE, timeout=5):
                ElementActions.click_on_element(self.driver, SignupPageLocator.NEW_NICKNAME_BUTTON)
                continue
            break
