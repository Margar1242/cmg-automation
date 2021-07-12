import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, TYPE, RunModes, Types
from pages.mobile_specific_page import MobileSpecificPage


@allure.feature("Mobile Specific Game Page")
@allure.story("Mobile Specific Game Page")
@pytest.mark.usefixtures("get_driver")
class TestGamePage(TestCase):

    def setUp(self):
        self.main_page: MobileSpecificPage = MobileSpecificPage(self.driver)
        self.main_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify drawer menu items')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_specific
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_drawer_menu_items(self):
        # MOB-1
        self.main_page.click_on_toggle()

        self.assertTrue(self.main_page.search_bar.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Search bar'))
        self.assertTrue(self.main_page.az_games.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('All Games A-Z'))
        self.assertTrue(self.main_page.strategy.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Strategy'))
        self.assertTrue(self.main_page.numbers.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Numbers'))
        self.assertTrue(self.main_page.trivia.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Trivia'))
        self.assertTrue(self.main_page.skill.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Skill'))
        self.assertTrue(self.main_page.logic.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Logic'))
        self.assertTrue(self.main_page.playlists.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Playlists'))
        self.assertTrue(self.main_page.daily_games.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Daily games'))
        self.assertTrue(self.main_page.more.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('More'))
        self.assertTrue(self.main_page.signup_button.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Signup button'))
        self.assertTrue(self.main_page.login_button.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Login button'))

        self.main_page.click_on_toggle()

    @allure.testcase('2')
    @allure.title('Verify "More" menu items')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_specific
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_more_menu_items(self):
        # MOB-2
        self.main_page.click_on_toggle()

        expected_text_before_click = 'More'
        current_text_before_click = self.main_page.get_more_button_text()
        self.assertEqual(expected_text_before_click, current_text_before_click,
                         msg=self.main_page.exceptions['object_comparing'].format(expected_text_before_click,
                                                                                  current_text_before_click, 'text'))
        self.main_page.click_on_more_button()

        expected_text_after_click = 'Less'
        current_text_after_click = self.main_page.get_more_button_text()
        self.assertEqual(expected_text_after_click, current_text_after_click,
                         msg=self.main_page.exceptions['object_comparing'].format(expected_text_after_click,
                                                                                  current_text_after_click, 'text'))

        self.assertTrue(self.main_page.classic.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Classic'))
        self.assertTrue(self.main_page.puzzles.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Puzzles'))
        self.assertTrue(self.main_page.geography.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Geography'))
        self.assertTrue(self.main_page.word_games.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Word games'))
        self.assertTrue(self.main_page.memory.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Memory'))
        self.assertTrue(self.main_page.science.is_displayed(),
                        msg=self.main_page.exceptions['not_displayed'].format('Science'))

        self.main_page.click_on_toggle()

    @allure.testcase('3')
    @allure.title('Verify "More" button')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_specific
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_more_button(self):
        # MOB-3
        self.main_page.click_on_toggle()

        expected_text_before_click = 'More'
        current_text_before_click = self.main_page.get_more_button_text()
        self.assertEqual(expected_text_before_click, current_text_before_click,
                         msg=self.main_page.exceptions['object_comparing'].format(expected_text_before_click,
                                                                                  current_text_before_click, 'text'))

        self.main_page.click_on_more_button()

        expected_text_after_click = 'Less'
        current_text_after_click = self.main_page.get_more_button_text()
        self.assertEqual(expected_text_after_click, current_text_after_click,
                         msg=self.main_page.exceptions['object_comparing'].format(expected_text_after_click,
                                                                                  current_text_after_click, 'text'))
        self.main_page.click_on_more_button()
        categories = self.main_page.get_more_section_categories()
        for category in categories:
            category_name = category.text.capitalize()
            self.assertFalse(category.is_displayed(),
                             msg=self.main_page.exceptions['is_not'].format(category_name, 'invisible'))

        self.main_page.click_on_toggle()

    @allure.testcase('3')
    @allure.title('Verify profile "Games" button')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.mobile_specific
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[TYPE] not in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Web not automated')
    def test_profile_games(self):
        # MOB-4
        self.main_page.click_on_login_button()
        self.main_page.enter_username_and_password()
        self.main_page.click_on_user_profile_button()
        dropdown_items = self.main_page.get_dropdown_items()
        expected_filters = ['XP', 'Alphabetical', 'Likes', 'Recently Played']
        for item in expected_filters:
            self.assertTrue(dropdown_items[item].is_enabled(), msg=self.main_page.exceptions['is_not'].
                            format(f'{item}', 'clickable'))
        self.main_page.click_on_dropdown()

        # MOB-5
        games = self.main_page.get_profile_games()
        if len(games) > 3:
            self.assertTrue(self.main_page.view_all_button.is_displayed(),
                            msg=self.main_page.exceptions['not_displayed'].format('"View All" button'))
            # MOB-6
            self.main_page.click_on_view_all_button()
            for name, link in games.items():
                if name:
                    self.assertTrue(link.is_displayed(),
                                    msg=self.main_page.exceptions['not_displayed'].format(name))
        else:
            self.assertFalse(self.main_page.view_all_button.is_displayed(),
                             msg=self.main_page.exceptions['is_not'].format('"View All" button', 'invisible'))
