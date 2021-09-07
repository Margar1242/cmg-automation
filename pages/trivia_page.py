import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.color import Color
from random import choice

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from action_wrapper.wait_actions import WaitActions
from constants.locators.trivia_page_locators import TriviaPageLocators
from pages.base_page import BasePage


class TriviaPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = 'trivia'

    def is_loaded(self, url=None):
        try:
            WaitActions.wait_until_element_is_visible(self.driver, TriviaPageLocators.HEADER_LOCATOR)
        except TimeoutError:
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def __getattr__(self, item):

        mapper = {
            'latest_quizzes': TriviaPageLocators.LATEST_QUIZZES,
            'most_popular_game': TriviaPageLocators.MOST_POPULAR_GAME,
            'trivia_categories': TriviaPageLocators.TRIVIA_CATEGORIES,
            'more_favorites': TriviaPageLocators.MORE_FAVORITES,
            'show_more_button': TriviaPageLocators.SHOW_MORE_BUTTON,
            'question_image': TriviaPageLocators.QUESTION_IMAGE,
            'correct_answer': TriviaPageLocators.CORRECT_ANSWER,
            'current_answer': TriviaPageLocators.CURRENT_ANSWER,
            'longest_answer': TriviaPageLocators.LONGEST_ANSWER,
            'timer': TriviaPageLocators.TIMER,
            'quiz_name': TriviaPageLocators.QUIZ_NAME,
            'start_quiz': TriviaPageLocators.START_QUIZ,
            'get_the_answer': TriviaPageLocators.GET_THE_ANSWER,
            'see_all_trivia': TriviaPageLocators.SEE_ALL_TRIVIA,
            'question_text': TriviaPageLocators.QUESTION_TEXT,
            'left_quizzes': TriviaPageLocators.LEFT_QUIZZES,
            'next_question_button': TriviaPageLocators.NEXT_QUESTION_BUTTON,
            'answer_0': TriviaPageLocators.ANSWER_0,
            'answer_1': TriviaPageLocators.ANSWER_1,
            'times_up': TriviaPageLocators.TIMES_UP,
            'result': TriviaPageLocators.RESULT
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Click on 'Show More' button in Trivia Page")
    def click_on_show_more_button(self):
        WaitActions.wait_until_element_is_visible(self.driver, TriviaPageLocators.MORE_SECTION__VISIBLE_GAMES)
        ElementActions.click_on_element(self.driver, TriviaPageLocators.SHOW_MORE_BUTTON)

    @allure.step("Get 'More Favorite' games in Trivia Page")
    def get_expanded_games(self, child=2, random=False):
        games = ElementFinder.find_element_from_element(self.more_favorites,
                                                        f'.home-more-quizzes:nth-child({child}) li', multiple=True)
        if not random:
            return games
        return choice(games)

    @allure.step("Get expanded games in Trivia Page")
    def get_game_name_and_thumbnail(self, game):
        return ElementFinder.find_element_from_element(game, '.quiz-row'), \
               ElementFinder.find_element_from_element(game, '.quizzes-feed-content')

    @allure.step("Click on 'More Favorites' section random game in Trivia Page")
    def click_on_random_game(self, element):
        a_tag = ElementFinder.find_element_from_element(element, 'a')
        url = ElementActions.get_attribute_from_element(a_tag, 'href')
        self.get(url)
        return url

    @allure.step("Click on 'See All Trivia' link in Trivia Page")
    def click_on_see_all_trivia(self):
        url = ElementActions.get_attribute(self.driver, TriviaPageLocators.SEE_ALL_TRIVIA, 'href')
        self.get(url)

    @allure.step("Click on 'Start The Quiz' button in Trivia Page")
    def click_on_start_the_quiz_button(self):
        ElementActions.click_on_element(self.driver, TriviaPageLocators.START_QUIZ)

    @allure.step("Click on answer button in Trivia Page")
    def click_on_answer_button(self):
        ElementActions.click_on_element(self.driver, TriviaPageLocators.ANSWER_0)
        style = ElementActions.get_attribute(self.driver, TriviaPageLocators.ANSWER_0, 'style')
        rgb = style[style.index('rgb'):style.rfind(')') + 1]
        color = Color.from_string(rgb).hex
        return color

    @allure.step("Click on 'Times Up' text in Trivia Page")
    def get_times_up_text(self):
        element = ElementFinder.find_element(self.driver, TriviaPageLocators.TIMES_UP, timeout=30)
        text = element.text
        return text

    @allure.step("Click on 'Next Question' button in Trivia Page")
    def click_on_next_question_button(self):
        ElementActions.click_on_element(self.driver, TriviaPageLocators.NEXT_QUESTION_BUTTON)

    @allure.step("Click on left quizzes count in Trivia Page")
    def get_left_quizzes_count(self):
        left = ElementActions.get_text(self.driver, TriviaPageLocators.LEFT_QUIZZES)
        correct = ElementActions.get_text(self.driver, TriviaPageLocators.CORRECT_ANSWER)
        current = ElementActions.get_text(self.driver, TriviaPageLocators.CURRENT_ANSWER)
        return int(left), int(correct), int(current)
