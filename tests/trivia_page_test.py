import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.trivia_page import TriviaPage


@allure.feature("Trivia Page")
@allure.story("Trivia Page")
@pytest.mark.usefixtures("get_driver")
class TestTriviaPage(TestCase):

    def setUp(self):
        self.trivia_page: TriviaPage = TriviaPage(self.driver)
        self.trivia_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify the structure of Trivia Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.trivia
    @pytest.mark.mobile
    @pytest.mark.web
    def test_trivia_page_structure(self):
        # TP-1
        self.assertTrue(self.trivia_page.most_popular_game.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Most popular game'))
        if not self.trivia_page.is_mobile:
            self.assertTrue(self.trivia_page.trivia_categories.is_displayed(),
                            msg=self.trivia_page.exceptions['not_displayed'].format('Trivia categories'))
        self.assertTrue(self.trivia_page.more_favorites.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Most favorites section'))
        self.assertTrue(self.trivia_page.show_more_button.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('"Show More" button'))

    @allure.testcase('2')
    @allure.title('Verify more favorites section of Trivia Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.trivia
    @pytest.mark.mobile
    @pytest.mark.web
    def test_more_favorites_section(self):
        # TP-2
        self.trivia_page.click_on_show_more_button()
        expanded_games = self.trivia_page.get_expanded_games()
        self.assertTrue(expanded_games,
                        msg=self.trivia_page.exceptions['not_displayed'].format('Expanded games after click'))

        for game in expanded_games:
            name, thumbnail = self.trivia_page.get_game_name_and_thumbnail(game)
            self.assertTrue(name.is_displayed(), msg=self.trivia_page.exceptions['not_displayed'].format('Game name'))
            self.assertTrue(thumbnail.is_displayed(),
                            msg=self.trivia_page.exceptions['not_displayed'].format('Game thumbnail'))

    @allure.testcase('3')
    @allure.title('Verify more favorites section of Trivia Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.trivia
    @pytest.mark.mobile
    @pytest.mark.web
    def test_trivia_page_game(self):
        # TP-3
        game = self.trivia_page.get_expanded_games(child=1, random=True)
        expected_url = self.trivia_page.click_on_random_game(game)
        current_url = self.trivia_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.trivia_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

        # TP-4
        if not self.trivia_page.is_mobile:
            self.assertTrue(self.trivia_page.question_image.is_displayed(),
                            msg=self.trivia_page.exceptions['not_displayed'].format('Quiz thumbnail'))
        self.assertTrue(self.trivia_page.correct_answer.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Correct answer counter'))
        self.assertTrue(self.trivia_page.current_answer.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Current answer counter'))
        self.assertTrue(self.trivia_page.longest_answer.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Longest answer counter'))
        self.assertTrue(self.trivia_page.timer.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Timer'))
        self.assertTrue(self.trivia_page.quiz_name.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Quiz name'))
        self.assertTrue(self.trivia_page.start_quiz.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Start quiz button'))
        self.assertTrue(self.trivia_page.get_the_answer.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('"Get the answer..." text'))
        self.assertTrue(self.trivia_page.see_all_trivia.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('See all trivia'))

        # TP-5
        expected_url = f'{self.trivia_page.main_url()}/trivia'
        self.trivia_page.click_on_see_all_trivia()
        current_url = self.trivia_page.current_url()
        self.assertEqual(expected_url, current_url,
                         msg=self.trivia_page.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

        # TP-6
        game_url = f'{self.trivia_page.main_url()}/trivia/which-came-first'
        answer_color = {'green': False, 'red': False}
        expected_green = '#65e08e'
        expected_red = '#fd625e'
        self.trivia_page.get(game_url)
        self.trivia_page.click_on_start_the_quiz_button()

        # TP-7
        expected_timer_text = "time's up"
        current_timer_text = self.trivia_page.get_times_up_text()
        self.assertIn(expected_timer_text, current_timer_text.lower(),
                      msg=self.trivia_page.exceptions['object_comparing'].format(expected_timer_text.upper(),
                                                                                 current_timer_text, 'text'))
        self.trivia_page.click_on_next_question_button()

        # TP-6
        expected_quizzes_to_left = 9
        expected_correct_answer = 0
        expected_current_answer = 0

        for i in range(9):
            left, correct, current = self.trivia_page.get_left_quizzes_count()
            self.assertEqual(expected_quizzes_to_left, left,
                             msg=self.trivia_page.exceptions['object_comparing'].format(expected_quizzes_to_left, left,
                                                                                        'quiz count to left'))
            self.assertEqual(expected_correct_answer, correct,
                             msg=self.trivia_page.exceptions['object_comparing'].format(expected_correct_answer,
                                                                                        correct,
                                                                                        'correct answer count'))
            self.assertEqual(expected_current_answer, current,
                             msg=self.trivia_page.exceptions['object_comparing'].format(expected_current_answer,
                                                                                        current,
                                                                                        'correct answer count'))
            background_color = self.trivia_page.click_on_answer_button()
            if background_color == expected_green:
                answer_color['green'] = True
                expected_current_answer += 1
                expected_correct_answer += 1
            elif background_color == expected_red:
                answer_color['red'] = True
                expected_current_answer = 0
            self.trivia_page.click_on_next_question_button()
            expected_quizzes_to_left -= 1

        for key, value in answer_color.items():
            self.assertTrue(value, msg=self.trivia_page.exceptions['is_not'].format('Correct answer color',
                                                                                    f'{key}({eval(f"expected_{key}")})')
                            )
        # TP-9
        self.assertTrue(self.trivia_page.result.is_displayed(),
                        msg=self.trivia_page.exceptions['not_displayed'].format('Result'))
