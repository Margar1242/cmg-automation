import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, TYPE, RunModes, Types
from pages.all_games_page import AllGamesPage


@allure.feature("All Games Page")
@allure.story("All Games Page")
@pytest.mark.usefixtures("get_driver")
class TestAllGamesPage(TestCase):

    def setUp(self):
        self.game_page: AllGamesPage = AllGamesPage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify filters for All Games Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.all_games
    @pytest.mark.mobile
    @pytest.mark.web
    def test_all_games_page_filters(self):
        # AG-1
        expected_links = {
            'ac': f'{self.game_page.main_url()}/1-complete-game-list',
            'dg': f'{self.game_page.main_url()}/1-complete-game-list/d-g',
            'hm': f'{self.game_page.main_url()}/1-complete-game-list/h-m',
            'nr': f'{self.game_page.main_url()}/1-complete-game-list/n-r',
            'sz': f'{self.game_page.main_url()}/1-complete-game-list/s-z',
        }

        for filter_ in expected_links:
            self.game_page.click_on_filter(filter_)
            expected_url = expected_links[filter_]
            current_url = self.game_page.current_url()
            self.assertEqual(expected_url, current_url,
                             msg=self.game_page.exceptions['object_comparing'].format(f"{expected_url}",
                                                                                      f"{current_url}", 'urls'))

    @allure.testcase('2')
    @allure.title('Verify all games for All Games Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.all_games
    @pytest.mark.mobile
    @pytest.mark.web
    def test_all_games_page_all_games(self):
        # AG-2
        filters = ['ac', 'dg', 'hm', 'nr', 'sz']
        games = {}
        for filter_ in filters:
            self.game_page.click_on_filter(filter_)
            page_games = self.game_page.get_games_url()
            games.update(page_games)

        for game_name, url in games.items():
            self.game_page.get(url)
            expected_game_title = game_name.lower()
            current_game_title = self.game_page.get_game_title()
            self.assertEqual(expected_game_title, current_game_title,
                             msg=self.game_page.exceptions['object_comparing'].format(f'{expected_game_title}',
                                                                                      f'{current_game_title}', 'urls'))

    @allure.testcase('3')
    @allure.title('Verify flash player required game for All Games Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.all_games
    @pytest.mark.web
    @pytest.mark.skipif(os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value}, reason='Not mobile automated')
    def test_flash_player_required_game(self):
        # AG-3
        self.game_page.get(f'{self.game_page.main_url()}/0-3-pandas')
        expected_flash_image = 'flash-page-message'
        flash_robot_image = self.game_page.get_flash_robot_image()
        self.assertIn(expected_flash_image, flash_robot_image,
                      msg=self.game_page.exceptions['is_not'].format('Expected flash image', 'displayed'))

        self.assertTrue(self.game_page.related_games.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Related games section'))

        expected_games_count = 4
        offered_games = self.game_page.get_offered_games()
        self.assertEqual(expected_games_count, len(offered_games),
                         msg=self.game_page.exceptions['object_comparing'].format(expected_games_count,
                                                                                  len(offered_games),
                                                                                  f'({offered_games}) games count',
                                                                                  ))
