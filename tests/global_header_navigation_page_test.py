import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.global_header_navigation_page import GlobalHeaderNavigationPage


@allure.feature("Global Header Navigation Page")
@allure.story("Global Header Navigation Page")
@pytest.mark.usefixtures("get_driver")
class TestGlobalHeaderNavigationPage(TestCase):

    def setUp(self):
        self.global_header_navigation_page: GlobalHeaderNavigationPage = GlobalHeaderNavigationPage(self.driver)
        self.global_header_navigation_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify login button functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    @pytest.mark.demo
    def test_home_page_login_button(self):
        # GH-1
        self.global_header_navigation_page.click_on_login_button()
        self.assertTrue(self.global_header_navigation_page.login_form.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('Login form'))

    @allure.testcase('2')
    @allure.title('Verify signup button functionality')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    @pytest.mark.demo
    def test_home_page_sign_up_button(self):
        # GH-2
        self.global_header_navigation_page.click_on_sign_up_button()
        self.assertTrue(self.global_header_navigation_page.sign_up_form.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('Sign Up form'))

    @allure.testcase('3')
    @allure.title('Verify user profile')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.global_header_navigation
    def test_home_page_userprofile(self):
        # GH-3
        self.global_header_navigation_page.click_on_login_button()
        self.global_header_navigation_page.enter_username_and_password()
        self.assertTrue(self.global_header_navigation_page.avatar.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('Avatar'))
        self.assertTrue(self.global_header_navigation_page.username.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('Username'))
        self.assertTrue(self.global_header_navigation_page.progress_bar.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('Progress bar'))
        self.assertTrue(self.global_header_navigation_page.log_out.is_displayed(),
                        msg=self.global_header_navigation_page.exceptions['not_displayed'].format('User profile'))

        # GH-4
        self.global_header_navigation_page.click_on_user_profile_button()
        nickname = self.global_header_navigation_page.get_nickname()
        url_tail = f'/profile/{nickname}'
        user_profile_url = self.global_header_navigation_page.current_url()
        self.assertIn(url_tail, user_profile_url,
                      msg=self.global_header_navigation_page.exceptions['object_comparing'].format(url_tail,
                                                                                                   user_profile_url,
                                                                                                   'urls'))

        # GH-5
        self.global_header_navigation_page.close_ad_popup_button()
        self.global_header_navigation_page.click_on_log_out_button()
        current_url = self.global_header_navigation_page.current_url()
        correct_url = self.global_header_navigation_page.correct_url()
        self.assertEqual(current_url, correct_url,
                         msg=self.global_header_navigation_page.exceptions['object_comparing'].format(current_url,
                                                                                                      correct_url,
                                                                                                      'urls'))
