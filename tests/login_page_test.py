import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, TYPE, RunModes, Types
from pages.login_page import LogInPage


@allure.feature("Login Page")
@allure.story("Login Page")
@pytest.mark.usefixtures("get_driver")
class TestLogInPage(TestCase):

    def setUp(self):
        self.login_page: LogInPage = LogInPage(self.driver)
        self.login_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify the structure of Log in Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.mobile
    @pytest.mark.web
    def test_login_page_structure(self):
        # L-1
        expected_title = 'LOG IN'
        current_title = self.login_page.get_log_in_text()
        self.assertEqual(expected_title, current_title,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_title, current_title,
                                                                                   'texts'))

        expected_signup_txt = "Please enter your Login ID or Nickname. (Don’t have an account? Sign Up.)" \
                              "If you’re a Premium Member, you can also use your email address."
        current_signup_txt = self.login_page.get_user_signup_text()
        self.assertEqual(expected_signup_txt, current_signup_txt,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_signup_txt,
                                                                                   current_signup_txt, 'texts'))
        self.assertTrue(self.login_page.get_signup_link(),
                        msg=self.login_page.exceptions['not_displayed'].format('signup link'))

        expected_login_placeholder = 'Your Login ID or Nickname'
        current_login_placeholder = self.login_page.get_login_placeholder()
        self.assertEqual(expected_login_placeholder, current_login_placeholder,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_login_placeholder,
                                                                                   current_login_placeholder, 'texts'))
        expected_pwd_placeholder = 'Password'
        current_pwd_placeholder = self.login_page.get_password_placeholder()
        self.assertEqual(expected_pwd_placeholder, current_pwd_placeholder,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_pwd_placeholder,
                                                                                   current_pwd_placeholder, 'texts'))
        self.assertTrue(self.login_page.get_forgot_password_link(),
                        msg=self.login_page.exceptions['not_displayed'].format('forgot password link'))

        self.assertTrue(self.login_page.submit_button.is_displayed(),
                        msg=self.login_page.exceptions['not_displayed'].format('submit button'))

    @allure.testcase('2')
    @allure.title('Verify the error message for incorrect details')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.mobile
    @pytest.mark.web
    def test_incorrect_login_password(self):
        # L-2
        self.login_page.enter_incorrect_username_and_password()
        self.login_page.click_on_login_button()
        expected_alert = 'Sorry, we don’t have a record of that nickname and/or password.' \
                         ' Free users should enter their Login ID or Nickname,' \
                         ' Premium Users can also enter their email address'
        alert = self.login_page.get_alert()
        self.assertEqual(expected_alert, alert,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_alert,
                                                                                   alert, 'texts'))

    @allure.testcase('3')
    @allure.title('Verify the Forgot password functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.mobile
    @pytest.mark.web
    def test_forgot_password_button(self):
        # L-4
        self.assertTrue(self.login_page.forgot_password.is_displayed(),
                        msg=self.login_page.exceptions['not_displayed'].format('Forgot password button'))

        self.login_page.click_on_forgot_password_link()

        expected_url = f'{self.login_page.correct_url()}/forgot-password'
        current_url = self.login_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

    @allure.testcase('4')
    @allure.title('Verify the user is able to login with a valid credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.mobile
    @pytest.mark.web
    def test_valid_username_password(self):
        # L-3
        self.login_page.enter_valid_username_and_password()
        self.login_page.click_on_login_button(need_wait=True)
        expected_url = self.login_page.main_url()
        current_url = self.login_page.current_url()
        current_url = current_url[:-1] if current_url.endswith('/') else current_url
        self.assertEqual(expected_url, current_url,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

    @allure.testcase('5')
    @allure.title('Verify the functionality of Sign up button')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    @pytest.mark.mobile
    @pytest.mark.web
    def test_signup_button(self):
        # L-5
        self.assertTrue(self.login_page.user_signup.is_displayed(),
                        msg=self.login_page.exceptions['not_displayed'].format('Sign Up button'))
        self.login_page.click_on_signup_link()
        expected_url = f'{self.login_page.main_url()}/signup'
        current_url = self.login_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.login_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))
