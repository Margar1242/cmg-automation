import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.daily_games_page import DailyGamesPage


@allure.feature("Daily Games")
@allure.story("Daily Games")
@pytest.mark.usefixtures("get_driver")
class TestDailyGamesPage(TestCase):

    def setUp(self):
        self.game_page: DailyGamesPage = DailyGamesPage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify daily games category games')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.daily_games
    @pytest.mark.web
    @pytest.mark.mobile
    def test_daily_games(self):
        games = self.game_page.get_game_link_and_name()
        expected_games = {
            'Spot the Difference': f'{self.game_page.main_url()}/0-spot-the-difference',
            'Up and Down Words': f'{self.game_page.main_url()}/0-up-and-down-words',
            'Daily Jumble': f'{self.game_page.main_url()}/0-daily-jumble',
            'Daily KenKen': f'{self.game_page.main_url()}/0-daily-kenken',
            'Unolingo': f'{self.game_page.main_url()}/0-unolingo',
            'Play Four': f'{self.game_page.main_url()}/0-play-four',
            'Daily Crossword': f'{self.game_page.main_url()}/0-daily-crossword',
            'Daily FreeCell': f'{self.game_page.main_url()}/0-daily-freecell'
        }
        for game in expected_games:
            url = games.get(game)
            if self.game_page.is_mobile and game in ['Daily Jumble', 'Play Four', 'Daily Crossword']:
                continue
            expected_game_url = expected_games[game]
            self.game_page.click_on_game(url)
            current_game_url = self.game_page.current_url()
            self.assertEqual(expected_game_url, current_game_url,
                             msg=self.game_page.exceptions['object_comparing'].format(expected_game_url,
                                                                                      current_game_url,
                                                                                      f'({game}) urls'))
