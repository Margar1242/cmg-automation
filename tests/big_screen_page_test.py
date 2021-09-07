import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, TYPE, RunModes, Types
from pages.big_screen_page import BigScreenPage


@allure.feature("Big Screen")
@allure.story("Big Screen")
@pytest.mark.usefixtures("get_driver")
class TestBigScreenPage(TestCase):

    def setUp(self):
        self.game_page: BigScreenPage = BigScreenPage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        self.driver.delete_all_cookies()
        self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify big screen button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_big_screen_button(self):
        # BS-1
        self.game_page.click_on_continue_button()
        self.assertTrue(self.game_page.big_screen_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('big screen Button'))

    @allure.testcase('2')
    @allure.title('Verify big screen button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_big_screen_and_progress_bar(self):
        # BS-2
        self.game_page.click_on_continue_button()
        progress_bar, big_screen = self.game_page.get_container_elements()
        self.assertEqual(self.game_page.progress_bar.location, progress_bar.location,
                         msg=self.game_page.exceptions['is_not'].format('First element', 'Progress Bar'))
        self.assertEqual(self.game_page.big_screen_button.location, big_screen.location,
                         msg=self.game_page.exceptions['is_not'].format('Second element', 'Big Screen Button'))

    @allure.testcase('3')
    @allure.title('Verify big screen popup content for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_big_screen_popup(self):
        # BS-3
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        expected_popup_text = 'To Play This Game in Big Screen Mode'
        current_popup_text = self.game_page.get_big_screen_popup_text()
        self.assertEqual(expected_popup_text, current_popup_text,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_popup_text,
                                                                                  current_popup_text, 'texts'))

        self.assertTrue(self.game_page.X.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Popup X button'))

        self.assertTrue(self.game_page.sponsored_video_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('View a Sponsored Video Button'))

        expected_or_text = 'OR'
        current_or_text = self.game_page.get_popup_or_text()
        self.assertEqual(expected_or_text, current_or_text,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_or_text, current_or_text,
                                                                                  'texts'))

        self.assertTrue(self.game_page.premium_access_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Pay For Premium Access Button'))

        self.assertTrue(self.game_page.return_to_regular_mode.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].
                        format('No thanks, return to regular mode button'))

    @allure.testcase('5')
    @allure.title('Verify "X" button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_X_button(self):
        # BS-6
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        self.game_page.click_on_x_button()
        self.assertFalse(self.game_page.get_popup_big_screen_popup(),
                         msg=self.game_page.exceptions['is_not'].format('Big screen popup',
                                                                        'closed after click on X'))

    @allure.testcase('6')
    @allure.title('Verify "return to regular mode" button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_return_to_regular_mode_button(self):
        # BS-7
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        self.game_page.click_on_regular_mode_button()
        self.assertFalse(self.game_page.get_popup_big_screen_popup(),
                         msg=self.game_page.exceptions['is_not'].format('Big screen popup',
                                                                        'closed after click on "return to '
                                                                        'regular mode button"'))

    @allure.testcase('7')
    @allure.title('Verify "View a Sponsored Video" button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_view_sponsored_video_button(self):
        # BS-8
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        self.game_page.click_sponsored_video_button()

        self.assertTrue(self.game_page.play_big_screen_now_button,
                        msg=self.game_page.exceptions['not_displayed'].format('"Play Big Screen Now" button'))

    @allure.testcase('8')
    @allure.title('Verify "Play Big Screen Now" button for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_play_big_screen_now_button(self):
        # BS-9
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        self.game_page.click_sponsored_video_button()
        self.game_page.click_play_big_screen_now_button()

        self.assertTrue(self.game_page.get_full_screen_window(),
                        msg=self.game_page.exceptions['is_not'].format('Game', 'in full screen mode'))

    @allure.testcase('9')
    @allure.title('Verify "Big Screen" button for premium user for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_big_screen_button_for_premium_user(self):
        # BS-10
        self.game_page.enter_premium_username_password()
        try:
            self.assertTrue(self.game_page.big_screen_button.is_displayed(),
                            msg=self.game_page.exceptions['not_displayed'].format('Big Screen button for premium user'))
        finally:
            self.game_page.click_on_logout_button()

    @allure.testcase('10')
    @allure.title('Verify "Exit Big Screen" button  for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_exit_big_screen_button(self):
        # BS-11
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()
        self.game_page.click_sponsored_video_button()
        self.game_page.click_play_big_screen_now_button()
        self.game_page.click_on_exit_big_screen_button()

        self.assertFalse(self.game_page.get_full_screen_window(),
                         msg=self.game_page.exceptions['is_not'].format('Game', 'in normal screen mode'))

    @allure.testcase('11')
    @allure.title('Verify "Pay for Premium Access" functionality for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_premium_access_membership(self):
        # BS-12
        try:
            self.game_page.click_on_continue_button()
            self.game_page.click_on_big_screen_button()
            self.game_page.click_on_pay_for_premium_access_button()
            self.game_page.fill_premium_membership_fields()

            expected_text = 'YOU NOW HAVE PREMIUM ACCESS!'
            current_text = self.game_page.get_premium_access_message()

            self.assertEqual(expected_text, current_text,
                             msg=self.game_page.exceptions['object_comparing'].format(expected_text, current_text, 'texts'))
        finally:
            self.driver.switch_to.default_content()

    @allure.testcase('12')
    @allure.title('Verify premium modal window for Big Screen Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.big_screen
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Mobile not automated')
    def test_premium_modal_window(self):
        # BS-4
        self.game_page.click_on_continue_button()
        self.game_page.click_on_big_screen_button()

        self.assertTrue(self.game_page.big_screen_popup.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format("Premium modal window"))
