import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, TYPE, RunModes, Types
from pages.game_page import GamePage


@allure.feature("Game Page")
@allure.story("Game Page")
@pytest.mark.usefixtures("get_driver")
class TestGamePage(TestCase):

    def setUp(self):
        self.game_page: GamePage = GamePage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify game page playlists')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_game_page_playlist(self):
        # GP-4
        self.assertTrue(self.game_page.playlists_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Playlists button'))

        expected_url = f'{self.game_page.main_url()}/playlists/{self.game_page.page}'
        self.game_page.click_playlists_button()

        current_url = self.game_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

    @allure.testcase('2')
    @allure.title('Verify game page also like section')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    def test_game_page_also_like_section(self):
        # GP-5
        self.assertTrue(self.game_page.also_like_section.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section'))
        self.assertTrue(self.game_page.right_arrow.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section right arrow'))
        self.assertTrue(self.game_page.left_arrow.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section left arrow'))

    @allure.testcase('3')
    @allure.title('Verify game page arrows')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    def test_game_page_arrows(self):
        # GP-6
        games, visible_games_count = self.game_page.get_also_like_section_game_list()
        self.game_page.click_also_like_section_right_arrow()
        actual_visible_games_after_right_arrow_click = [game.get_attribute('href') for game in games
                                                        if game.is_displayed()]
        visible_games_after_right_click_arrow = self.game_page. \
            get_expected_visible_after_right_arrow_click_games(games, visible_games_count)
        self.assertEqual(actual_visible_games_after_right_arrow_click, visible_games_after_right_click_arrow,
                         msg=self.game_page.exceptions['object_comparing'].
                         format(f'also like section visible games({visible_games_after_right_click_arrow})',
                                f'also like section visible games({actual_visible_games_after_right_arrow_click})',
                                'after right arrow click'))
        self.game_page.click_also_like_section_left_arrow()
        actual_visible_games_after_left_arrow_click = [game.get_attribute('href') for game in games
                                                       if game.is_displayed()]
        visible_games_after_left_click_arrow = self.game_page. \
            get_expected_visible_after_left_arrow_click_games(games, visible_games_count)

        self.assertEqual(actual_visible_games_after_left_arrow_click, visible_games_after_left_click_arrow,
                         msg=self.game_page.exceptions['object_comparing'].
                         format(f'also like section visible games({visible_games_after_left_click_arrow})',
                                f'also like section visible games({actual_visible_games_after_left_arrow_click})',
                                'after left arrow click'))

    @allure.testcase('5')
    @allure.title('Verify game page random game url')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    def test_game_page_playlist_game_url(self):
        # GP-7
        expected_url, element = self.game_page.get_also_like_section_random_game_url()
        self.game_page.click_also_like_section_random_game(element)
        current_url = self.game_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

    @allure.testcase('6')
    @allure.title('Verify game page like button')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    def test_game_page_like_button(self):
        # GP-8
        self.assertTrue(self.game_page.like_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Like button'))
        expected_text_before_like = 'like this game' if self.game_page.is_mobile else 'like'
        text_before_like = self.game_page.get_like_this_game_text()
        # TODO
        # self.assertIn(expected_text_before_like, text_before_like,
        #               msg=self.game_page.exceptions['is_not'].
        #               format(f'Expected text before click({expected_text_before_like})',
        #                      f'in current text before click({text_before_like})'))
        button_color = self.game_page.get_like_button_color()
        is_white = 'grey' in button_color or 'white' in button_color
        self.assertTrue(is_white, msg=self.game_page.exceptions['is_not'].format('Like button color', 'white'))
        self.game_page.click_like_button()
        # TODO
        # expected_text_after_like = 'thanks for voting'
        # text_after_like = self.game_page.get_like_this_game_text()
        # self.assertIn(expected_text_after_like, text_after_like,
        #               msg=self.game_page.exceptions['is_not'].
        #               format(f'Expected text before click({expected_text_after_like})',
        #                      f'in current text before click({text_after_like})'))
        self.assertIn('green', self.game_page.get_like_button_color(),
                      msg=self.game_page.exceptions['is_not'].format('Like button color', 'green'))

    @allure.testcase('7')
    @allure.title('Verify game page load process')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    @pytest.mark.timeout(60)
    def test_game_load_process(self):
        # GP-1
        self.assertTrue(self.game_page.timer.is_displayed())
        timer = self.game_page.timer
        start = self.game_page.get_timer_seconds(timer)
        stack = [second for second in range(start, 0, -1)]
        expected_countdown_order = stack[:]
        countdown = []
        while True:
            current_time = self.game_page.get_timer_seconds(timer)
            if current_time in stack:
                countdown.append(current_time)
                stack.remove(current_time)

            if current_time is None:
                self.assertEqual(expected_countdown_order, countdown,
                                 msg=self.game_page.exceptions['object_comparing'].
                                 format(f'countdown ({expected_countdown_order})', f'countdown ({countdown})',
                                        'orders'))
                break
        # GP-2
        self.assertTrue(self.game_page.continue_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format)

        # GP-3
        self.game_page.click_continue_button()
        self.assertTrue(self.game_page.progress_bar.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Progress bar'))
        self.assertTrue(self.game_page.full_screen_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Full screen button'))

    @allure.testcase('8')
    @allure.title('Verify game page structure')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_game_page_structure(self):
        # GP-9
        self.assertTrue(self.game_page.game_name_title.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Game name title'))
        self.assertTrue(self.game_page.like_this_game.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('N% like this game'))
        self.assertTrue(self.game_page.like_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Like button'))
        self.assertTrue(self.game_page.dislike_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Dislike button'))
        self.assertTrue(self.game_page.also_like_section.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section'))
        self.assertTrue(self.game_page.left_arrow.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section left arrow'))
        self.assertTrue(self.game_page.get_also_like_section_visible_games(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section games'))
        self.assertTrue(self.game_page.right_arrow.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Also like section right arrow'))
        self.assertTrue(self.game_page.playlists_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Playlists button'))
        self.assertTrue(self.game_page.skip_all_ad_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Skip all ads button'))
        self.assertTrue(self.game_page.timer.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Countdown timer'))
        instructions_title = self.game_page.get_instructions_title()
        expected_instructions_title = 'INSTRUCTIONS'
        self.assertEqual(instructions_title, expected_instructions_title,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_instructions_title,
                                                                                  instructions_title,
                                                                                  'texts'))
        self.assertTrue(self.game_page.get_instructions_text(),
                        msg=self.game_page.exceptions['not_displayed'].format('Game instructions text'))
        top_picks_title = self.game_page.get_top_picks_title()
        expected_top_picks_title = "COOLMATH TOP PICKS"
        self.assertEqual(top_picks_title, expected_top_picks_title,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_top_picks_title,
                                                                                  top_picks_title, 'texts'))
        self.assertTrue(self.game_page.get_top_picks_section_visible_games(),
                        msg=self.game_page.exceptions['not_displayed'].format('Top picks section games'))
        self.assertTrue(self.game_page.game_iframe.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Game iframe'))

    @allure.testcase('9')
    @allure.title('Verify game page right-rail content')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.demo
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_game_page_structure(self):
        # GP-10
        self.assertTrue(self.game_page.gear_promo.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Gear promo'))
        self.assertTrue(self.game_page.go_ad_free_promo.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('GO AD-FREE promo'))
        self.assertTrue(self.game_page.profile_promo.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('User profile promo'))
        self.assertTrue(self.game_page.get_az_games_link(),
                        msg=self.game_page.exceptions['not_displayed'].format('User profile promo'))

        expected_aiming_games_title = 'Aiming Games'
        aiming_games_title = self.game_page.get_aiming_games_title()
        self.assertEqual(aiming_games_title, expected_aiming_games_title,
                         msg=self.game_page.exceptions['object_comparing']
                         .format(f'aiming games title({expected_aiming_games_title})',
                                 f'aiming games title {aiming_games_title}', 'texts'))

        self.assertTrue(self.game_page.get_az_games_list(),
                        msg=self.game_page.exceptions['not_displayed'].format('AZ Games section games'))
        self.assertTrue(self.game_page.leaderboard.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Leaderboard promo'))
