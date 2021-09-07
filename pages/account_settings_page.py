import os
from constants.general_constants import TYPE, Types
import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from pages.base_page import BasePage
from helpers.helpers import generate_random_string

from constants.locators.account_settings_locators import AccountSettingsLocators
from constants.locators.account_settings_locators import AccountSettingsPageStaticTexts


class AccountSettingsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = 'profile/account-settings'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, AccountSettingsLocators.ACCOUNT_SETTINGS_TITLE)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            # AS-1
            'account_settings_title': AccountSettingsLocators.ACCOUNT_SETTINGS_TITLE,
            'login_id_title': AccountSettingsLocators.LOGIN_ID_TITLE,
            'login_id_description': AccountSettingsLocators.LOGIN_ID_DESCRIPTION,
            'users_login_id': AccountSettingsLocators.USERS_LOGIN_ID,
            'change_button_login_id': AccountSettingsLocators.CHANGE_BUTTON_LOGIN_ID,
            'password_title': AccountSettingsLocators.PASSWORD_TITLE,
            'masked_password': AccountSettingsLocators.MASKED_PASSWORD,
            'password_change_button': AccountSettingsLocators.CHANGE_BUTTON_PASSWORD,
            'learn_more_link': AccountSettingsLocators.LEARN_MORE_LINK,
            'save_radiobuttons': AccountSettingsLocators.SAVE_BUTTON_FOR_RADIOBUTTONS,
            'keep_loggedin_checkmark': AccountSettingsLocators.KEEPMELOGGEDIN_CHECKMARK,
            'save_button_keep_me_logged_in': AccountSettingsLocators.SAVE_BUTTON_FOR_KEEPMELOGGEDIN,
            'customize_my_page_link': AccountSettingsLocators.CUSTOMIZE_MY_PAGE_LINK,
            # AS-3
            'user_login_id': AccountSettingsLocators.USERS_LOGIN_ID,
            'save_button_for_login_id': AccountSettingsLocators.SAVE_BUTTON_FOR_LOGIN_ID,
            'cancel_button_for_login_id': AccountSettingsLocators.CANCEL_BUTTON_FOR_LOGIN_ID,
            # AS-7
            'current_password': AccountSettingsLocators.CURRENT_PASSWORD_FIELD,
            'new_password': AccountSettingsLocators.NEW_PASSWORD_FIELD,
            'confirm_password': AccountSettingsLocators.CONFIRM_PASSWORD_FIELD,
            'save_button_for_password': AccountSettingsLocators.SAVE_BUTTON_FOR_PASSWORD,
            'cancel_button_for_passwords': AccountSettingsLocators.CANCEL_BUTTON_FOR_PASSWORD,
            'username': AccountSettingsLocators.USERNAME,
            'follow_button': AccountSettingsLocators.FOLLOW_BUTTON,
            'login_id_input': AccountSettingsLocators.LOGIN_ID_INPUT
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @staticmethod
    def static_texts(item):
        mapper = {
            # STATIC TEXTS
            'as_exp_title': AccountSettingsPageStaticTexts.ACCOUNT_SETTINGS_EXPECTED_TITLE,
            'login_exp_title': AccountSettingsPageStaticTexts.LOGIN_ID_EXPECTED_TITLE,
            'login_exp_des': AccountSettingsPageStaticTexts.LOGIN_ID_EXPECTED_DESCRIPTION,
            'pass_exp_title': AccountSettingsPageStaticTexts.PASSWORD_EXPECTED_TITLE,
            'want_people_exp_title': AccountSettingsPageStaticTexts.WANT_PEOPLE_EXPECTED_TITLE,
            'want_people_exp_des': AccountSettingsPageStaticTexts.WANT_PEOPLE_EXPECTED_DESCRIPTION,
            'first_radiobutton_exp_text': AccountSettingsPageStaticTexts.FIRST_RADIOBUTTON_EXPECTED_TEXT,
            'second_radiobutton_exp_text': AccountSettingsPageStaticTexts.SECOND_RADIOBUTTON_EXPECTED_TEXT,
            'keep_me_logged_exp_title': AccountSettingsPageStaticTexts.KEEP_ME_LOGGED_IN_EXPECTED_TITLE,
            'keep_logged_checkmark_exp_text': AccountSettingsPageStaticTexts.KEEP_ME_LOGGED_CHECKMARK_EXPECTED_TEXT,
            'change_appearance_exp_text': AccountSettingsPageStaticTexts.CHANGE_APPEARANCE_TEXT,
            'changed_login_id': AccountSettingsPageStaticTexts.CHANGED_LOGIN_ID,
        }

        return mapper[item]

    @allure.step("Get Account Settings title")
    def get_account_settings_title(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.ACCOUNT_SETTINGS_TITLE)[:16]

    @allure.step("Get Login ID title")
    def get_login_id_title(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.LOGIN_ID_TITLE)

    @allure.step("Get Login ID description")
    def get_login_id_des(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.LOGIN_ID_DESCRIPTION)

    @allure.step("Get Users Login ID")
    def get_user_login_id(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.USERS_LOGIN_ID)

    @allure.step("Get Password title")
    def get_password_title(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.PASSWORD_TITLE)

    @allure.step("Get Want people to follow title")
    def get_want_people_to_follow_title(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.WANT_PEOPLE_TO_FOLLOW_TITLE)

    @allure.step("Get Want people to follow description")
    def get_want_people_to_follow_des(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.WANT_PEOPLE_TO_FOLLOW_DESCRIPTION)

    @allure.step("Get First radiobutton text")
    def get_first_radio_button_text(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.FIRST_RADIOBUTTON)

    @allure.step("Get Second radiobutton text")
    def get_second_radio_button_text(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.SECOND_RADIOBUTTON)

    @allure.step("Get Keep me logged in title")
    def get_keep_me_logged_in_title(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.KEEP_ME_LOGGED_IN_TITLE)

    @allure.step("Get Keep me logged in checkmark text")
    def get_keep_me_logged_checkmark_text(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.KEEP_ME_LOGGED_IN_BUTTON_TEXT)

    @allure.step("Get Change appearance text")
    def get_change_appearance_text(self) -> str:
        return ElementActions.get_text(self.driver, AccountSettingsLocators.CHANGE_APPEARANCE_TEXT)

    @allure.step("Click on change button")
    def click_on_login_section_change_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.CHANGE_BUTTON_LOGIN_ID)

    @allure.step("Get current user login id from LOGIN ID section")
    def get_user_login_id_from_input(self):
        return ElementActions.get_text(self.driver, AccountSettingsLocators.CURRENT_LOGIN_ID)

    @allure.step("Change users login id")
    def change_user_login_id(self, change_login=None):
        self.clear_user_login_id()
        login = change_login if change_login else generate_random_string()
        ElementActions.put_text(self.driver, AccountSettingsLocators.LOGIN_ID_INPUT, login)
        return login

    @allure.step("Click on cancel button")
    def click_on_login_section_cancel_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.CANCEL_BUTTON_FOR_LOGIN_ID)

    @allure.step("Click on Save button")
    def click_on_login_section_save_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.SAVE_BUTTON_FOR_LOGIN_ID)

    @allure.step("Clear login id field")
    def clear_user_login_id(self):
        self.login_id_input.clear()

    @allure.step("Get current user login id from LOGIN ID section")
    def get_error_msg_text(self):
        return ElementActions.get_text(self.driver, AccountSettingsLocators.ERROR_MESSAGE_FOR_LOGIN)

    @allure.step("Click on Change button")
    def click_on_password_section_change_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.CHANGE_BUTTON_PASSWORD)

    @allure.step("Click on Cancel button")
    def click_on_password_section_cancel_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.CANCEL_BUTTON_FOR_PASSWORD)

    @allure.step("Fill Current Password field")
    def put_current_password(self):
        ElementActions.put_text(self.driver, AccountSettingsLocators.CURRENT_PASSWORD_FIELD, "currentpass")

    @allure.step("Fill New Password field")
    def put_new_password(self, new_pass=AccountSettingsPageStaticTexts.CHANGED_LOGIN_ID):
        ElementActions.put_text(self.driver, AccountSettingsLocators.NEW_PASSWORD_FIELD, new_pass)

    @allure.step("Fill Confirm Password field")
    def put_confirm_password(self, new_pass=AccountSettingsPageStaticTexts.CHANGED_LOGIN_ID):
        ElementActions.put_text(self.driver, AccountSettingsLocators.CONFIRM_PASSWORD_FIELD, new_pass)

    @allure.step("Get password don't match error message")
    def get_password_error_msg_text(self):
        return ElementActions.get_text(self.driver, AccountSettingsLocators.ERROR_MESSAGE_FOR_PASSWORD)

    @allure.step("Click on Cancel button")
    def click_on_password_section_save_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.SAVE_BUTTON_FOR_PASSWORD)

    @allure.step("Get error message at least 5 character")
    def get_password_do_not_match_req_text(self):
        return ElementActions.get_text(self.driver, AccountSettingsLocators.ERROR_MESSAGE_AT_LEAST_5_CHARACTER)

    @allure.step("Click on Customize my page link")
    def click_on_customize_my_page_link(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.CUSTOMIZE_MY_PAGE_LINK)

    @allure.step("Get username from header")
    def get_username_from_header(self):
        return ElementActions.get_text(self.driver, AccountSettingsLocators.USERNAME_FROM_HEADER).lower()

    @allure.step("Enter valid username and password on Login Page")
    def enter_valid_username_and_password(self, user=1):
        self.username.clear()
        username = getattr(AccountSettingsPageStaticTexts, f'USERNAME_{user}')
        password = getattr(AccountSettingsPageStaticTexts, f'PASSWORD_{user}')
        ElementActions.put_text(self.driver, AccountSettingsLocators.USERNAME, username)
        ElementActions.put_text(self.driver, AccountSettingsLocators.PASSWORD, password)

    @allure.step("Click on Log In button on Login Page")
    def click_on_login_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.SUBMIT_BUTTON)

    @allure.step("Click on Log Out button on Account Settings Page")
    def click_on_logout_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.LOGOUT_BUTTON)

    @allure.step("Click on First radiobutton")
    def click_on_first_radiobutton(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.FIRST_RADIOBUTTON)

    @allure.step("Click on Second radiobutton")
    def click_on_second_radiobutton(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.SECOND_RADIOBUTTON)

    @allure.step("Click on following section save button")
    def click_on_following_section_save_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.SAVE_BUTTON_FOR_RADIOBUTTONS)

    @allure.step("Click on mobile burger button")
    def click_on_mobile_burger_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.MOBILE_BURGER_BUTTON)

    @allure.step("Click on mobile logout button")
    def click_on_mobile_logout_button(self):
        ElementActions.click_on_element(self.driver, AccountSettingsLocators.MOBILE_LOGOUT_BUTTON)

    @allure.step("Logout")
    def logout(self):
        if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}:
            self.click_on_mobile_burger_button()
            self.click_on_mobile_logout_button()
        else:
            self.click_on_logout_button()
