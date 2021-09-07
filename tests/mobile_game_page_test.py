import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import TYPE, Types
from pages.mobile_game_page import MobileGamePage


@allure.feature("Game Page")
@allure.story("Game Page")
@pytest.mark.usefixtures("get_driver")
class TestMobileGamePage(TestCase):

    def setUp(self):
        self.game_page: MobileGamePage = MobileGamePage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        self.driver.delete_all_cookies()
        self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify game content')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_game
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_mobile_game_page_content(self):
        # MG-1
        self.game_page.click_on_play_button()
        self.game_page.click_on_continue_button()
        self.game_page.switch_to_game_iframe()
        self.assertTrue(self.game_page.game_content.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Game content'))

    @allure.testcase('2')
    @allure.title('Verify not supported game')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_game
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_not_supported_game(self):
        # MG-2
        self.game_page.get_not_supported_game_page()
        expected_message = 'Sorry... this game is not playable in your browser.'
        current_message = self.game_page.get_message()
        self.assertEqual(expected_message, current_message,
                         msg=self.game_page.exceptions['object_comparing'].format(f'"{expected_message}"',
                                                                                  f'"{current_message}"', 'text'))

    @allure.testcase('3')
    @allure.title('Verify instruction section buttons')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_game
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_show_more_button(self):
        # MG-3
        self.assertTrue(self.game_page.show_more_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('"Show More" button'))

    @allure.testcase('3')
    @allure.title('Verify instruction section buttons')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_game
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_show_more_button_expanding(self):
        self.game_page.click_on_show_more_button()

        # MG-4
        self.assertTrue(self.game_page.show_less_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('"Show less" button'))

    @allure.testcase('3')
    @allure.title('Verify instruction section buttons')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_game
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_show_less_button(self):
        # MG-5
        self.game_page.click_on_show_more_button()
        self.assertTrue(self.game_page.more_text.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Instruction more text'))
