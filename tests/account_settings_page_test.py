import os
from unittest import TestCase
import allure
import pytest
from pages.account_settings_page import AccountSettingsPage
from constants.general_constants import RUN_MODE, RunModes
from action_wrapper.element_finder import ElementFinder
from constants.locators.account_settings_locators import AccountSettingsLocators


@allure.feature("Account Settings Page")
@allure.story("Account Settings Page")
@pytest.mark.usefixtures("get_driver")
class TestAccountSettingsPage(TestCase):

    def setUp(self):
        self.account_settings_page: AccountSettingsPage = AccountSettingsPage(self.driver)
        self.account_settings_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify the structure of Account Settings Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_account_settings_page_structure(self):
        # AS-1
        self.account_settings_page.enter_valid_username_and_password()
        self.account_settings_page.click_on_login_button()

        self.assertEqual(self.account_settings_page.get_account_settings_title(),
                         self.account_settings_page.static_texts("as_exp_title"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("as_exp_title"),
                                self.account_settings_page.get_account_settings_title()))

        self.assertEqual(self.account_settings_page.get_login_id_title(),
                         self.account_settings_page.static_texts("login_exp_title"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("login_exp_title"),
                                self.account_settings_page.get_login_id_title()))

        self.assertEqual(self.account_settings_page.get_login_id_des(),
                         self.account_settings_page.static_texts("login_exp_des"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("login_exp_des"),
                                self.account_settings_page.get_login_id_des()))

        self.assertTrue(self.account_settings_page.users_login_id.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('users_login_id'))
        self.assertTrue(self.account_settings_page.change_button_login_id.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('change_button_login_id'))

        self.assertEqual(self.account_settings_page.get_password_title(),
                         self.account_settings_page.static_texts("pass_exp_title"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("pass_exp_title"),
                                self.account_settings_page.get_password_title()))

        self.assertTrue(self.account_settings_page.masked_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('masked_password'))
        self.assertTrue(self.account_settings_page.password_change_button.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('password_change_button'))

        self.assertEqual(self.account_settings_page.get_want_people_to_follow_title(),
                         self.account_settings_page.static_texts("want_people_exp_title"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.get_want_people_to_follow_title(),
                                self.account_settings_page.static_texts("want_people_exp_title")))

        self.assertEqual(self.account_settings_page.get_want_people_to_follow_des(),
                         self.account_settings_page.static_texts("want_people_exp_des"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("want_people_exp_des"),
                                self.account_settings_page.get_want_people_to_follow_des()))

        self.assertTrue(self.account_settings_page.learn_more_link.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('learn_more_link'))

        self.assertEqual(self.account_settings_page.get_first_radio_button_text(),
                         self.account_settings_page.static_texts("first_radiobutton_exp_text"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("first_radiobutton_exp_text"),
                                self.account_settings_page.get_first_radio_button_text()))

        self.assertEqual(self.account_settings_page.get_second_radio_button_text(),
                         self.account_settings_page.static_texts("second_radiobutton_exp_text"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("second_radiobutton_exp_text"),
                                self.account_settings_page.get_second_radio_button_text()))

        self.assertTrue(self.account_settings_page.save_radiobuttons.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('save_radiobuttons'))

        self.assertEqual(self.account_settings_page.get_keep_me_logged_in_title(),
                         self.account_settings_page.static_texts("keep_me_logged_exp_title"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("keep_me_logged_exp_title"),
                                self.account_settings_page.get_keep_me_logged_in_title()))

        self.assertTrue(self.account_settings_page.keep_loggedin_checkmark.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('keep_loggedin_checkmark'))

        self.assertEqual(self.account_settings_page.get_keep_me_logged_checkmark_text(),
                         self.account_settings_page.static_texts("keep_logged_checkmark_exp_text"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("keep_logged_checkmark_exp_text"),
                                self.account_settings_page.get_keep_me_logged_checkmark_text()))

        self.assertTrue(self.account_settings_page.save_button_keep_me_logged_in.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].
                        format('save_button_keep_me_logged_in'))

        self.assertEqual(self.account_settings_page.get_change_appearance_text(),
                         self.account_settings_page.static_texts("change_appearance_exp_text"),
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(self.account_settings_page.static_texts("change_appearance_exp_text"),
                                self.account_settings_page.get_change_appearance_text()))

        self.assertTrue(self.account_settings_page.customize_my_page_link.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('customize_my_page_link'))

    @allure.testcase('2')
    @allure.title('Verify the functionality of "Change" button in LOGIN ID section')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_change_button_functionality(self):
        # AS-3
        self.account_settings_page.click_on_login_section_change_button()
        self.assertTrue(self.account_settings_page.save_button_for_login_id.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('save_button_for_login_id'))
        self.assertTrue(self.account_settings_page.cancel_button_for_login_id.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('cancel_button_for_login_id'))
        self.account_settings_page.click_on_login_section_cancel_button()

    @allure.testcase('3')
    @allure.title('Verify clicking on Cancel button closes the field in LOGIN ID  section')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_login_section_cancel_button_functionality(self):
        # AS-4
        login_id_before = self.account_settings_page.get_user_login_id()
        self.account_settings_page.click_on_login_section_change_button()
        self.account_settings_page.change_user_login_id()
        self.account_settings_page.click_on_login_section_cancel_button()

        login_id_after = self.account_settings_page.get_user_login_id()
        self.assertEqual(login_id_after, login_id_before,
                         msg=self.account_settings_page.exceptions['is_not'].format(login_id_before, login_id_after))

    @allure.testcase('4')
    @allure.title('Verify Save button saves the user changes in LOGIN ID  section')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_login_section_save_button_functionality(self):
        # AS-5
        login_id_before_change = self.account_settings_page.get_user_login_id()
        try:
            self.account_settings_page.click_on_login_section_change_button()
            changed_login_id = self.account_settings_page.change_user_login_id()
            self.account_settings_page.click_on_login_section_save_button()
            login_id_after_change = self.account_settings_page.get_user_login_id()
            self.assertEqual(login_id_after_change, changed_login_id,
                             msg=self.account_settings_page.exceptions['is_not'].
                             format(changed_login_id, login_id_after_change))
        finally:
            self.account_settings_page.click_on_login_section_change_button()
            self.account_settings_page.clear_user_login_id()
            self.account_settings_page.change_user_login_id(login_id_before_change)
            self.account_settings_page.click_on_login_section_save_button()

    @allure.testcase('5')
    @allure.title('Verify an error displays when user tries to change its private username with exising one')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_error_displays_trying_enter_existing_one(self):
        # AS-6
        expected_error_message = "Sorry, please enter a different login id"
        self.account_settings_page.click_on_login_section_change_button()
        self.account_settings_page.change_user_login_id("test")
        self.account_settings_page.click_on_login_section_save_button()

        self.assertEqual(self.account_settings_page.get_error_msg_text(), expected_error_message,
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(expected_error_message, self.account_settings_page.get_error_msg_text()))
        self.account_settings_page.click_on_login_section_cancel_button()

    @allure.testcase('6')
    @allure.title('Verify the functionality of "Password" section for non subscribed user')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_password_section_structure(self):
        # AS-7
        self.account_settings_page.click_on_password_section_change_button()
        self.assertTrue(self.account_settings_page.current_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('current_password'))
        self.assertTrue(self.account_settings_page.new_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('new_password'))
        self.assertTrue(self.account_settings_page.confirm_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('confirm_password'))
        self.assertTrue(self.account_settings_page.save_button_for_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('save_button_for_password'))
        self.assertTrue(self.account_settings_page.cancel_button_for_passwords.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format(
                            'cancel_button_for_passwords'))
        self.account_settings_page.click_on_password_section_cancel_button()

    @allure.testcase('7')
    @allure.title('Verify Cancel button functionality in Password field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_password_cancel_button_functionality(self):
        # AS-8
        self.account_settings_page.click_on_password_section_change_button()
        self.account_settings_page.click_on_password_section_cancel_button()
        self.assertTrue(self.account_settings_page.masked_password.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('masked_password'))
        self.assertTrue(self.account_settings_page.password_change_button.is_displayed(),
                        msg=self.account_settings_page.exceptions['not_displayed'].format('password_change_button'))

    @allure.testcase('8')
    @allure.title('Verify an error displays if passwords in New and Confirm fields do not match ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_new_and_confirm_fields_do_not_match(self):
        # AS-9
        expected_password_error_msg = "Sorry, those passwords do not match"
        self.account_settings_page.click_on_password_section_change_button()
        self.account_settings_page.put_current_password()
        self.account_settings_page.put_new_password()
        self.account_settings_page.put_confirm_password("asdsfsdfe4521")
        self.account_settings_page.click_on_password_section_save_button()
        current_password_error_message = self.account_settings_page.get_password_error_msg_text()
        self.assertEqual(current_password_error_message, expected_password_error_msg,
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(expected_password_error_msg, expected_password_error_msg))
        self.account_settings_page.click_on_password_section_cancel_button()

    @allure.testcase('9')
    @allure.title('Verify an error displays if the new passwords do not match the requirements ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_new_password_do_not_match_requirements(self):
        # AS-10
        expected_error_message = "Please enter a new password at least 5 characters long."
        self.account_settings_page.click_on_password_section_change_button()
        self.account_settings_page.put_current_password()
        self.account_settings_page.put_new_password("1")
        self.account_settings_page.put_confirm_password("1")
        self.account_settings_page.click_on_password_section_save_button()

        current_error_message = self.account_settings_page.get_password_do_not_match_req_text()
        self.assertEqual(current_error_message, expected_error_message,
                         msg=self.account_settings_page.exceptions['is_not'].
                         format(expected_error_message, current_error_message))
        self.account_settings_page.click_on_password_section_cancel_button()

    @allure.testcase('10')
    @allure.title('Verify the functionality when "Sure, other players on Coolmath Games can follow me" is selected ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_following_section_functionality_when_selected_first_option(self):
        # AS-11
        self.account_settings_page.click_on_first_radiobutton()
        self.account_settings_page.click_on_following_section_save_button()
        first_username = self.account_settings_page.get_username_from_header()
        self.account_settings_page.logout()
        self.account_settings_page.get(f'{self.account_settings_page.main_url()}/login')
        self.account_settings_page.enter_valid_username_and_password(user=2)
        self.account_settings_page.click_on_login_button()
        self.account_settings_page.get(f'{self.account_settings_page.main_url()}/profile/{first_username}')
        try:
            self.assertTrue(self.account_settings_page.follow_button.is_displayed(),
                            msg=self.account_settings_page.exceptions['not_displayed'].format('follow_button'))
        finally:
            self.account_settings_page.logout()
            self.account_settings_page.get(f'{self.account_settings_page.main_url()}/login')
            self.account_settings_page.enter_valid_username_and_password()
            self.account_settings_page.click_on_login_button()
            self.account_settings_page.get()

    @allure.testcase('11')
    @allure.title('Verify the functionality when "Nope, don’t let anyone on Coolmath Games follow me" is selected')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_following_section_functionality_when_selected_second_option(self):
        # AS-12
        self.account_settings_page.click_on_second_radiobutton()
        self.account_settings_page.click_on_following_section_save_button()
        first_username = self.account_settings_page.get_username_from_header()
        self.account_settings_page.logout()
        self.account_settings_page.get(f'{self.account_settings_page.main_url()}/login')
        self.account_settings_page.enter_valid_username_and_password(user=2)
        self.account_settings_page.click_on_login_button()
        self.account_settings_page.get(f'{self.account_settings_page.main_url()}/profile/{first_username}')
        try:
            self.assertFalse(ElementFinder.get_element_existence(self.account_settings_page.driver,
                                                                 AccountSettingsLocators.FOLLOW_BUTTON),
                             msg="Follow button displayed when "
                                 "'Nope, don’t let anyone on Coolmath Games follow me' is selected")
        finally:
            self.account_settings_page.logout()
            self.account_settings_page.get(f'{self.account_settings_page.main_url()}/login')
            self.account_settings_page.enter_valid_username_and_password()
            self.account_settings_page.click_on_login_button()
            self.account_settings_page.get()

    @allure.testcase('12')
    @allure.title('Verify the functionality of  "Customize My Page" section/link  ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.account_settings
    @pytest.mark.web
    @pytest.mark.mobile
    def test_customize_my_page_link_functionality(self):
        # AS-15
        self.account_settings_page  .click_on_customize_my_page_link()

        expected_url = f'{self.account_settings_page.main_url()}/profile' \
                       f'/{self.account_settings_page.get_username_from_header().lower()}/edit'
        current_url = self.account_settings_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.account_settings_page.exceptions['object_comparing'].
                         format(expected_url, current_url, 'urls'))
