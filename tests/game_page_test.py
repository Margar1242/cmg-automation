import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import TYPE, Types
from pages.game_page import GamePage
from constants.game_page_constants import GAME_WITH_DIFFERENT_INSTRUCTIONS_SECTION


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
        self.driver.delete_all_cookies()
        self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify playlists for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
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
    @allure.title('Verify also like section for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.mobile
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
    @allure.title('Verify left/right arrows for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.mobile
    @pytest.mark.web
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

    @allure.testcase('4')
    @allure.title('Verify random game url for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.mobile
    @pytest.mark.web
    def test_game_page_playlist_game_url(self):
        # GP-7
        expected_url, element = self.game_page.get_also_like_section_random_game_url()
        self.game_page.click_also_like_section_random_game(element)
        current_url = self.game_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.game_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

    @allure.testcase('5')
    @allure.title('Verify like button for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.mobile
    @pytest.mark.web
    def test_game_page_like_button(self):
        # GP-8
        self.assertTrue(self.game_page.like_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Like button'))
        expected_text_before_like = 'like this game' if self.game_page.is_mobile else 'like'
        text_before_like = self.game_page.get_like_this_game_text()
        self.assertIn(expected_text_before_like, text_before_like,
                      msg=self.game_page.exceptions['is_not'].
                      format(f'Expected text before click({expected_text_before_like})',
                             f'in current text before click({text_before_like})'))
        button_color = self.game_page.get_like_button_color()
        is_white = 'grey' in button_color or 'white' in button_color
        self.assertTrue(is_white, msg=self.game_page.exceptions['is_not'].format('Like button color', 'white'))
        self.game_page.click_like_button()
        expected_text_after_like = 'thanks for voting'
        text_after_like = self.game_page.get_like_this_game_text()
        self.assertIn(expected_text_after_like, text_after_like,
                      msg=self.game_page.exceptions['is_not'].
                      format(f'Expected text before click({expected_text_after_like})',
                             f'in current text before click({text_after_like})'))
        self.assertIn('green', self.game_page.get_like_button_color(),
                      msg=self.game_page.exceptions['is_not'].format('Like button color', 'green'))

    @allure.testcase('6')
    @allure.title('Verify game load process for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    @pytest.mark.timeout(150)
    @pytest.mark.flaky(reruns=2)
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

    @allure.testcase('7')
    @allure.title('Verify game page structure')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
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
        self.assertTrue(self.game_page.rating_module.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Rating module'))
        self.assertTrue(self.game_page.rating.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Rating'))
        self.assertTrue(self.game_page.rating_value.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Rating value'))
        self.assertTrue(self.game_page.votes_count.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Rating votes count'))
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

        self.game_page.click_continue_button()
        self.assertTrue(self.game_page.game_iframe.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Game iframe'))

    @allure.testcase('8')
    @allure.title('Verify promos for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_game_promos(self):
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


    @allure.testcase('9')
    @allure.title('Verify continue button for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_continue_button(self):
        # GP-2
        self.assertTrue(self.game_page.continue_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format)


    @allure.testcase('10')
    @allure.title('Verify big screen button and progress bar for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_big_screen_button_and_progress_bar(self):
        # GP-3
        self.game_page.click_continue_button()
        self.assertTrue(self.game_page.progress_bar.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Progress bar'))
        self.assertTrue(self.game_page.full_screen_button.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Full screen button'))


    @allure.testcase('11')
    @allure.title('Verify like button text for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    def test_game_page_like_text(self):
        # GP-9
        self.game_page.get(f'{self.game_page.main_url()}/1-complete-game-list')
        filters = ['ac', 'dg', 'hm', 'nr', 'sz']
        all_games = {}
        games, nodes = self.game_page.get_games_data_and_nodes()
        for filter_ in filters:
            self.game_page.click_on_filter(filter_)
            page_games = self.game_page.get_games_url()
            all_games.update(page_games)

        for game_name, url in all_games.items():
            check_like_message = True
            self.game_page.get(url)
            game_node = games.get(game_name)
            like_percentage = nodes.get(game_node)
            expected_n_percent_like_text = f'{like_percentage} like this game'
            current_text = self.game_page.get_like_this_game_text()
            if not like_percentage:
                check_like_message = False
                expected_n_percent_like_text = 'like this game?'
            self.assertEqual(expected_n_percent_like_text, current_text,
                             msg=self.game_page.exceptions['object_comparing'].format(expected_n_percent_like_text,
                                                                                      current_text,
                                                                                      f'({url}) texts'))
            if check_like_message:
                expected_like_message = 'thanks for voting!'
                self.game_page.click_like_button()
                current_like_message = self.game_page.get_like_message()
                self.assertEqual(expected_like_message, current_like_message,
                                 msg=self.game_page.exceptions['object_comparing'].format(expected_like_message,
                                                                                          current_like_message,
                                                                                          f'({url}) texts'))

    @allure.testcase('12')
    @allure.title('Verify difference instructions section for Game Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.game
    @pytest.mark.web
    def test_game_page_difference_instructions_section(self):
        for expected_text, url in GAME_WITH_DIFFERENT_INSTRUCTIONS_SECTION.items():
            self.game_page.get(url)
            current_text = self.game_page.get_instructions_title().lower()
            self.assertEqual(expected_text, current_text,
                             msg=self.game_page.exceptions['object_comparing'].format(expected_text,
                                                                                      current_text,
                                                                                      f'({url}) instructions section '
                                                                                      f'text'))
