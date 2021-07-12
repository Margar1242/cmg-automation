import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class TriviaPageLocators:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    # TP-1
    TRIVIA = (By.CSS_SELECTOR, f'{HEADER} .menu_trivia a')
    LATEST_QUIZZES = (By.ID, 'trivia-home-latest-quizzes')
    MOST_POPULAR_GAME = (By.ID, 'hpHero')
    TRIVIA_CATEGORIES = (By.CLASS_NAME, 'category-sidebar-nav')
    MORE_FAVORITES = (By.ID, 'trivia-home-more-quizzes')  # ul li
    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, '#show-more-button a')
    MORE_SECTION__VISIBLE_GAMES = (By.CSS_SELECTOR, ".home-more-quizzes:nth-child(1) li")

    # TP-4
    QUESTION_IMAGE = (By.CLASS_NAME, 'question-image')
    CORRECT_ANSWER = (By.CSS_SELECTOR, '.scoreboard-inner .total-correct')
    CURRENT_ANSWER = (By.CSS_SELECTOR, '.scoreboard-inner .streaks > .current > .current-streak')
    LONGEST_ANSWER = (By.CSS_SELECTOR, '.scoreboard-inner .streaks > .longest')
    TIMER = (By.ID, 'timer-placeholder1')
    QUIZ_NAME = (By.ID, 'start-the-quiz-title')
    START_QUIZ = (By.ID, 'start-the-quiz')
    GET_THE_ANSWER = (By.ID, 'bottom-text-img')
    SEE_ALL_TRIVIA = (By.CLASS_NAME, 'see-all-trivia')

    # TP-6
    QUESTION_TEXT = (By.CLASS_NAME, 'howManyLeft')
    LEFT_QUIZZES = (By.CSS_SELECTOR, '.howManyLeft > span:first-child')
    NEXT_QUESTION_BUTTON = (By.CSS_SELECTOR, '#quiz-next-button > a')
    ANSWER_0 = (By.ID, 'answer_0')
    ANSWER_1 = (By.ID, 'answer_1')

    # TP-7
    TIMES_UP = (By.CLASS_NAME, 'times-up')

    # TP-9
    RESULT = (By.CLASS_NAME, 'quiz-results-inner')
